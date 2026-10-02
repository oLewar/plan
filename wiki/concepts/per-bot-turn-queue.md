# Per-bot turn queue

One actor per named bot. It owns that bot's coding-agent process and runs **one turn at a time**. The agent is someone else's loop, spoken over ACP. The queue is the product.

Public case: [[wiki/sources/codync|Codync]] `host/src/agent/bot.rs`. Not a harness axis.

## Causal split

| What you see | What it is |
|---|---|
| A bot «working» | `Actor.turn` is set; `next_in_queue` will not start another item |
| Several messages sent while it works | Folded into **one** next prompt if they share a lane (`\n\n`) |
| A bot asking another bot | A separate queue item. The reply is **not** written into the recipient's memory (`turn_text = None`) |
| A group chat | Same: each member's main session, the group itself has no harness. Caps in `group.rs`: `MAX_ROUNDS = 3`, `MAX_REPLIES = 10` |
| The phone shows a short chat | Final reply, permissions, notices. Tool trace is a separate sheet |
| Host crashed and came back | An inflight user turn younger than **1 hour** (`STALE_RESUME_MS`) is resumed. Older is dropped. Asks, group turns, and routines are not silently resumed |
| «It knows my new instructions» | A frozen snapshot for this session, or a profile update on the **next** message. Not a write from the trajectory |

## What this is not

| Layer | Public case | What mutates |
|---|---|---|
| Loop composition | DeepSeek Harness | Which plugins are mounted |
| Style wrap | pstack | Nothing in the loop; playbook copied |
| Place / PTY | Herdr | Server-owned terminals |
| Continual supplemental H | Prime Agent | `/refine` from the trajectory |
| **Turn queue (not an axis)** | **Codync** | Who speaks next, and which transcript lane the reply lands in |

Herdr and Codync are both places in front of an existing CLI. Herdr keeps the PTY alive when the UI detaches. Codync keeps a **chat queue and a SQLite transcript**, and the phone is a client of that queue. Neither one edits the agent's prompt from the last run.

Hermes is not in Codync's `HARNESSES` (26 ids). That absence is about the built-in table only. The ACP registry is a separate, fetched list.

## Sources

- [[wiki/sources/codync]]
- Contrast: [[wiki/concepts/agent-runtime-multiplexer]], [[wiki/concepts/everything-is-a-plugin]], [[wiki/concepts/continual-harness]], [[wiki/concepts/playbook-routed-agent-mode]]
