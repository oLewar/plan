# NumPy paper toy (see the op, don't cite the run)

## Definition (working)

A **NumPy paper toy** is a notebook that rewrites one idea from a paper in array code on synthetic data, so a reader can watch the operation. It is not a reproduction.

The public case is [[wiki/sources/sutskever-30-implementations]]: 30 files, one per item on Sutskever's list, badge "30/30". Census of the source at ingest:

- **0 / 30** notebooks have saved cell outputs.
- **6 / 30** contain a loop that updates weights (`02`, `05`, `09`, `18`, `26`, `27`).
- The Transformer notebook (`13`) is a forward block: scaled dot-product, multi-head, positions. No `backward`, no train loop.
- The scaling-laws notebook (`22`) *draws* a power law. It does not fit one.

```
paper
  ├─ file exists            → the author's "implemented"
  ├─ functions + classes    → you can read the op
  ├─ loop updates W         → a toy might have learned something
  └─ saved outputs + paper's metric on the paper's data
                            → reproduction (this repo does not claim it, and does not have it)
```

## Why it matters for `pro/plan`

- Stops a specific false cause: "we have the notebook, so the result holds." The file is evidence of *structure*, not of *fit*. Same shape as [[wiki/concepts/causal-analysis]] ("DONE ≠ success", "survived ≠ the model played").
- Pairs with [[wiki/concepts/composed-error-analysis]]. A toy that never trains cannot tell approximation from optimization from generalization — there is no overall error to decompose.
- Efficiency: reading the 6 notebooks that update `W` is cheaper than treating all 30 as equal depth. Porting any of them to a framework is a different project (the author says so in Paper 8 and Paper 18).
- Not a fifth harness axis. Not an agent. Do not install it to "have the papers."

## Related

- Source: [[wiki/sources/sutskever-30-implementations]]
- Timeless pole: [[wiki/concepts/barbell-strategy]]
- Formal three-term error: [[wiki/concepts/composed-error-analysis]]
- Causal hygiene: [[wiki/concepts/causal-analysis]]
