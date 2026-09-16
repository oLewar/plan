# OpenResearch (`orx`)

Local-first **research workspace**: dashboard + SQLite + git experiment tree. Wraps Claude Code, Codex, OpenCode, Cursor. Does not replace them. **Hermes is not a supported harness.**

- Full wiki source: [[wiki/sources/openresearch]]
- Entity: [[wiki/entities/alphaxiv]]
- Concept: [[wiki/concepts/git-native-experiment-tree]]
- GitHub: https://github.com/alphaXiv/OpenResearch
- Site / docs: https://openresearch.sh · https://openresearch.sh/docs
- License: MIT
- Version at ingest: **v0.2.3** (2026-09-16); HEAD `325eb509dc8e` (2026-09-16); stars **3858** (GitHub API 2026-09-16)
- Dashboard: `http://127.0.0.1:4791` (`orx up`); sibling `orx serve` default `:4790`
- Data dir: `~/.local/share/openresearch` (`orx.db`, `worktrees/`, `run-logs/`)
- Credentials: `~/.config/openresearch/credentials.json` (optional for local projects)

## Install (docs; not run here)

This Linux Hermes host has **no** `orx`.

```bash
curl -LsSf https://openresearch.sh/install.sh | sh
orx up
```

Release also ships musl tarballs (`openresearch-cli-x86_64-unknown-linux-musl.tar.xz`) and `openresearch-cli-installer.sh` from GitHub Releases. Pipe-to-sh. Official builds send opt-out telemetry.

```bash
orx projects
orx project view <project-id>
orx runs <project-id>
orx logs <run-id>
orx exp run <experiment-id>
orx discover keyword <query>
orx paper <arxiv-id-or-doi>
orx telemetry off
orx install-skills          # claude | codex | opencode | cursor | all
```

Local projects do not require `orx login`. Managed compute / orgs / instances do.

## Hermes / Chappy

Harness `registry()` = Claude Code, Codex, OpenCode, Cursor. No Hermes id, no `~/.hermes` skill target.

At ingest: **reference only**. Do not pipe `install.sh`, do not bind `:4791`, do not write `~/.hermes/config.yaml` or coding-agent skill dirs without an explicit ask.

Honest steal: freeze-on-answer + fixed run command + stacked-bush tree shape ([[wiki/concepts/git-native-experiment-tree]]).

## Operating constraints

- Remote `orx up --remote user@host`: README says loopback **without** app-level auth; clap help says authenticated. **Unknown**. Other users on the remote host may reach it.
- Windows beta: Git for Windows required (not WSL `bash.exe`); `--remote-host` refused (Unix socket); unsigned `orx.exe` hits SmartScreen.
- Official-release telemetry on by default (`cli_*` events, random install id). Source builds do not send. `orx telemetry off` / `--no-telemetry`.
- Overleaf integration can import a browser session cookie from the local store.
- Uncommitted files never run. Frozen experiment branches must not be rebased.
- Playbook tells wrapped agents not to mention `orx` to the user.

## Mental model

**Lineage workspace**, not an agent loop. Contrast loop-replace ([[wiki/concepts/everything-is-a-plugin]]), style wrap ([[wiki/concepts/playbook-routed-agent-mode]]), PTY runtime ([[wiki/concepts/agent-runtime-multiplexer]]), `/refine` ([[wiki/concepts/continual-harness]]).
