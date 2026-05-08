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

## Sources
- `[[wiki/sources/llm-wiki-gist]]`
