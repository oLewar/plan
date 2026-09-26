# Supplied-option ranker (score the answers you wrote)

## Definition (working)

A **supplied-option ranker** reads a state and a closed list of answers and returns one of them, with a score per slot. It does not write the answer. If the right fact is not among the options, the model cannot supply it — the evaluations do not test that.

Three public speakers of the same question dictionary (`choice` / `score` / `noul`), three different machines:

| | Machine | Wire | Weights |
|---|---|---|---|
| TypeSafe Jev | hosted System One | `POST /v1/systemone` | not local |
| [[wiki/sources/clm\|CLM]] | frozen Qwen3-8B + two contrastive heads, dot product | same HTTP wire | local |
| [[wiki/sources/julia-1\|Julia 1]] | mmBERT-small (ModernBERT, MIT) + a 2-layer marker head | Python `engine.predict` — **no** System One HTTP in the repo | local, Apache-2.0, 144.3M, 550.5 MiB |

`score` on Julia is an expected index (a float), not an argmax. `noul` is P(true) with false/true fixed. A native call takes 2–20 options. Longer lists go through a Router that narrows first; the survivors' softmax is not a distribution over the original list.

```
state + question + options you wrote
        │
        ├─ right answer in the list, short list  → the accuracy tables measure this
        ├─ right answer dropped by the shortlist → Router failure (Banking77)
        ├─ right answer never supplied           → not this model's job
        └─ legacy API shows 1.0                 → display rounding above 0.95, not certainty
```

## Why it matters for `pro/plan`

- Same hygiene as [[wiki/concepts/causal-analysis]]: a high score means "best of the options you wrote", not "true" and not "the agent did it".
- Julia is the cheap local speaker (CPU, ~30 ms on an M4 for a 4-way toy call — author measurement). CLM is the other local speaker and needs a GPU encoder. Jev is the hosted one. None of the three is a harness axis.
- Do not treat a supplied Jev reference column as a paired rerun. Julia's card says the Jev numbers were copied from the protocol.
- Display rounding and a shortlist are different causes of a confident-looking wrong answer. Name which one.

## Related

- Sources: [[wiki/sources/julia-1]], [[wiki/sources/clm]], [[wiki/sources/jev-ultrafast]]
- Contrastive machine (different weights, same questions): [[wiki/concepts/contrastive-action-ranker]]
- Browser case of a closed action list: [[wiki/concepts/indexed-action-space]]
- Causal split: [[wiki/concepts/causal-analysis]]
