# Multi-action feed ranking

## Definition

Подход к ранжированию ленты, где модель предсказывает **набор вероятностей действий** пользователя на кандидате (like, reply, dwell, follow, mute/block/report, …), а финальный score собирается **явной** взвешенной суммой, а не одним скрытым «relevance».

Формула (из X For You / Phoenix):

```text
Final Score = Σ (weight_i × P(action_i))
```

Далее обычно идут post-score adjustments: diversity по автору, OON discount, boost новых авторов, diversity re-rank (DPP / embedding neighbour penalty).

## Causal structure (useful decomposition)

1. **Candidate generation** — откуда вообще взялся пост (follow graph vs retrieval/clusters).
2. **Multi-action prediction** — что зритель *может* сделать.
3. **Objective blend (weights)** — что продукт *хочет* оптимизировать.
4. **Policy / visibility** — что *разрешено* показать (отдельный слой: DROP / INTERSTITIAL / ALLOW).
5. **Blending** — ads / prompts / non-post units interleaved after organic ranking.

Ключевой design split: **ranking order ≠ eligibility**. Eligibility читает labels, graph edges (block/mute), settings, country; ranking читает engagement history + post features.

## Why separate ranking and visibility

- Разные failure modes: «плохой порядок» vs «нельзя показывать».
- Policy можно ужесточать без переобучения ranker.
- OON-only high-recall spam rules: один и тот же пост allowed follower'у и dropped как recommendation — causal dependence on **edge type**, not only content score.

## Design properties called out by X algorithm README

- **Candidate isolation** at inference: score(post|viewer) independent of other candidates in batch → cacheable, stable.
- **Hash-based embeddings**: cold-start friendly, no vocab rebuild.
- **Composable pipeline stages**: source → hydrator → filter → scorer → selector → side effects.

## Links to `pro/plan` mission

- Makes product trade-offs (attention vs social vs negative feedback) **inspectable** → better causal diagnosis of «почему вырос/упал reach».
- Template for any ranking surface (agent tool pickers, research digests, content products in 1M Strategy): predict multiple outcomes, blend with explicit weights, filter with separate policy.

## Sources

- [[wiki/sources/x-algorithm]]
- Entity: [[wiki/entities/xai]]
