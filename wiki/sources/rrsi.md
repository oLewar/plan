# RRSI (google-research/rrsi)

## Bibliographic / source

| Field | Value |
|---|---|
| Title | **RRSI** — Regularized Recursive Self-Improvement of Agent Harnesses |
| Org | [[wiki/entities/google-research\|Google Research]] (`google-research`; «not an officially supported Google product») |
| Repo | [google-research/rrsi](https://github.com/google-research/rrsi) |
| Paper | [arXiv:2609.24972](https://arxiv.org/abs/2609.24972) (submitted 2026-09-21; abs updated 2026-09-23) |
| Project page | https://regularized-rsi.com/ |
| License | Apache-2.0 (repo). `third_party/` carries its own licenses (harbor Terminus-2, archipelago) |
| Language | Python (388k) + Shell (35k). `requires-python >= 3.10` |
| Version | **0.1.0** (`pyproject.toml`). **Zero git tags, zero GitHub releases** — README version is package metadata, not a release |
| Default branch / HEAD | `main` @ `e4d1a7a0388e` (2026-09-22, paper link) |
| Stars / forks | **174** / **14** (GitHub API, 2026-09-23) |
| Created / last push | 2026-09-16 / 2026-09-22 |
| Description (API) | `None` |
| Domain | test-time harness search with regularization against evolve-set overfitting |
| Raw capture | [[40_Research/sources/finance/google-research-rrsi-readme]] (cron `f4921ae` routed inbox here; body sha matches GitHub README) |

Authors (arXiv, not separate entity pages): Peng Xia, Rujun Han, Zifeng Wang, Yanfei Chen, Yufan Zhang, Yoonho Lee, Chengsong Huang, Han Yu, Zhongying CuiZhu, Yifei Ming, Huaxiu Yao, Burak Gokturk, Tomas Pfister, Chen-Yu Lee.

## One-line purpose

Search loop that **edits a frozen-model agent harness** (prompts, control flow, tools, skills, memory, sub-agents) against a fixed evolve set, but **regularizes the search** so a candidate cannot bundle unbounded edits, memorize task ids, or buy a within-noise score with extra tokens.

## Thesis (README + `rrsi/*.py` + domain `rrsi.json` + arXiv abstract)

1. **The harness is the mutable object; the policy model is frozen.** Search roles (proposer, analyst, critic) and the task policy are separate. Search roles default to Claude Opus 4.8 on Vertex (`RRSI_SEARCH_MODEL`, `rrsi/llm.py`). Coding policy is `vertex_ai/claude-opus-4-8`. Harvey LAB judge is `gemini-3.5-flash`.
2. **Open edit space, constrained trajectory.** Vocabulary `K` = prompt, control_flow, config, output_plumbing, context_mgmt, client_tool, skill, memory, subagent. Structural subset `K_str` = client_tool, skill, memory, subagent. Constraints act on *how many* edits one candidate may bundle and *which* survive selection — not on what the harness may eventually contain.
3. **Algorithm 1 (proposal)** = annealed L0 budget `b_t = ceil(b_min + (b_max-b_min)·½(1+cos(π t / T)))` (`rrsi/schedule.py`). History JSONL so a falsified hypothesis is not redrawn. Stall flag redirects toward untried components. Declared component tags are checked against the diff (`rrsi/components.py: normalize`) so a prompt tweak cannot be labelled a skill.
4. **Algorithm 2 (selection)** is pure functions in `rrsi/selection.py`. Noise floor: `S' >= S* - delta`. If gain `> delta`, extra relative tokens must fit `beta0 + beta1·ΔS`. Inside the band, shaped score `w_s·ΔS - w_c·ΔC + w_n·ν` must be `> 0`. Winner is argmax `S'` among admissible, else incumbent stays. `S*` only moves up.
5. **Critic screens before eval.** Regex precheck (hard-coded credential pattern + domain denylist) plus LLM review: leakage / task ids, degenerate no-op, grader gaming, undeclared bundling, unbounded retry. Unparseable critic JSON after 3 tries = **reject**. Critic does not judge runtime crashes — smoke/compile does.
6. **Git is the incumbent.** Each candidate is a worktree off `evolve/<domain>`. Accept fast-forwards that branch. `runs/<domain>/` holds frontier, edit history, raw trials. `STOP` file, `readjudicate`, `reevaluate` exist.
7. **One core, three Domain adapters.** Coding (Terminal-Bench 2.1 → SWE-bench Verified), workspace (Harvey LAB → JobBench / GDPval / APEX), eng (EngDesign → EngDesign v1 / Frontier-Eng). Core never reads a trajectory format itself.
8. **Author numbers, not reproduced here.** Opus 4.8, same window vs unevolved `H_0`: TB2.1 74.2→80.2 (+6.0), SWE-bench 82.0→83.8, Harvey LAB evolve 89.4→90.5 / held-out 86.9→89.2, JobBench +4.7, GDPval +3.5, APEX +3.7, EngDesign 50.0→54.9, Frontier-Eng 17.7→22.0. Abstract: up to +14.1 ID, up to +4.7 OOD, ~30% fewer policy tokens than *unregularized* evolution. Gemini 3.5 Flash policy on coding: TB2.1 64.6→78.7, SWE-bench 76.8→79.0. The +14.1 is the Flash ID delta, not the Opus table.

## Architecture snapshot

```
rrsi.py --domain {coding|workspace|eng} {smoke|baseline|run|status|readjudicate|reevaluate}
        │
        ▼
Run.round  (rrsi/loop.py)
  Analyze (analyst + digester) → failure modes
  b_t, stall, untried, prune_set
  draft m candidates in git worktrees
  critic (regex + LLM) + smoke
  Evaluate on full evolve set (missing trial = 0, full denominator)
  select_round → fast-forward evolve/<domain> or keep H_t
```

| Piece | Role |
|---|---|
| `rrsi/loop.py` | Round driver |
| `rrsi/schedule.py` | Annealed edit budget |
| `rrsi/propose.py` | Draft (component, hypothesis, diff); budget enforced in `done()` |
| `rrsi/selection.py` | Floor, cost rule, within-band rule, argmax |
| `rrsi/critic.py` | Leakage / cheat screen **before** eval |
| `rrsi/components.py` | Tag vocabulary + novelty `ν` |
| `rrsi/history.py` | JSONL edit ledger, stall, prune set |
| `domains/<name>/adapter.py` | `Domain`: splits, run/score, traces, guards, denylist |
| `domains/<name>/{SKILL.md,PATTERNS.md,rrsi.json}` | Proposer constitution + hyperparameters |
| `third_party/harbor_terminus2` | Coding `H_0` (Terminus-2) |
| `third_party/archipelago` | Workspace + eng `H_0` (react_toolbelt) |

### Instance hyperparameters (from `rrsi.json` `_doc`, code-verified)

| | Coding | Workspace | Eng |
|---|---|---|---|
| Evolve | TB 2.1, 89 tasks, k=2 (178 trials) | Harvey LAB 120 tasks, k=2 | EngDesign-Open 61 tasks, k=4 (244 trials) |
| `T` / `m` | 20 / 2 | 20 / 2 | 40 / 2 |
| `b_min`–`b_max` | 1–4 | 1–3 | 1–4 |
| `delta` | 0.017 (3/178) | 0.004 (~60 criteria / ~14100) | 0.020 (5/244) |
| `w_s` | **0** (inside band: token save or new structural component only) | 1414 per unit S | 244 per unit S |
| `w_c` | 15 | 15 | 2 |
| `beta0` / `beta1` | 0.10 / 44.5 | 0.10 / 35.4 | 0.15 / 24.4 |
| OOD | SWE-bench Verified | held-out 40 + JobBench, GDPval, APEX | EngDesign v1, Frontier-Eng |
| Guards | — | — | valid-rate drop ≤ 0.03, no-payload rise ≤ 0.02 |

`delta: null` re-estimates via `rrsi/calibrate.py` (`delta_z` × sd of null score difference). Defaults in `RRSIConfig` (`w_s=100`, `beta1=40`) are **not** the paper instances — the JSON files override them.

## Contrast (not a fifth axis, and not `/refine`)

| | RRSI | Continual harness ([[wiki/concepts/continual-harness]]) | Git-native experiment tree ([[wiki/concepts/git-native-experiment-tree]]) |
|---|---|---|---|
| What changes | A **candidate harness** in a worktree | Next-turn supplemental prompt/memory | A child branch after a measured node |
| Gate | Critic + noise floor + token budget + optional domain guards | `/refine` write (weak) | Freeze-on-answer |
| Accepts within noise? | Only if shaped score > 0 (coding: `w_s=0`) | Not a measured floor | N/A — status ≠ evidence |
| Owns the task loop? | **No** — evolves Terminus-2 / react_toolbelt | Yes (IPython) | No — wraps other CLIs |
| Model | Frozen policy | The same agent that writes H | Whatever CLI you wrap |

Four public harness axes stay: DSH = loop-as-plugin, pstack = style wrap, Herdr = place/PTY, Prime Agent = continual supplemental H. RRSI is **regularized offline search over harness diffs**.

## Why it matters for `pro/plan`

- Direct answer to backlog item 9 («`/refine` vs human-gated SOUL»): a public method that **measures** a harness edit and can **reject** it for leakage, noise, or token cost — instead of writing the next prompt from the trajectory.
- Coding `w_s = 0` is the sharp rule: inside the noise band, a score bump is not a reason to accept. Only a token saving or a genuinely new structural component.
- Honest steal without install: edit ledger (component, hypothesis, ΔS, ΔC, verdict) + leakage critic before eval. Do **not** point this loop at Hermes `SOUL.md` / memories.
- Author +14.1 / +4.7 / −30% tokens stay **author claims**. PDF tables not read.

## Status

- Ingest depth: **README + pyproject + `rrsi/{selection,schedule,config,components,critic,llm,__init__}.py` + loop.round sketch + three `rrsi.json` + three domain READMEs + arXiv abstract + GitHub API repo/languages/tree/commits/tags**. Not cloned. **Not installed. Not run.** Paper PDF not read. Project page not fetched.
- Confidence: **high** for public algorithm/hyperparameters/CLI (they match the code); **medium** for the results table (README/abstract, not reproduced); **low** for whether a new domain adapter is cheap on this host.
- Tree: 128 blobs, 28 trees, not truncated, HEAD `e4d1a7a0388e`. No tags.
- Hermes/Chappy: **reference only**. Do not `pip install` or set Vertex env without an explicit ask.

## Possible Hermes/Chappy integration paths

1. **Leave as reference** — default.
2. **Process-borrow** the selection predicate (floor + relative token budget + `w_s=0` inside the band) and the leakage critic checklist onto eval write-ups. No code install.
3. **Do not** run `rrsi.py` against `~/.hermes` or `pro/plan`. The evolve set would be this vault; the critic exists because that overfits.
4. **Do not** treat RRSI as a Hermes adapter or a fifth harness axis.

## Links

- Entity: [[wiki/entities/google-research]]
- Concept: [[wiki/concepts/regularized-harness-search]]
- Tool card: [[10_Reference/tools/rrsi]]
- Adjacent list: [[10_Reference/Agents/tools/harness]]
- Contrast: [[wiki/sources/prime-agent]], [[wiki/concepts/continual-harness]], [[wiki/concepts/git-native-experiment-tree]], [[wiki/concepts/memory-poisoning]], [[wiki/sources/openresearch]]

## Sources / provenance

- README `main` fetched 2026-09-23, sha256 `4822dae4f4bf69a4502bfbf23ebbf80aeccd65e1f0cefde3652cafda586cfac8` (12070 bytes, LF). Durable file: `40_Research/sources/finance/google-research-rrsi-readme.md` (cron `f4921ae`; theme route is finance, not agent-dev — no `__2` sibling; body sha unchanged).
- `pyproject.toml` version `0.1.0`; `domains/{coding,workspace,eng}/rrsi.json`
- `rrsi/selection.py`, `rrsi/schedule.py`, `rrsi/config.py`, `rrsi/components.py`, `rrsi/critic.py`, `rrsi/llm.py`
- arXiv abs API `2609.24972` (published 2026-09-21, updated 2026-09-23) — abstract only
- GitHub API repo + languages + recursive tree + commits + tags (0) 2026-09-23
- HEAD `e4d1a7a0388e` (2026-09-22)
