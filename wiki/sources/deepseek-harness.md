# DeepSeek Harness (deepseek-ai/deepseek-harness)

## Bibliographic / source

| Field | Value |
|---|---|
| Title | **DeepSeek Harness** (`dsh`) |
| Org | [[wiki/entities/deepseek\|DeepSeek AI]] |
| Repo | [deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness) |
| Site | https://deepseek.com/harness |
| npm | [`@deepseek-ai/dsh`](https://www.npmjs.com/package/@deepseek-ai/dsh) (bin `dsh`) |
| Python | `deepseek-harness-sdk` / `deepseek-harness-runtime-bin` (subprocess JSON-RPC) |
| License | MIT (+ `THIRD_PARTY_NOTICES.md`) |
| Language | TypeScript/Node (pnpm workspaces); Python SDK; native Landlock |
| Version at ingest | repo `package.json` **0.1.0-rc.8**; npm `latest` **0.1.0-rc.7**, `next` **0.1.0-rc.8** (2026-08-19) |
| Stars / forks | 171867 / 18523 (GitHub API, 2026-08-20) |
| Created / last push | 2026-08-13 / 2026-08-19 |
| Status | **developer preview**; compatibility-breaking changes promised |
| Domain | agent harness, plugin runtime, coding agent, Cordis composition |
| Raw capture | `[[raw/deepseek-ai-deepseek-harness-readme]]` |
| Cordis | [cordiverse/cordis](https://github.com/cordiverse/cordis) · paper [A Programming Paradigm for Spatiotemporal Composability](https://github.com/cordiverse/paper) |
| Plugin discovery | GitHub topic [`dsh-plugin`](https://github.com/topics/dsh-plugin) · list [awesome-dsh-plugin](https://github.com/awesome-dsh-plugin/awesome-dsh-plugin) |

## One-line purpose

Open-source coding-agent harness: **everything is a plugin** (model adapter, tools, session log, agent loop). Compose a running product from ordered **profiles + bundles + patches**, not a privileged core.

## Thesis (from README + architecture + AGENTS.md)

1. **No privileged core.** Extend by mounting a plugin; registrations are Cordis *effects* that unwind on unload.
2. **Profiles compose bundles.** `web` and `headless` ship as templates. Layers: each bundle in listed order → profile `cordis.patch.yml` → home-level patch → `--patch`. Inspect with `dsh --profile web --dump-config`.
3. **`dsh-base` is the first layer** of every profile: model adapters, tools, persistence, sandbox/approval, settings, credentials, telemetry. `dsh-web-app` adds the browser app; `dsh-headless` is a one-shot runner with no server.
4. **Turn = steps.** A step is one model request plus the tools it calls. Durable session events vs live `agent/*` / `tools/*` waterfalls. **Model-visible ⟺ logged.**
5. **Capability seams** = Service Definition + Provider + Consumer. Swap filesystem/subprocess providers (local → remote sandbox / E2B) without forking Bash/PTY/LSP.
6. **External PRs not accepted** (CONTRIBUTING.md, early stage). Community path = plugins with topic `dsh-plugin`, discussions, ecosystem — not core patches.
7. **Pre-release:** no compatibility promise (`SESSION_FORMAT_VERSION` at `0`; SQLite `SCHEMA_VERSION` monotonic). Node `^22.19 \|\| >=24`. Default Web UI `127.0.0.1:3080`.

## Architecture snapshot

```
empty entry list
  → bundle patches (profile order; dsh-base first)
  → profile cordis.patch.yml
  → $DSH_HOME/cordis.patch.yml
  → --patch overlays
```

Turn flow (docs/architecture.md):

```
turn/start
  claim next-step input
  assemble prompt + tool schemas
  -> agent/pre-step  (reject | enter)
     step/start
     agent/request -> llm/stream -> assistant/message
     tool/call* -> tools/pre-execute -> execute -> post-execute -> tool/result*
     step/end
  -> agent/turn-stopping
turn/end
```

### Core `ctx` keys (architecture table)

| Package | Owns | `ctx` key |
|---|---|---|
| `core/session` | append-only `SessionEvent` log | `ctx.sessions` |
| `core/system-prompt` | prompt sections + tool schemas | `ctx.systemPrompt` |
| `core/tools` | scoped registry + guarded execute | `ctx.tools` |
| `core/agent` | `Agent` interface + `agent/*` events | `ctx.agents` |
| `core/agent-loop` | default driver | `ctx.agentLoop` |
| `llm/llm` | stream vocabulary + adapter seam | `ctx.llm` |

### Product surfaces

| Surface | How |
|---|---|
| Web UI | `npx @deepseek-ai/dsh web` → `:3080`; Settings → Models (DeepSeek key or OpenAI-compatible) |
| Headless | `dsh --profile headless "job"` — one persisted session, print, exit |
| Plugin mgmt | `dsh plugin --profile <name> <pnpm args>` |
| Python | JSON-RPC over stdio to bundled runtime |
| ACP | automation-only Agent Client Protocol server |
| Sandbox | `ctx.sandbox`: bwrap / Landlock / Seatbelt; E2B group is **POC** |
| Skills | `skill/` provider registry + local impl + catalog/loader tool |
| Self-mod | `extensions/` / `self-modification`: inspect/mount own plugins |

## Why it matters for `pro/plan`

- Direct competitor/peer to the **agent harness** required by [[25_Projects/1M_Strategy/Overview]]: design-doc-first, replaceable loop, verification gates.
- Causal pattern: **composition, not a monolith** — same as vault skills/cron vs a single chat ([[wiki/concepts/everything-is-a-plugin]]).
- Contrast: Claude Code / Hermes have a privileged loop; DSH claims the loop itself is a plugin.
- Do **not** treat 172k stars as maturity: created 2026-08-13, RC, no external PRs, breaking changes.

## Status

- Ingest depth: **README + architecture.md + AGENTS.md layout + packages/README groups + CLI/Python READMEs + npm metadata**. Not cloned; not run.
- Confidence: **high** for public claims above; **low** for runtime quality vs Hermes/Claude Code (not compared empirically).
- Hermes/Chappy: **reference only** at ingest — not installed.

## Links

- Entity: [[wiki/entities/deepseek]]
- Concept: [[wiki/concepts/everything-is-a-plugin]]
- Tool card: [[10_Reference/tools/deepseek-harness]]
- Adjacent list: [[10_Reference/Agents/tools/harness]]
- Ecosystem (not ingested): [awesome-dsh-plugin](https://github.com/awesome-dsh-plugin/awesome-dsh-plugin), [anywhere-labs/deepseek-harness-desktop](https://github.com/anywhere-labs/deepseek-harness-desktop)

## Sources / provenance

- README `master` 2026-08-20, sha256 `cd7f5d59b4e9c27bb6a0480b131a7e0712ac0d33dd5b3a02deba7e5318dfcc38`
- `docs/architecture.md`, `AGENTS.md`, `packages/README.md`, `apps/cli/README.md`, `python/README.md`, `CONTRIBUTING.md`
- GitHub API repo metadata 2026-08-20; npm registry `@deepseek-ai/dsh` same day
