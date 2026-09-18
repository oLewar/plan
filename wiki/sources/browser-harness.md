# Browser Harness (browser-use/browser-harness)

## Bibliographic / source

| Field | Value |
|---|---|
| Title | **Browser Harness** |
| Tagline | Connect an LLM to a real browser through one editable CDP websocket |
| Org | [[wiki/entities/browser-use]] |
| Repo | [browser-use/browser-harness](https://github.com/browser-use/browser-harness) |
| Site | https://browser-harness.com |
| Cloud | https://cloud.browser-use.com |
| License | MIT (`LICENSE` «Copyright (c) 2026 Browser Use» + GitHub API `spdx_id`) |
| Language | Python (`src/browser_harness/`); PyPI `browser-harness` |
| Version at ingest | **v0.1.13** (GitHub release 2026-09-04T02:52:52Z, target `c24e5072ee66`; PyPI wheel 2026-09-04). HEAD is **past** the tag. |
| Default branch / HEAD | `main` @ `afbcc381b963` («Merge pull request #757 … video-export-nested-output», 2026-09-07) |
| Stars / forks / subscribers | **17663** / **1729** / **55** (GitHub API 2026-09-18). `watchers_count` == stars |
| Open issues | **357** (API mixes issues+PRs) |
| Created / last push | 2026-04-17 / 2026-09-12 |
| Tree size | GitHub API `size` 4406 KB; recursive tree **190 blobs / 113 trees**, not truncated |
| Domain | CDP browser harness; agent-editable helpers; optional Browser Use Cloud |
| Raw capture | durable `40_Research/sources/agent-dev/browser-use-browser-harness-readme.md` (cron moved from inbox; banner SVG localized) |
| Agent contract | root [SKILL.md](https://github.com/browser-use/browser-harness/blob/main/SKILL.md) (~14 KB) + [install.md](https://github.com/browser-use/browser-harness/blob/main/install.md) + [AGENTS.md](https://github.com/browser-use/browser-harness/blob/main/AGENTS.md) |
| Plugin manifests | `.claude-plugin/plugin.json` **0.1.0** (≠ PyPI 0.1.13) |

## One-line purpose

Thin **CDP harness**: a long-lived daemon holds one Chrome websocket; the agent sends short Python that calls pre-imported helpers. Core `src/browser_harness/` stays protected; task-specific code goes in `agent-workspace/agent_helpers.py`.

## Thesis (README + SKILL.md + AGENTS.md + pyproject + sampled Python)

1. **README is marketing (~3 KB).** Architecture is `SKILL.md` (agent contract), `install.md` (uv + Chrome `chrome://inspect/#remote-debugging`), `AGENTS.md` (core vs workspace), and `src/`.
2. **Not a fifth harness axis.** This is a **browser I/O layer** for whoever already has a loop (Claude Code, Codex, Cursor, Hermes `browser_exec`). Contrast DSH / pstack / Herdr / Prime Agent. Jev sits *on top* of this CLI ([[wiki/sources/jev-ultrafast]]).
3. **Self-healing = writable workspace, frozen core.** Agent may add helpers in `$BH_AGENT_WORKSPACE/agent_helpers.py` and (opt-in) `domain-skills/<site>/`. Package code is not the agent's edit surface.
4. **One local daemon, one attached tab.** Default `BU_NAME=default`. Extra local daemons each open another Chrome CDP connection and may show another Allow prompt. Parallel interactive work → Cloud browsers, not a second local daemon.
5. **Local Chrome needs no API key.** Cloud (`start_remote_daemon`) needs `browser-harness auth login` / `BROWSER_USE_API_KEY`. `BU_AUTOSPAWN` is opt-in; key alone does not spawn.
6. **PyPI 0.1.13 ≠ plugin.json 0.1.0 ≠ HEAD.** Install path is `uv tool install --python 3.12 --upgrade --force browser-harness`. Claude plugin manifest still says **0.1.0**. npm `browser-harness@0.0.58` is a **different** package — do not confuse.
7. **Skill name vs identity.** `SKILL.md` frontmatter `name: browser-harness`. `AGENTS.md`: «Skill identity (`name` + trigger) = `browser-use` (do not rename)». **Unknown** which string a host actually matches; record both.
8. **Telemetry is opt-out PostHog.** `src/browser_harness/telemetry.py`: EU `https://eu.i.posthog.com`, key `phc_rCPCLPtaXB3EuBdiH7JLKtU2Wj5iPnuwdsbw58CnjYXc`. Disable: `browser-harness telemetry disable` or env `BH_TELEMETRY` / `BROWSER_HARNESS_TELEMETRY` / `ANONYMIZED_TELEMETRY` ∈ {0,false,no,off}. `cli_event` still sends `task` (cap 20 000 chars) and `output`. Agent detection includes `HERMES_SESSION_ID` → client `hermes`. **Author redaction is not a wire capture.**
9. **Domain skills off by default.** `BH_DOMAIN_SKILLS=1` to enable. Tree has **97** site dirs / **111** files under `agent-workspace/domain-skills/` (two dirs are empty `.gitkeep`: salesforce, spreadshirt).

## Architecture snapshot

```
agent  →  browser-harness CLI (stdin Python, helpers pre-imported)
              │
              ├── daemon (Unix socket POSIX / TCP loopback Windows)
              │     holds CDP websocket to local Chrome or Cloud
              ├── src/browser_harness/   (protected)
              └── $BH_HOME/agent-workspace/agent_helpers.py  (agent-writable)
```

| Piece | Role |
|---|---|
| `browser-harness` (`run.py`) | CLI: stdin scripts, `--doctor`, `skill`, `auth`, `recordings`, `telemetry`, `--update` |
| `daemon.py` | Long-lived CDP WS holder + IPC relay. One daemon per `BU_NAME` |
| `helpers.py` | `cdp`, `new_tab`, `goto_url`, `page_info`, `click_at_xy`, `js`, `list_tabs`, …; loads agent helpers last |
| `admin.py` | `ensure_daemon`, doctor, update-from-PyPI, `start_remote_daemon` / `stop_remote_daemon` |
| `paths.py` | State: `BH_HOME` / `BROWSER_HARNESS_HOME` else `$XDG_CONFIG_HOME/browser-harness` else `~/.config/browser-harness` (mode 0700) |
| MCP extra | `browser-harness-mcp` via extra `mcp==2.1.1`; 22 tools prefixed `browser_` over stdio (`docs/MCP.md`) |
| Local CDP probe | `127.0.0.1:9222` and `:9223` `/json/version` must expose `webSocketDebuggerUrl` |

### Contrast vs other vault products

| | Browser Harness | Herdr | CloakBrowser | Jev Ultrafast |
|---|---|---|---|---|
| Owns | CDP connection + helper CLI | PTYs of *whatever* CLI | Stealth Chromium binary | Indexed action policy |
| Loop | Unchanged (host agent) | Unchanged | Unchanged | TypeSafe + text LLM |
| Writes | `agent_helpers.py` | nothing about the browser | fingerprints | nothing (executor is code) |

## Why it matters for `pro/plan`

- This Linux Hermes host already exposes a **Browser Use-shaped** `browser_exec` tool (same helper names, `BH_AGENT_WORKSPACE`, AX-tree-first). Ingest is **reference**; do not `uv tool install` a second copy.
- Efficiency: one reusable CDP lane vs screenshot-only computer-use ([[wiki/concepts/efficiency-metric]]).
- Causal split: «browser failed» is not one cause — missing `chrome://inspect` tick, stale daemon, Snap Chromium, Cloud timeout, or a domain skill that was never enabled ([[wiki/concepts/causal-analysis]]).
- Safety: local Chrome = the user's logged-in profile. Login walls: stop. Telemetry may ship the *task string*. Cloud browsers bill until `stop_remote_daemon`.
- Adjacent 1M / software-factory: browser I/O is a **tool backend**, not a new identity/harness ([[25_Projects/1M_Strategy/Links]]).

## Status

- Ingest depth: README `main` + SKILL.md + install.md + AGENTS.md + CLAUDE.md + pyproject **0.1.13** + plugin.json **0.1.0** + MCP.md + sampled `run.py` / `helpers.py` / `daemon.py` / `admin.py` / `telemetry.py` / `paths.py` / `mcp_server.py` + GitHub API repo/release/tags/commits/org/recursive tree. **Not executed. Not installed.**
- Confidence: **high** on versions/tree/CLI surface (files + API); **medium** on Cloud billing/live-view (docs only); **author claim** on «you will never use the browser again».
- This host: `browser-harness` **not on PATH**. Leftover `~/.config/browser-harness/version-cache.json` (2026-09-01, `banner_shown_on` only) is not an install.

## Links

- Entity: [[wiki/entities/browser-use]]
- Concept: [[wiki/concepts/self-healing-cdp-harness]]
- Sibling policy agent: [[wiki/sources/jev-ultrafast]]
- Tool card: [[10_Reference/tools/browser-harness]]
- Adjacent browser notes: [[10_Reference/tools/cloakbrowser]]

## Sources / provenance

- Repo https://github.com/browser-use/browser-harness (`main` @ `afbcc381b963`, 2026-09-18)
- GitHub README sha256 `ee3cdce98e1163125222e61895228faeb188b100b61347369923be250105aab9` (2952 bytes, LF). After cron image localization the durable body is 2936 bytes, sha256 `1bc61f1ce063cb01bacf833a3a170dde5e87c283b07e88d524bb41bbe11e7089` (frontmatter still records the GitHub sha).
- PyPI https://pypi.org/pypi/browser-harness/json **0.1.13**
- Do not cite npm `browser-harness@0.0.58` as this product
