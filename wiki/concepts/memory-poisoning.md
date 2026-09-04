# Memory poisoning (ASI06)

## Definition (working)

Атака, при которой **вредоносный текст попадает в persistent memory агента** (notes, goals, tool observations, identity keys) и на следующих ходах читается как privileged context. Переживает reset окна контекста, потому что память — не контекст.

OWASP слот: **ASI06 — Memory & Context Poisoning**. Reference impl в vault: [[wiki/sources/owasp-agent-memory-guard]].

## Why input filters miss it

```
user prompt  →  (maybe filtered)  →  model
memory store →  injected on next turn as "what we already know"
                 ↑ attacker only needed one successful write
```

Причины write'а могут быть легитимными с виду: tool output, RAG chunk, другой агент, сам агент («self-reinforcement»).

## Control pattern (from AMG)

1. **Mediate every write** (and sensitive reads) — не доверять store.
2. **Classify source:** `external_tool` / `user_input` / `agent_authored` / `system`.
3. **Detect** injection, leakage, protected-key tamper, size/churn, self-similar self-writes, tool-abuse.
4. **Act via policy:** allow / redact / quarantine / block — не один boolean.
5. **Integrity + rollback:** hash immutable keys; snapshots to known-good.
6. **Emit events** for SIEM; TTL/`retire_if` for tool observations.

## Causal map

| Cause | Effect |
|---|---|
| Memory write without policy | Next-turn instruction override / exfil / tool hijack |
| Treating tool output as trusted memory | Primary injection vector (AMG LangChain middleware thesis) |
| Agent rewriting its own goal/notes unchecked | Self-poisoning loop |
| No provenance on writes | Cannot correlate or retire untrusted classes |
| Prompt-only guardrails | False safety: attack lives past the prompt |

## Vault / Hermes implications

- `memories/USER.md`, `SOUL.md`, wiki ingest, cron outputs — все write-once-then-trusted surfaces.
- [[wiki/concepts/human-in-the-loop-gtm]] закрывает *send*; этот концепт закрывает *remember*.
- [[wiki/concepts/efficiency-metric]]: дешёвый local gate vs хвост инцидента; Safety в формуле не ноль.
- Не ставить AMG в прод Hermes на одном README; сначала карта write-path'ов.

## Status

- `Confirmed` as a named OWASP ASI06 class and as AMG's problem statement.
- `Hypothesis` that AMG's 92.5% / 0% FPR generalizes beyond their 55-payload set.
- `Unknown` how well regex/heuristic detectors hold against adaptive attackers.

## Sources

- [[wiki/sources/owasp-agent-memory-guard]]
- Related: [[wiki/entities/owasp]], [[10_Reference/tools/owasp-agent-memory-guard]], [[wiki/concepts/causal-analysis]], [[wiki/concepts/efficiency-metric]], [[wiki/concepts/continual-harness]] (Prime Agent `/refine` is a first-class self-write; Factorio RCON cheat skills are the cautionary case), [[wiki/concepts/mcp-tool-broker]] (same MCP family, opposite trust: AMG gates writes; HexStrike weaponizes CLIs)
