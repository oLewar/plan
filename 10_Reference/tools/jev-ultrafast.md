# Jev Ultrafast

Browser **policy**: TypeSafe Jev picks operation + observed element in one request; a small LLM types only on `TYPE_TEXT`. Sits on [[10_Reference/tools/browser-harness]]. Model never emits selectors.

- Full wiki source: [[wiki/sources/jev-ultrafast]]
- Entity: [[wiki/entities/browser-use]]
- Concept: [[wiki/concepts/indexed-action-space]]
- Other Jev backends (catalog): [[wiki/sources/jev-usage-examples]]
- GitHub: https://github.com/browser-use/jev-ultrafast
- License: MIT
- Version at ingest: pyproject **0.1.0**; **no git tags / no PyPI**; HEAD `452c1ad2dd62` (2026-09-17); stars **3316** (API 2026-09-18)
- Pin: `browser-harness==0.1.13`
- Inspector: `http://127.0.0.1:8766` (`jev`); Host/Origin/token checks

## Install (docs; not run here)

This host has **no** `jev`. Needs `TYPESAFE_API_KEY` + `TEXT_MODEL_API_KEY` (example: OpenRouter `inception/mercury-2.5`).

```bash
git clone https://github.com/browser-use/jev-ultrafast.git
cd jev-ultrafast
uv sync
# fill .env from .env.example
uv run jev
```

Library: `from jev_ultrafast import Agent`. Flights example verifies the page; it does not book.

## Hermes / Chappy

At ingest: **reference only**. Do not `uv sync`, do not bind `:8766`, do not put TypeSafe keys in Hermes config.

Honest steal: closed operation set + independent DONE check. Author 7.073 s Flights is **3 pairs / one task**, not a SLA.

## Operating constraints

- Budgets: 60 actions, 120 TypeSafe requests, 250 candidates.
- MVP: no shadow/iframe/canvas/uploads/new tabs/nested scroll.
- Tabs share the existing Chrome profile (via Browser Harness).
- Default text-model env in example ≠ code fallback (`openrouter` vs `api.deepseek.com`) — configure explicitly.

## Mental model

**Typed choice over observed nodes**, not a harness. Contrast CDP helper CLI ([[wiki/concepts/self-healing-cdp-harness]]), screenshot agents, `/refine` ([[wiki/concepts/continual-harness]]).
