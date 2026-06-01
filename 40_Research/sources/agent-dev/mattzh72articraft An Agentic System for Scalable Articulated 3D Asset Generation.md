---
title: "mattzh72/articraft: An Agentic System for Scalable Articulated 3D Asset Generation"
source: "https://github.com/mattzh72/articraft"
author:
published:
created: 2026-05-21
description: "An Agentic System for Scalable Articulated 3D Asset Generation - mattzh72/articraft"
tags:
  - "clippings"
---
## Articraft

**An Agentic System for Scalable Articulated 3D Asset Generation.**

[Paper](https://arxiv.org/abs/2605.15187) | [Project Page](https://articraft3d.github.io/)

Articraft transforms the creation of articulated 3D assets into a programmatic, code-generation workflow powered by LLMs. Engineered for large-scale dataset generation, it bypasses heavyweight manual tools to rapidly produce objects with semantic parts, robust geometry, and physical joints.

[![Articraft viewer showing an articulated desk lamp with joint controls and dataset metadata](../../../assets/external/github.com/136522ed58530256.png)](../../../assets/external/github.com/9d2c85e4e1ddf9dc.png)

> **Security Note:** Articraft compiles and inspects generated records by executing their `model.py` files as Python code. Only run generated records and model scripts from trusted sources.

---

## Quickstart

### 1\. Prerequisites

- Python 3.12 recommended (or 3.11). *Note: 3.13+ is not currently supported.*
- [`uv`](https://docs.astral.sh/uv/) for incredibly fast Python package management.
- [`just`](https://github.com/casey/just) as the command runner.
- [`Git LFS`](https://git-lfs.com/) for hydrating dataset records on demand.
- [`npm`](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm) (optional, but needed for local viewer frontend).

### 2\. Setup

From the repo root, run:

```
just setup
```

Fresh clones are code-first: `data/records/**` is stored with Git LFS and excluded from automatic LFS fetch by `.lfsconfig`, so it does not need to be hydrated before developing the code or browsing indexed metadata. Hydrate records only when you want to inspect, render, or edit their payloads:

```
uv run articraft data hydrate --record <record_id>
uv run articraft data hydrate --category <category_slug>
uv run articraft data hydrate --time-from 2026-04-01 --time-to 2026-04-07
uv run articraft data hydrate --last 7d
uv run articraft data hydrate --all
```

### 3\. Add API Keys

Open `.env` and set one or more provider keys (e.g. `OPENAI_API_KEY`, `GEMINI_API_KEYS`, `ANTHROPIC_API_KEYS`).

> **No API Keys?** No problem! If you don't have API keys set up, you can use external AI agents like Claude Code, Codex, or Cursor. Just point them to this repository and prompt them:
> 
> *"Create a realistic articulated \[object name\] and add it to the Articraft dataset. Follow EXTERNAL\_AGENT\_DATA.md."*

### 4\. Create an Asset

Generate your first model directly from a prompt using `articraft generate`:

```
uv run articraft generate "Create a realistic articulated desk lamp with a weighted base, two hinged arms, and an adjustable lamp head."
```

If you specify no overrides, it defaults to `--model gpt-5.5-2026-04-23 --thinking-level high`. You can change models and caps:

```
uv run articraft generate --model gemini-3-flash-preview --max-cost-usd 1.5 "Create a compact desk fan with adjustable tilt."
```

### 5\. Open the Viewer

Browse the objects you just generated. The local viewer API and React frontend can be started with:

```
just viewer
```

The viewer can browse/search the dataset from `data/records_index.jsonl` before record payloads are hydrated. When you select an unhydrated record, use the "Hydrate record" action before opening source files, traces, or rendered assets.

### 6\. Edit an Existing Asset

Fork an existing record when you want to modify it:

```
uv run articraft fork data/records/<record_id> "make the handle longer"
```

Forking creates a new child record and leaves the parent unchanged. See [Editing Existing Records](https://github.com/mattzh72/articraft/blob/main/docs/record_editing.md) for model options, dataset behavior, and history viewing.

---

## Contribute Data

A huge part of Articraft's mission is crowdsourcing a diverse, massive dataset of articulated 3D models. We welcome generation via our CLI, batch processing, or through external AI agents (like Claude Code, Codex, or Cursor).

For full details on our data pipelines, generation guides, and opening pull requests, please read the complete **[Data Contribution Workflow in CONTRIBUTING.md](https://github.com/mattzh72/articraft/blob/main/CONTRIBUTING.md)**.

**Data Usage & Licensing**  
By contributing data to the Articraft project, you acknowledge and agree that your submissions will be used to build, evaluate, and improve machine learning models, and will be distributed publicly as part of our datasets. You explicitly agree that all contributed data is released under the **[Creative Commons Attribution 4.0 International (CC-BY 4.0)](https://creativecommons.org/licenses/by/4.0/)** license.

---

## Documentation & Advanced Usage

- **[Architecture & Project Structure](https://github.com/mattzh72/articraft/blob/main/docs/architecture.md)**
- **[Editing Existing Records](https://github.com/mattzh72/articraft/blob/main/docs/record_editing.md)**
- **[Dataset Generation & Batch Processing](https://github.com/mattzh72/articraft/blob/main/docs/dataset_generation.md)**
- **[Contributing Standards & Workflow](https://github.com/mattzh72/articraft/blob/main/CONTRIBUTING.md)**
- **[Security Policy](https://github.com/mattzh72/articraft/blob/main/SECURITY.md)**

## Citation

```
@article{zhou2026articraft,
  title     = {Articraft: An Agentic System for Scalable Articulated 3D Asset Generation},
      = {Zhou, Matt and Li, Ruining and Lyu, Xiaoyang and Song, Zhaomou and Huang, Zhening and Zheng, Chuanxia and Rupprecht, Christian and Vedaldi, Andrea and Wu, Shangzhe},
  journal   = {arXiv preprint arXiv:2605.15187},
  year      = {2026}
}
```

This repository is licensed under the [Apache-2.0 License](https://github.com/mattzh72/articraft/blob/main/LICENSE).