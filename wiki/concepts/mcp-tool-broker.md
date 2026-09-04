# MCP tool broker (LLM → stdio → local API → subprocess)

## Definition (working)

A **protocol adapter** that turns an MCP-compatible LLM client into an operator of host-side programs:

```
model  --stdio MCP-->  broker process  --(often HTTP)-->  executor  --shell/API-->  tools
```

The model never talks to nmap/sqlmap directly. It calls named MCP tools; the broker translates each call into a command, HTTP request, or in-process function. **Whatever the executor user can do, the model can do** — unless the broker enforces allowlists, auth, sandbox, and bind address.

Canonical public case in this vault: [[wiki/sources/hexstrike-ai]]. Status of «HexStrike is an AI pentest platform with 12 LLM agents»: **Refuted** at code depth (classes + lookup tables; the only LLM is the client). Status of «MCP here is an unauthenticated shell broker»: **Confirmed** (`execute_command` → `POST /api/command` → `subprocess.Popen(shell=True)`; Flask `0.0.0.0:8888`; no `before_request` auth).

## Mechanism (HexStrike shape)

1. Client config points `command: python3 hexstrike_mcp.py --server http://HOST:8888`.
2. FastMCP registers ~150 `@mcp.tool` functions (HexStrike: 151 registrations, 149 unique).
3. Each tool is `safe_post`/`safe_get` to Flask. No bearer token in the client we read.
4. Flask wraps argv *or* takes a raw `command` string (`/api/command`).
5. Optional extras: write/run Python, file CRUD, browser Selenium, payload builders.

Sibling claims that must **not** be collapsed into «it has MCP»:

| Claim | Owner | Not the same as |
|---|---|---|
| MCP stdio exists | `hexstrike_mcp.py` / any `mcpServers` entry | The tools are safe |
| Named scanner wrappers | `/api/tools/nmap` etc. | Bounded to that binary |
| Generic command tool | `/api/command`, MCP `execute_command` | A scanner |
| «AI decision engine» | hardcoded score tables | A second model |
| Client ethics prompt | README jailbreak recipe | Server-side RoE |
| Loopback default | env `HEXSTRIKE_HOST=127.0.0.1` (printed) | Actual bind (`0.0.0.0` in HexStrike `app.run`) |

## Causal map

| Cause | Effect |
|---|---|
| MCP tool = arbitrary shell | LLM (or anyone who can speak MCP/HTTP) gets host RCE as the server user |
| Bind `0.0.0.0` + no auth | LAN/WAN clients skip the MCP client entirely and hit Flask |
| 150 wrappers + `execute_command` | Client tool-limit bypass is the *point* of v7 README copy; also the incident surface |
| Lookup tables branded as agents | Operators over-trust «autonomous AI»; refusals get socially engineered («I own the site») |
| Same MCP as a defensive server (AMG) | Protocol familiarity hides opposite trust: write-gate vs weaponize-CLI |

## Contrast

| | MCP tool broker (HexStrike) | Memory MCP ([[wiki/sources/owasp-agent-memory-guard]]) | Native Hermes MCP | Continual harness ([[wiki/concepts/continual-harness]]) |
|---|---|---|---|---|
| Trust direction | Model → host weapons | Host → memory writes | User-configured servers | Trajectory → prompt/skills |
| Failure | Unauthorized scan / RCE | Poisoned next turn (ASI06) | Whatever that server is | Self-poison / cheat skills |
| Default install here | **No** | **No** | Already a platform feature | **No** `/refine` on SOUL |

## Why it matters for `pro/plan`

- Causal hygiene: «we added MCP» is not a safety control. Name the executor, bind, auth, and whether a generic `execute_command` exists.
- Efficiency: wrapping Kali in MCP can look 10× faster on a README table; **Safety** in `Priority = (I×C×S)/Cost` goes to ~0 on a shared Hermes host.
- Hermes/Chappy: native MCP is fine for *narrow, authenticated, loopback* servers. HexStrike as shipped is the anti-pattern. Do not add it to `config.yaml` without an explicit ask + isolated VM + written authorization.
- Policy already forbids writing exploits / attacking systems regardless of ownership theater in a README.

## Status

- `Confirmed` as a pattern instantiated by HexStrike v6 tree (2026-09-04 ingest).
- `Hypothesis` that most «AI pentest MCP» READMEs share the generic-command + no-auth shape — do not generalize past this repo without a tree check.
- `Unknown` how many of the 11.5k stargazers run Flask on a public interface.

## Related

- Source: [[wiki/sources/hexstrike-ai]]
- Entity: [[wiki/entities/0x4m4]]
- Tool: [[10_Reference/tools/hexstrike-ai]]
- Adjacent: [[wiki/concepts/memory-poisoning]], [[wiki/concepts/efficiency-metric]], [[wiki/concepts/causal-analysis]]

## Sources

- [[wiki/sources/hexstrike-ai]]
