# Prime Agent (PrimeIntellect-ai/prime-agent)

## Bibliographic / source

| Field | Value |
|---|---|
| Title | **Prime Agent** |
| Tagline | A self-improving RLM agent / harness |
| Org | [[wiki/entities/prime-intellect\|Prime Intellect]] |
| Repo | [PrimeIntellect-ai/prime-agent](https://github.com/PrimeIntellect-ai/prime-agent) |
| Blog | https://www.primeintellect.ai/blog/prime-agent |
| Paper | [arXiv:2608.23552](https://arxiv.org/abs/2608.23552) (submitted 2026-08-24) |
| Docs (in-tree) | `packages/coding-agent/docs/index.md` |
| Related PI repos | [verifiers](https://github.com/PrimeIntellect-ai/verifiers) · [prime-rl](https://github.com/PrimeIntellect-ai/prime-rl) (not ingested) |
| Upstream TUI | hard fork of [`pi` / pi-mono](https://github.com/earendil-works/pi) (`@earendil-works/pi-coding-agent`) |
| License | MIT (Copyright 2025 Mario Zechner + 2026 Prime Intellect) |
| Language | TypeScript (npm workspaces) + Python REPL kernel (`prime-agent-runtime`) |
| Node | `>=22.8.0` |
| Version at ingest | **v0.8.1** (root `package.json` + GitHub latest release, 2026-08-26; lockstep across packages) |
| Default branch / HEAD | `main` @ `5b6c0e94` (2026-08-29, session ownership on in-flight join) |
| Stars / forks / watchers | **19049** / **2062** / **77** (GitHub API, 2026-08-29) |
| Open issues | 72 (API mixes issues+PRs) |
| Created / last push | 2026-05-08 / 2026-08-29 |
| Config dir | `.prime/agent` (`piConfig.configDir` in coding-agent package.json) |
| Domain | coding-agent harness, RLM / programmatic tool calling, continual self-refinement, long-horizon evals |
| Raw capture | [[raw/PrimeIntellect-ai-prime-agent-readme]] |

## One-line purpose

Open-source coding/research **harness**: the model's only built-in tool is a **persistent IPython REPL**; subagents, files, shell, skills, and harness CRUD are Python calls. `/refine` can edit supplemental harness state from the trajectory. Daemon workers keep sessions running after the TUI detaches.

## Thesis (from README + docs + blog + arXiv abstract)

1. **Programmatic, not schema-tool.** Default model tool = `ipython`. File/shell/skill/subagent work starts as code in a kernel that survives compaction.
2. **`rlm(...)` admits children, does not return answers.** Handle comes back at admission; results arrive via `agent_message` or files. Children are full sessions (own kernel, JSONL, model).
3. **Continual Harness** = durable H = (prompt notes ρ, subagent specs G, skills K, memory M). Same CRUD surface. `/refine` applies *small evidence-backed* edits; **base system prompt is immutable**; snapshots support rollback.
4. **Daemon owns execution.** TUI is a client. Worker = one root session tree. Crash recovery from JSONL + kernel snapshot. Not a security sandbox (same OS perms as the user).
5. **A2A is nuclear-family only** (parent / sibling / child) — not a global bus.
6. **Long-running kit:** detach/reattach, `/goal`, `/heartbeat` + `rlm_heartbeat`, `prime-agent schedule`, `/autonomous` with gates and turn/token/time budgets. A passed gate checks only that gate; hitting a limit ≠ success.
7. **Built on `pi`, now the product.** Public install is versioned release artifacts (`install.sh` + SHA-256), not the inherited npm package names.
8. **Author eval claims** (blog/arXiv, not independently reproduced here): Opus 5 + Prime Agent **95.5% RHAE Best@1** on ARC-AGI-3 vs 95.4% human-expert baseline; Factorio `/refine` also learned **RCON cheat skills**. No model is trained *around* this harness yet.

## Architecture snapshot

```
TUI / JSON / RPC / ACP clients
        │  AgentConnection (does not own execution)
        ▼
Daemon supervisor  (routing, attachments, A2A, recovery)
        │
        ├── catalog process (saved-session scans)
        └── session worker  (one root tree)
                ├── AgentSessionRuntime + scheduler
                ├── root AgentSession + IPython kernel
                └── rlm(...) children (session ± kernel)
```

| Piece | Role |
|---|---|
| Client | Render, keys, local UI prefs |
| Supervisor | Discovery, attach, worker health, family messaging |
| Worker | Root runtime, kernels, descendants, schedules |
| `AgentSession` | Provider streams, queues, tools, compaction, goals, transcript |
| Python kernel | Model-facing control env; typed `rlm.host_request(...)` for host-owned state |
| Storage | Append-only JSONL + artifacts; branch by moving the leaf pointer |

### Persistence vs Herdr

| | Prime Agent | [[wiki/sources/herdr]] |
|---|---|---|
| Owns | Agent loop + kernel + session JSONL | PTY of *whatever CLI* you run |
| Detach | Worker keeps the **agent** | Server keeps the **terminal process** |
| Built-in Herdr reporter | `herdr-agent-state.ts` (no-op unless `HERDR_ENV=1`); defers if file-based `pi` integration already loaded | Detects Prime Agent as `pi` / screen+hooks |

They compose: Prime Agent can live *inside* a Herdr pane.

### Continual Harness vs `/refine`

| Layer | Mutable? |
|---|---|
| Base system prompt | **No** |
| Supplemental prompts / memories / skill *descriptions* / subagent specs | Yes, via `rlm.harness` CRUD and `/refine` |
| Executable Python skill on disk | Separate `skill-creator` packaging; `/refine` does **not** replace that |

### Skills

- Agent Skills spec (markdown) **plus** Python-backed packages installed into kernel venv (`~/.prime/agent/kernel-venv`).
- Locations: `~/.prime/agent/skills/`, `~/.agents/skills/`, project `.prime/agent/skills/`, `.agents/skills/`.
- Built-ins: `prime-intellect`, `skill-creator`, `websearch` (Serper). Can also point at `~/.claude/skills` / `~/.codex/skills`.
- MCP: through Python skills, **not** by exploding the model tool list.

### Trust model (docs, explicit)

Prime Agent runs model-generated Python and project commands **as your user**. Workers/kernels isolate *lifecycle*, not security. README warning: use trusted repos/skills; untrusted work needs an *external* sandbox.

`/refine` writing memories/skills is an ASI06-class write path ([[wiki/concepts/memory-poisoning]]): Factorio blog case is the causal demo — the same loop that stores useful tactics stored the cheat.

## Why it matters for `pro/plan`

- Fourth public harness axis next to DSH (**loop is a plugin**), pstack (**style wrap**), Herdr (**place / PTY**): Prime Agent is **programmatic REPL + self-editing supplemental harness**.
- 1M / software-factory long jobs: daemon + goals + autonomous gates is closer to an eval runtime than a chat CLI ([[25_Projects/1M_Strategy/Overview]]).
- Direct Herdr overlap: in-tree reporter, so Chappy-on-Herdr research already has a peer agent that speaks the socket.
- Do **not** treat 19k stars or ARC 95.5% as «install tonight»: pipe-to-sh, unsandboxed Python as the model, `/refine` can poison its own skills (author-documented).

## Status

- Ingest depth: **README + docs index/architecture/rlm/long-running/skills + root & coding-agent package.json + LICENSE + blog + arXiv abstract + GitHub API repo/release/org + HEAD + sampled `herdr-agent-state.ts`**. Not cloned; **not installed; not run**. Paper PDF not read.
- Confidence: **high** for public architecture/CLI/trust claims; **medium** for blog eval numbers (author claims; they even discarded their own CC/Codex reruns in favor of official harness numbers); **low** for runtime quality vs Hermes on this host.
- Hermes/Chappy: **reference only**. Do not pipe `install.sh` without an explicit ask.

## Possible Hermes/Chappy integration paths

1. **Leave as reference** — default.
2. **Read-only peer** — study RLM/`/refine` vs Hermes skills+memory; do not copy CRUD-from-trajectory onto SOUL/memories without a write-gate.
3. **Compose with Herdr** — Prime Agent already reports lifecycle inside a Herdr pane; Hermes uses a separate official plugin.
4. **Do not** treat Prime Agent as a drop-in Hermes replacement (different loop: REPL vs tool schemas) or as a sandbox.

## Next (optional)

- [ ] Read arXiv PDF tables vs blog (contamination / Best@k protocol)
- [ ] Compare `rlm.harness` write-gate vs AMG / vault ingest policy
- [ ] Smoke-test only if user asks; prefer disposable worktree

## Links

- Entity: [[wiki/entities/prime-intellect]]
- Concept: [[wiki/concepts/continual-harness]]
- Tool card: [[10_Reference/tools/prime-agent]]
- Adjacent list: [[10_Reference/Agents/tools/harness]]
- Contrast: [[wiki/sources/deepseek-harness]], [[wiki/sources/herdr]], [[wiki/sources/pstack]], [[wiki/concepts/everything-is-a-plugin]], [[wiki/concepts/agent-runtime-multiplexer]], [[wiki/concepts/memory-poisoning]]

## Sources / provenance

- README `main` 2026-08-29, sha256 `968b64da5dbd48cabc25f3f0ae0bf36ba3227c115d045d1d89bdf98b790645ec` (9339 bytes)
- Docs: `packages/coding-agent/docs/{index,architecture,rlm,long-running-agents,skills}.md`
- Blog: https://www.primeintellect.ai/blog/prime-agent
- arXiv: https://arxiv.org/abs/2608.23552 (abstract only)
- `package.json` version `0.8.1`; GitHub release `v0.8.1` (2026-08-26)
- GitHub API `PrimeIntellect-ai/prime-agent` + `/releases/latest` + org + commit `main` 2026-08-29
- Built-in Herdr reporter: `packages/coding-agent/src/core/extensions/builtin/herdr-agent-state.ts`
