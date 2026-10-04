# Build A Reasoning Model From Scratch 6 — GRPO for RLVR

## Bibliographic

| Field | Value |
|---|---|
| Title | Build A Reasoning Model From Scratch 6: Reinforcement Learning 1 (Implementing GRPO for RLVR) |
| Channel | Sebastian Raschka (`@SebastianRaschka`) |
| Published | 2026-10-03 |
| Duration | **Unknown**. Last chapter starts at 1:24:05; the player never reported a runtime |
| URL | https://www.youtube.com/watch?v=237Hf7Q3lgg |
| Transcript source | **description-only** — no caption track, timedtext empty, transcript panel empty |
| Series | "Build A Reasoning Model From Scratch", episode 6 (playlist link in the description) |
| Speaker | [[wiki/entities/sebastian-raschka]] |
| Raw capture | `[[raw/youtube-237Hf7Q3lgg]]` |

## One-line purpose

Raschka walks a from-scratch Python implementation of RLVR with GRPO, training a small reasoning model and checking it on MATH-500.

## Thesis

The bullets below are the description's own chapter titles, in order. They are the author's outline of what the lecture covers. They are not quotes from speech, and nothing here was checked against code.

- A reasoning model is treated as different in kind: reasoning traces, then how much capability those traces buy (00:00–08:29).
- Rewards split into accuracy and format. The outline names "aha moments" and DeepSeek-R1 training, then reasoning effort as a function of answer length (08:29–18:38).
- RLHF is set next to RLVR, then GRPO next to PPO. GRPO is explained with a cooking analogy, and the outline isolates a KL term and a "simplified GRPO" (18:38–35:04).
- The implementation path, as titled: load a pretrained model, load MATH training data, sample responses, compute verifiable rewards, compute advantages, then token and sequence log probabilities (35:04–57:37).
- One chapter is an error fix ("Fixing the inference-mode error"), then the GRPO loss, one GRPO step, and the training loop with settings, logging, and checkpoints (57:37–1:17:24).
- Close: run training, inspect outputs, load and evaluate checkpoints, report MATH-500 results and training stability, then memory requirements and next steps (1:17:24–1:24:05 and after).

What the description states in prose, as an author claim: the video is a from-scratch Python implementation of Reinforcement Learning with Verifiable Rewards (RLVR) using Group Relative Policy Optimization (GRPO) to train a small reasoning model.

Linked from the description, not opened: a reasoning book (`amzn.to/4aAKiFY`), a reasoning GitHub repo under `rasbt` (URL truncated in the page), plus the earlier "LLMs from Scratch" book and repo.

## Status

| | |
|---|---|
| Confidence | **low** on every technical claim — the spoken argument was not captured |
| Depth | description + chapter list only |
| Not a tool | A lecture. No tool card. Not a harness, so not added to the harness card. Not added to barbell. |
| Not installed | The repos named in the description were not cloned. |

## Provenance

- Title and author: YouTube oEmbed, 2026-10-04.
- Date, view count (6,735), likes (131), and the description body: watch-page HTML after a headless browser load, same day. Description links render truncated.
- Duration and transcript: not obtained. `yt-dlp` is not installed; the video file was not downloaded. Player API returned `LOGIN_REQUIRED` ("Sign in to confirm you're not a bot"); no `captionTracks`; timedtext list was empty; the transcript panel rendered zero segments.
- Body sha256 `c1dfbd9c7e26a11c6602d4f6a13fd58a8540ba4c42a3dda070e1c19af093ce5c` on `[[raw/youtube-237Hf7Q3lgg]]`.

## Sources

- `[[raw/youtube-237Hf7Q3lgg]]`
