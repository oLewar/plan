# HexStrike AI

Offensive **MCP + Flask broker** for pentest CLIs (nmap, nuclei, sqlmap, hydra, …). Two Python files. The LLM is the MCP *client*; in-tree «AI agents» are classes + score tables, not models.

- Full wiki source: [[wiki/sources/hexstrike-ai]]
- Entity: [[wiki/entities/0x4m4]]
- Concept: [[wiki/concepts/mcp-tool-broker]]
- GitHub: https://github.com/0x4m4/hexstrike-ai
- Site: https://www.hexstrike.com/ (GitHub redirect at ingest)
- License: MIT · README **v6.0** · **no tags/releases** · HEAD `d689933` (2026-08-03)
- Stars: **11529** (GitHub API 2026-09-04)

## Install (docs; not run here)

```bash
git clone https://github.com/0x4m4/hexstrike-ai.git
cd hexstrike-ai
python3 -m venv hexstrike-env
source hexstrike-env/bin/activate
pip3 install -r requirements.txt   # flask, fastmcp, selenium, pwntools, angr, …
# 125+ Kali-style binaries are separate
python3 hexstrike_server.py          # Flask; code does app.run(host="0.0.0.0", port=8888)
python3 hexstrike_mcp.py --server http://127.0.0.1:8888
```

MCP snippet (`hexstrike-ai-mcp.json`): `command: python3`, `args: [hexstrike_mcp.py, --server, http://IPADDRESS:8888]`, `timeout: 300`, `alwaysAllow: []`.

## Hermes / Chappy

Native MCP could physically point at this server. **Do not.** At ingest: **reference only**.

Would expose: ~149 MCP tools including `execute_command` (arbitrary `shell=True`), `execute_python_script`, file CRUD, hydra/sqlmap/msfvenom. Flask has **no auth**. Bind in code is **0.0.0.0** despite env default `HEXSTRIKE_HOST=127.0.0.1`.

Do not write `~/.hermes/config.yaml` `mcpServers.hexstrike-ai`. Do not clone onto this host for «tryout». Authorized use, if ever: dedicated VM, loopback-only patch, drop generic command/file/python tools, written RoE.

## Operating constraints

- README 24× / 98.7% / v7.0 «250+ agents» / desktop app: **author claims**, not in tree.
- Legal: README itself lists unauthorized testing as prohibited. Hermes policy: no exploits, no attacking systems.
- `pickle` in tree is for *generating* deserialization payloads, not a confirmed pickle-load RCE in the server — still an offensive module.
- Health inventory ≈ **125** binaries; MCP unique tools **149**; Flask routes **156**. Do not quote «150+» as a single measured count.
