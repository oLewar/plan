# Typed IR artifact delivery (fail-closed diagrams)

## Definition (working)

A **communication artifact** pipeline where:

1. An agent authors a small **typed JSON intermediate representation** (strict schema, `additionalProperties: false`).
2. A **deterministic, zero-dependency compiler** validates schema, layout, HTML/SVG, routes, and label clearance **before** the showcase file may replace the last known good output.
3. Viewer features (search, reach, routes, stories, share cards) may only **reuse authored topology**. They must not invent edges or claim runtime impact.
4. Optional network is **notification-only** (remind, never download/install).

Canonical public case in vault: [[wiki/sources/archify]]. Status of «Archify diagrams are a faithful map of a live system»: **Hypothesis** unless repository-evidence gates (`--repo-root` + commit SHA) actually passed. Status of «deliver is fail-closed»: **Confirmed** at README/SKILL/CHANGELOG depth, not executed here.

## Mechanism (from Archify SKILL + README)

```
candidate JSON
    │
    ├─ validate --json     → one receipt; diagnostics[].supportedFixes only
    ├─ two repair rounds   → stop if objective error count does not improve
    ├─ deliver             → snapshot bytes → render → check → atomic rename
    │                         failure: delete candidate, keep previous HTML
    └─ visual-check        → browser measurements; visualReview stays pending
```

Sibling claims that must **not** be collapsed into «the diagram is good»:

| Claim | Owner | Not the same as |
|---|---|---|
| Schema/layout/artifact gates | `validate` / `deliver` | Looks pretty |
| Bounded viewport evidence | `visual-check` | Human perceptual pass |
| Authored reach / route | viewer, from IR | Blast radius / outage impact |
| Architecture Delta | `compare` on two snapshots | Merge safety / PR risk |
| Update notice | GET stable manifest | Auto-patch the skill |

## Why it matters for `pro/plan`

- Causal hygiene: a wrong architecture slide is a **false causal map**. Fail-closed delivery is the diagram analog of evidence gates on code (pstack prove-it-works, AMG write-gate).
- Efficiency: one HTML + 1200×630 card vs rewriting Mermaid until it «looks ok». Cost is Node 18+ and two repair rounds; hosted editors are out of scope on purpose.
- Safety: update checker must stay reminder-only; DSH bundle pinning **2.14** while HEAD is **2.16** is a real drift — do not assume `dsh plugin add` equals latest skill.
- This host: concept is portable; **skill is not installed**.

## Contrast

| | Typed IR delivery (Archify) | Mermaid-in-markdown | Continual harness ([[wiki/concepts/continual-harness]]) | Plugin loop ([[wiki/concepts/everything-is-a-plugin]]) |
|---|---|---|---|---|
| Source of truth | Versioned JSON + schemas | Prose + renderer heuristics | Trajectory → memory/skill | Config rows + plugins |
| On failure | Keep last-good HTML | Partial/broken render | Poisoned next turn (ASI06) | Unload effects |
| Invents topology? | Forbidden | Easy | n/a | n/a |

## Related

- Source: [[wiki/sources/archify]]
- Entity: [[wiki/entities/archify]]
- Tool: [[10_Reference/tools/archify]]
- Adjacent: [[wiki/concepts/efficiency-metric]], [[wiki/concepts/causal-analysis]], [[wiki/concepts/everything-is-a-plugin]], [[wiki/concepts/playbook-routed-agent-mode]] (verbatim gates vs pretty output)

## Sources

- [[wiki/sources/archify]]
