# Efficiency metric

## Definition
Ключевая метрика: эффективность = максимум ценности при минимуме времени, риска и когнитивной перегрузки.

## Practical scoring
Оцениваем каждый шаг по 1..5:
- Impact (влияние на цель)
- Confidence gain (уменьшение неопределённости)
- Safety (контроль риска)
- Cost (время/сложность)

Приоритет:
`Priority = (Impact × Confidence gain × Safety) / Cost`

## Decision rule
При прочих равных делать шаг с более высоким Priority.

## Related signals (from later sources)
- **Payment / revenue** as high-confidence impact signal for product experiments ([[wiki/sources/fireside-chat-arman-suleimenov-2026-08-07]], [[wiki/entities/nfactorial-school]]).
- **Asset fit** raises expected efficiency: prefer ideas that reuse existing audience/community/domain edge ([[wiki/concepts/idea-as-function-of-assets]]).
- **Barbell allocation** of learning time: frontier tools + timeless principles, skip mid-noise ([[wiki/concepts/barbell-strategy]]).

## Sources
- `[[wiki/sources/llm-wiki-gist]]`
- `[[wiki/sources/fireside-chat-arman-suleimenov-2026-08-07]]`
