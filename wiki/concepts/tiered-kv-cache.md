# Tiered KV cache (hot RAM + cold SSD)

## Definition (working)

A **paged** key/value cache for transformer inference with two storage tiers:

1. **Hot (RAM / unified memory):** recently used blocks, prefix-shared, Copy-on-Write.
2. **Cold (SSD):** overflow blocks serialized (here: safetensors). A later request with a **matching prefix** restores blocks instead of recomputing prefill — including **after process restart**.

Canonical public case in vault: [[wiki/sources/omlx]] on Apple Silicon / MLX. Pattern is older (vLLM block paging); oMLX’s claim is making the **disk tier** practical for local coding-agent context.

Status of «SSD restore is always cheaper than prefill»: **Hypothesis** (depends on disk, prefix length, kernel path). Status of «oMLX implements hot+cold + CoW + prefix sharing»: **Confirmed** at README/architecture-diagram depth, not traced in Python.

## Mechanism (from oMLX README)

```
request prefix
    │
    ├─ hot hit     → reuse RAM blocks
    ├─ cold hit    → load safetensors → promote to hot
    └─ miss        → compute prefill → write hot; evict to SSD when full
```

Continuous batching (scheduler + `BatchGenerator`) is a **sibling** mechanism: many in-flight requests share the GPU/ANE-or-Metal path. Do not collapse «slow» into one label — see [[wiki/concepts/composed-error-analysis]] for the training analog; here the split is **kernel path vs cache hit vs concurrency vs model size**.

## Why it matters for `pro/plan`

- Efficiency: restore-from-SSD vs full prefill is the Cost knob for long coding sessions (Claude Code / Hermes as API clients).
- Causal hygiene: a slow turn after restart is a **cold miss**, not «the model got worse». A slow GLM-5.2 prefill with `pip install -e .` may be **missing Metal kernels**, not cache.
- Interface trick nearby: oMLX **scales reported tokens** so Claude Code auto-compact fires on small-context models — that is **not** more real context. Do not cite it as a context-window upgrade.
- This host is Linux: the concept is portable; the implementation is not.

## Contrast

| | Tiered KV (oMLX) | Agent-runtime multiplexer ([[wiki/concepts/agent-runtime-multiplexer]]) | Continual harness ([[wiki/concepts/continual-harness]]) |
|---|---|---|---|
| Persists | Attention KV blocks | PTYs / session files | Prompts, memories, skills |
| Survives | Server restart (cold tier) | UI quit (not server restart, unless snapshot) | Next turn of the same agent |
| Failure | Disk full / prefix mismatch / silent kernel fallback | Killing the runtime | Poisoned write (ASI06) |

## Related

- Source: [[wiki/sources/omlx]]
- Entity: [[wiki/entities/omlx]]
- Tool: [[10_Reference/tools/omlx]]
- Adjacent: [[wiki/concepts/efficiency-metric]], [[wiki/concepts/causal-analysis]], [[wiki/concepts/agent-runtime-multiplexer]]

## Sources

- [[wiki/sources/omlx]]
