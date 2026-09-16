# OpenResearch (alphaXiv/OpenResearch)

## Bibliographic / source

| Field | Value |
|---|---|
| Title | **OpenResearch** |
| Tagline | The local-first workspace for research agents and autoresearch |
| Org | [[wiki/entities/alphaxiv]] |
| Repo | [alphaXiv/OpenResearch](https://github.com/alphaXiv/OpenResearch) |
| Site | https://openresearch.sh/ |
| Docs | https://openresearch.sh/docs |
| Paper site | https://www.alphaxiv.org |
| License | MIT (`LICENSE` «Copyright (c) 2026 alphaXiv» + GitHub API `spdx_id`) |
| Language | Rust 2021 (`openresearch-cli`, bin `orx`) + TypeScript dashboard (`ui/`, package `orx-ui` **0.1.0**) |
| Version at ingest | **v0.2.3** (`Cargo.toml` + GitHub release 2026-09-16T01:25:30Z). HEAD is **past** the tag. |
| Default branch / HEAD | `main` @ `325eb509dc8e4ca7074568cf0ae1f0f98704eac0` («Add Hindi (hi) locale (#351)», 2026-09-16) |
| Release commit | `c5f2c02cca63` («feat: streamline onboarding and track harness setup (#350)») |
| Stars / forks / subscribers | **3858** / **246** / **16** (GitHub API 2026-09-16). `watchers_count` == stars |
| Open issues | **30** (API mixes issues+PRs) |
| Created / last push | 2026-06-07 / 2026-09-16 |
| Tree size | GitHub API `size` 97838 KB; recursive tree **513 blobs / 68 trees**, not truncated |
| Domain | research workspace; git-native experiment tree; coding-agent wrapper; local SQLite dashboard; compute routing |
| Raw capture | inbox `raw/alphaXiv-OpenResearch-readme.md`; cron may move to `40_Research/sources/agent-dev/` |
| Agent contract | root [SKILL.md](https://github.com/alphaXiv/OpenResearch/blob/main/SKILL.md) + [AGENTS.md](https://github.com/alphaXiv/OpenResearch/blob/main/AGENTS.md) + `agent-skills/orx-*/` |
| Playbook | [SYSTEM_PROMPT.md](https://github.com/alphaXiv/OpenResearch/blob/main/SYSTEM_PROMPT.md) (injected per harness) |
| In-tree docs | `docs/local-models.md`, `docs/windows.md` only |

## One-line purpose

Local **research workspace**: wrap Claude Code / Codex / OpenCode / Cursor, give each session a private git worktree, and record variants as a **frozen git-native experiment tree** whose runs execute an immutable archive of a recorded commit.

## Thesis (README + SKILL.md + AGENTS.md + Cargo.toml + sampled Rust)

1. **`orx` is the local product; `openresearch.sh` is the companion service.** AGENTS.md: CLI owns dashboard, SQLite, agent integrations, experiment orchestration, backends. The site owns accounts, orgs, sandbox catalogs, managed compute. Projects/experiments/runs/logs/artifacts stay on the machine.
2. **Not a fifth harness axis.** Registry in `src/local/harness/mod.rs` is exactly four CLIs: `claude-code`, `codex`, `opencode`, `cursor`. **Hermes is not in the registry.** OpenResearch wraps loops it does not own; it owns lineage + dashboard + compute routing. Contrast DSH / pstack / Herdr / Prime Agent.
3. **Four cardinal rules** (root `SKILL.md`; expanded in `orx-experiment-tree`): never edit a node a run has *answered*; run command **and** env are a fixed contract; vary committed code/config, never knobs-in-the-command; grow **stacked bushes** (small fan of co-equal options, then descend onto that round's winner) — not a flat fan off the root and not a noodle.
4. **Freeze is permanent.** A run that OOMs / times out / misses a dep answered nothing → repair the same node (cap: two empty runs, then ask). A number, even `nan` or a disappointment, freezes the branch. Uncommitted files never enter a run; the runner archives the recorded commit.
5. **Local by default, loopback, SQLite.** Dashboard `orx up` binds `127.0.0.1:4791` (`UpArgs` default). Sibling daemon `orx serve` defaults `127.0.0.1:4790`. Data dir: `$ORX_DATA_DIR` → `settings.json` `dataDir` → `$XDG_DATA_HOME/openresearch` → `~/.local/share/openresearch`. Windows docs still use that Unix-shaped path, not `%APPDATA%`.
6. **Account is optional for local work.** Credentials at `~/.config/openresearch/credentials.json` (mode 0600). API default `https://api.openresearch.sh`. Literature primitives (`orx discover` / `orx paper`) hit alphaXiv / OpenAlex / bioRxiv **without** login. Managed compute, instances, orgs need `orx login`.
7. **Remote bind vs auth is two texts.** README: `orx up --remote user@host` — remote service binds loopback, **no application-level authentication**, other users on that host can reach it. Clap help on `--remote`: «Starts an **authenticated** server there». **Unknown** which is true at HEAD; do not pick a winner. Windows: `--remote-host` refused (Unix domain socket).
8. **Telemetry is official-builds-only, opt-out.** Events `cli_*` → `https://api.openresearch.sh/analytics/v1/cli-events` under a random install UUID in `settings.json`. Source/dev builds do not send. `--no-telemetry` / `orx telemetry off`. Consent opt-out is still queued so the choice is observable (`record_consent`). README claim «no code/prompts/paths/repo names/tokens/emails/ids» — **author guarantee**, not independently traced here.
9. **Trendshift «#1 of the day» is a README badge**, not a GitHub metric. Star claim = API **3858** (2026-09-16).

## Architecture snapshot

```
browser  →  orx up  (127.0.0.1:4791, embedded ui/dist)
                │
                ├── SQLite orx.db  (projects, experiments, runs, chat_*)
                ├── run-logs/<runId>.log  (append-only; not in the db)
                ├── worktrees/<projectId>/<sessionId>  (private git worktree)
                └── Harness trait
                      claude-code │ codex │ opencode │ cursor
                            spawn CLI, normalize event stream

orx exp run  →  immutable archive of recorded commit
                backends: local | ssh | slurm | k8s | ray | hf | modal | tinker | openresearch
```

| Piece | Role |
|---|---|
| `orx` (`src/main.rs`) | clap CLI; Rust port of an earlier TS surface |
| `orx up` | Local dashboard + JSON/SSE API over the store; default port **4791** |
| `orx serve` | Loopback HTTP/SSE over the run store; default **4790** |
| `orx.db` | rusqlite, bundled SQLite, WAL. Tables include `local_projects`, `local_experiments`, `runs`, `chat_sessions` / `chat_messages` / `chat_turns`, `overleaf_links`, `ui_state` |
| Experiment node | Local `orx/<slug>` branch; child inherits parent run command |
| Session worktree | `data_dir/worktrees/<projectId>/<sessionId>`; session starts detached on baseline |
| `Harness` trait | detect / `run_turn` / skill install. Registry: Claude Code, Codex, OpenCode, Cursor only |
| Playbook | `SYSTEM_PROMPT.md` injected: Claude `--append-system-prompt-file`, Codex `developerInstructions`, OpenCode `instructions`. Instructs agents **not** to mention `orx` to the user |
| Skills | Bundled `agent-skills/orx-*` written into the session worktree each turn; `orx install-skills` also shims `~/.claude/skills/orx`, `~/.agents/skills/orx` (+ Codex legacy `~/.codex/prompts/orx.md`), `$XDG/opencode/skills`, `~/.cursor/skills` |
| Jobs | `src/jobs/{localbox,ssh,slurm,kubernetes,ray,huggingface,modal,tinker,openresearch}.rs` |
| UI | Vite + React 19 + TanStack Router; `ui/dist` is committed and rust-embedded |

### Cardinal rules vs other vault products

| | OpenResearch | Prime Agent (`/refine`) | Herdr |
|---|---|---|---|
| Owns | Experiment tree + dashboard + compute routing | Agent loop + IPython kernel | PTYs of *whatever* CLI |
| What is frozen | A node after a run **answers** it | Base system prompt | Nothing about experiment lineage |
| What may vary | Committed code on `orx/<slug>` | Supplemental H from trajectory | Pane layout / which CLI |
| Hermes | **Not in registry** | Optional Herdr reporter | Official `herdr integration install hermes` |

### Autoresearch loop (from `orx-experiment-tree`)

Per completed run: **repair** (answered nothing) / **refill** (next sibling) / **promote** (winner becomes next parent) / **stop** (~3 failed or regressed runs, or goal met). `orx exp wait --project` returns on the **first** completion; `orx runs` is the source of truth after each wake.

## Why it matters for `pro/plan`

- Closest public cousin of the vault's own ingest/eval discipline: **freeze answered nodes**, vary code not CLI knobs, evidence = run log not status ([[wiki/concepts/git-native-experiment-tree]]).
- 1M / software-factory long jobs: parallel worktrees + stacked-bush search is a research runtime, not a chat CLI ([[25_Projects/1M_Strategy/Overview]]).
- Do **not** treat 3.8k stars or «turn coding agents into research agents» as «install tonight»: pipe-to-sh installer, official-build telemetry on by default, remote loopback may be unauthenticated (README), Overleaf cookie import from the local browser store, **no Hermes adapter**.
- Honest steal-without-runtime-swap: freeze-on-answer + fixed run contract + stacked bushes — not wrapping Chappy inside `orx up`.

## Status

- Ingest depth: **README `main` + AGENTS.md + SKILL.md + SYSTEM_PROMPT.md + CLAUDE.md + LICENSE + Cargo.toml 0.2.3 + dist-workspace.toml + docs/local-models.md + docs/windows.md + .gitignore + GitHub API repo/release/tags/commits/org/recursive tree + sampled `src/main.rs`, `src/store.rs`, `src/config.rs`, `src/telemetry.rs`, `src/local/{git,harness,datadir,storage}.rs`, `src/commands/{mod,serve,telemetry,install_skills,up/harness_setup}.rs`, `ui/package.json`, six `agent-skills/orx-*/SKILL.md`**. Not cloned; **not installed; not run**. Docs site `openresearch.sh/docs` not scraped.
- Confidence: **high** for public CLI/tree/SQLite/harness-registry/version claims; **medium** for telemetry payload contents (module docs + README; wire not captured); **Unknown** for remote-host authentication (README vs clap help).
- Hermes/Chappy: **reference only**. Do not pipe `install.sh`, do not bind `:4791`, do not write `~/.hermes/config.yaml` or `~/.claude/skills` without an explicit ask.

## Possible Hermes/Chappy integration paths

1. **Leave as reference** — default.
2. **Process-borrow** the four cardinal rules into eval/wiki ingest (freeze answered notes; don't rewrite a measured baseline).
3. **Do not** treat OpenResearch as a Hermes host: registry has no Hermes id; playbook hides `orx` from the user; wrapping Chappy would be a new adapter, not a config flag.
4. **Do not** confuse with Herdr (PTY multiplexer) or Prime Agent (self-editing loop).

## Next (optional)

- [ ] Resolve remote bind/auth: read `src/commands/up_remote.rs` vs README
- [ ] Scrape https://openresearch.sh/docs if architecture drifted past in-tree `docs/`
- [ ] Smoke `orx` on this Linux host only if explicitly asked (musl release exists)

## Links

- Entity: [[wiki/entities/alphaxiv]]
- Concept: [[wiki/concepts/git-native-experiment-tree]]
- Tool: [[10_Reference/tools/openresearch]]
- Adjacent list: [[10_Reference/Agents/tools/harness]]
- Contrast: [[wiki/sources/prime-agent]], [[wiki/sources/herdr]], [[wiki/sources/deepseek-harness]], [[wiki/sources/pstack]]

## Sources / provenance

- https://github.com/alphaXiv/OpenResearch (`main` @ `325eb509dc8e`, 2026-09-16)
- Raw README sha256 `0c9042c88d535e3d061dd16e7a3a672ba3e06f25026ab81a92c6b48692bde752` (5645 bytes, LF)
- GitHub API repo / releases/latest `v0.2.3` / tags / commits / org `alphaXiv` / `git/trees/main?recursive=1`
- In-tree AGENTS.md, SKILL.md, SYSTEM_PROMPT.md, Cargo.toml `0.2.3`, sampled Rust cited above
