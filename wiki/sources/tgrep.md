# tgrep (microsoft/tgrep)

## Bibliographic / source

| Field | Value |
|---|---|
| Title | **tgrep** |
| Tagline | Trigram-indexed grep with a client/server architecture for fast regex search in large codebases locally |
| Org | [[wiki/entities/microsoft]] |
| Workspace author | Shengyu Fu ([shengyufu](https://github.com/shengyufu)); `Cargo.toml` `authors = ["Shengyu Fu"]` |
| Repo | [microsoft/tgrep](https://github.com/microsoft/tgrep) |
| License | MIT (`LICENSE` «Copyright (c) Microsoft Corporation» + GitHub API `spdx_id`) |
| Language | Rust 2024 edition; workspace crates `tgrep-core` + `tgrep-cli` (bin `tgrep`) |
| Version at ingest | **v1.0.5** (`[workspace.package] version` + GitHub release 2026-09-08T18:11:23Z). HEAD is **past** the tag. |
| Default branch / HEAD | `main` @ `50f5d8f6a54e9e4d16d021954cfcd4e77d342d7b` («fix: print search stats after matches (#146)», 2026-09-09) |
| Stars / forks / subscribers | **2430** / **93** / **8** (GitHub API 2026-09-09). `watchers_count` == stars |
| Open issues | **1** (API mixes issues+PRs) |
| Created / last push | 2026-04-03 / 2026-09-09 |
| Tree size | GitHub API `size` 1073 KB; recursive tree **98 blobs / 15 trees**, not truncated |
| Domain | local code search; trigram inverted index; ripgrep-compatible CLI; optional TCP JSON-RPC server |
| Raw capture | inbox `raw/microsoft-tgrep-readme.md`; cron may move to `40_Research/sources/agent-dev/` |
| In-tree agent guide | [AGENTS.md](https://github.com/microsoft/tgrep/blob/main/AGENTS.md) (not a second raw capture) |
| Benchmarks | [BENCHMARKS.md](https://github.com/microsoft/tgrep/blob/main/BENCHMARKS.md) — 24 Aug 2026 sweep at `82b88a1` |

## One-line purpose

**ripgrep-shaped CLI** that answers regex searches from a pre-built **trigram index** (optional long-lived `serve` process) instead of scanning every file on every query.

## Thesis (README + AGENTS.md + Cargo.toml + GitHub API)

1. **The product is candidate pruning, not a new regex engine.** grep/ripgrep are O(total bytes) per query. tgrep extracts overlapping 3-byte trigrams, looks up posting lists, then verifies only candidate files with the full regex (rayon).
2. **Three answer paths, one command.** Search order: running `tgrep serve` over TCP → on-disk `./.tgrep` with no server → brute walk (stderr warning). Agents should not pick a path; they should know results **differ** across them.
3. **Cold `serve` is empty, not partial.** First build publishes nothing until complete; queries return no matches. A *resumed* partial index does answer from what it has. `tgrep status` `Indexing: complete` is **not** a freshness signal.
4. **Index membership flags must match** across `index` / `serve` / search (`--exclude`, `--no-require-git`, `--max-filesize` / `--no-max-filesize`, `--index-path`). A mismatch looks like «file contains no match».
5. **Default 64 MiB size cap is a deliberate ripgrep divergence.** Named so an outlier generated artifact is not re-scanned on every candidate query. `--no-max-filesize` restores ripgrep-identical membership. A file named on the CLI is not dropped by the *inherited* default.
6. **Speedup is not uniform.** Author BENCHMARKS (shared GitHub runners, 24 Aug 2026): geometric mean **14.6× Windows / 8.61× macOS / 2.82× Linux** vs ripgrep. tgrep wins 17/18 cells; **Kubernetes on Linux 0.93×** is the loss. Margin = repo size × match-delivery cost, not «tgrep is always faster».
7. **Integrated into GitHub Copilot CLI** — README claim. **Not verified** here (no Copilot CLI smoke).
8. **Agent-facing contract lives in AGENTS.md** (2026-09-08, PR #143): put `--` before the pattern; prefer `-F` for user-typed symbols; do not commit `.tgrep/`; treat exit `1` as no results; always return stderr (the «no index» warning can arrive with 0 or 1).
9. **Not a harness.** Owns an inverted index + optional local TCP server. Contrast loop-replace ([[wiki/concepts/everything-is-a-plugin]]), PTY runtime ([[wiki/concepts/agent-runtime-multiplexer]]), `/refine` ([[wiki/concepts/continual-harness]]), MCP broker ([[wiki/concepts/mcp-tool-broker]]).

## Architecture snapshot

```
tgrep <pattern> ---TCP JSON-RPC--> tgrep serve (multi-client, newline-delimited)
    (client)                         |
                                HybridIndex
                                /         \
                         IndexReader    LiveIndex
                         (mmap disk)   (in-memory overlay)
                              ^              ^
                              |              |
                        Periodic Flush  File Watcher (notify)
                        (50K files /    Background Indexer
                         5 min)         (rayon; 1024-file batches)
```

| Piece | Role |
|---|---|
| `tgrep-core` | Trigrams, walker (git/p4 ignore), on-disk format, builder, mmap reader, query planner, HybridIndex |
| `tgrep-cli` | clap CLI: `index` / `serve` / search / `status` / `count-files` |
| IndexReader | mmap'd sorted trigram lookup; zero-copy binary search |
| LiveIndex | overlay for files changed after start / still being indexed |
| HybridIndex | merge; overlay wins |
| Background indexer | parallel batches of 1,024 files (byte-split); cold start serves **empty** until first publish |
| Periodic flush | every 50K files or 5 min → swap reader; bounds RAM |
| Watcher | native `notify` with sticky poll fallback; `--no-watch` kills refresh |
| TCP server | JSON-RPC 2.0, one thread per connection |
| File cache | 50K-entry content cache, `RwLock` |
| Default index dir | `./.tgrep` (`serve.json` = PID + port). `.gitignore` in-repo ignores `.tgrep/` |

### On-disk format (README)

| File | Description |
|---|---|
| `lookup.bin` | Sorted 16-byte entries: trigram(u32) + offset(u64) + length(u32) |
| `index.bin` | Concatenated posting lists: file_id(u32) |
| `files.bin` | file_id → path |
| `files-extra.bin` | `--files` paths with no searchable content |
| `meta.json` | Version, counts, timestamps |
| `serve.json` | Server PID and TCP port |

### Search resolution (AGENTS.md)

1. Server for this tree → TCP.
2. On-disk index, no server → read `.tgrep/` (stale vs last publication; interrupted first build can leave an incomplete index **without warning**).
3. No index → scan like grep.

`--no-index` forces a walk (still applies ignore/hidden/binary/size rules).

### Flags that bypass the index (even with a server)

`-E/--encoding`, `-a/--text`, `--binary`, `-./--hidden`, every `--no-ignore*` variant, naming a **single file**, and explicit `--no-index`.

### Install surfaces (docs; not run here)

| Path | Notes |
|---|---|
| GitHub Releases **v1.0.5** | musl Linux, Darwin, Windows zips; README unpacks Linux into `mktemp` then `install` to `~/.local/bin` |
| Homebrew | `brew install tgrep` |
| From source | `cargo install --path tgrep-cli --locked` |

Release assets at ingest: `tgrep-v1.0.5-{aarch64,x86_64}-{apple-darwin,unknown-linux-musl,pc-windows-msvc}` + `checksums.txt`.

## Benchmarks (author; shared runners)

Sweep 2026-08-24 @ `82b88a1`. Compare **within a row**, not ms across OS. Geometric means: Windows 14.6×, macOS 8.61×, Linux 2.82×.

| Repo | Files | Windows | macOS | Linux |
|---|---:|---:|---:|---:|
| chromium | 504,351 | 17.6× | 15.8× | 3.81× |
| gecko-dev | 387,841 | 38.6× | 51.9× | 7.36× |
| linux | 95,831 | 34.8× | 21.0× | 9.38× |
| rust | 62,326 | 7.69× | 2.69× | 1.61× |
| kubernetes | 31,300 | 7.08× | 2.81× | **0.93×** |
| go | 15,833 | 7.53× | 3.12× | 1.29× |

Index-build **private** peak in that sweep: Chromium 332–463 MiB; Go ~108–137 MiB. README also reports Linux-kernel external-merge default ~152–160 MiB private vs multi-GiB `--index-strategy=memory`.

**What decides the margin (BENCHMARKS):** (1) corpus size; (2) match-delivery cost over TCP/print vs ripgrep writing stdout from the scan thread. A query with millions of matches can lose even when the index pruned to 4–12% of files.

Treat as **author measurements on GitHub-hosted runners**, not a controlled-machine study. Not re-run here.

## Contrast vs vault axes

| | tgrep | [[wiki/sources/herdr]] | [[wiki/sources/hexstrike-ai]] | [[wiki/sources/omlx]] |
|---|---|---|---|---|
| Owns | **Trigram index + local search server** | PTYs | MCP→shell broker | Weights + KV |
| Network | Local TCP JSON-RPC (`serve.json` port) | Local TUI/server | Flask `0.0.0.0:8888` + MCP | `localhost:8000` |
| This Linux host | **Not installed** (`rg` is) | Not installed | Do not install | Cannot run (macOS) |

Not a fifth harness axis. Local search helper for coding agents.

## Why it matters for `pro/plan`

- Efficiency: on a 100k+ file tree, agent `grep`/`rg` is the Cost knob; an index changes the unit from «bytes scanned» to «candidates verified».
- Causal split: empty hits with a running server can be **cold first build**, **flag bypass**, **membership mismatch**, or **stale on-disk index** — not «the symbol is gone». Slow tgrep can be **match-volume delivery**, not a broken index.
- Hermes/Chappy already grep via tools; tgrep is a possible CLI swap, not a loop swap. AGENTS.md is the integration contract if we ever wrap it.
- Adjacent to [[wiki/concepts/trigram-index-search]] and [[wiki/concepts/efficiency-metric]].

## Status

- **Ingest depth:** README `main` (CRLF, 44418 bytes) + AGENTS.md + BENCHMARKS.md head/takeaways + `LICENSE` + workspace/`tgrep-cli`/`tgrep-core` `Cargo.toml` + `.gitignore` + GitHub API repo/releases/tags/commits/recursive tree. **Not executed.** No clone, no `tgrep` binary on this host.
- **Confidence:** high on version **v1.0.5**, MIT, crate split, search-order/cold-start contract, 64 MiB default cap, tree size (98 blobs). Medium on Copilot CLI integration and benchmark ratios (author, shared runners). Stars are GitHub API 2026-09-09.
- **Hermes/Chappy:** **reference only**. Do not install, do not start `tgrep serve`, do not write `~/.hermes/config.yaml`.
- **Reading status:** not used in production on this host.

## Next (optional)

- [ ] Install v1.0.5 musl binary and smoke `tgrep --help` / `tgrep status` — only if user asks
- [ ] Decide whether Hermes `search_files` / agent grep should prefer tgrep on large worktrees
- [ ] Verify Copilot CLI actually shells out to tgrep

## Links

- Entity: [[wiki/entities/microsoft]]
- Concept: [[wiki/concepts/trigram-index-search]]
- Tool: [[10_Reference/tools/tgrep]]
- Raw: `raw/microsoft-tgrep-readme.md`

## Sources / provenance

- README `main` 2026-09-09, sha256 `4b8007db13a078a70f497df02deece7423695ec7f08b49297c74d8b297d20e98` (44418 bytes, CRLF)
- AGENTS.md sha256 `751573f92feb1470a0c7ad93975f6ae1b189ae62140c2d30bb737a2675e37f85` (10756 bytes, LF)
- BENCHMARKS.md sha256 `d6b488ce0102d80e79b18fcec297cdeaf9338ee7f88e86e7a4816e45865fa33f` (37259 bytes, CRLF)
- GitHub API: https://api.github.com/repos/microsoft/tgrep
- Latest release: https://github.com/microsoft/tgrep/releases/tag/v1.0.5 (published 2026-09-08T18:11:23Z)
- HEAD: `50f5d8f6a54e9e4d16d021954cfcd4e77d342d7b`
- Workspace version file: https://raw.githubusercontent.com/microsoft/tgrep/main/Cargo.toml (`version = "1.0.5"`)
