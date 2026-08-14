# Multi-action feed ranking

## Definition

Подход к ранжированию ленты, где модель предсказывает **набор вероятностей действий** пользователя на кандидате (like, reply, dwell, follow, mute/block/report, …), а финальный score собирается **явной** взвешенной суммой, а не одним скрытым «relevance».

Формула (из X For You / Phoenix):

```text
Final Score = Σ (weight_i × P(action_i))
```

Далее обычно идут post-score adjustments: diversity по автору, OON discount, boost новых авторов, diversity re-rank (DPP / embedding neighbour penalty).

## X default objective shape (public `param.rs`, 2026-08)

**Что ценится (defaults, rounded human view → exact where noted):**

| Action | ≈ weight |
|---|---:|
| Copy link | **+20** |
| Reply / quote | **+5** |
| Follow author | **+4** |
| Favorite (like) | **+0.5** |
| Open link | **+0.2** |

**Что жёстко наказывается:**

| Action | ≈ weight | exact in code |
|---|---:|---|
| Report | **-234** | -234.0 |
| Mute author | **-59** | -58.8 |
| Not interested | **-43** | -43.2 |

**Практически игнорируется в default scoring:**

- dwell time (`DwellWeight = 0.0`; continuous dwell residual tiny)
- profile click (`ProfileClickWeight = 0.0`)
- «AI-generated or not» — **нет** action-weight в ranking params (не objective head)

Следствие: **алгоритм не оптимизируется под лайки**. Conversation + distribution (copy/share) + follow >> like; negative feedback доминирует по |magnitude|. Defaults — baseline; live experiments can change weights.

Полная таблица и param names: [[wiki/sources/x-algorithm]].

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

- Makes product trade-offs **inspectable** → diagnosis «почему вырос/упал reach» через heads (copy/reply/follow vs like vs mute/report), не через vanity likes.
- Content strategy heuristic from X defaults: design for reply/quote/share loops; treat likes as weak proxy; avoid triggers that produce mute/report/not-interested.
- Template for any ranking surface (agent tool pickers, research digests, content products in 1M Strategy): predict multiple outcomes, blend with explicit weights, filter with separate policy.

## Sources

- [[wiki/sources/x-algorithm]]
- Entity: [[wiki/entities/xai]]
