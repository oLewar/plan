# Contrastive action ranker

## Definition (working)

A decision model that embeds a **state** and each **candidate action** with separate encoders, scores them by alignment (dot product), and returns a distribution over the closed set you passed in. Typed questions are that ranker plus a softmax. The policy model does not emit new text, selectors, or tool schemas.

Canonical public case: [[wiki/sources/clm]] (Contrastive-LM, package `contrastive-lm` 0.1.0). Same HTTP wire as TypeSafe System One (`POST /v1/systemone`), which [[wiki/concepts/indexed-action-space|Jev]] also speaks. Jev is a hosted model; CLM is a local encoder plus two small heads.

## Mechanism (from `src/clm/schema.py` + README)

```
state text + question instructions
    → state encoder (frozen LLM + projection head)
candidate text for each option
    → action encoder (frozen LLM + projection head)
dot products → temperature softmax → noul | choice | score
```

Cache key is the text. A repeated action skips the encoder. A head hot-reload changes the cache generation so old projections are not reused.

| This is | This is not |
|---|---|
| Closed-set ranker / verifier | A generative agent loop |
| Local weights you serve (`clm-serve` + vLLM pooling) | Hosted `jev-latest` |
| Softmax over texts the caller wrote | A model that invents the option list |
| A drop-in for callers that already send System One questions | A fifth harness axis |

## Contrast

| Style | What the model emits | Who owns the outcome |
|---|---|---|
| Privileged CLI | tool calls / prose | The agent loop |
| Indexed action space ([[wiki/concepts/indexed-action-space]]) | one op + one observed index | Browser Harness executes; DONE still needs a checker |
| **Contrastive action ranker** | a probability over the candidates you supplied | You execute the argmax. A shield in front of it is a different system |
| Regularized harness search ([[wiki/concepts/regularized-harness-search]]) | nothing at decision time; it edits harness diffs offline | Critic + noise floor |

Not a harness axis. The four stay: loop-as-plugin (DSH), style wrap (pstack), place (Herdr), supplemental-H CRUD (Prime Agent).

Status of «CLM matches Jev and is ~9× faster»: **Hypothesis** (README chart; not reproduced). Status of «T-Rex survival 5/5 means the model plays the game»: **Refuted** for the shipped table — the planner writes Safe/Unsafe into the prompt and the shield can replace the argmax. Shipped JSON: CLM agrees with the planner **0.658**, Jev **0.987**; both survive 5/5 with the shield on.

## Causal map

| Cause | Effect |
|---|---|
| Contrastive heads on frozen embeddings | Cost is one embed per fresh text + a dot product per cached candidate, not a full generation |
| Action set reused across states | Latency drops on games and routing; a never-repeated set still pays the encoder |
| Question text includes the planner's «Best» / «Unsafe» | Agreement with the planner is not zero-shot action selection |
| Shield replaces unsafe argmax | Survival rate measures planner + model, not the model |
| Summary `shield_interventions` ≠ sum of per-seed `shield_interventions` | Quoting the summary alone mixes counters (CLM JSON: 4883 vs 364) |
| Hosted Jev on the same wire | Same client, different weights, API key, and latency |

## Why it matters for `pro/plan`

- Efficiency: ranking a closed set is cheaper than asking a chat model to invent the next action — only if the candidate list is already the decision ([[wiki/concepts/efficiency-metric]]).
- Causal hygiene: «the agent survived» splits into **planner label**, **model argmax**, **shield replacement**, **emergency save**.
- Honest steal: separate state/action caches, and never report a shielded score as the model's score. Do not install the vLLM stack on ingest.

## Related

- Source: [[wiki/sources/clm]]
- Entity: [[wiki/entities/contrastive-lm]]
- Tool: [[10_Reference/tools/clm]]
- Adjacent: [[wiki/concepts/indexed-action-space]], [[wiki/sources/jev-ultrafast]], [[wiki/sources/jev-usage-examples]], [[wiki/concepts/efficiency-metric]], [[wiki/concepts/causal-analysis]]

## Sources

- [[wiki/sources/clm]]
