# Browser Use

| Field | Value |
|---|---|
| Type | Company / GitHub org (browser infrastructure for agents) |
| GitHub org | [browser-use](https://github.com/browser-use) — created 2024-12-17; **57** public repos; **4190** followers; verified (org API 2026-09-18) |
| Site | https://browser-use.com |
| Cloud | https://cloud.browser-use.com |
| X | [@browser_use](https://x.com/browser_use) (org `twitter_username`) |
| First wiki sources | [[wiki/sources/browser-harness]], [[wiki/sources/jev-ultrafast]] |
| License (these two repos) | MIT, «Copyright (c) 2026 Browser Use» |

## Relevance

- Publisher of **Browser Harness** (CDP CLI + writable `agent_helpers.py`) and **Jev Ultrafast** (indexed action-space policy on top of that CLI).
- Distinct from vault stealth-browser notes ([[10_Reference/tools/cloakbrowser]]): CloakBrowser patches Chromium; Browser Use attaches to *the user's* Chrome or hosts Cloud Chrome.
- Distinct from harness vendors ([[wiki/entities/deepseek]], [[wiki/entities/herdr]], [[wiki/entities/prime-intellect]], [[wiki/entities/cursor]]). Owns **browser I/O**, not the agent loop.
- Product `browser-use/browser-use` (Python agent library) is already a URL on [[10_Reference/tools/web-scraping-open-source-tools]] — **not** ingested as a wiki source here.

## What this vault currently knows

- Browser Harness **v0.1.13** (PyPI + GitHub 2026-09-04). HEAD `afbcc381b963` (2026-09-07). Stars **17663** (API 2026-09-18). Repo created 2026-04-17.
- Jev Ultrafast pyproject **0.1.0**, no tags. HEAD `452c1ad2dd62` (2026-09-17). Stars **3316**. Repo created 2026-09-16. Pins `browser-harness==0.1.13`.
- This Hermes host: CLI **not on PATH**. `browser_exec` tool already speaks a Browser Use-shaped helper API — reference only, no second install.

## Related

- Sources: [[wiki/sources/browser-harness]], [[wiki/sources/jev-ultrafast]]
- Concepts: [[wiki/concepts/self-healing-cdp-harness]], [[wiki/concepts/indexed-action-space]]
- Tools: [[10_Reference/tools/browser-harness]], [[10_Reference/tools/jev-ultrafast]]
- Contrast: [[wiki/entities/herdr]], [[wiki/entities/deepseek]], [[wiki/entities/prime-intellect]], [[wiki/entities/cursor]]

## Sources

- [[wiki/sources/browser-harness]]
- [[wiki/sources/jev-ultrafast]]
