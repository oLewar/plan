# Self-healing CDP harness

## Definition (working)

A **browser I/O layer** for agents:

- A long-lived **daemon** holds one Chrome DevTools websocket (local profile or hosted Cloud Chrome).
- The agent sends **short Python** that calls a frozen helper set (`cdp`, `new_tab`, `page_info`, `click_at_xy`, …).
- **Self-healing** means the agent may add **task-specific helpers** in a writable workspace file. The packaged core is not the edit surface.

Canonical public case in this vault: [[wiki/sources/browser-harness]]. Hermes `browser_exec` on this host already speaks the same helper names — that is a *shaped API*, not proof this CLI is installed.

## Mechanism (from Browser Harness SKILL.md + AGENTS.md + sampled Python)

```
ensure_daemon()
  → attach local Chrome (chrome://inspect tick) or Cloud CDP
agent stdin Python
  → helpers.py  +  $BH_AGENT_WORKSPACE/agent_helpers.py
core src/browser_harness/ stays protected
```

| This is | This is not |
|---|---|
| CDP connection + helper CLI | An agent loop (DSH / Prime Agent) |
| Writable `agent_helpers.py` | `/refine` of identity/memory ([[wiki/concepts/continual-harness]]) |
| One shared local Chrome lane | A PTY multiplexer ([[wiki/concepts/agent-runtime-multiplexer]]) |
| Opt-in `domain-skills/<site>/` | A typed action policy ([[wiki/concepts/indexed-action-space]]) |

## Contrast

| Style | Owns | What the model emits | Loop |
|---|---|---|---|
| Privileged coding CLI | The agent process | Tool calls | The product |
| Plugin harness ([[wiki/concepts/everything-is-a-plugin]]) | Composition of loop/tools | Whatever the mounted loop says | Loop is a plugin (DSH claim) |
| **Self-healing CDP harness** | Websocket + helpers | Python against a helper API | Unchanged; this is I/O |
| Indexed action space ([[wiki/concepts/indexed-action-space]]) | Policy on top of CDP | Operation + element index | Unchanged |
| Stealth Chromium (CloakBrowser) | Patched browser binary | Playwright-like commands | Unchanged |

Not a fifth harness axis. DSH = loop-as-plugin; pstack = style wrap; Herdr = place/PTY; Prime Agent = supplemental H. This is **browser transport**.

Status of «agent-written helpers compound into a general browser skill»: **Hypothesis** (product claim; domain-skills tree is large, not evaluated here). Status of «this host already runs this CLI»: **Refuted** (`browser-harness` not on PATH at ingest).

## Causal map

| Cause | Effect |
|---|---|
| `chrome://inspect` remote-debugging off | Daemon cannot attach; doctor reports permission-blocked |
| Second local `BU_NAME` for one sequential task | Extra Chrome Allow prompt; two controllers on one profile |
| Two agents clicking at once on one daemon | Cross-tab races; SKILL.md says serialize or use Cloud |
| Snap Chromium on Linux | DevTools not exposed the way the harness needs (`doctor --fix-snap`) |
| Telemetry left on | `cli_event` may include the task string (cap 20 000) to PostHog |
| Treating Cloud live-view URL as secret-free | URL is created even if `BH_OPEN_LIVE_URL=0`; callers must not log it |
| Domain skills off (`BH_DOMAIN_SKILLS` unset) | 97 site dirs in the repo are ignored — not a missing install |

## Why it matters for `pro/plan`

- Efficiency: AX-tree + coordinate click is cheaper than screenshot-only computer-use for form/nav work ([[wiki/concepts/efficiency-metric]]).
- Safety: local attach = the user's cookies. Login walls stop. Do not install a second CLI beside Hermes `browser_exec` without an explicit ask.
- 1M / software-factory: browser I/O is a **tool backend**, not a new identity.

## Related

- Source: [[wiki/sources/browser-harness]]
- Entity: [[wiki/entities/browser-use]]
- Tool: [[10_Reference/tools/browser-harness]]
- Adjacent: [[wiki/concepts/indexed-action-space]] (Jev *uses* this layer), [[wiki/concepts/agent-runtime-multiplexer]] (place ≠ CDP), [[wiki/concepts/continual-harness]] (trajectory CRUD ≠ helper file)

## Sources

- [[wiki/sources/browser-harness]]
