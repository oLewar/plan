# oMLX

Local **LLM/VLM inference server** for **Apple Silicon**. Continuous batching + hot RAM / cold SSD KV cache. Native macOS menu bar. OpenAI + Anthropic APIs on `localhost:8000`.

- Full wiki source: [[wiki/sources/omlx]]
- Entity: [[wiki/entities/omlx]]
- Concept: [[wiki/concepts/tiered-kv-cache]]
- GitHub: https://github.com/jundot/omlx
- Site: https://omlx.ai
- License: Apache-2.0
- Version at ingest: **v0.6.4** (2026-08-29); stars **21040** (GitHub API 2026-08-30)
- Config: `~/.omlx/settings.json`; models `~/.omlx/models`; CLI `~/.omlx/bin/omlx` (app shim)

## Install (docs; not run here)

Requires macOS 15.0+, Apple Silicon, Python 3.11–3.13. **This Linux Hermes host cannot run oMLX.**

```bash
# Homebrew
brew tap jundot/omlx https://github.com/jundot/omlx
brew install jundot/omlx/omlx
omlx start

# or DMG from https://github.com/jundot/omlx/releases (v0.6.4)
```

```bash
omlx serve --model-dir ~/models
# OpenAI-compatible: http://localhost:8000/v1
# Admin:            http://localhost:8000/admin
```

Useful flags: `--paged-ssd-cache-dir ~/.omlx/cache`, `--hot-cache-max-size 20%`, `--max-concurrent-requests 16` (default **8**), `--memory-guard safe`, `--api-key …`.

Custom kernels (GLM-5.2 / MiniMax M3 / Qwen3.5): official DMG, or `OMLX_WITH_CUSTOM_KERNEL=1` / `brew install … --HEAD --with-custom-kernel` **and full Xcode**. Verify:

```bash
python -c "from omlx.custom_kernels import native_kernel_status; print(native_kernel_status())"
```

## Hermes / Chappy

README: admin Integrations can set up **Hermes Agent** in one click (also OpenClaw, OpenCode, Codex, Copilot, Pi). **Not verified** here. Typical shape would be pointing the client at `http://localhost:8000/v1`.

At ingest: **reference only** — wrong OS on this host. Do not install, do not write `~/.hermes/config.yaml`.

## Operating constraints

- Apple Silicon only. Unified-memory OOM still possible; default cap is system RAM − 8GB.
- Silent slow path if custom kernels were not built.
- Claude Code «context scaling» changes **reported** token counts, not real context.
- Experimental multi-Mac split is a source-build feature with its own security doc.
- `--api-key` exists; localhost skip is an admin toggle — do not assume auth is on.
- 21k stars / Alpha classifiers / 1191 open issues: treat as fast-moving, not a frozen standard.

## Mental model

Local **model server** (weights + KV), not an agent harness. Contrast loop-replace ([[wiki/concepts/everything-is-a-plugin]]), PTY runtime ([[wiki/concepts/agent-runtime-multiplexer]]), `/refine` ([[wiki/concepts/continual-harness]]).
