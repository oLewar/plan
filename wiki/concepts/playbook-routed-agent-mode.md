# Playbook-routed agent mode

## Definition (working)

Agent control style where **one sticky mode** sits on the conversation, **matches the task to a named playbook**, copies that playbook's steps **verbatim** into the todo list, and **routes other skills** as those steps fire. Situational slash commands still exist, but they are not the default entry.

Canonical public case in vault: [[wiki/sources/pstack]] (`/poteto-mode`).

## Mechanism (from pstack)

```
user goal + checkable outcome  (plain language; need not name a playbook)
    → sticky mode matches a playbook
    → todo[0] = read principles index
    → remaining todos = playbook steps copied verbatim
    → skip only with `skip: <reason>`
    → situational skills (how / architect / tdd / interrogate / …) fire per step
    → subagents of a typed wrapper (poteto-agent), models picked per role
    → prove against the real artifact, then shared closer (open PR)
```

Sticky: stays on across turns when a playbook matches or the task needs rigor; stays out of casual turns; user can opt out in language.

## Design split vs neighboring styles

| Style | Entry | Who owns process | Loop |
|---|---|---|---|
| Playbook-routed mode (pstack) | one sticky `/mode` | playbooks + named principles | wraps host loop (Cursor) |
| Composable skills ([[wiki/sources/mattpocock-skills]]) | user-invoked orchestrate; model-invoked discipline | small editable skills; user-invoked must not call other user-invoked | wraps host loop (Claude/Codex) |
| Plugin harness ([[wiki/concepts/everything-is-a-plugin]]) | profiles + bundles + patches | runtime composition; unload unwinds | **loop is a plugin** |
| HITL GTM ([[wiki/concepts/human-in-the-loop-gtm]]) | schedule + skill + KB | human on every send | drafts, does not ship to customer |

## Causal map

| If missing | Failure mode |
|---|---|
| No playbook match / bespoke plan after reading | Named gates (`architect`, throughput checkpoint, prove-it-works) silently drop |
| Silent skip | Reviewer cannot see which rigor was declined |
| `generalPurpose` instead of typed wrapper | Principles index never read; style drifts |
| One model for code + prose + review | Weak instruction-following on specified sequences, or weak judgment on design |
| Proxy verification («it compiles», self-report) | False done; overnight runs ship slop |
| Import `never-block-on-the-human` into customer send | Brand/legal risk (GTM anti-pattern) |

## Why it matters for `pro/plan`

- Template for any coding-agent surface (Hermes/Chappy, Cursor, Claude Code): **goal + checkable outcome** is enough routing signal; the mode picks the playbook.
- Matches efficiency rubric: cost of a skipped evidence gate is huge (false done), so copying steps verbatim is cheap insurance.
- 21 named principles are a steerable mid-task vocabulary («laziness-protocol», «prove-it-works») without rewriting the prompt.
- Status: `Confirmed` as pstack's published design; `Hypothesis` that the same router works unchanged outside Cursor's `Task` / plugin runtime.

## Related

- Source: [[wiki/sources/pstack]]
- Tool: [[10_Reference/tools/pstack]]
- Neighbors: [[wiki/sources/mattpocock-skills]], [[wiki/concepts/everything-is-a-plugin]], [[wiki/concepts/human-in-the-loop-gtm]], [[wiki/concepts/agent-runtime-multiplexer]]
- Entities: [[wiki/entities/lauren-tan]], [[wiki/entities/cursor]]

## Sources

- [[wiki/sources/pstack]]
