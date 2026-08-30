# Composed error analysis (ANN training)

## Definition (working)

Overall error обучения сети **не одно число и не одна причина**. В разложении [[wiki/sources/mathematical-introduction-to-deep-learning|Jentzen–Kuckuck–von Wurstemberger]] (Part V, Ch. 14–15) он собирается из трёх слагаемых:

1. **Approximation error** — выбранный класс ANN (архитектура / глубина / активации) *в принципе* не содержит хорошего приближения целевой функции. Даже идеальный оптимизатор и бесконечные данные не спасут.
2. **Optimization error** — класс достаточно богат, но процедура (GF / GD / SGD / Adam / …) не находит хороший параметр. Landscape, learning rate, KL-режим, random init.
3. **Generalization error** — эмпирический риск на конечной выборке хорошо оптимизирован, истинный риск нет. Concentration, covering numbers, finite-sample vs population.

```
target function / risk
        │
        ├─ class too small          → approximation
        ├─ optimizer misses minimizer → optimization
        └─ n samples ≠ distribution → generalization
                 └─ sum (with a precise decomposition) → overall training error
```

Status of the three-term split as a *useful causal map*: **Confirmed** in this source (the book *defines* and proves variants of it). Status of any specific rate/constant in the book: **Unread** here.

## Why it matters for `pro/plan`

- Mission hygiene: не писать «модель плохая» / «агент тупой» одним ярлыком. Сначала спросить, *какой член* доминирует.
- Efficiency: чинить не тот член = высокий Cost при нулевом Confidence gain (учить optimizer, когда не хватает capacity; копить данные, когда landscape не сходится).
- Совместимо с [[wiki/concepts/causal-analysis]] (альтернативные объяснения + confidence states) и [[wiki/concepts/barbell-strategy]] (math decomposition = timeless; конкретный AdamW/Muon = frontier).
- Не путать с agent-harness осями (plugin loop / playbook / PTY / `/refine`): это про *обучение сети*, не про runtime агента.

## Related patterns

- **Capacity vs optimizer vs data** as three independent knobs (Hypothesis as everyday product language; Confirmed as the book's formal split).
- **PINN/DGM/DKM** (Part VI того же источника) — другой трек: PDE → stochastic optimization. Не подставлять «generalization» из supervised learning без переноса теоремы.
- **Silent skip of a named gate** в coding agents ([[wiki/concepts/playbook-routed-agent-mode]]) — аналог optimization error: процедура не дошла до минимума evidence, хотя класс решений достаточен.

## Sources

- [[wiki/sources/mathematical-introduction-to-deep-learning]]
- Related: [[wiki/concepts/causal-analysis]], [[wiki/concepts/efficiency-metric]], [[wiki/concepts/barbell-strategy]]
