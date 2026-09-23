# Google Research

| Field | Value |
|---|---|
| Type | Research org (GitHub publisher of RRSI) |
| GitHub org | [google-research](https://github.com/google-research) |
| First wiki source | [[wiki/sources/rrsi]] |
| Disclaimer (repo) | «This is not an officially supported Google product.» Not in the Google Open Source Vulnerability Rewards Program. |

## Relevance

- Publisher of **RRSI**: regularized test-time search over agent-harness diffs (Apache-2.0, package 0.1.0, no git tags at ingest). Paper arXiv:2609.24972.
- Not a harness *vendor* in the DSH / Prime Agent sense. The repo evolves other people's starting harnesses (harbor Terminus-2, archipelago react_toolbelt).
- Contrast labs in vault: [[wiki/entities/prime-intellect]] (continual `/refine`), [[wiki/entities/deepseek]] (`dsh` plugin loop), [[wiki/entities/herdr]] (PTY runtime), [[wiki/entities/anthropic]] (Claude Code + Cowork), [[wiki/entities/cursor]] (pstack style wrap).

## What this vault currently knows

- RRSI core is domain-agnostic (`rrsi/`); three instances live under `domains/{coding,workspace,eng}/`.
- Search roles call Claude on Vertex. Frozen policy in the paper runs is Claude Opus 4.8; one coding ablation uses Gemini 3.5 Flash. Harvey LAB judge is Gemini 3.5 Flash.
- Paper authors are listed on the source page, not as separate entities.
- Org metadata beyond this repo (creation date, repo count) was **not** fetched.

## Related

- Source: [[wiki/sources/rrsi]]
- Concept: [[wiki/concepts/regularized-harness-search]]
- Tool: [[10_Reference/tools/rrsi]]
- Contrast: [[wiki/entities/prime-intellect]], [[wiki/entities/deepseek]], [[wiki/entities/herdr]], [[wiki/entities/anthropic]]

## Sources

- [[wiki/sources/rrsi]]
