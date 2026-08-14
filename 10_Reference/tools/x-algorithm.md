# X For You Feed Algorithm (xai-org/x-algorithm)

Open-source core of the **X For You** ranking + visibility stack.

- Full wiki source note: [[wiki/sources/x-algorithm|x-algorithm]]
- Entity: [[wiki/entities/xai|xAI]]
- Concept: [[wiki/concepts/multi-action-feed-ranking|Multi-action feed ranking]]
- GitHub: https://github.com/xai-org/x-algorithm
- README: https://github.com/xai-org/x-algorithm/blob/main/README.md
- Under the Hood: https://x.com/i/under_the_hood
- License: Apache-2.0
- README update noted in source: 2026-08-13

## What it is

Request-time feed assembly: Thunder (in-network) + Phoenix/SimClusters (out-of-network) → multi-action Phoenix scoring → Top-K → visibility filtering → blending with ads/prompts.

## Quick mental model

1. Predict many user actions (Phoenix).
2. Weighted sum + diversity/OON/new-author adjustments.
3. Separately decide ALLOW / INTERSTITIAL / DROP via labels + viewer graph.
4. Some safety prompts/rules stay private; outcomes surface via Under the Hood.

## Default weights (what X values)

Public defaults in `home-mixer/params/param.rs` (experiments may override):

**Positive:** copy link **+20** · reply/quote **+5** · follow **+4** · like **+0.5** · open link **+0.2**

**Negative:** report **-234** · mute **~-59** · not interested **~-43**

**Near-zero / ignored in scoring:** dwell time, profile click; AI-generated is not a ranking weight.

→ algorithm is **not** like-optimized; conversation/share/follow >> favorite; negatives dominate magnitude.

Full table + param names: [[wiki/sources/x-algorithm]].
