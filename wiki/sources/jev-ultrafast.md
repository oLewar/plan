# Jev Ultrafast (browser-use/jev-ultrafast)

## Bibliographic / source

| Field | Value |
|---|---|
| Title | **Jev Ultrafast** |
| Tagline | A browser agent with a dynamic, indexed action space |
| Org | [[wiki/entities/browser-use]] × [TypeSafe](https://docs.typesafe.ai/introduction) (Jev model; TypeSafe itself **not ingested**) |
| Repo | [browser-use/jev-ultrafast](https://github.com/browser-use/jev-ultrafast) |
| Site | https://browser-use.com (org homepage; no dedicated product URL) |
| License | MIT (`LICENSE` «Copyright (c) 2026 Browser Use») |
| Language | Python 3.12+ (`jev_ultrafast/`); inspector on loopback |
| Version at ingest | crate/pyproject **0.1.0**. **No git tags. No PyPI package.** HEAD is the only version. |
| Default branch / HEAD | `main` @ `452c1ad2dd62` («Reduce browser round trips and record a 7-second Flights demo», 2026-09-17) |
| First commit | `68c077bf79ca` 2026-09-17 («Build Jev Ultrafast browser agent and real-web demo») — repo created 2026-09-16 |
| Stars / forks / subscribers | **3316** / **194** / **2** (GitHub API 2026-09-18) |
| Open issues | **21** |
| Tree size | GitHub API `size` 4478 KB; recursive tree **40 blobs / 6 trees**, not truncated |
| Domain | typed browser policy; indexed DOM actions; TypeSafe speculative fan-out |
| Raw capture | durable `40_Research/sources/agent-dev/browser-use-jev-ultrafast-readme.md` (cron moved from inbox) |
| Agent contract | [AGENTS.md](https://github.com/browser-use/jev-ultrafast/blob/main/AGENTS.md) + [docs/design.md](https://github.com/browser-use/jev-ultrafast/blob/main/docs/design.md) + [jev_ultrafast/agent.py](https://github.com/browser-use/jev-ultrafast/blob/main/jev_ultrafast/agent.py) |
| Runtime dep | `browser-harness==0.1.13` (pinned in `pyproject.toml`) |

## One-line purpose

Give **one natural-language goal**. TypeSafe's Jev picks an **operation + observed element** in one request. A small LLM writes text **only** when the operation is `TYPE_TEXT`. Code owns execution; the model never emits selectors, coordinates, or JS.

## Thesis (README + AGENTS.md + design.md + performance.md + sampled Python)

1. **README is a product page (~8 KB) with a real tree.** Architecture is `agent.py` / `snapshot.js` / `model.py` / `docs/design.md`, not the banner. Medium-README + live-tree class.
2. **Not a fifth harness axis and not a CDP harness.** Jev is a **policy** on [[wiki/sources/browser-harness]]. The loop is still «host agent or `jev` inspector»; Browser Harness owns the websocket.
3. **Indexed action space.** Observation builds `[1] role · label · value`. Operations: `CLICK`, `TYPE_TEXT`, `SELECT`, `SCROLL_UP`, `SCROLL_DOWN`, `WAIT`, `DONE`, `BLOCKED`. Target heads contain only compatible elements. Speculative targets; only the chosen operation's head executes.
4. **DONE is not success.** Independent predicate in `examples/flights.py` checks URL/path, one-way control, Zürich/London, date, visible «Select flight» rows. Author: «A `DONE` choice still requires independent outcome verification.»
5. **Demo numbers are one-task, three-pair.** Recorded Flights run **7073 ms** (`docs/flights-measurement.json`). Matched medians **9.450 s → 7.092 s** (25%), protocol calls **1092 → 101**, TypeSafe requests **22 → 17**, 3/3 verified each arm. Author: sign-test p = 0.25; not a general benchmark. Wikipedia smoke **2.798 s**; local hotel fixture **1.896 s**.
6. **Text helper is not hardcoded.** `.env.example`: `TEXT_MODEL_BASE_URL=https://openrouter.ai/api/v1`, `TEXT_MODEL=inception/mercury-2.5`, `TEXT_MODEL_REASONING=none`. Code default if env unset: `https://api.deepseek.com/v1` / `deepseek-chat`. Recorded run generated «Zurich» 581 ms and «London» 346 ms; OpenRouter **$0.00006272** for two text calls. TypeSafe tokens 90 558 in / 6 325 out — **no billed dollar** in the JSON.
7. **Budgets (design.md + `questions.py`).** `MAX_STEPS = 60` actions; 120 decision requests (`len(decisions) >= MAX_STEPS * 2`). Up to 250 action candidates; truncated cannot be selected. Inspector binds **`127.0.0.1:8766`** (`TYPESAFE_DEMO_PORT`); Host / Origin / `X-Demo-Token` checks.
8. **MVP limits (author).** No full accessible-name spec; no shadow roots, frames, canvas, uploads, pop-up tabs, nested scrolling, arbitrary keyboard widgets. Owned tabs share the existing Chrome profile.

## Architecture snapshot

```
goal
  → Browser Harness CDP session (background tab, 1120×780, focus emulation)
  → snapshot.js  (atomic HTML/ARIA table + WeakMap node ids)
  → TypeSafe POST https://api.typesafe.ai/v1/systemone
        questions: operation + click_target + type_text_target + select_target
  → if TYPE_TEXT: OpenAI-compatible helper → JSON {text}
  → executor: geometry + occlusion check; no model-authored selectors
  → independent verify (examples), not the DONE token
```

| File | Job |
|---|---|
| `jev_ultrafast/agent.py` | Loop: predict → act; text-cache only if helper *input* identical |
| `jev_ultrafast/snapshot.js` | One browser call: visible controls, names, values, node identity |
| `jev_ultrafast/browser.py` | `ensure_daemon()` + CDP; waits 50 ms / combobox 200 ms / WAIT 100 ms |
| `jev_ultrafast/model.py` | Dynamic heads; `TYPESAFE_MODEL` default `jev-latest` |
| `jev_ultrafast/demo.py` | Loopback inspector `jev` |
| `docs/performance.md` | Matched comparison + limits |

### Contrast

| | Jev | Browser Harness | Typical screenshot agent |
|---|---|---|---|
| Model sees | Indexed elements + page text | Whatever the host agent prints (`page_info`, AX, screenshot) | Pixels |
| Chooses | Operation + index | Free Python / CDP | Click xy / typed plan |
| Writes helpers? | No | Yes (`agent_helpers.py`) | Sometimes |
| Proof of done | Independent checker | Human / host agent | Often the model's own STOP |

## Why it matters for `pro/plan`

- Causal split: **choice ≠ generation**. Typed heads bound the action space; text LLM is a *field filler*, not a planner ([[wiki/concepts/causal-analysis]]).
- Efficiency: one TypeSafe round-trip per cycle vs serial operation-then-target; no default screenshots in the library loop ([[wiki/concepts/efficiency-metric]]).
- Honest steal without install: «model output never becomes selectors» + independent DONE check. Do not treat 7.1 s Flights as a product SLA.
- Not a Hermes adapter. Needs `TYPESAFE_API_KEY` + text-model key + live Chrome via Browser Harness.
- Sibling catalog of **other** Jev backends (not this loop): [[wiki/sources/jev-usage-examples]] (20 public repos, 2026-09-22).

## Status

- Ingest depth: README `main` + AGENTS.md + design.md + performance.md + performance-prepared.md + pyproject **0.1.0** + `.env.example` + sampled `agent.py` / `model.py` / `browser.py` / `questions.py` / `demo.py` / `examples/flights.py` + `docs/flights-measurement.json` + GitHub API repo/commits/tree. **Not executed. Not installed.**
- Confidence: **high** on loop/API/pin (`browser-harness==0.1.13`); **author-claim / small-n** on 7.1 s and 25% (3 pairs, live Google).
- No release tags. README version is **0.1.0** in pyproject only.

## Links

- Entity: [[wiki/entities/browser-use]]
- Concept: [[wiki/concepts/indexed-action-space]]
- Runtime it sits on: [[wiki/sources/browser-harness]]
- Tool card: [[10_Reference/tools/jev-ultrafast]]
- Examples catalog: [[wiki/sources/jev-usage-examples]]

## Sources / provenance

- Repo https://github.com/browser-use/jev-ultrafast (`main` @ `452c1ad2dd62`, 2026-09-18)
- Raw capture sha256 `fa269c28298a17792e9ed8738b4269e757d24f38ab83087908fcd256de458cfe` (8401 bytes, LF)
- Measurement JSON `elapsed_ms: 7073`, `verification.passed: true`
- TypeSafe docs cited by README, **not** ingested as a separate source
