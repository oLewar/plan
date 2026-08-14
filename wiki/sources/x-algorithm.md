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
- Multi-action heads + explicit weights make trade-offs inspectable (what is optimized: dwell vs follow vs not-interested).
- Relevant to AI Signal Monitor / X distribution understanding and to product ranking for 1M Strategy content surfaces.
- Transparency model: publish code + outcomes, withhold only high-gaming surfaces.

## Status

- **Ingest depth:** README-level architecture + components + scoring formula; no deep dive into Phoenix training code or VF rule registry.
- **Confidence:** medium-high for stated architecture (primary source = official README, 2026-08-13 update); production traffic share of experiments / exact live weights may drift even if params are synced.
- **Not done:** clone full monorepo into vault; per-component notes; weight table extraction from `param.rs`.

## Next (optional)

- [ ] Extract live-ish weight names from `home-mixer/params/param.rs` into a concept table
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
- User request: Telegram link ingest
