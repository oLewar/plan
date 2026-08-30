# oMLX / Jun Kim (`jundot`)

| Field | Value |
|---|---|
| Type | Open-source product + author |
| GitHub user | [jundot](https://github.com/jundot) |
| Canonical repo | [jundot/omlx](https://github.com/jundot/omlx) |
| Site | https://omlx.ai |
| Contact (README) | junkim.dot@gmail.com · https://omlx.ai/me |
| License (runtime) | Apache-2.0 |
| First wiki source | [[wiki/sources/omlx]] |

## Relevance

- Public **Apple Silicon inference server**: local OpenAI/Anthropic API with continuous batching and RAM+SSD KV cache.
- Distinct from vault harness axes: does not own the agent loop ([[wiki/entities/deepseek]]), PTY place ([[wiki/entities/herdr]]), playbook style ([[wiki/entities/cursor]]), or `/refine` ([[wiki/entities/prime-intellect]]). Owns **weights and KV**.
- README lists **Hermes Agent** as a one-click Integrations target (author claim, not smoked here).

## What this vault currently knows

- Latest documented stable at ingest: **v0.6.4** (2026-08-29). Stars **21040** (GitHub API 2026-08-30). Classifiers: Alpha.
- Requires macOS 15+ / Apple Silicon. **This Hermes host cannot run it.**
- Forked historically from vllm-mlx v0.1.0, then grew admin UI, menubar app, VLM, tiered cache.
- Custom Metal kernels are optional and easy to miss (`pip install -e .` silent fallback).

## Related

- Source: [[wiki/sources/omlx]]
- Concept: [[wiki/concepts/tiered-kv-cache]]
- Tool: [[10_Reference/tools/omlx]]
- Contrast: [[wiki/entities/herdr]], [[wiki/entities/deepseek]], [[wiki/entities/prime-intellect]], [[wiki/entities/anthropic]]

## Sources

- [[wiki/sources/omlx]]
