# Jev usage examples (20 public repos)

## Bibliographic / source

| Field | Value |
|---|---|
| Title | **Jev usage examples** |
| Kind | Catalog of public TypeSafe **Jev** backends — not 20 separate architecture ingestions |
| Canonical loop | [[wiki/sources/jev-ultrafast]] (item 1; already ingested 2026-09-18) |
| Concept | [[wiki/concepts/indexed-action-space]] |
| Ingested | 2026-09-22 |
| Depth | GitHub API `/repos` + README + recursive `git/trees` for all 20; extra files for json-render Jev docs, Prism `engine/jev-*.ts`, Canny README «Jev», agent-desktop `skills/jev-desktop/SKILL.md`, jev-review README, several `package.json` / `Cargo.toml` / `pyproject.toml`. **Not executed. Not installed.** |
| Stars date | GitHub API **2026-09-22** (unauthenticated; remaining hit 0 at the last repo) |
| TypeSafe product | Still **not** ingested as its own source |

User list (order preserved). Item 1 is the already-ingested canonical policy; 2–20 are **examples**, not a fifth harness axis.

## How to read this catalog

Jev here means TypeSafe **System One**: typed `Choice` / `Score` / `Noul` over JSON state, not a chat model. Most of these repos **do not** drive a browser. Shared pattern: **code owns the workflow; Jev answers a bounded question; a probability is not a proof.**

| This catalog is | This catalog is not |
|---|---|
| Pointers + one-line role + tree/API facts | 20 wiki/sources pages |
| README + tree class | Verified runtime evals |
| Evidence that «indexed ops» escaped the browser demo | A claim that Jev is a harness |

**Confirmed:** all 20 URLs resolve; none archived. **Author claims** (7.1 s Flights, −60 % router backtest, 24.0 rows/s curate, drone ablation, …) stay labelled. **Unknown** where a README version and git tags disagree or license API is `None`.

Do not `uv sync` / `npx` / `curl \| sh` / write `~/.hermes` on this note.

## Snapshot (API 2026-09-22)

| # | Repo | ★ | License | Lang | Tree (blobs) | Version at snapshot | Jev's job |
|---|---|---:|---|---|---:|---|---|
| 1 | [browser-use/jev-ultrafast](https://github.com/browser-use/jev-ultrafast) | 17303 | MIT | Python | 40 | pyproject 0.1.0, **no tags** | Indexed browser ops on Browser Harness. Full source: [[wiki/sources/jev-ultrafast]] |
| 2 | [tamaratran/fast-jev-compaction](https://github.com/tamaratran/fast-jev-compaction) | 6169 | MIT | TS | 26 | npm **0.2.0**, no tags | Drop/truncate stale tool_use+result; user/assistant text stays verbatim |
| 3 | [vercel-labs/json-render](https://github.com/vercel-labs/json-render) | 18025 | Apache-2.0 | TS | 1653 | `@json-render/core` **0.21.0** (`v0.21.0`) | Generative UI framework; **experimental** Jev composer (`experimental_composeSpec`). Jev APIs **unreleased** on npm (in-tree docs) |
| 4 | [itsmostafa/typesafe-mcp](https://github.com/itsmostafa/typesafe-mcp) | 246 | MIT | Go | 20 | **v0.4.3** | One MCP tool `evaluate` → `POST /v1/systemone` (or OpenRouter Decisions) |
| 5 | [jkudish/jev-mcp](https://github.com/jkudish/jev-mcp) | 262 | MIT | JS | 22 | npm `@jkudish/jev-mcp` **0.5.0** | Ten purpose-built MCP tools (`jev_verify` … `jev_gate`) |
| 6 | [sharziki/semdecide](https://github.com/sharziki/semdecide) | 33 | MIT | Python | 25 | **v0.2.1** (GitHub wheel; **not on PyPI**) | Unix `is` / `choose` / `score` / `filter` / `guard` + exit codes |
| 7 | [0xNatoshi/jev-codex-router](https://github.com/0xNatoshi/jev-codex-router) | 201 | MIT | JS | 1360 | no tags | Per-call Codex model+effort routing (`jev_server.py` `127.0.0.1:4319`) |
| 8 | [GhalebDweikat/winnow](https://github.com/GhalebDweikat/winnow) | 63 | MIT | Python | 69 | no tags, no `pyproject.toml` | Claude Code hook: hide low-relevance tool-result blocks; sidecar `:47311` |
| 9 | [devagrawal09/jev-review](https://github.com/devagrawal09/jev-review) | 526 | MIT | TS | 29 | no tags | Staged diff/codebase review; dashboard `127.0.0.1:4317` |
| 10 | [ellipsis-dev/blink](https://github.com/ellipsis-dev/blink) | 57 | **None** (API) | TS | 19 | private bun package | Ensemble walkers rank filesystem nodes for a NL query |
| 11 | [lahfir/agent-desktop](https://github.com/lahfir/agent-desktop) | 1458 | Apache-2.0 | Rust | 1237 | workspace **0.9.2** | Desktop AX CLI; optional `jev-desktop` skill (ops+target, tree stays out of context) |
| 12 | [fhshaik/typesafe-mario](https://github.com/fhshaik/typesafe-mario) | 344 | **None** (API) | Python | 14 | no tags | Jev picks NES buttons from structured RAM/telemetry — **no screenshots, no ROM in repo** |
| 13 | [RomanSlack/jev-drone](https://github.com/RomanSlack/jev-drone) | 123 | MIT | Python | 54 | no tags | MuJoCo quadrotor; Jev ~2.5 Hz advisory; 50 Hz code keeps the veto |
| 14 | [emrickgarrett/OneVOneJev](https://github.com/emrickgarrett/OneVOneJev) | 20 | **None** (API) | TS | 47 | no tags | 1v1 browser FPS; server-side Jev ~9 Hz; heuristic fallback if API down |
| 15 | [jarrodwatts/jev-trader](https://github.com/jarrodwatts/jev-trader) | 1950 | MIT | TS | 63 | no tags | One buy/sell per Monad block on Kuru MON-USDC; dry-run without `PRIVATE_KEY` |
| 16 | [irfndi/prism-liquidity-agent](https://github.com/irfndi/prism-liquidity-agent) | 71 | MIT | TS | 479 | **v0.2.39** | Solana DLMM LP agent; Jev is **shadow/advisory** (`engine/jev-service.ts`) — never ENTER/EXIT |
| 17 | [jexp/neo4jev](https://github.com/jexp/neo4jev) | 85 | MIT | Jupyter | 29 | no tags | One-hop Neo4j navigation: Choice over edges + Noul «goal reached?» in one `system_one` |
| 18 | [AkashPriyadarshii/jev-curate](https://github.com/AkashPriyadarshii/jev-curate) | 23 | MIT | Rust | 55 | crate **0.1.0** | Stream Parquet/JSONL through Choice/Score/Noul; measured **24.0 rows/s** mock bench |
| 19 | [qkal/Canny](https://github.com/qkal/Canny) | 32 | MIT | TS | 98 | npm `canny-warden` **0.2.0** / tag **v0.2.1** | Claude/Codex done-gate + ledger; Jev only two Noul questions; works with key unset |
| 20 | [monteduro/killmyidea](https://github.com/monteduro/killmyidea) | 83 | **None** (API) | TS | 61 | no tags | 8 scored questions → KILL/FIX/SHIP; key stays on `api/evaluate.ts` |

README sha256 (body, LF) at fetch 2026-09-22:

| Repo | bytes | sha256 |
|---|---:|---|
| jev-ultrafast | 8650 | `29f5276b3e6295cabe322cda598e354a9e053dbfd9d831d20f09d0cca279a379` |
| fast-jev-compaction | 8688 | `5499bdb4f3ec13ac9e228cb09ab2894fd1a4e3128db04722735dbfc794f27299` |
| json-render | 25237 | `4f0b85cbce1da48fa5a698cf559df7d6a858fbc444d810f0899355a10ac6326a` |
| typesafe-mcp | 7309 | `40f08262041d235fbf068238747907e5d78377abdad86152a10bb04d447bb710` |
| jev-mcp | 40984 | `fffa09701cc047f4c5a8a226122f3de4e619a398c15f1cc4772c1c0867d057ad` |
| semdecide | 6988 | `26559f1a7445c1da2bbffb65d7f1adfcaf0bd2092b3b45caa2c8b6f72d8f792e` |
| jev-codex-router | 24393 | `064bd1347ed441cc7eae6e6f164ed4b0165191a134ef619cb54514d144576d77` |
| winnow | 25783 | `0ebe29d9bc0c2bb41c7477bd1d57929d6331c9031e68b92e2c00c84c2bf08afb` |
| jev-review | 3371 | `d8d98618015949ce1ab1c820d28d84ed64601fa7dd81c4bdbfde2fb9e30a9afe` |
| blink | 5326 | `168cf8958a9c569df45a586438099e2774b5b96e4ede7665d1008eaefbd20a44` |
| agent-desktop | 26432 | `e3ae5ffd493f6951067df808686b6d92828ac79ece4901129c6976c31fb20673` |
| typesafe-mario | 4358 | `c489f93504144937f7c8088f681d0d6370d46114ca6d09987f405b120a357504` |
| jev-drone | 14107 | `74571cdbc72381595ec06f836f62483694f8e292ab91598d1743f25d0e7decce` |
| OneVOneJev | 4027 | `754aa76597cf83165cbba51f36b53820ab611429d5656a0836c5701886ab11af` |
| jev-trader | 5566 | `f84691a188a7380ed35ae315b7ab18ff4a19c9408de1f6b755f6690296091861` |
| prism-liquidity-agent | 24064 | `d6eb6f89cfed7db5aae8641a34628cab556aecc1153ce5dc662ef09e85e4a6a6` |
| neo4jev | 10756 | `2d5e808a6e22b6623442ccb9068cfbde2f293dadd69772725f5dc3e05ba2361c` |
| jev-curate | 8820 | `89be7359c6163511730264839413f410caaf03ec70369230e991ac9e7b08cfa4` |
| Canny | 23855 | `7d91fe563b95be582adeb8eaa8d6306f4fb346ef8aa840f4106096f0b052aa95` |
| killmyidea | 6942 | `7db5cea5304f3ea7f9f225f8037207df2e1535b200bfecacf5858af931b25cec` |

Item 1 README drifted vs 2026-09-18 capture (`fa269c28…`, 8401 B): waitlist banner added. Re-ingest of [[wiki/sources/jev-ultrafast]] **not** done in this pass.

No `raw/` inbox for 2–20 (catalog, not 20 GitHub source ingests — would race cron 20×).

## Roles (what Jev actually answers)

### Context and tool results

- **fast-jev-compaction** — Claude Code plugin + npm lib. Two `noul`s per non-pinned tool call: keep the *call*? keep the *result* verbatim? Failures throw; hook decides fallback. Default `maxStateTokens` 25k / `maxRequestTokens` 30k (under Jev 32k).
- **winnow** — Claude Code **function-hook** (2.1.260+, flag). Splits Read/Bash/Grep output into ~25-line blocks; parallel «is this needed?». Hides confident-no behind `winnow_recall`. Sidecar `127.0.0.1:47311` (author: 381 ms cold Python vs 16 ms resident). `WINNOW_MODE=shadow` judges but does not rewrite. Error-looking output is never hidden.

### MCP / Unix

- **typesafe-mcp** — Go binary `evaluate`. Setup: `curl …/install.sh | sh` or `go install`. Registers Claude Code / Desktop / Codex; `evaluate setup pi` writes `~/.pi/agent/extensions/evaluate.ts`. `TYPESAFE_API_KEY` wins over `OPENROUTER_API_KEY`. **Hermes is not a listed client.**
- **jev-mcp** — `npx -y @jkudish/jev-mcp`. Ten tools; author latency 150–500 ms. Early software (README).
- **semdecide** — package `reflex_guard` internally; CLI `semdecide`. Credentials: env or `~/.config/typesafe/credentials.env` mode 600. JSON `schema_version: "1"`. Model in example JSON: `jev-1.13.0`.

### Coding-agent control plane

- **jev-codex-router** — embeds a Codex Router fork under `router/` (1360 blobs). Jev sees a *bounded* decision state; the executing model gets the full Codex replay. Fail-open; kill-switch file. Author historical sim **≈ −60 % vs full Astra** on 237 turns — **not** measured Codex quota (README + `BACKTEST.md`). Default env file in quickstart: `~/.hermes/.env` then `~/.jev.env` — **key path, not a Hermes adapter**.
- **Canny** (`canny-warden` 0.2.0 vs tag v0.2.1 — record both). Ledger of what the agent *did*; will not finish on a claim. Jev: **two Noul only**. Cache `~/.canny/jev/`; act only outside 0.1–0.9. Unset key → deterministic gate still runs. Clipped diffs leave the machine if the key is set.
- **jev-review** — Noul risk matrix → Choice/Score file profiles → evidence → mechanism → severity. Findings are **review prompts, not proof of a defect**. Loopback dashboard only.

### Search / UI / desktop

- **blink** — Bun + `@typesafe-ai/sdk` ^0.6.0. `./blink "query" dir [-r] [-n walkers]`. License **unset** in GitHub API.
- **json-render** — Vercel Labs generative-UI (created 2026-01-14, long before Jev week). Jev path: `apps/web/lib/jev/`, docs `/docs/jev`. Composer never executes actions. Playground key is `JEV_AI_GATEWAY_API_KEY` (Gateway `typesafe-ai` provider), **not** `TYPESAFE_API_KEY`.
- **agent-desktop** — Rust AX CLI (observe/decide/act on OS trees). `skills/jev-desktop/SKILL.md`: operations `CLICK`, `TYPE_TEXT`, `CHECK`/`UNCHECK`, `EXPAND`/`COLLAPSE`, `SCROLL`, `DRILL`, `WIDEN`, `WAIT`, `DONE`, `BLOCKED`. Text is supplied by the caller — skill does not invent strings. Same *indexed ops* idea as [[wiki/sources/jev-ultrafast]], different substrate (AX vs CDP).

### Games / sim (Jev as controller)

- **typesafe-mario** — object-centric JSON from emulator RAM; 7 legal buttons. No Nintendo ROM in tree.
- **jev-drone** — 500 Hz geometric controller / 50 Hz safety reflex / ~2.5 Hz Jev (`maneuver` Choice, `risk` Score, `target_truly_lost` Noul). Author ablation: baseline stuck at 17.7 m; Jev 77.5 m whole course; 0 collisions both arms. **Author table, not reproduced.**
- **OneVOneJev** — `@typesafe-ai/sdk` `jev-latest`; ~9 Hz move/yaw/pitch/ADS/fire/jump. Heuristic fallback so matches never stall.

### Markets / data

- **jev-trader** — `MODEL=jev` + `TYPESAFE_AI_API_KEY` (note the extra `AI`); default `mock` momentum. Live posts post-only limits. Not financial advice; not run here.
- **Prism** — rule agent every 10 min on Meteora DLMM. `engine/jev-service.ts`: four judgments, **NEVER drives ENTER/EXIT**; fail-open to deterministic gates. `engine/jev-gate.ts`: min interval **2000 ms**, escalating 429 breaker (1–60 min). Overlay can talk to **Hermes ACP/HTTP** (`AGENT_RUNTIME=hermes`) as a *messenger* — that is not Jev-in-Hermes.
- **neo4jev** — beam search over relationship Choices; one round-trip per hop. Default graph: public Neo4j `companies2`. Without `TYPESAFE_API_KEY`, failures are shown verbatim + labelled stand-ins (README).
- **jev-curate** — README targets 1 500+ rows/s and $4.20/100M tokens; **measured in-tree mock is 24.0 rows/s**. Vendor 444.6× cheaper / 193.6× faster vs generative LLMs = **TypeSafe claim**, not this vault.
- **killmyidea** — 10 parallel questions, 8 scored 0–4, weighted average, clarity gate. `TYPESAFE_MOCK=1` for UI without a key (ignored on Vercel). Site https://killmyidea.stemonte.io

## Contrast vs the four harness axes

Still **not** a fifth axis. These are **judgment backends** plugged into someone else's loop (Claude Code, Codex, a game server, an LP engine, a UI catalog).

| Layer | Public case | What mutates |
|---|---|---|
| Loop composition | DSH | Which plugins are mounted |
| Style wrap | pstack | Nothing in the loop |
| Place / PTY | Herdr | Server-owned terminals |
| Continual H | Prime Agent | `/refine` from trajectory |
| **Judgment backend (this catalog)** | Jev examples | A probability over a closed question; workflow stays in code |

Sibling: [[wiki/sources/jev-ultrafast]] is the browser-shaped member of the same family.

## Hermes / Chappy

| Repo | Hermes? |
|---|---|
| typesafe-mcp | **Refuted** as a listed client (Claude/Codex/pi only) |
| jev-codex-router | Reads `~/.hermes/.env` for `TYPESAFE_API_KEY` — path default, not an adapter |
| Prism | Can POST to Hermes HTTP / spawn `hermes` ACP for *alerts*; Jev stays advisory |
| Canny / winnow / fast-jev-compaction | Claude Code / Codex hooks, not Hermes |
| rest | No Hermes surface in README/tree at this depth |

Honest steal without install: **code owns workflow; model gets a closed question; DONE/probability is not proof; fail-open or deterministic fallback.** Canny's «won't finish on a claim» is the closest process-borrow to vault evidence gates.

## Safety

- **Keys:** almost every live path sends task/diff/tool-result JSON to `api.typesafe.ai` (or Gateway / OpenRouter). Unset-key fallbacks exist in Canny, neo4jev, OneVOneJev, jev-trader `mock`, killmyidea `TYPESAFE_MOCK`.
- **Pipe-to-sh:** typesafe-mcp `install.sh`; Prism `scripts/install.sh`.
- **Loopback binds:** jev-review `:4317`, winnow `:47311`, jev-codex-router `:4319` / Codex router `:4202`.
- **Money / chain:** jev-trader, Prism — reference only; do not fund wallets from this ingest.
- **Copyright:** typesafe-mario ships no ROM; operator must have a legal copy.
- **json-render Jev** and **agent-desktop jev-desktop** are optional experiments on large products — do not ingest the whole json-render/agent-desktop trees as «Jev architecture».

## Status

- Catalog depth: **README-level + tree + API + a few in-tree contracts**. Not a code audit of 1653-blob json-render or 1360-blob router fork.
- Confidence: **high** on existence, licenses-or-None, blob counts, advertised Jev role; **author-claim** on speed/money/ablation tables; **Unknown** on unpublished Jev quota (Prism gate comment).
- This host: **none of 2–20 installed.** Item 1 still not on PATH (see [[10_Reference/tools/jev-ultrafast]]).

## Links

- Canonical policy: [[wiki/sources/jev-ultrafast]]
- Concept: [[wiki/concepts/indexed-action-space]]
- CDP substrate: [[wiki/sources/browser-harness]]
- Entity (item 1 only): [[wiki/entities/browser-use]]

## Sources / provenance

- User list of 20 GitHub URLs, 2026-09-22
- GitHub API `/repos`, `/git/trees?recursive=1`, `/tags?per_page=5`
- README raw.githubusercontent.com (hashes above)
- Extra: json-render `apps/web/lib/jev/README.md` + `docs/jev/page.mdx`; Prism `engine/jev-gate.ts` + `jev-service.ts`; Canny README § Jev; agent-desktop `skills/jev-desktop/SKILL.md`; package/Cargo/pyproject versions as cited
