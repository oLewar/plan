# Cursor

| Field | Value |
|---|---|
| Type | Company / product (AI code editor) |
| Products / surfaces | Cursor IDE; agent chat; Plan mode; `/loop`; official plugin spec |
| OSS note | [cursor/plugins](https://github.com/cursor/plugins) — plugin specification and official plugins |
| First wiki source | [[wiki/sources/pstack]] |

## Relevance

- Host of **pstack** (Lauren Tan / poteto): official plugin that encodes a rigorous multi-model engineering style on top of Cursor's agent loop.
- Adjacent research already in vault: adversarial multi-model review as a *local* Cursor plugin (`40_Research/sources/finance/joi-labcursor-multimodel-review…`) — different artifact from official `pstack`.
- Contrast labs/products: [[wiki/entities/anthropic]] (Claude Code + Cowork), [[wiki/entities/deepseek]] (`dsh` plugin harness), Hermes/Chappy (skills around a host loop).

## What this vault currently knows

- Official plugins live in `cursor/plugins` (public, 4341★ at pstack ingest, created 2026-01-23). License of the **parent repo** is unset in GitHub API; **pstack itself** is MIT (Lauren Tan).
- pstack install: `/add-plugin pstack` inside Cursor, not a standalone npm/CLI.
- Complementary official plugin named in pstack README: `cursor-team-kit` (`/deslop`, `control-cli`, `control-ui`) — **not ingested**.
- Models referenced as first-class Cursor slugs in pstack defaults: Grok 4.6, GPT-5.6 Sol, Claude Fable 5, Claude Opus 5.

## Related

- Source: [[wiki/sources/pstack]]
- People: [[wiki/entities/lauren-tan]]
- Concept: [[wiki/concepts/playbook-routed-agent-mode]]
- Tool: [[10_Reference/tools/pstack]]
- Contrast: [[wiki/entities/anthropic]], [[wiki/entities/deepseek]]

## Sources

- [[wiki/sources/pstack]]
