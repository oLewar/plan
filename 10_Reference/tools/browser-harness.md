# Browser Harness

CDP **browser I/O** for agents: daemon holds one Chrome websocket; stdin Python calls pre-imported helpers. Core package frozen; task helpers go in `agent_helpers.py`.

- Full wiki source: [[wiki/sources/browser-harness]]
- Entity: [[wiki/entities/browser-use]]
- Concept: [[wiki/concepts/self-healing-cdp-harness]]
- Policy that sits on it: [[wiki/sources/jev-ultrafast]]
- GitHub: https://github.com/browser-use/browser-harness
- Site / cloud: https://browser-harness.com · https://cloud.browser-use.com
- License: MIT
- Version at ingest: **v0.1.13** (PyPI + GitHub 2026-09-04); HEAD `afbcc381b963` (2026-09-07); stars **17663** (API 2026-09-18)
- State dir: `~/.config/browser-harness` (`BH_HOME` / `BROWSER_HARNESS_HOME`)
- Local CDP probe: `127.0.0.1:9222` / `:9223` `/json/version`

## Install (docs; not run here)

This Linux Hermes host has **no** `browser-harness` on PATH. Do not `uv tool install` unless explicitly asked. Hermes `browser_exec` already uses the same helper names.

```bash
uv tool install --python 3.12 --upgrade --force browser-harness
browser-harness skill > "${CODEX_HOME:-$HOME/.codex}/skills/browser-harness/SKILL.md"
browser-harness --doctor
```

Cloud is optional (`browser-harness auth login`). Local Chrome needs the `chrome://inspect/#remote-debugging` tick.

```bash
browser-harness <<'PY'
print(page_info())
PY
browser-harness telemetry disable
```

Optional MCP: `uvx --from 'browser-harness[mcp]' browser-harness-mcp` (22 `browser_*` tools).

## Hermes / Chappy

At ingest: **reference only**. Do not write `~/.hermes/config.yaml`, do not register MCP, do not enable domain skills (`BH_DOMAIN_SKILLS=1`).

Honest steal: AX-tree → box → `click_at_xy`; one default daemon; serialize local tab work; login walls stop.

## Operating constraints

- Telemetry opt-out PostHog EU; `cli_event` can include the task string. `HERMES_SESSION_ID` is detected as client `hermes`.
- Snap Chromium on Linux: `browser-harness doctor --fix-snap`.
- Plugin.json **0.1.0** ≠ PyPI **0.1.13**. npm `browser-harness@0.0.58` is a different package.
- AGENTS.md skill identity string `browser-use` vs SKILL.md `name: browser-harness` — **Unknown** which a host matches.
- Domain-skills tree (97 sites) is off unless `BH_DOMAIN_SKILLS=1`.

## Mental model

**Browser transport**, not an agent loop. Contrast loop-replace ([[wiki/concepts/everything-is-a-plugin]]), style wrap ([[wiki/concepts/playbook-routed-agent-mode]]), PTY runtime ([[wiki/concepts/agent-runtime-multiplexer]]), `/refine` ([[wiki/concepts/continual-harness]]), typed ops ([[wiki/concepts/indexed-action-space]]).
