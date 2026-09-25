# Contrastive-LM

| Field | Value |
|---|---|
| Type | GitHub publisher of CLM (research code + weights) |
| GitHub | [Contrastive-LM](https://github.com/Contrastive-LM) — org profile **not fetched** this ingest |
| Blog | https://contrastive-lm.notion.site |
| Weights org | https://huggingface.co/Contrastive-LM |
| First wiki source | [[wiki/sources/clm]] |
| Named author (pyproject) | Jacky Kwok, UC Berkeley email. Citation coauthors are on the source page, not entity pages |

## Relevance

- Publisher of **CLM**: local System One ranker (`contrastive-lm` 0.1.0) that speaks the same `POST /v1/systemone` wire as TypeSafe Jev.
- Not a harness vendor. The repo serves two projection heads on a frozen Qwen3-8B encoder. The T-Rex example *uses* a planner and a shield; it does not own an agent loop.
- Contrast in vault: [[wiki/entities/browser-use]] (Jev / Browser Harness — hosted judgment model and CDP I/O), [[wiki/entities/google-research]] (RRSI — offline harness-diff search, not a ranker).

## What this vault currently knows

- Public repo created 2026-09-23, HEAD 2026-09-24, 947 stars at ingest. No git tags.
- Reference head: `Contrastive-LM/CLM-v0.1-8B`. Other cited Hub sets (`deepswe-clm-heads-8k`, `deepswe-clm-embeddings-8k`, `LocalLLaMA/typed-decisions`) were **not** opened.
- README points scaling experiments and data pipelines at «the research repo's `main` branch». That repo was not identified or fetched.

## Related

- Source: [[wiki/sources/clm]]
- Concept: [[wiki/concepts/contrastive-action-ranker]]
- Tool: [[10_Reference/tools/clm]]
- Contrast: [[wiki/entities/browser-use]], [[wiki/entities/google-research]]

## Sources

- [[wiki/sources/clm]]
