# tgrep

**Trigram-indexed grep**: ripgrep-compatible CLI with a pre-built inverted index and optional `tgrep serve` (TCP JSON-RPC, file watcher). For large repos, searches touch candidate files instead of every byte.

- Full wiki source: [[wiki/sources/tgrep]]
- Entity: [[wiki/entities/microsoft]]
- Concept: [[wiki/concepts/trigram-index-search]]
- GitHub: https://github.com/microsoft/tgrep
- License: MIT
- Version at ingest: **v1.0.5** (2026-09-08); HEAD `50f5d8f6a5` (2026-09-09); stars **2430** (GitHub API 2026-09-09)
- Agent guide: https://github.com/microsoft/tgrep/blob/main/AGENTS.md
- Index dir: `./.tgrep` (do not commit)

## Install (docs; not run here)

This Linux Hermes host has `/usr/bin/rg`, **no** `tgrep`.

```bash
# release (x86_64 musl) — README unpacks in mktemp, then install
# https://github.com/microsoft/tgrep/releases/tag/v1.0.5

brew install tgrep   # macOS / Linux Homebrew

# from a checkout
cargo install --path tgrep-cli --locked
```

```bash
tgrep index .
tgrep serve . &          # writes .tgrep/serve.json (PID, port)
tgrep status .
tgrep -- -F "fn main" .
```

Keep membership flags aligned on `index` / `serve` / search (`--index-path`, `--exclude`, `--max-filesize`, `--no-require-git`).

## Hermes / Chappy

AGENTS.md sketches a tool schema (`pattern`, `path`, `flags`) and requires `--` before the pattern, path canonicalization under the repo root, and returning stdout+stderr+exit (`1` = no hits). **Not wired, not installed.**

At ingest: **reference only**. Do not install a binary, do not start a server, do not replace `search_files` / `rg`, do not write `~/.hermes/config.yaml`.

## Operating constraints

- Cold `serve` answers **empty** until the first index publish.
- `--hidden` / `--no-ignore` / `-a` / `--binary` / `-E` / naming one file **bypass** the index (full walk).
- Default skip: files **> 64 MiB**. `--no-max-filesize` to match ripgrep membership.
- Watcher fallback to polling is sticky until restart; `--no-watch` disables refresh.
- Author benches: big win on Windows/macOS large trees; Linux can **lose** (k8s 0.93×) when match volume dominates.
- Copilot CLI integration is a README claim, not smoked here.

## Mental model

Local **code-search index**, not an agent harness. Contrast loop-replace ([[wiki/concepts/everything-is-a-plugin]]), PTY runtime ([[wiki/concepts/agent-runtime-multiplexer]]), `/refine` ([[wiki/concepts/continual-harness]]), MCP broker ([[wiki/concepts/mcp-tool-broker]]).
