---
title: "perplexityai/pplx-garden: Perplexity open source garden for inference technology"
source: "https://github.com/perplexityai/pplx-garden"
author:
published:
created: 2026-05-27
description: "Perplexity open source garden for inference technology - perplexityai/pplx-garden"
tags:
  - "clippings"
---
## pplx-garden

Perplexity AI open source garden for inference technology

## Projects

### fabric-lib

RDMA TransferEngine, P2P MoE dispatch/combine kernel

- Docs: [docs/fabric-lib.md](https://github.com/perplexityai/pplx-garden/blob/main/docs/fabric-lib.md)
- MLSys'26 paper: [fabric-lib: RDMA Point-to-Point Communication for LLM Systems](https://arxiv.org/abs/2510.27656)
- Blog Post: [RDMA Point-to-Point Communication for LLM Systems](https://research.perplexity.ai/articles/rdma-point-to-point-communication-for-llm-systems)
- Blog Post: [Enabling Trillion-Parameter Models on AWS EFA](https://research.perplexity.ai/articles/enabling-trillion-parameter-models-on-aws-efa)
- Blog Post: [Weight Transfer for RL Post-Training in under 2 seconds](https://research.perplexity.ai/articles/weight-transfer-for-rl-post-training-in-under-2-seconds)
- Blog Post: [Disaggregated Prefill and Decode](https://research.perplexity.ai/articles/disaggregated-prefill-and-decode)

### pplx-unigram

Unigram tokenizer encoder

## Directory Structure

- `fabric-lib/`: RDMA TransferEngine library
- `p2p-all-to-all/`: P2P MoE All-to-All implementation
- `pplx-unigram/`: Unigram tokenizer encoder
- `python-ext/`: Python extension module from Rust code
- `python/pplx_garden/`: Python code for the `pplx_garden` package
- `rust/`: Rust utility libraries