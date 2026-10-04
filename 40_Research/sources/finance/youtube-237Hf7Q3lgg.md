---
source_url: https://www.youtube.com/watch?v=237Hf7Q3lgg
channel: Sebastian Raschka
channel_url: https://www.youtube.com/@SebastianRaschka
upload_date: 2026-10-03
ingested: 2026-10-04
transcript_source: description-only
duration: unknown
sha256: c1dfbd9c7e26a11c6602d4f6a13fd58a8540ba4c42a3dda070e1c19af093ce5c
---

# Build A Reasoning Model From Scratch 6: Reinforcement Learning 1 (Implementing GRPO for RLVR)

- Channel: Sebastian Raschka (`@SebastianRaschka`, https://www.youtube.com/@SebastianRaschka)
- Published: 2026-10-03 (page date text "Oct 3, 2026"; relative label at fetch was "20 hours ago")
- Duration: unknown. The player never started (YouTube "Sign in to confirm you're not a bot"); the progress bar stayed at 0:00 / 0:00. The description's last chapter starts at 1:24:05, which is a lower bound, not a runtime.
- Views / likes at fetch: 6,735 views, 131 likes. Channel subscriber count shown as 98.2K. These are page counters, not measurements.
- URL: https://www.youtube.com/watch?v=237Hf7Q3lgg

## Description (from the watch page, expanded description body)

This video covers a from-scratch implementation of Reinforcement Learning with Verifiable Rewards (RLVR) using the Group Relative Policy Optimization (GRPO) algorithm in Python to train a small reasoning model.

Reasoning playlist: Build A Reasoning Model From Scratch 1: Mo... (link text truncated in the page)
Reasoning Book: https://amzn.to/4aAKiFY
Reasoning GitHub repo: https://github.com/rasbt/reasoning-fr... (link text truncated in the page)

LLMs from Scratch book: https://amzn.to/4fqvn0D
LLMs from Scratch repo: https://github.com/rasbt/LLMs-from-sc... (link text truncated in the page)
LLMs from Scratch playlist: Build an LLM from Scratch 1: Set up your c... (link text truncated in the page)

00:00 Introduction
01:54 What makes a reasoning model different?
04:25 Reasoning traces and model capability
08:29 Accuracy and format rewards
11:34 Aha moments and DeepSeek-R1 training
14:41 Reasoning effort and answer length
18:38 RLHF and RLVR
23:04 GRPO vs. PPO
26:40 GRPO explained with a cooking analogy
31:43 The KL term and simplified GRPO
35:04 Loading the pretrained model
36:07 Loading the MATH training data
39:26 Sampling model responses
46:30 Computing verifiable rewards
49:55 Computing advantages
51:54 Token and sequence log probabilities
55:29 Implementing sequence log probabilities
57:37 Fixing the inference-mode error
1:02:24 Computing the GRPO loss
1:04:37 Putting the GRPO step together
1:09:19 The GRPO training loop
1:12:57 Training settings, logging, and checkpoints
1:17:24 Running training and inspecting outputs
1:19:28 Loading and evaluating checkpoints
1:22:33 MATH-500 results and training stability
1:24:05 Memory requirements and next steps

## Transcript

None. Description-only.

- `yt-dlp` is not installed. The video file was not downloaded.
- `web_extract` failed (import error).
- The watch-page HTML and a headless browser both hit YouTube's "Sign in to confirm you're not a bot". `ytInitialPlayerResponse` had no `videoDetails` and no `captionTracks`. The innertube `/youtubei/v1/player` call returned `LOGIN_REQUIRED`.
- `https://www.youtube.com/api/timedtext?v=237Hf7Q3lgg` (list, en, de, en asr) returned an empty body.
- The "Show transcript" button opened an engagement panel with zero segment renderers.
- Title and channel were confirmed via the YouTube oEmbed endpoint. The description and chapter list above are the expanded description body from the watch page, not spoken lines.
