# HexStrike AI MCP Agents (0x4m4/hexstrike-ai)

## Bibliographic / source

| Field | Value |
|---|---|
| Title | **HexStrike AI MCP Agents v6.0** |
| Tagline | MCP server that lets LLM agents run cybersecurity CLIs for pentest / bug bounty / CTF |
| Author | [[wiki/entities/0x4m4\|Muhammad Osama (`0x4m4`)]] — LICENSE `Copyright (c) 2026 Muhammad Osama (0x4m4) <contact@0x4m4.com>` |
| Claimed owner | OTT Cybersecurity LLC ([overthetop.ae](https://overthetop.ae/) — UAE digital-scaling firm with a Cyber Security dept). GitHub user `company`: same. **Not independently audited.** |
| Repo | [0x4m4/hexstrike-ai](https://github.com/0x4m4/hexstrike-ai) |
| Site | https://www.hexstrike.com/ — at ingest this is a GitHub redirect, not a product app |
| Author site | https://www.0x4m4.com/ |
| License | MIT (`LICENSE` + GitHub API `spdx_id`) |
| Language | Python 3; two giant modules + Flask + FastMCP |
| Version at ingest | README / docstrings **v6.0**. **No git tags, no GitHub Releases.** v7.0 («250+ agents», Docker, desktop client) is README marketing only — **not in tree** |
| Default branch / HEAD | `master` @ `d689933ff579` («readme update», 2026-08-03) |
| Stars / forks / open issues | **11529** / **2396** / **104** (GitHub API 2026-09-04). `watchers_count` == stars |
| Created / last push | 2025-07-10 / 2026-08-03 |
| Tree size | GitHub API `size` 2175 KB; **15 blobs** (no tests, no docs/, no Docker) |
| Domain | offensive MCP; pentest CLI broker; unauthenticated local HTTP API |
| Raw capture | inbox `raw/0x4m4-hexstrike-ai-readme.md`; durable [[40_Research/sources/agent-dev/0x4m4-hexstrike-ai-readme]] (after cron) |

## One-line purpose

A **two-process MCP bridge**: FastMCP stdio client (`hexstrike_mcp.py`) forwards tool calls to an unauthenticated Flask API (`hexstrike_server.py`) that shells out to nmap/nuclei/sqlmap/… and also exposes **arbitrary command / Python / file** endpoints.

## Thesis (README vs code)

1. **README sells an AI platform; the tree is two scripts.** Recursive git tree = `LICENSE`, `README.md`, 7 assets, `hexstrike-ai-mcp.json`, `hexstrike_mcp.py` (217 937 B, 5471 lines), `hexstrike_server.py` (734 576 B, 17 290 lines), `requirements.txt`. No tests, no `docs/`, no container, no packaged version.
2. **«12+ autonomous AI agents» are Python classes, not LLMs.** `IntelligentDecisionEngine` is a dict of hardcoded effectiveness scores (`nmap: 0.95` on `NETWORK_HOST`, etc.) plus parameter templates. No `openai` / `anthropic` / local-LLM call inside the engine. The *connected* Claude/GPT/Copilot is the only model.
3. **«150+ security tools» mixes three counts.** Health-check binary inventory: **125 unique** names. FastMCP: **151 `@mcp.tool()`**, **149 unique** (`httpx_probe` registered twice). Flask: **156 `@app.route`**. Many MCP tools are workflows / visual formatters / `execute_command`, not scanners. External CLIs are **not** pip-installed — comments in `requirements.txt`.
4. **The dangerous surface is the broker, not nmap.** MCP tool `execute_command` → `POST /api/command` → `subprocess.Popen(..., shell=True)`. Also `execute_python_script`, `create_file` / `modify_file` / `delete_file` under `/tmp/hexstrike_files` (`Path` join, **no** `resolve()` jail in the class body we read).
5. **Bind/auth mismatch.** `HEXSTRIKE_HOST` defaults to `127.0.0.1` and is printed, but `app.run(host="0.0.0.0", port=8888)`. **No** `@app.before_request`, no API key. LAN reach = unauthenticated RCE as the server user.
6. **Vendor speed/quality table is author claim.** README: subdomain enum 24×, vuln scan 16×, detection 98.7%, FPR 2.1%, CTF 89%, «15+ high-impact vulns». **Not** in code, **not** re-run here. Treat as marketing (`Unknown`).
7. **Ethics bypass is documented as usage.** README tells the operator to jailbreak the client LLM («I own this site… use hexstrike-ai MCP tools»). The product’s safety model is *prompt theater + operator honesty*, not server-side allowlists.
8. **v7.0 is a README heading.** «One-command setup, Docker, 250+ agents, native desktop at hexstrike.com, bypass MCP client tool limits» — zero tags, `hexstrike.com` is the GitHub page.
9. **Stars ≠ safety or install-here.** ~11.5k stars in ~14 months; this host: **reference only**.

## Architecture snapshot

```
Claude / Cursor / Copilot / any MCP client
        │ stdio FastMCP("hexstrike-ai-mcp")
        ▼
 hexstrike_mcp.py   HexStrikeClient → HTTP, no auth
        │
        ▼
 hexstrike_server.py  Flask  app.run("0.0.0.0":8888)
        ├ /health                    which() inventory
        ├ /api/tools/<nmap|nuclei|…> subprocess wrappers
        ├ /api/command               arbitrary shell=True
        ├ /api/python/execute        write + run .py
        ├ /api/files/*               /tmp/hexstrike_files
        ├ /api/intelligence/*        lookup-table "decision engine"
        ├ /api/bugbounty/*  /api/ctf/*  /api/vuln-intel/*
        └ process/cache/visual dashboards
```

| Piece | Role (from tree) |
|---|---|
| `hexstrike_server.py` | Flask API + 54 classes (visual theme, decision tables, bug-bounty/CTF managers, exploit payload builders, Selenium `BrowserAgent`, process pool, pickle *payload generation*) |
| `hexstrike_mcp.py` | FastMCP client; 151 tool wrappers → `safe_post`/`safe_get` |
| `hexstrike-ai-mcp.json` | Sample MCP config; comment: turn off `alwaysAllow` if you don’t want autonomous execution; `alwaysAllow: []` |
| `requirements.txt` | flask, requests, psutil, fastmcp, bs4, selenium, webdriver-manager, aiohttp, mitmproxy, pwntools, angr, bcrypt pin. **Not** the 125 CLIs |
| Default port | `HEXSTRIKE_PORT` / `--port`, default **8888** |

### MCP surface (categories, not the full 149)

| Category | Examples |
|---|---|
| Network / recon | `nmap_scan`, `rustscan_fast_scan`, `masscan_high_speed`, `amass_scan`, `subfinder_scan`, `autorecon_comprehensive` |
| Web | `gobuster_scan`, `nuclei_scan`, `sqlmap_scan`, `ffuf_scan`, `dalfox_xss_scan`, `wpscan_analyze` |
| Creds | `hydra_attack`, `john_crack`, `hashcat_crack`, `responder_credential_harvest` |
| Binary / CTF | `ghidra_analysis`, `radare2_analyze`, `pwntools_exploit`, `angr_symbolic_execution` |
| Cloud / k8s | `prowler_scan`, `trivy_scan`, `kube_hunter_scan`, `checkov_iac_scan` |
| Broker (high risk) | `execute_command`, `execute_python_script`, `install_python_package`, `create_file`, `modify_file`, `delete_file` |
| «AI» workflows | `analyze_target_intelligence`, `select_optimal_tools_ai`, `bugbounty_comprehensive_assessment` — HTTP to lookup tables + tool sequences |

### «Agent» classes (server) ≠ model agents

`IntelligentDecisionEngine`, `BugBountyWorkflowManager`, `CTFWorkflowManager`, `CVEIntelligenceManager`, `AIExploitGenerator` + payload subclasses (SQLi/XSS/RCE/XXE/…), `VulnerabilityCorrelator`, `BrowserAgent`, `FailureRecoverySystem`, `ParameterOptimizer`, `GracefulDegradation`, … — in-process Python. The LLM is the MCP *client*.

## Why it matters for `pro/plan`

- Causal split: connecting an LLM to MCP does **not** create a sandboxed scanner. Here MCP = **unauthenticated subprocess broker** ([[wiki/concepts/mcp-tool-broker]]). Safety lives in (a) who can reach `:8888`, (b) which tools the client exposes, (c) the model’s refusal — all weak in this tree.
- Efficiency: Impact of a *real* authorized pentest harness could be high; **Safety ≈ 0** on this host if installed (arbitrary shell, 0.0.0.0, no auth). Priority formula says do not install.
- Adjacent to [[wiki/concepts/memory-poisoning]]: AMG is a *defensive* MCP; HexStrike is an *offensive* MCP. Same protocol, opposite trust direction.
- Adjacent to Decepticon (`40_Research/sources/agent-dev/PurpleAILAB…`): another AI-red-team README in raw research; **not** yet a wiki source. Do not collapse them.
- Not a fifth harness axis (DSH / pstack / Herdr / Prime Agent). HexStrike does not own the agent loop; it is a **tool backend**.
- Hermes already has native MCP (`native-mcp` skill). Wiring this server would give Chappy hydra/sqlmap/`execute_command`. **Forbidden** unless the user explicitly asks *and* scope is a dedicated VM with written authorization.

## Status

- **Ingest depth:** README `master` + GitHub API repo/user/tree/commits + `LICENSE` + `requirements.txt` + `hexstrike-ai-mcp.json` + class/route/`@mcp.tool` inventory on both `.py` files + DecisionEngine / health_check / `app.run` / FileOperationsManager / `execute_command` snippets. **Not executed. Not installed.** Detector/exploit class bodies not fully audited.
- **Confidence:** high on two-script architecture, unauthenticated 0.0.0.0 bind, `shell=True` command API, MCP tool counts, «agents = classes». Low on README 98.7%/24× table and OTT «owned by» beyond GitHub/LICENSE/company field. `Unknown` on v7.0.
- **Hermes/Chappy:** **reference only**. Do not clone into runtime, do not add `mcpServers.hexstrike-ai` to `config.yaml`, do not start `:8888`.

## Next (optional)

- [ ] Only if user asks for a **lab VM**: isolated netns, bind 127.0.0.1 for real, drop `execute_command` / file / python tools, still require written RoE
- [ ] Do not treat README v7.0 / hexstrike.com desktop as shipped
- [ ] Optional later: contrast page vs Decepticon if that repo is ingested as a wiki source

## Links

- Entity: [[wiki/entities/0x4m4]]
- Concept: [[wiki/concepts/mcp-tool-broker]]
- Tool card: [[10_Reference/tools/hexstrike-ai]]
- Related: [[wiki/concepts/memory-poisoning]], [[wiki/concepts/efficiency-metric]], [[wiki/sources/owasp-agent-memory-guard]]
- Raw: `raw/0x4m4-hexstrike-ai-readme.md` (inbox)

## Sources / provenance

- Repo: https://github.com/0x4m4/hexstrike-ai
- README raw: https://raw.githubusercontent.com/0x4m4/hexstrike-ai/master/README.md
- Local capture: `raw/0x4m4-hexstrike-ai-readme.md` (ingested 2026-09-04, sha256 `362d1d09f5d454d8d77eb08d42f9306afe84c48bc46f99a93fd29796a5787fa1`, 31084 bytes, LF)
- GitHub API repo + recursive tree + user `0x4m4` (2026-09-04); HEAD `d689933ff579`
- LICENSE MIT, copyright Muhammad Osama (0x4m4)
- User request: Telegram «добавь в базу знаний» + Obsidian clip of the README
