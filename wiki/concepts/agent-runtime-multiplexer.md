# Agent-runtime multiplexer

## Definition (working)

A **runtime** for coding agents is a background server that owns real terminal processes (PTYs). Every UI — TUI, CLI, SSH, phone, future desktop/web — is a **client**. Quitting the viewer must not kill the herd. The runtime also knows which panes are agents and whether each is `working`, `blocked`, `done`, or `idle`, so wait/notify is semantic, not «process up».

Canonical public case in vault: [[wiki/sources/herdr]].

## Mechanism (from Herdr docs)

```
client attach  →  render + input
client detach  →  server keeps PTYs
server restart →  layout snapshot; processes gone
                 + optional native agent --resume
                 + optional pane-history replay (secrets risk)
live handoff   →  experimental: move live PTYs to a new server
```

Detection stack:

1. Foreground process (who is in the pane).
2. If a **lifecycle integration** is installed and reporting → it is the sole status authority.
3. Else **screen manifest** on the live bottom-buffer snapshot (not the scrolled viewport).
4. No matching blocked rule for a known agent → `idle` fallback, not guessed `blocked`.

`done` vs `idle` is a **seen** bit from the focused UI, not a different process state. CLI `agent read` does not mark seen.

## Contrast

| Style | Owns | Agents if the window dies | Loop |
|---|---|---|---|
| Privileged coding CLI (Claude Code, Hermes, Codex) | The agent process | Dies with the terminal unless something else owns the PTY | The product |
| Plugin harness ([[wiki/concepts/everything-is-a-plugin]]) | Composition of loop/tools/UI | Depends on the host process | Loop is a plugin (DSH claim) |
| Playbook-routed mode ([[wiki/concepts/playbook-routed-agent-mode]]) | Style on an existing IDE loop | Dies with the IDE | Unchanged (pstack on Cursor) |
| Classic multiplexer (tmux / Zellij) | PTYs | Survive detach | No agent semantics |
| Manager / dashboard app | A window | Usually die with the app | External |
| **Agent-runtime multiplexer** | PTYs **and** agent state | Survive detach | Unchanged; runtime waits on `blocked` |

Status of «Herdr is strictly better than tmux for this host»: **Hypothesis** until installed and smoked.

## Causal map

| Cause | Effect |
|---|---|
| Server owns PTYs, UI is a client | Close laptop ≠ kill six-hour job |
| Semantic `blocked` from approval UI | No pane-by-pane hunting; waits don't fire keystrokes hoping |
| Strict blocked rules | Novel prompts show `idle` (false negative), not false `blocked` that auto-answers |
| Lifecycle hook vs screen dual-source | Two authorities fight; Herdr forbids screen fallback while a lifecycle source reports |
| `pane_history = true` | Restart shows the last screen **and** persists secrets/tokens |
| Plugin = argv as your user | Marketplace convenience; no sandbox — treat like an editor extension |
| Nested tmux inside a Herdr pane | Detector sees `tmux`, not the agent behind it |
| Calling Herdr CLI without `HERDR_ENV=1` | Skill forbids it: you don't own that session |

## Why it matters for `pro/plan`

- 1M / software-factory long jobs need this layer even if the loop stays Hermes/Claude/Codex ([[25_Projects/1M_Strategy/Architecture]]).
- Efficiency: one glance at blocked vs polling terminals ([[wiki/concepts/efficiency-metric]]).
- Safety: do not auto-send into `blocked`; do not enable pane history as default; do not pipe-install plugins from untrusted GitHub.
- Hermes is already in Herdr's agent table — integration is a config write under `~/.hermes`, not a new product.

## Related

- Source: [[wiki/sources/herdr]]
- Entity: [[wiki/entities/herdr]]
- Tool: [[10_Reference/tools/herdr]]
- Adjacent: [[wiki/concepts/everything-is-a-plugin]], [[wiki/concepts/playbook-routed-agent-mode]], [[wiki/concepts/human-in-the-loop-gtm]] (blocked pane still needs a human on approvals)

## Sources

- [[wiki/sources/herdr]]
