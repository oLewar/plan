# Regularized harness search

## Definition (working)

Test-time search that proposes **component-wise edits of an agent harness** around a **frozen** model, then accepts an edit only if it clears a leakage screen, a noise floor, and a token-cost rule. The edit space stays open. The constraints are on the *search trajectory* (how many edits one candidate may bundle, which hypotheses may be redrawn, what counts as a gain).

Canonical public case: [[wiki/sources/rrsi]] (Google Research, arXiv:2609.24972). Not the same object as [[wiki/concepts/continual-harness]] (`/refine` writes next-turn supplemental state with no measured floor).

## Mechanism (from `rrsi/selection.py` + `rrsi/schedule.py`)

```
H_t  (incumbent = commit on evolve/<domain>)
  → Analyze failures
  → draft m candidates, each with at most b_t edits
       b_t anneals from b_max toward b_min (cosine)
  → critic rejects leakage / grader-gaming / undeclared bundles
  → Evaluate on the full evolve set (missing trial = 0)
  → admissible iff
       S' >= S* - delta
       and cost rule
       and domain guards
  → H_{t+1} = argmax S' among admissible, else H_t
  → fast-forward the branch
```

Cost rule (`selection.cost_rule`):

- If `ΔS > delta`: relative token change `ΔC` must be `≤ beta0 + beta1·ΔS`.
- Else: `w_s·ΔS - w_c·ΔC + w_n·ν > 0`, where `ν` counts structural component types (tool / skill / memory / subagent) the incumbent has never accepted.

Coding instance sets `w_s = 0`: inside the noise band a score bump alone cannot win. A token saving or a new structural component can.

Declared component tags are not trusted. `components.normalize` keeps a tag only when the diff contains evidence for it.

| This is | This is not |
|---|---|
| Offline search over harness diffs, gated by measurement | `/refine` CRUD of the next prompt |
| Frozen policy model | Training the backbone |
| Critic *before* the expensive eval | A style playbook copied verbatim |
| Git worktree per candidate; incumbent is a commit | A fifth agent-loop product |

## Contrast

| Style | What mutates | Who authorizes |
|---|---|---|
| Privileged CLI (Hermes / Claude Code / Codex) | skills/hooks around a frozen loop | Human / config |
| Plugin harness ([[wiki/concepts/everything-is-a-plugin]]) | which plugins are mounted | Human profile/patch |
| Playbook-routed mode ([[wiki/concepts/playbook-routed-agent-mode]]) | nothing in the loop; steps are copied | Human sticky `/mode` |
| Continual harness ([[wiki/concepts/continual-harness]]) | supplemental H from the trajectory | Agent + `/refine` (weak write-gate) |
| Git-native experiment tree ([[wiki/concepts/git-native-experiment-tree]]) | child *code* branches after a measured node | Human/agent creating a child |
| **Regularized harness search** | a candidate harness diff | Critic + noise floor + token budget; else keep `H_t` |
| Self-healing CDP harness ([[wiki/concepts/self-healing-cdp-harness]]) | `agent_helpers.py` only | Agent, scoped to browser workspace |
| Indexed action space ([[wiki/concepts/indexed-action-space]]) | nothing; policy is code | Human running Jev |

Not a fifth harness axis. The four stay: loop-as-plugin (DSH), style wrap (pstack), place (Herdr), supplemental-H CRUD (Prime Agent).

Status of «RRSI beats ungated `/refine` on OOD coding»: **Hypothesis** (author table: ID gains shrink but do not all vanish; not reproduced here). Status of «point this loop at Hermes SOUL/memories»: **Refuted** as a plan — the critic exists because evolving on the same tasks you care about overfits.

## Causal map

| Cause | Effect |
|---|---|
| Unregularized harness RSI on the evolve set | Large ID gain that shrinks or vanishes OOD (paper claim) |
| Annealed `b_t` | Early rounds may bundle edits; late rounds are sparse and attributable |
| Critic denylist + LLM leakage screen | Task-id / grader-gaming diffs never spend an eval |
| `S' < S* - delta` | Within-noise «wins» do not move the incumbent |
| Coding `w_s = 0` | A small score bump cannot pay for itself inside the band |
| Missing trial counted as 0 with full denominator | A crashed eval cannot look like a partial success |
| Tag not backed by the diff | Proposer cannot relabel a prompt tweak as an untried skill to fill an exploration slot |
| `/refine` without this gate | Previous trajectory becomes next privileged prompt ([[wiki/concepts/memory-poisoning]]) |

## Why it matters for `pro/plan`

- Efficiency: rejecting a harness edit *before* another full eval, and refusing within-noise score bumps, is cheaper than celebrating a +0.5 that is the estimator ([[wiki/concepts/efficiency-metric]]).
- Causal hygiene: «the harness improved» is not one cause. Split **leakage**, **noise**, **token-expensive real gain**, **structural novelty inside the band**.
- Honest steal: the edit ledger (component, hypothesis, ΔS, ΔC, verdict) and the critic checklist. Do not install the Vertex loop onto Chappy.

## Related

- Source: [[wiki/sources/rrsi]]
- Entity: [[wiki/entities/google-research]]
- Tool: [[10_Reference/tools/rrsi]]
- Adjacent: [[wiki/concepts/continual-harness]], [[wiki/concepts/git-native-experiment-tree]], [[wiki/concepts/memory-poisoning]], [[wiki/concepts/everything-is-a-plugin]], [[wiki/concepts/causal-analysis]], [[wiki/concepts/efficiency-metric]]

## Sources

- [[wiki/sources/rrsi]]
