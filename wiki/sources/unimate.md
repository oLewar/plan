# UniMate (Friedrich-M/UniMate)

## Bibliographic / source

| Field | Value |
|---|---|
| Title | **UniMate: One Unified Model to Animate Diverse Skeletons** |
| Repo | https://github.com/Friedrich-M/UniMate |
| Paper | arXiv:2609.05415 (abstract not fetched) |
| Project page | https://linzhanmou.com/unimate/ |
| Demo | https://linzhanmou.com/unimate/interactive.html |
| Authors | Linzhan Mou, Jiahui Lei, Zhiyang Dou, Chenyue Cai, Chaoyue Song, Adam Finkelstein, Szymon Rusinkiewicz |
| Affiliations on the README | Princeton · UC Berkeley · MIT · NTU. No per-author affiliation checked |
| Venue claim | "accepted to SIGGRAPH Asia 2026" (README news, 2026-07-18). Not verified against the conference program |
| Default branch | `main`. Created 2026-07-22, pushed 2026-09-27 |
| Stars / forks | 644 / 68 (GitHub API, 2026-09-30) |
| License (code) | MIT (`LICENSE`, API `spdx_id` MIT) |
| License (data) | Not MIT. Mixamo: Adobe terms. Objaverse-XL: per-object license. Truebones ZOO motions: commercial pack, not redistributed — the HF dataset is prompts, metadata, and renders only |
| Tags / releases | **none** (tags API `[]`, releases API `[]`) |
| Tree | 169 blobs, not truncated. Six PNGs in `assets/` account for ~30 MB of the 33 MB repo size. Not downloaded |
| Checkpoints | https://huggingface.co/Linzhan/UniMate — README says "preview"; "new checkpoints will be synced". **Not downloaded** |
| Dataset | UniML3D, https://huggingface.co/datasets/Linzhan/UniML3D — "being prepared for open release"; captions were re-processed and "do not necessarily match" the project page or the paper. **Not downloaded** |
| Raw capture | [[raw/Friedrich-M-UniMate-readme]] |

## One-line purpose

One motion model for many skeleton topologies (human, quadruped, bird, fish, insect, snake, rigid articulated objects), conditioned on a text prompt plus the target rig's T-pose. No per-skeleton retraining and no test-time optimization. The same weights also in-between, edit, and extend a motion by pinning part of it and denoising the rest.

## Thesis (README checked against the denoiser, the flow path, one config, and the in-between sampler — not a training run)

1. **Topology is an input, not a separate model.** The default pairing (`graph` × `adaln`, class `UniMateGraphAdaLN`) factors attention into a per-frame spatial pass and a per-joint temporal pass. The spatial pass carries learned graph-distance, edge-type, and depth biases, so the skeleton enters attention rather than being baked into a fixed joint count. The other shipped pairing (`full` × `cross_attn`) flattens joint×time into one attention and feeds the caption as cross-attention K/V. The README says the two axes are independent and all four combinations run; the paper compares the two shipped ones. Not checked past the two class files.
2. **Training is flow matching, and the config agrees.** `configs/uniml3d_60frames_graph_adaln.json`: `training.diff_model = "flow"`, 10 layers, latent 512, 8 heads, Flan-T5-base, `cond_mask_prob` 0.1, 120,000 steps, batch 16, AdamW at 1e-4, cosine with warmup, grad clip 1.0, EMA 0.9999. Loss weights in that file: geodesic `lambda_geo` 0.5, smoothness `lambda_smooth` 0.1. The linear interpolant is `ICPlan`: x_t = t·x1 + (1−t)·x0, target is the velocity. CFG at sample time defaults to 3.0 in this config.
3. **The three "applications" are one sampler with a different mask.** `inbetween_sample_ode` clamps whatever `keep_mask` selects: `(B,1,1,T)` keeps frames (in-betweening), `(B,J,1,1)` keeps joints (editing). At every Euler step the kept slice is overwritten with `(1−t)·ε + t·x1_known`, same ε as the initial noise. At t = 1 the kept slice equals the known motion. Expansion pins the head of segment n to the tail of segment n−1. The README's "holds exactly rather than being encouraged by a loss" matches this replacement. Two caveats are in the code and easy to miss: it requires `diff_model == "flow"` (diffusion would need a RePaint loop, which is not implemented), and it uses fixed-step Euler, **not** the dopri5 adaptive solver that plain text sampling uses. So the constrained modes integrate the same ODE at lower order.
4. **The dataset number is a README claim, and one source is not in the download.** 13,006 text-paired sequences, seven morphology buckets, one canonicalization. Truebones motions must be bought; the pipeline expects the stock `Truebone_Z-OO` folder. Joint names are cleaned to a shared vocabulary so the same anatomical joint embeds the same way across rigs (`use_joint_name_emb: true`). A stale text-embedding cache "costs speed rather than correctness" — the loader encodes a miss. Objaverse rigs can collapse a run (flat, rotated, inverted rest poses; clips that stitch unrelated actions); the README's fix is to train Mixamo+Truebones first, then add skip lists. Not reproduced.
5. **Inference still needs the training features.** Sampling reads `config.json`, `dataset_stats.npy`, and a checkpoint from a run directory, and takes the target skeleton from `dataset/features/<dataset>/`. A checkpoint without that directory does not animate an arbitrary FBX. Driving the original mesh is a later pipeline stage (`scripts/run_animate_motion.sh`), not the sampler.

## What was not checked

- arXiv PDF, project page, interactive demo, Hugging Face dataset and checkpoints.
- `data_process/` (47 KB of its own README, Blender export, LLM joint-name cleanup, VLM captioning). The 13,006 figure and the morphology list live there and in the paper, not in a file counted here.
- Whether the four attention×conditioning combinations all train. Two classes were opened; the README asserts the other two exist.
- Any sample. Nothing was installed (`conda`, `pip`, Accelerate).

## Why it matters for `pro/plan`

- A constraint can be a **replacement**, not a loss. Pinning known frames to the analytic interpolant holds them exactly at the last step; a penalty term would only encourage it. That is a different mechanism from "add a loss weight until it looks right", and it is why the constrained modes cannot use the adaptive solver (its internal stages never expose a t to re-pin at).
- [[wiki/concepts/causal-analysis]]: "the model generated the walk" and "frames 0 and −1 were copied from the clip" are different causes. The kept slice is not a prediction.
- [[wiki/concepts/efficiency-metric]]: one set of weights for many topologies is the cheap story. It is paid for by the canonicalization pipeline, a bought commercial pack the download does not include, and a features directory that must sit next to the checkpoint. A checkpoint alone is not the system.
- Not a harness and not a ranker. Do not put it on the harness list. MIT code license does not cover Mixamo, Objaverse, or Truebones.

## Status

- **Ingest depth**: README (19,645 bytes) + GitHub repo/tree/tags/releases API + one config + `ICPlan` + `UniMateGraphAdaLN` / `UniMateFullCrossAttn` headers + `inbetween_sample_ode`. Not a training run, not a sample.
- **Confidence**: high on license split, star count, absence of tags, the config numbers, the linear interpolant, and the replacement step (those are files). Medium on "real time" and "no per-skeleton retraining" — README claims, no timing measured here. The 13,006 and the SIGGRAPH Asia acceptance are README claims, unverified. The caption mismatch between the release and the paper is the README's own warning.
- **Do not cite**: a generated motion as if the pinned frames were predicted; Truebones motions as downloadable; the preview checkpoints as the final ones; captions on the project page as the released captions.

## Links

- Concept: [[wiki/concepts/pinned-flow-sampling]]
- Entity: [[wiki/entities/linzhan-mou]]
- Tool card: [[10_Reference/tools/unimate]]
- Adjacent: [[wiki/concepts/causal-analysis]], [[wiki/concepts/efficiency-metric]]
