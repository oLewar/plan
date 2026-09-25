# CLM (Contrastive-LM/CLM)

## Bibliographic / source

| Field | Value |
|---|---|
| Title | **Contrastive Language Models (CLM)** — a System One model for fast, generalizable decision-making |
| Org | [[wiki/entities/contrastive-lm\|Contrastive-LM]] (GitHub `Contrastive-LM`; org metadata **not fetched**) |
| Repo | [Contrastive-LM/CLM](https://github.com/Contrastive-LM/CLM) |
| Blog | https://contrastive-lm.notion.site (not fetched; citation calls it a Notion blog, not a paper) |
| Weights | [Contrastive-LM/CLM-v0.1-8B](https://huggingface.co/Contrastive-LM/CLM-v0.1-8B) (`CLM_v0.1-8B.pt`) |
| Discord | https://discord.gg/5dAQEDJBs |
| PyPI | `contrastive-lm` (commit `fe9b720dc172`, 2026-09-24, «Publish to PyPI»; not verified on PyPI from this host) |
| License | Apache-2.0 (code and the released CLM-8B weights, per README) |
| Language | Python + JS/CSS/HTML playground + shell |
| Version | **0.1.0** (`pyproject.toml` and `src/clm/__init__.py`). **Zero git tags, zero GitHub releases** |
| Default branch / HEAD | `main` @ `bb42c6c5bf91` (2026-09-24, 2048-token limit note) |
| Stars / forks / issues | **947** / **71** / **4** (GitHub API, 2026-09-25) |
| Created / last push | 2026-09-23 / 2026-09-24 |
| Description (API) | `None` |
| Author (pyproject) | Jacky Kwok (`jackykwok@berkeley.edu`). Citation also names Hangoo Kang, Tarun Suresh, Jon Saad-Falcon, Marco Pavone, Christopher Ré, Azalia Mirhoseini — not separate entity pages |
| Domain | local System One ranker: frozen encoder + small contrastive heads; TypeSafe-compatible wire |
| Raw capture | [[raw/Contrastive-LM-CLM-readme]] |

## One-line purpose

Score a **closed set of candidate actions** against a state by embedding both and taking a dot product. Typed questions (`noul` / `choice` / `score`) are that ranker with a softmax. Same wire as TypeSafe `POST /v1/systemone`, so a Jev client can point at `clm-serve` instead of the hosted API.

## Thesis (README + `src/clm` + T-Rex example)

1. **Not a generative policy.** Two encoders (frozen LLM + ~20M projection head each) trained with bidirectional InfoNCE. At serve time: one embedding per fresh text, a dot product per cached candidate, softmax over the closed set. No free-form tool call, no selectors.
2. **Disaggregated state and action.** Embeddings cache independently. Default vector arena is 2% of device memory (`--action-cache`), LRU, keyed by head generation so a hot-reloaded checkpoint does not reuse stale rows. A cache hit skips the encoder. `usage.input_tokens` counts only cache misses.
3. **Three question types, one primitive.** `choice` embeds each option's description (or the key if the description is empty). `score` is an ordered rubric; the answer is the expected index. `noul` is P(true). `confidence` = top probability minus the mean of the rest (`schema.py`). State text is prose (`key: value` / `- item`), never JSON.
4. **Reference stack is local.** `vllm serve Qwen/Qwen3-8B --runner pooling --max-model-len 2048` on `:8090`, then `clm-serve` on `:8700`. Heads default to CPU if torch sees no GPU (`--device` / `CLM_DEVICE`). First run downloads the head to `~/.cache/clm/` via `clm-download` (HF repo `Contrastive-LM/CLM-v0.1-8B`, file `CLM_v0.1-8B.pt`). `clm-raw` is an ablation: cosine in raw encoder space, no head. States longer than 2048 tokens are truncated unless both limits are raised.
5. **TypeSafe-compatible, not TypeSafe.** `CLMClient.system_one(state, questions)` and `POST /v1/systemone` accept the same question dicts. T-Rex (`examples/t_rex/trex/backends.py`) sends one client at either `http://127.0.0.1:8700` (`clm-latest`) or `https://api.typesafe.ai` (`jev-latest`). Jev still needs `TYPESAFE_API_KEY`. CLM key is optional (`CLM_API_KEY`).
6. **Training recipe is README-claimed, code for fine-tune only.** Pre-train ~60M Nemotron DQA pairs, mid-train ~30M Gemini 2.5 Flash-Lite hard negatives, post-train ~1M ADP / Endless-Terminals / LiteCoder trajectories with 40% DQA replay. This branch ships `train/finetune.py` (heads only, frozen encoder) and `evaluation/bon_eval.py`. README says scaling experiments and data pipelines live on «the research repo's `main` branch» — that other repo was **not** fetched. No arXiv id in the citation.
7. **Author numbers, not reproduced here.** Zero-shot chart: on par with Jev, up to **9×** lower latency (computer-use, gaming, tool-calling; WikiRacing and T-Rex called out). Verifier: sample solutions (**Opus 5** on DeepSWE, **Fable 5** on Terminal-Bench 2.1), CLM or Jev picks one. Held-out **38** DeepSWE and **30** TB2.1 tasks; Jev «below pass@1»; fine-tuned CLM **81.6%** and **87.6%**, **4.1–5.7×** faster than Jev, latency on an H100. Scaling: InfoNCE power law; optimal head size ~**310 tokens per parameter** (`N* ∝ D^1.02`). Blog holds the fits. Not run on this host.
8. **Shipped T-Rex is not a pure model score.** Planner labels each of `jump` / `duck` / `run` Safe or Unsafe and marks the best one in the Choice text. Shield (on in the published table) replaces an unsafe argmax with the model's most probable safe action. README: survival measures the **combined system**; agreement and interventions measure the model.

## Architecture snapshot

```
client / playground
    → clm-serve :8700  (FastAPI, CPU or GPU heads)
         POST /v1/systemone · POST /v1/rank · GET /v1/models · GET /health · GET /
         state head + action head (~20M), vector arena
    → vLLM Qwen3-8B pooling :8090  /v1/embeddings
```

| Piece | Role |
|---|---|
| `src/clm/schema.py` | Question → (state text, candidate texts); softmax; confidence |
| `src/clm/engine.py` | `answer` / `rank`; models `clm-latest`, `clm-raw`; release date constant `2026-09-19` |
| `src/clm/client.py` | HTTP client, no torch. Default `http://127.0.0.1:8700` |
| `src/clm/heads.py` | MLP head (`hidden 4096 → proj 512`), HF download, hot-reload |
| `src/clm/server.py` | `clm-serve`. `--cors` off by default (API key must not be readable by any origin) |
| `src/clm/static/` | Playground, no build step. `--no-ui` drops it |
| `train/finetune.py` | Fine-tune heads. `docs/FINETUNING.md` is an autonomous loop over that one file |
| `examples/t_rex/` | Real-time dino clone (from laya-vs-jev, Apache-2.0) + shipped JSON |

Tree: 46 blobs, 15 trees, not truncated, HEAD `bb42c6c5bf91`. No tags.

### Shipped T-Rex JSON (author runs, in-repo)

Prompt `labeled`, shield on, 5 seeds × 60 s, 6 requests in flight, course `original`. Both report **5/5 survived, 0 deaths, mean best score 697**.

| | CLM (`clm-latest`, local, README: RTX 4090, 2026-09-23) | Jev (answered `jev-1.13.0`, 2026-09-22) |
|---|---|---|
| Client p50 latency | 16.5 ms | 149.8 ms |
| Server/model p50 | 2.6 ms | 131.9 ms |
| Mean agreement with planner | **0.658** | **0.987** |
| Mean decisions | 3342 | 1119 |
| Summary `shield_interventions` | **4883** | **28** |
| Per-seed `shield_interventions` (sum) | 46+86+86+72+74 = **364** | **0** |
| Per-seed `arrival_saves` (sum) | **4519** | **18** |
| Per-seed `emergency_saves` (sum) | 0 | **10** |

The summary field adds more than the per-seed `shield_interventions` column (CLM 4883 ≠ 364). Do not quote 4883 as «the shield replaced the model 4883 times» without saying which field. The per-seed split is the one that matches the README's two counters (unsafe-argmax replacements vs arrival/emergency saves). Jev agrees with the planner ~99% and barely needs the shield; CLM is ~9× lower latency on this trace and agrees only ~66%. Survival is tied because the shield is on. `--no-shield` is explicitly not part of the table.

## Contrast

| | CLM | Jev ([[wiki/sources/jev-ultrafast]], [[wiki/concepts/indexed-action-space]]) |
|---|---|---|
| What it is | Local ranker: frozen Qwen3-8B + two small heads | Hosted TypeSafe model (`jev-latest` / pinned `jev-1.13`) |
| Wire | `POST /v1/systemone` with `noul` / `choice` / `score` | Same wire (T-Rex sends both through one client) |
| Weights | You serve them (`clm-serve` + vLLM) | API key, no local weights |
| Closed set | Yes — softmax over the texts you pass | Yes — op + observed element index in the browser policy |
| This repo's loop | None. T-Rex planner owns physics and the shield | Browser Harness loop is a different repo |

Not a harness axis. Not a replacement for the Jev browser policy. It is a **drop-in System One backend** for callers that already speak that wire, plus a fine-tunable verifier head.

`docs/FINETUNING.md` is a separate thing: an instruction sheet for an LLM to loop on `train/finetune.py` only (no other files, no training on the eval split). That is an experiment protocol, not the CLM model.

## Why it matters for `pro/plan`

- The Jev catalog ([[wiki/sources/jev-usage-examples]]) assumed a hosted TypeSafe key. CLM is the public local speaker of the same question wire. Still not installed here.
- Honest steal: cache state and action embeddings separately; count only cache-miss tokens; don't treat a shielded survival rate as the model's score.
- Do not copy the 9× / 87.6% / 81.6% lines into a decision without the held-out sizes (30 and 38) and the «author, not reproduced» label.
- Pointing `clm-serve` at Hermes tool-picking would still be a closed-set ranker. It does not write memories and it does not replace the agent loop.

## Status

- Ingest depth: **README + pyproject + `src/clm/{__init__,schema,engine,client,heads}.py` (defs + schema body) + T-Rex README + `backends.py` + both realtime JSON + `docs/FINETUNING.md` (head) + GitHub API repo/languages/tree/commits/tags**. Not cloned. **Not installed. Not run.** Blog and weight file not fetched. Org API not fetched. Paper PDF does not exist in the citation.
- Confidence: **high** for the serve path, wire, and the shipped T-Rex JSON; **medium** for training-scale and benchmark claims (README/blog only); **low** for «research repo `main`» contents (not opened).
- Hermes/Chappy: **reference only**. Do not `pip install contrastive-lm` or start vLLM without an explicit ask. A 24 GB GPU note is in the README (`--max-model-len 2048`); this host was not checked.

## Links

- Entity: [[wiki/entities/contrastive-lm]]
- Concept: [[wiki/concepts/contrastive-action-ranker]]
- Tool card: [[10_Reference/tools/clm]]
- Contrast: [[wiki/sources/jev-ultrafast]], [[wiki/concepts/indexed-action-space]], [[wiki/sources/jev-usage-examples]]
- Adjacent list: [[10_Reference/Agents/tools/harness]]

## Sources / provenance

- README `main` fetched 2026-09-25, sha256 `e0f9a2a5016a314f6f963ca1d759f044895f5ca4bb134cc4e8e3e3f2a1a1483e` (21687 bytes, LF)
- `pyproject.toml` version `0.1.0`; scripts `clm-serve`, `clm-download`
- `src/clm/schema.py`, `heads.py` (`HF_REPO`, `HIDDEN=4096`, `PROJ_DIM=512`)
- `examples/t_rex/README.md`, `trex/backends.py`, `results/{clm,jev}_realtime.json`
- GitHub API repo + languages + recursive tree + commits + tags (0), 2026-09-25
- HEAD `bb42c6c5bf91` (2026-09-24)
