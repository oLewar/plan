# Julia 1 (Supersonic Labs)

## Bibliographic / source

| Field | Value |
|---|---|
| Page | https://supersoniclabs.ia.br/julia-1/ (EN; PT twin `/pt/julia-1/` not fetched) |
| Title | Introducing Julia 1 |
| Lab | Supersonic Labs — X [@supersonicai](https://x.com/supersonicai). Site line: "fast, local, and accessible AI" on hardware people already own |
| Weights | https://huggingface.co/SupersonicLabs/Julia-1 — Apache-2.0, created 2026-09-23, SHA `7a169d1c100b` at ingest, **29 likes, 0 downloads** (API 2026-09-26) |
| ONNX / WebGPU sibling | https://huggingface.co/SupersonicLabs/Julia-1-ONNX (named, not fetched) |
| Base | [jhu-clsp/mmBERT-small](https://huggingface.co/jhu-clsp/mmBERT-small) — ModernBERT encoder, MIT, fill-mask. Hidden 384, 22 layers, 6 heads, vocab 256000, max position 8192 |
| Package | `supersonic-julia` **0.1.0**, Python ≥3.11, `torch>=2.6`, `transformers>=5.0,<5.1` |
| Checkpoint | `weights_sha256` `df853bf7fe424420011f3d0c47a05d7341aa9eefa7fb9f203ea4aada4ad95b72`. Provenance: family Julia-1, variant `posttrained-candidate`, **step 500**, `quality_gate: false`. Parent SHA `e0fce3f70bc1…` |
| Size | 144.3M parameters (encoder ~140M + decision head). FP32 weights **550.5 MiB** |
| Raw capture | [[raw/supersonic-labs-julia-1]] |

## One-line purpose

Локальный энкодер, который по тексту и 2–20 готовым вариантам возвращает один выбор (`choice` / `score` / `noul`). Тот же словарь вопросов, что у TypeSafe Jev и у CLM. Не чат и не генератор.

## Thesis (from the page, the model card, and `julia/model.py`)

1. **One interface, three question types.** `predict(state, questions)` with caller-defined ids. `choice` maps ids to descriptions and returns the winning id. `score` is an ordered rubric; the answer is the *expected* zero-based index (a float, not an argmax). `noul` omits criteria and returns P(true), with options fixed as false then true. Native call: 2–20 options. Named-question path returns a full softmax. The legacy list API rounds for display: if the winner is above 0.95 and every other bar is under 0.045, probabilities become 1 and 0 (`julia/probabilities.py`).
2. **Encoder plus a marker head, not a contrastive pair.** `JuliaDecisionModel` runs mmBERT, adds a learned type embedding (3 types), then a 2-layer `TransformerEncoder` over the sequence. Only option-marker positions are scored (`LayerNorm → Linear → GELU → Linear → 1`). Invalid options are masked at −1e4. A separate `act_head` (width+4 → 256 → 2) can emit an action from the top-two gap, entropy, and option count. `julia_config.json`: `head_layers: 2`, `n_act: 2`. Page states outright: **not a fine-tuned Qwen**.
3. **The Jev column is a supplied reference, not a run they did.** Card: "Jev numbers are supplied comparison references, not a new Jev run." Protocol pin: [AbdelStark/jev-benchmarks@0d610cc](https://github.com/AbdelStark/jev-benchmarks/tree/0d610cc53e79bcbec691312b0c4adb4a0e371642) and dataset `btzsc/btzsc`. Typed decisions: [LocalLLaMA/typed-decisions](https://huggingface.co/datasets/LocalLLaMA/typed-decisions) @ `c76749ec`.
4. **Long lists go through a Router, and the Router can drop the right label.** Banking77 is 72 labels narrowed to a top-16 shortlist, not a native 72-way call. Grouped probabilities cover the survivors only, not the original list.
5. **Budget and successor, as claimed.** Page: cloud GPU spend about **R$540 (US$104.08)**. Julia 2 is planned on their own foundation, without mmBERT, and is not released. Planned API price **$0.025 / M input tokens, $0.00 output** — not open at ingest. Training pipeline is **not** in the repo.

## Numbers (author files, not our run)

H200 BF16, strict encoding, 1024-token limit, 2026-09-24. Same SHA `df853bf7…`. From `metrics/accuracy-20260924.json`:

| Task | Julia 1 | Jev reference (supplied) |
|---|---|---|
| Typed decisions | 1,463 / 2,000 = **73.15%** | 72.70% |
| — choice | 428 / 600 = 71.33% | |
| — noul | 484 / 600 = 80.67% | |
| — score | 551 / 800 = 68.88% | |
| AG News, 4 labels, n=100 | 94% | 91% |
| DAIR Emotion, 6 labels, n=100 | 86% | 48% |
| Banking77, 72→top-16, n=100 | 64% (1 abstention; coverage 0.99) | 87% |

MASSIVE, 18 scenarios, 52 locales, 2,974 each: **110,573 / 154,648 = 71.50%**. The card calls this macro accuracy; the unweighted mean of per-locale accuracies is the same 0.715 because every locale has the same count. Span: am-ET **44.9%** (1,334/2,974) to en-US **86.8%** (2,580). pt-PT 86.2% (2,565). Intent and slot filling were not measured. Brazilian Portuguese was not in this table.

CPU rerun, 2026-09-25, PyTorch 2.14.0+cpu, same SHA (`data/julia-1-cpu-20260925.json`): typed **1,451 / 2,000 = 72.55%** (choice 426, noul 483, score 542); AG News 94; Emotion 86; Banking77 **60 / 100 with 3 abstentions**. The page's "three abstentions" belongs to this CPU run. The H200 JSON has **one**.

Latency, same checkpoint, workloads not comparable (`data/julia-1-hardware-20260926.json`):

| Machine | Workload | Median |
|---|---|---|
| Apple M4, 4 CPU threads | 128 synthetic calls, 100 words, 4 options, batch 1 | 33.15 ms (28 req/s); RSS end 279 MiB |
| Apple M4, batch 16 | same 128 | 312 ms/batch (51 req/s); RSS end 371 MiB |
| Samsung SM-X510, ONNX Runtime 1.27, CPU fallback | 40 typed decisions, ~92 tokens | 203 ms (5 req/s); peak RSS 393 MB. XNNPACK left out: a `Reshape` miscompiles. Trace not attached |
| Intel i5-1235U | the 2,300-row CPU eval | typed 295 ms; AG News 108 ms; Emotion 90 ms; Banking77 **3.7 s** (the shortlist) |

8,192-token context is the runtime default. Historical accuracy used 1,024. An 8k smoke test is in the repo; **8k task accuracy is not established**.

## Why it matters for `pro/plan`

- Third public speaker of the closed-choice dictionary, after hosted Jev and local CLM. Different machine: mmBERT markers, not Qwen contrastive heads, and **no** `POST /v1/systemone` in this repo — the Python API is `engine.predict`. See [[wiki/concepts/supplied-option-ranker]].
- The useful causal split is the same one as [[wiki/concepts/contrastive-action-ranker]]: a score over options **you** wrote is not knowledge and not a multi-step proof. Banking77 is the concrete failure (64 and 60 vs a supplied 87) and it is a Router failure, not a native 72-way failure.
- Display rounding can turn 0.96 into 1.0. Do not quote legacy `probabilities` as the softmax.
- Not a harness. Not installed here. Weights not downloaded.

## Status

- **Ingest source**: the lab page (200, 66555 B) + HF model API + README + `provenance.json` + `metrics/accuracy-20260924.json` + both lab data JSON + `julia/{model,typed,probabilities}.py` + `pyproject.toml` + both configs + mmBERT model API. Not cloned. Weights not downloaded. ONNX repo, PT page, Jev-benchmark tree, and the training pipeline not fetched.
- **Confidence**: high on architecture, SHA, the 2026-09-24 table, MASSIVE 71.50%, and the CPU JSON (those are files). High that the Jev column is a supplied reference (the card says so). Medium on the R$540 figure and the Samsung trace (page / "summary provided by the user"; raw trace not attached). The 100-example pilots are the author's n, not a confidence interval.
- **Do not cite**: 73.15% as "beats Jev" without "supplied reference, not a paired rerun"; Banking77 64% as a native 72-way accuracy; 8k as a measured accuracy; download count 0 as "nobody has it" (config-based Hub count misses bare `model.safetensors` fetches, and the card says it is not unique users).

## Links

- Concept: [[wiki/concepts/supplied-option-ranker]]
- Entity: [[wiki/entities/supersonic-labs]]
- Tool card: [[10_Reference/tools/julia-1]]
- Same question dictionary: [[wiki/sources/clm]], [[wiki/sources/jev-ultrafast]], [[wiki/concepts/contrastive-action-ranker]], [[wiki/concepts/indexed-action-space]]
