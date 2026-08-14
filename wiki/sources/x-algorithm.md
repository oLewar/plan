# X For You Feed Algorithm (xai-org/x-algorithm)

## Bibliographic / source

| Field | Value |
|---|---|
| Title | **X For You Feed Algorithm** |
| Org | [[wiki/entities/xai\|xAI]] / X |
| Repo | [xai-org/x-algorithm](https://github.com/xai-org/x-algorithm) |
| README | [blob/main/README.md](https://github.com/xai-org/x-algorithm/blob/main/README.md) |
| Raw capture | `[[raw/xai-org-x-algorithm-readme]]` |
| License | Apache License 2.0 |
| Domain | recommendation systems, feed ranking, visibility filtering, content safety labels |
| Latest README update noted | **2026-08-13** |

## One-line purpose

Публичный core-код, который определяет **какие посты** зритель видит в **For You** на X: in-network + out-of-network retrieval, multi-action ranking (Phoenix), visibility filtering и labeling path.

## Thesis (from README)

1. **For You = per-request assembly**, не статическая лента: кандидаты из follow-graph и OON-источников ранжируются одной моделью, затем отдельно фильтруются на видимость.
2. **Два контура**:
   - **Request path** (`home-mixer` / candidate pipeline): hydrate viewer → sources → hydrate candidates → pre-score filters → score/rank → select top-K → post-selection VF filters → blending (ads / Who to Follow / prompts).
   - **Labeling path** (async): content understanding → label rules → storage → visibility filtering answers ALLOW / INTERSTITIAL / DROP.
3. **Phoenix** предсказывает вероятности **многих actions**, а не один «relevance»; `RankingScorer` делает weighted sum + diversity/OON/new-author adjustments.
4. **Ranking ≠ visibility**: порядок и «можно ли показать» — разные сервисы, входы и правила.
5. **Transparency trade-off**: код + Under the Hood labels; часть prompts/rules намеренно не публикуется, чтобы снизить gaming.

## Architecture snapshot

### Candidate sources

| Source | Role |
|---|---|
| `thunder/` | In-memory recent posts from accounts the viewer **follows** |
| `phoenix/` retrieval | Vector nearest posts for **out-of-network** |
| `simclusters/` | Cluster similarity (who engages with what) for OON candidates |

### Ranking stack

| Piece | Role |
|---|---|
| Phoenix ranking | Multi-action probabilities (engagement / clicks / attention / author / negative) |
| `RankingScorer` | `Final Score = Σ (weight_i × P(action_i))` + author diversity decay, OON discount, new-author boost |
| `vm-ranker/` | DPP-style reorder over embeddings for neighbour diversity |

Weights live in `home-mixer/params/param.rs` (prod defaults synced into repo via cron scripts).

### Default action weights (what X values in ranking)

Source of truth for defaults in public code: `home-mixer/params/param.rs` (comment: weights combine product value of the action **and** action rarity/propensity). Experiments can override these at traffic share.

**Positive (selected, human framing):**

| Signal (RU / EN) | Default weight | Param |
|---|---:|---|
| Скопировать ссылку / share via copy link | **+20** | `ShareViaCopyLinkWeight` |
| Ответ / reply | **+5** | `ReplyWeight` |
| Цитата / quote | **+5** | `QuoteWeight` |
| Подписка на автора / follow author | **+4** | `FollowAuthorWeight` |
| Share (generic) | +2 | `ShareWeight` |
| Retweet | +1 | `RetweetWeight` |
| Лайк / favorite | **+0.5** | `FavoriteWeight` |
| Открыть ссылку / open link | **+0.2** | `OpenLinkWeight` |
| Post click | +0.4 | `ClickWeight` |
| Share via DM | +5 | `ShareViaDmWeight` |

**Вывод по позитиву:** алгоритм **не** оптимизируется под лайки. Copy-link / reply-quote / follow доминируют над favorite (~40× / 10× / 8× относительно like).

**Negative (selected):**

| Signal | Default weight | Param | Notes |
|---|---:|---|---|
| Жалоба / report | **-234** | `ReportWeight` | exact |
| Мьют автора / mute author | **-58.8** (~**-59**) | `MuteAuthorWeight` | often rounded to -59 |
| Не интересно / not interested | **-43.2** (~**-43**) | `NotInterestedWeight` | often rounded to -43 |
| Block author | -31.2 | `BlockAuthorWeight` | |
| Not dwelled | -0.02 | `NotDwelledWeight` | tiny |

**Жёстче негатив, чем позитив:** один report ≈ −11.7× copy-link; mute ≈ −3× copy-link; not-interested ≈ −2× copy-link. Редкие negative actions намеренно имеют огромный |weight|.

**Отсутствует / practically ignored in default scoring:**

| Signal | Default | Reality check |
|---|---:|---|
| Dwell / время на посте (`DwellWeight`) | **0.0** | почти игнор; `ContDwellTimeWeight` = 0.004 (микроскопически) |
| Profile click / просмотр профиля | **0.0** | `ProfileClickWeight` |
| Continuous click-dwell / active secs residual | 0.0 | related cont heads off/zero |
| AI-generated or not | — | **нет** ranking weight в `param.rs`; если влияет, то через labels / visibility / content models, не через `RankingScorer` objective |

**Caveats:** defaults may differ from live experiment arms; additional boosts exist (e.g. bidirectional-follow reply boost **+15** on top of reply); OON discount / author diversity / VMRanker reordering apply after weighted sum.

### Visibility / safety (high level)

- Understanding: `grox/`, media models (`media-model-proxy/`, `clip/`, adult classifiers), account models (`agatha/`, `bdsm/`, `user-cred-v2/`).
- Rules: `scarecrow/` + `botmaker/` / `botmaker-rules/`, `abuse-enforcement-service/`, `safety-label-user-agg/`.
- Decision surface: `visibility-filtering/` → ALLOW / INTERSTITIAL / DROP; some rules apply **only** to OON recommendations (high-recall spam drop for non-followers).

### Notable filters (pre-scoring)

Age **48h**, self posts, blocked/muted, muted keywords, already seen/served, subscription eligibility, OON retweet/reply constraints, SimClusters NSFW author for non-followers, inventory holdout, etc.

## Key design decisions (repo framing)

1. **Multi-action prediction** — explicit combination of action probs vs single relevance score.
2. **Candidate isolation** — candidates don't attend to each other in transformer inference → consistent/cacheable scores.
3. **Hash-based embeddings** — no vocabulary maintenance; new posts representable immediately.
4. **Ranking and visibility are separate**.
5. **Composable candidate-pipeline** — stages (source/hydrator/filter/scorer/selector/side-effect), parallel where possible.

## What's intentionally missing / partial

- Some Grox LLM prompts (`.j2`) and some botmaker rules not published (anti-gaming).
- Deployment/infra glue may be incomplete; Phoenix training/serving is more runnable (Cargo/pyproject/quickstart + synthetic data).
- Interstitial UI rendering not in this repo.

## Transparency surface

- Tool: [Under the Hood](https://x.com/i/under_the_hood) — aggregate visibility-impacting labels on account/posts.
- Code: `under-the-hood/` jobs + serving.

## Why it matters for `pro/plan`

- **Causal map of a real large-scale recsys**: retrieval → multi-objective scoring → post-hoc policy filter is a reusable pattern for any ranking product (feeds, agent tool ranking, content surfacing).
- Separating **score order** from **policy/visibility** is a safety/product design principle (efficiency under constraint).
- Multi-action heads + explicit weights make trade-offs inspectable: X defaults prioritize **share/copy-link + conversation + follow**, not likes; negative feedback is orders of magnitude heavier.
- Practical content implication: optimize for reply/quote/share/follow loops; likes alone are weak; avoid mute/report/not-interested triggers.
- Relevant to AI Signal Monitor / X distribution understanding and to product ranking for 1M Strategy content surfaces.
- Transparency model: publish code + outcomes, withhold only high-gaming surfaces.

## Status

- **Ingest depth:** README architecture + **default weight table from `param.rs`** (verified 2026-08-14); no deep dive into Phoenix training code or full VF rule registry.
- **Confidence:** high for default weights in public `param.rs` at capture; medium for live production (experiments can override); AI-generated status not a ranking weight in this file.
- **Not done:** full monorepo clone; per-component notes; experiment-arm diffs vs defaults.

## Next (optional)

- [x] Extract default weight table from `home-mixer/params/param.rs`
- [ ] Compare Phoenix multi-action design vs classic single-score CTR models
- [ ] Map VF OON-only drop rules to gaming/spam failure modes
- [ ] Link Under the Hood observations when available for specific accounts

## Links

- Entity: [[wiki/entities/xai]]
- Concept: [[wiki/concepts/multi-action-feed-ranking]]
- Related research surface: [[40_Research/ai-signal-monitor/x-ai-accounts]]
- Raw: [[raw/xai-org-x-algorithm-readme]]

## Sources / provenance

- Repo: https://github.com/xai-org/x-algorithm
- README raw: https://raw.githubusercontent.com/xai-org/x-algorithm/main/README.md
- Local capture: `raw/xai-org-x-algorithm-readme.md` (ingested 2026-08-14, sha256 `e0791781737a051d8dfe39923d1edb930348b83c61dc0af0728a23ac981b8a9a`)
- Weights file: https://raw.githubusercontent.com/xai-org/x-algorithm/main/home-mixer/params/param.rs (checked 2026-08-14)
- User request: Telegram link ingest + human weight summary (copy-link +20 … report −234), cross-checked to `param.rs`
