# Pinned flow sampling (the constraint is a replacement, not a loss)

## Definition (working)

When part of a generated sample must equal a known signal, write that part in at every step instead of adding a penalty. For flow matching with a linear interpolant the known slice at time t is `(1−t)·ε + t·x_known`, using the same noise ε the sample started from. At t = 1 it equals `x_known` exactly. The network only chooses the unpinned part.

Working source: [[wiki/sources/unimate]]. `inbetween_sample_ode` does this for three tasks with one function: a mask over time keeps keyframes (in-betweening), a mask over joints keeps a limb (text-guided editing), and a mask over the head of the next segment keeps the seam (expansion).

```
sample x_t
    │
    ├─ unpinned axes  → Euler step on the predicted velocity
    └─ pinned axes    → overwritten with (1−t)·ε + t·x_known
              └─ at t = 1 the pinned axes are the known signal, not a prediction
```

## What has to be true

- The model predicts a **velocity** on a **linear** path (`ICPlan` in this repo). The replacement is the analytic interpolant, so there is no forward/back resampling loop. A diffusion checkpoint would need a RePaint-style loop; this file raises unless `diff_model == "flow"`.
- The solver is **fixed-step Euler**. An adaptive solver (the repo's plain text sampling uses dopri5) does not expose its internal stages, so there is no t at which to re-pin. The constrained modes are the same ODE at lower order than unconstrained sampling. "Same model" is not "same integrator".
- The mask only selects. Values outside it are ignored, and a short clip whose kept index falls past its real length is clamped to its last real frame by the caller. The docstring's guarantee is equality modulo the epsilon end-stop.

## Why it matters for `pro/plan`

- [[wiki/concepts/causal-analysis]]: a pinned frame is a copy. Reporting it as something the model "chose" attributes a constraint to a prediction.
- [[wiki/concepts/efficiency-metric]]: exact is cheaper to trust than a loss weight you then have to check. It costs a fixed grid and a flow-matching checkpoint. Don't spend tuning `lambda` on a constraint that could have been a mask.
- Not a claim about sample quality. No checkpoint was loaded and no motion was generated.

## Related

- Source: [[wiki/sources/unimate]]
- Don't report a copy as a choice: [[wiki/concepts/causal-analysis]]
- Exact constraint vs a tuned penalty: [[wiki/concepts/efficiency-metric]]
