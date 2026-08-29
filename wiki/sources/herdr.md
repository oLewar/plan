# Herdr (herdrdev/herdr)

## Bibliographic / source

| Field | Value |
|---|---|
| Title | **Herdr** |
| Tagline | the runtime your coding agents live on |
| Org | [[wiki/entities/herdr\|Herdr / herdrdev]] |
| Founder | Can (`ogulcancelik`); solo until YC F26 (author claim, 2026-08-06) |
| Repo | [herdrdev/herdr](https://github.com/herdrdev/herdr) |
| Site | https://herdr.dev |
| Docs | https://herdr.dev/docs/ |
| Agent guide (teach a human) | https://herdr.dev/agent-guide.md |
| Agent skill (operate Herdr) | [skills/herdr/SKILL.md](https://github.com/herdrdev/herdr/blob/master/skills/herdr/SKILL.md) |
| Compare | https://herdr.dev/compare/ |
| Blog (YC) | https://herdr.dev/blog/herdr-is-joining-y-combinator/ |
| X | [@herdrdev](https://x.com/herdrdev) |
| License | Apache-2.0 (switched from AGPL; author claim in YC post) |
| Language | Rust (`Cargo.toml` 2021 edition; TUI via ratatui/crossterm; PTY via vendored `portable-pty`) |
| Version at ingest | **v0.8.2** (`Cargo.toml` + GitHub latest release, published 2026-08-19) |
| Default branch / HEAD | `master` @ `c2637dc` (2026-08-28, special-key text) |
| Stars / forks / watchers | **33397** / **2428** / **95** (GitHub API, 2026-08-29) |
| Open issues | 261 (API, mixes issues+PRs) |
| Created / last push | 2026-03-27 / 2026-08-28 |
| Org created | `herdrdev` 2026-07-25 (after the repo) |
| Homepage marketing | **33111** stars / **612033** installs / **866** plugins / **21** agent CLIs (herdr.dev, 2026-08-29; marketing counters can lag GitHub API) |
| Domain | agent runtime, terminal multiplexer, coding-agent orchestration, TUI |
| Raw capture | [[raw/herdrdev-herdr-readme]] |
| Contact | hey@herdr.dev |

## One-line purpose

Background **server that owns real PTYs**; coding-agent CLIs keep running when every UI client detaches. Herdr does not wrap or replace Claude Code / Codex / Hermes / Grok — it owns their terminals and reads `working` / `blocked` / `idle`.

## Thesis (from README + docs + YC post)

1. **Runtime ≠ viewer.** A server owns panes/processes. TUI, CLI, SSH, phone, and future clients attach. Closing the lid or every client must not kill the herd.
2. **tmux inheritance + agent semantics.** Real PTYs, prefix `ctrl+b`, detach/reattach, SSH. Extra: detect which pane is an agent and wait on semantic state instead of polling text.
3. **Does not replace agent CLIs.** One Rust binary, no Electron; runs inside Ghostty/kitty/iTerm/Alacritty. Mouse-first *and* prefix keys.
4. **Two control surfaces, same API.** CLI wrappers for scripts; local socket API for protocol clients. Agents inside panes get `HERDR_ENV=1` and can spawn/wait on siblings.
5. **Detection is evidence-based.** Lifecycle hooks (when installed) beat screen manifests. Screen rules match the live *bottom buffer*, not the scrolled viewport. Unusual prompts fall back to `idle`, not false `blocked`.
6. **Core stays small; plugins are unsandboxed executables.** Marketplace = GitHub topic `herdr-plugin`. No plugin SDK — the whole CLI is the plugin API.
7. **YC F26, runtime stays Apache-2.0.** Author (Can) says the next product is connecting disconnected machines (laptop / VPS / sandbox). Details redacted on the homepage.

## Architecture snapshot

```
herdr client (TUI in your terminal, or thin --remote)
        │  attach / detach (ctrl+b q)
        ▼
herdr-server  (owns PTYs, layout, agent metadata, plugins)
        │
        ├── workspace (project) → tabs → panes (real terminals)
        ├── agent detector (process + screen TOML and/or lifecycle hooks)
        └── local socket + CLI  (same methods)
```

### Persistence (what actually survives)

| Case | Processes keep running | Layout returns | Recent screen | Agent conversation |
|---|---|---|---|---|
| Detach / reattach | Yes | Yes | Live terminal | Yes (process never stopped) |
| Server restart | No | Snapshot restore | Only if `[experimental] pane_history = true` | Only native session restore |
| `herdr update --handoff` | Best-effort live PTY transfer | Yes | Yes if handoff succeeds | Yes if processes kept |

`pane_history` is **off by default** (scrollback can hold secrets). Native restore is **on by default**; disable with `[session] resume_agents_on_restore = false`.

### Agent states

| State | Meaning |
|---|---|
| `blocked` | Visible approval / question / permission UI (strict for screen-manifest agents) |
| `working` | Actively running |
| `done` | Finished background work, tab not yet seen in focused UI |
| `idle` | Ready / finished and seen |
| `unknown` | Agent present, classification not confident — **not** proof of success |

CLI reads do **not** mark a pane seen. `agent prompt` on an already-`blocked` agent returns `agent_blocked` without sending keys.

### Status authority (docs/agents)

| Kind | Agents (docs, 2026-08-29) | State source |
|---|---|---|
| Lifecycle authority when installed | Pi, OMP, Kimi Code CLI, OpenCode, Kilo Code CLI, MastraCode | Hooks/plugins; **no** screen fallback while reporting |
| Session identity only | Claude Code, Codex, Copilot CLI, Devin, Droid, Qoder, Qwen, Cursor Agent CLI, **Hermes Agent**, Antigravity CLI, Grok CLI | Screen manifest for state; hooks for resume id |
| Screen only | Amp, Kiro CLI, Maki | Screen manifest; no official integration |
| Less tested detection | Gemini CLI, Cline | Still run as ordinary processes |

Hermes: `herdr integration install hermes` writes `plugins/herdr-agent-state/` under `HERMES_HOME` (`~/.hermes`) and enables it in `config.yaml`. Resume command: `hermes --resume <id>`. Docs disagree on minimum integration version: session-state table says **`2`**, integrations page says **`5`**. Treat as **Unknown** until `herdr integration status` on a live install.

### Control primitives

| Primitive | Job |
|---|---|
| Layout (`workspace` / `tab` / pane topology) | Create places. `agent start` never creates layout. |
| Pane | Raw terminal: `run`, `send-text`/`send-keys`, `read`, `wait-output` |
| Agent | Named occupant: `start`, `prompt`, `wait`, `read`, `attach` |

IDs: workspace `w1`, tab `w1:t1`, pane `w1:p1`. Closed IDs are not reused. Agent names: `[a-z][a-z0-9_-]{0,31}`.

### Install / config

| Channel | Command |
|---|---|
| Direct (Linux/macOS) | `curl -fsSL https://herdr.dev/install.sh \| sh` then `herdr update` |
| Homebrew / mise / Nix | `brew install herdr` · `mise use -g herdr` · flake `github:herdrdev/herdr` — update via the package manager (`herdr update` disabled) |
| Windows | `irm https://herdr.dev/install.ps1 \| iex` (or `install.cmd` if endpoint security blocks fileless PS) |
| Config | `~/.config/herdr/config.toml` (Linux/macOS); `%APPDATA%\herdr\config.toml` (Windows) |
| Defaults dump | `herdr --default-config` |
| Skill print | `herdr --skill` (release-matched copy) |

Remote: `ssh host && herdr` (tmux-style) **or** `herdr --remote workbox` (local thin client, can bridge clipboard images). Windows is not a remote *host*. `--handoff` is experimental.

### Compare field (vendor table, herdr.dev/compare)

| Kind | Examples | Agents if the UI quits |
|---|---|---|
| Runtime + clients | **Herdr** | Keep running on the server |
| Terminal multiplexer | tmux, Zellij | Keep running; no semantic agent state |
| Terminal app | cmux, Warp | Session restore / app-bound |
| Process dashboard | Solo | While the app is open |
| Manager app | Conductor, Emdash, Superset | Stop with the window |

Vendor framing. Pairing Herdr *with* a worktree/review manager is the intended composition, not a replacement.

## Why it matters for `pro/plan`

- Missing layer next to [[wiki/sources/deepseek-harness]] (replaceable *loop*) and [[wiki/sources/pstack]] (playbook *style* on Cursor): Herdr is **where agents live** while those loops run.
- Hermes/Chappy is a **first-class detected agent** with an official integration (`hermes --resume`). Directly relevant to Fusion/Codex/Claude multi-pane work on this host.
- Causal split: **process up/down ≠ agent blocked**. tmux/abtop/contrabass notes in research already assume panes; they do not classify approval UIs.
- 1M / software-factory: long jobs (hours–days) need a server-owned PTY, not a chat window. Matches [[25_Projects/1M_Strategy/Overview]] harness requirement.
- Do **not** treat 33k stars as “must install tonight”: pipe-to-sh installer, unsandboxed plugins, experimental handoff, docs version drift on Hermes integration.

## Status

- Ingest depth: **README + herdr.dev docs (concepts, agents, session-state, integrations/Hermes, agent-automation, socket-api, plugins, install, how-to-work, remote, agent-skill, compare) + agent-guide.md + YC blog + Cargo.toml + GitHub API repo/release/org + HEAD commit**. Not cloned; **not installed; not run**.
- Confidence: **high** for public docs/API numbers above; **medium** for homepage install/plugin counters (author marketing); **low** for runtime quality vs tmux on this host (no smoke test).
- Hermes/Chappy: **reference only** at ingest — do not `herdr integration install hermes` or pipe `install.sh` without an explicit user ask.

## Possible Hermes/Chappy integration paths

1. **Leave as reference** — default until someone wants a multiplexer for parallel Codex/Claude/Hermes panes.
2. **Install Herdr only** — `herdr` as the outer session; start `hermes` / `claude` / `codex` / `grok` inside panes. No Hermes config edits.
3. **Official Hermes plugin** — `herdr integration install hermes` writes under `~/.hermes` and touches `config.yaml`. Requires existing Hermes home + restart. Resume via `hermes --resume <id>`.
4. **Skill inside a pane** — `npx skills add herdrdev/herdr --skill herdr -g` only when `HERDR_ENV=1`. Skill forbids controlling Herdr from outside.
5. **Do not** treat Herdr plugins as a Hermes skill pack; they are host executables with full CLI/socket rights.

## Next (optional)

- [ ] Smoke-test `herdr --version` on this host vs installing
- [ ] Resolve Hermes integration min version `2` vs `5` against a live `herdr integration status`
- [ ] Decide whether Fusion/Codex worktrees should sit in Herdr workspaces or stay in the current coding-agent-orchestration flow

## Links

- Entity: [[wiki/entities/herdr]]
- Concept: [[wiki/concepts/agent-runtime-multiplexer]]
- Tool card: [[10_Reference/tools/herdr]]
- Adjacent list: [[10_Reference/Agents/tools/harness]]
- Contrast: [[wiki/sources/deepseek-harness]], [[wiki/sources/pstack]], [[wiki/concepts/everything-is-a-plugin]], [[wiki/concepts/playbook-routed-agent-mode]]

## Sources / provenance

- README `master` 2026-08-29, sha256 `d590c81b14ff17a5922e3cb9da1a12652263fc596e451d413c423b7bf099fc2c` (4431 bytes)
- Site: https://herdr.dev/ (live extract 2026-08-29)
- Docs: `/docs/`, `/docs/quick-start/`, `/docs/concepts/`, `/docs/agents/`, `/docs/session-state/`, `/docs/integrations/` (Hermes section), `/docs/agent-automation/`, `/docs/socket-api/`, `/docs/plugins/`, `/docs/install/`, `/docs/how-to-work/`, `/docs/persistence-remote/`, `/docs/agent-skill/`, `/compare/`
- https://herdr.dev/agent-guide.md
- YC post 2026-08-06: https://herdr.dev/blog/herdr-is-joining-y-combinator/
- `Cargo.toml` `version = "0.8.2"`; latest GitHub release `v0.8.2` (2026-08-19)
- GitHub API `herdrdev/herdr` + `/releases/latest` + `/orgs/herdrdev` + commit `master` 2026-08-29
- Skills/AGENTS.md sampled from `raw.githubusercontent.com` (not a full architecture deep-dive of `src/`)
