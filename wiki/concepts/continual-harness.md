# Continual harness

## Definition (working)

A harness whose **supplemental state** (prompt notes, memories, skill descriptions, subagent specs) is durable, CRUD-able by the running agent, and refined from the agent's **own trajectory** — without rewriting the immutable base system prompt. Distinct from (a) a plugin-replaceable *loop* and (b) a sticky human playbook copied verbatim.

Canonical public case in vault: [[wiki/sources/prime-agent]] (`/refine` + `rlm.harness`). Paper framing: Continual Harness arXiv:2605.09998 (cited by PI; that paper itself **not** ingested).

## Mechanism (from Prime Agent docs/blog)

```
trajectory (JSONL + kernel)
    → /refine or refine.run("…")
        plan (background LLM; does not block chat)
        apply (small CRUD write; rebuilds supplemental prompt at turn boundary)
    → disk + kernel `rlm.harness`
rollback by refinement snapshot id
base system prompt stays frozen
```

Formalism used by PI: H = (ρ, G, K, M) — prompts, subagents, skills, memory. Same create/read/update/delete surface for each kind.

| This is | This is not |
|---|---|
| Evidence-backed *small* edit to supplemental state | Rewriting the constitution / SOUL every turn |
| Skill *description* / contract in harness state | Packaging a new executable Python skill (`skill-creator`) |
| Programmatic REPL as the model tool | Fixed JSON tool schema per capability |
| Daemon worker owning the session | A multiplexer owning someone else's PTY ([[wiki/concepts/agent-runtime-multiplexer]]) |

## Contrast

| Style | What mutates | Who authorizes |
|---|---|---|
| Privileged CLI (Hermes / Claude Code / Codex) | skills/hooks around a frozen loop | Human / config |
| Plugin harness ([[wiki/concepts/everything-is-a-plugin]]) | which plugins are mounted | Human profile/patch |
| Playbook-routed mode ([[wiki/concepts/playbook-routed-agent-mode]]) | nothing in the loop; steps are copied | Human sticky `/mode` |
| **Continual harness** | supplemental H from trajectory | Agent + `/refine` (rollback exists; write-gate is weak) |

Status of «self-refine beats hand-written skills in production coding»: **Hypothesis** (author evals; Factorio also refined a *cheat*).

## Causal map

| Cause | Effect |
|---|---|
| REPL holds working context as variables | Long tasks spend tokens on *compute*, not re-reading blobs |
| `rlm()` returns admission handle, not the answer | Parent context stays small; results via messages/files |
| `/refine` writes memory/skill from failures | Next-turn privileged context changes — ASI06 surface ([[wiki/concepts/memory-poisoning]]) |
| Same loop, no write-gate | Factorio: RCON cheat became a stored skill despite anti-cheat heartbeat |
| Immutable base prompt | Rollback of supplemental layer is defined; identity layer is not self-edited |
| Worker ≠ sandbox | Model-generated Python = user perms |

## Why it matters for `pro/plan`

- Efficiency: persist a *lesson* instead of re-deriving it ([[wiki/concepts/efficiency-metric]]) — only if the write is gated.
- Direct warning for Hermes memories / SOUL / wiki ingest: trajectory-authored updates need the same reject-ledger as GTM, not «the agent learned so it must be true».
- 1M eval runtime: autonomous + goal + heartbeat is the research shape; copying `/refine` onto Chappy identity files is the expensive failure.

## Related

- Source: [[wiki/sources/prime-agent]]
- Entity: [[wiki/entities/prime-intellect]]
- Tool: [[10_Reference/tools/prime-agent]]
- Adjacent: [[wiki/concepts/memory-poisoning]], [[wiki/concepts/everything-is-a-plugin]], [[wiki/concepts/agent-runtime-multiplexer]], [[wiki/concepts/playbook-routed-agent-mode]]

## Sources

- [[wiki/sources/prime-agent]]
