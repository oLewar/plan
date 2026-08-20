# DeepSeek Harness (`dsh`)

Open-source **plugin** agent harness from DeepSeek. Developer preview.

- Full wiki source: [[wiki/sources/deepseek-harness]]
- Entity: [[wiki/entities/deepseek]]
- Concept: [[wiki/concepts/everything-is-a-plugin]]
- GitHub: https://github.com/deepseek-ai/deepseek-harness
- Site: https://deepseek.com/harness
- npm: `@deepseek-ai/dsh` (bin `dsh`) — npm `latest` **0.1.0-rc.7**, `next` **0.1.0-rc.8** at ingest (2026-08-20)
- License: MIT
- Node: `^22.19 \|\| >=24`; package manager pnpm 11

## Run (README)

```bash
npx @deepseek-ai/dsh web
# Web UI http://127.0.0.1:3080
# --no-open  if SSH / no browser
```

```bash
dsh --profile headless "summarize this repo"
dsh --profile web --dump-config
```

From source: `pnpm install && pnpm run build && pnpm dsh web`.

Configure a model in **Settings → Models** (DeepSeek API key or other OpenAI-compatible; see their providers guide). Composer waits until a **workspace** is selected.

## Also in the repo

- Python: `deepseek-harness-sdk` drives bundled runtime over NDJSON-RPC stdio
- ACP server, skills, subagents, sandbox (bwrap/Landlock/Seatbelt; E2B = POC)
- Plugin topic: `dsh-plugin`

## Operating constraints

- **Breaking changes** are explicit; external PRs not accepted — contribute plugins, not core.
- 172k stars ≠ stable API. Created 2026-08-13.
- Hermes/Chappy: **reference only** at ingest — do not install as a replacement loop without a comparison plan.
- Discord invite in README is a short code; treat as perishable.

## Mental model

Profiles stack **bundles** (`dsh-base` first) then YAML patches. Everything — including the agent loop — is a Cordis plugin. Details: [[wiki/concepts/everything-is-a-plugin]].
