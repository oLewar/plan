---
title: "buildingjoshbetter/TrueMemory: A living memory system that ingests long-horizon data to infer insights, enabling more decisive action, all while running on a single SQLite file locally."
source: "https://github.com/buildingjoshbetter/TrueMemory"
author:
published:
created: 2026-05-12
description: "A living memory system that ingests long-horizon data to infer insights, enabling more decisive action, all while running on a single SQLite file locally. - buildingjoshbetter/TrueMemory"
tags:
  - "clippings"
---
[![TrueMemory](https://github.com/buildingjoshbetter/TrueMemory/raw/main/assets/charts/hero-banner.png)](https://github.com/buildingjoshbetter/TrueMemory/blob/main/assets/charts/hero-banner.png)

A living memory system for AI agents. Long-horizon recall on commodity hardware.

[What is TrueMemory?](#-what-is-truememory) · [Quick Start](#-quick-start) · [Edge / Base / Pro](#%EF%B8%8F-edge--base--pro) · [Architecture](#-architecture) · [Benchmarks](#-benchmarks) · [API](#-python-api) · [Docs](#-docs) · [FAQ](#-faq)

---

## 💡 What is TrueMemory?

- **Remembers everything across sessions.** Facts, preferences, decisions, corrections. Your AI finally knows who you are.
- **93.0% on LoCoMo, 92.0% on LongMemEval, SOTA on BEAM-1M.** Beats every live-retrieval memory system across three major benchmarks. Independently reproducible.
- **Runs locally on a single SQLite file.** Zero cloud, zero API keys for Edge and Base tiers. Your memories never leave your machine.
- **Neuroscience-inspired architecture.** Six retrieval layers plus an encoding gate that filters noise from signal before anything gets stored.
- **Works with Claude Code, Codex CLI, Cursor, Gemini CLI, and Claude Desktop.** Lifecycle hooks capture conversations automatically. No manual work needed.

---

## 🚀 Quick Start

$Step 1.$ Open a terminal.

- **Mac:** `Cmd + Space`, type `Terminal`
- **Linux:** `Ctrl + Alt + T`
- **Windows:** open **PowerShell**

$Step 2.$ Paste this and press Enter:

**Mac / Linux:**

```
curl -LsSf https://raw.githubusercontent.com/buildingjoshbetter/TrueMemory/main/install.sh | sh
```

**Windows (PowerShell):**

```
irm https://raw.githubusercontent.com/buildingjoshbetter/TrueMemory/main/install.ps1 | iex
```

$Step 3.$ Wait 3-5 minutes for installation.

$Step 4.$ Quit Claude completely and reopen it (Mac: `Cmd+Q`, Windows: close all Claude windows).

$Step 5.$ Type **"Set up TrueMemory"** and pick Edge, Base, or Pro.

That's it. TrueMemory remembers your conversations automatically from here.

- **Switch tiers:** tell Claude "switch to Pro" or "switch to Base"
- **Update:** run `uv tool upgrade truememory` in Terminal, then restart Claude
- **Uninstall:** run `uv tool uninstall truememory`

> **⭐ Tip:** Quit your Claude sessions when you're done prompting. TrueMemory's memory hook runs when the session ends, so it can capture and store the full conversation.

**Click here for the advanced setup guide ▸**

#### What the installer does

Installs [uv](https://docs.astral.sh/uv/) (Astral's Python tool manager) if needed, fetches a managed Python 3.12, installs TrueMemory with all tier models into an isolated tool environment, registers the MCP server, wires up lifecycle hooks, and merges instructions into `~/.claude/CLAUDE.md`. Your system Python is never touched. No sudo, no venvs, no pip struggle.

#### Audit the script

It's ~200 lines of shell, no sudo, stays entirely under `$HOME`:

```
curl -LsSf https://raw.githubusercontent.com/buildingjoshbetter/TrueMemory/main/install.sh -o install.sh && less install.sh && sh install.sh
```

#### Python library (for developers)

If you're embedding TrueMemory in your own Python project (requires Python 3.10+):

```
pip install truememory
```

> `pip install` installs the Python library only. It does NOT register the MCP server, install hooks, or configure Claude. For Claude Code / Claude Desktop, always use the `curl | sh` installer above.

```
from truememory import Memory

m = Memory()
m.add("Prefers dark mode and TypeScript", user_id="alex")
m.add("Allergic to peanuts", user_id="alex")

results = m.search("What are Alex's preferences?", user_id="alex")
print(results[0]["content"])
# "Prefers dark mode and TypeScript"
```

The database is created automatically at `~/.truememory/memories.db`.

---

## 🏗️ Edge / Base / Pro

Same architecture, three tiers. All included in a single install — switch anytime.

|  | Edge | Base | Pro |
| --- | --- | --- | --- |
| **LoCoMo** (3-run mean) | 89.6% | 92.0% | 93.0% |
| **LongMemEval** (3-run mean) |  |  | 92.0% |
| **BEAM-1M** (3-run mean) |  |  | 76.6% (SOTA) |
| **BEAM-10M** (single run) |  |  | 65.0% |
| **Embedder** | Model2Vec potion-base-8M (8M params, 256d) | Qwen3-Embedding-0.6B (600M params, 256d) | Qwen3-Embedding-0.6B (600M params, 256d) |
| **Reranker** | MiniLM-L-6-v2 (22M) | gte-reranker-modernbert (149M) | gte-reranker-modernbert (149M) |
| **HyDE** | off | off | on (requires LLM API key) |
| **Runs on** | Any machine, CPU only | 4GB+ RAM, CPU or GPU | 4GB+ RAM + LLM API key |
| **Model size** | ~30MB | ~1.5GB | ~1.5GB |

**Edge** works everywhere. **Base** is the strongest fully-offline tier. **Pro** adds HyDE query expansion for the highest scores.

---

## 🧠 Architecture

TrueMemory uses a 6-layer retrieval pipeline inspired by how the brain encodes and recalls memory, plus an encoding gate that decides what gets stored.

### Ingest (what gets stored)

[![Ingest Pipeline](https://github.com/buildingjoshbetter/TrueMemory/raw/main/assets/charts/arch-ingest.png)](https://github.com/buildingjoshbetter/TrueMemory/blob/main/assets/charts/arch-ingest.png)

Every conversation flows through three stages before anything is stored:

| Stage | What it does |
| --- | --- |
| **LLM Extractor** | Pulls atomic facts from raw conversation text. Classifies each as personal, preference, decision, correction, temporal, technical, or relationship. |
| **Encoding Gate** | Three-signal filter: compression novelty + speech-act salience + embedding pair-diff prediction error. Rejects noise, keeps signal. |
| **Dedup** | ADD / UPDATE / SKIP against existing memories using vector similarity + word-overlap Jaccard matching. Prevents duplicates and catches rephrased versions of the same fact. |

### Encoding Gate + Storage

[![Encoding Gate](https://github.com/buildingjoshbetter/TrueMemory/raw/main/assets/charts/arch-gate.png)](https://github.com/buildingjoshbetter/TrueMemory/blob/main/assets/charts/arch-gate.png)

Three signals decide whether a fact gets stored or skipped:

| Signal | What it measures |
| --- | --- |
| **Compression Novelty** | gzip-based information gain. How much new information does this fact add compared to what's already stored? |
| **Speech-Act Salience** | Rule-based scorer for short messages, learned scorer for longer text. Filters out greetings, reactions, and filler. |
| **Embedding Pair-Diff** | Embedding divergence between the message and existing memories on the same topic. Detects when someone says something *different* about a known subject. |

The weighted sum of all three must exceed a threshold (default 0.30) to be stored. Everything below gets skipped. One SQLite file at `~/.truememory/memories.db`. Portable. Backupable. `cp` it anywhere.

### Retrieve (how it answers)

[![Retrieval Pipeline](https://github.com/buildingjoshbetter/TrueMemory/raw/main/assets/charts/arch-retrieve.png)](https://github.com/buildingjoshbetter/TrueMemory/blob/main/assets/charts/arch-retrieve.png)

When you ask a question, six layers work together:

| Layer | Name | What it does |
| --- | --- | --- |
| L0 | **Personality** | Char-n-gram style vectors + entity profiles. Answers "what kind of person is X?" questions that keyword search can't touch. |
| L2 | **Episodic** | FTS5 full-text keyword search with temporal filtering. Fast, broad recall. |
| L3 | **Semantic** | Dense vector search (Model2Vec or Qwen3 by tier) + RRF fusion + cross-encoder reranking. The heavy lifter. |
| L4 | **Salience** | Noise filtering + entity boosting. Learned 13-feature logistic regression scorer trained on retrieval-utility labels. |
| L5 | **Consolidation** | Structured fact summaries, contradiction resolution, and surprise-weighted reranking (alpha=0.2). |
| **+** | **Reranker** | Cross-encoder reranking (MiniLM or gte-modernbert by tier) for final precision. |

---

## 🔬 Benchmarks

[![LoCoMo Benchmark Leaderboard](https://github.com/buildingjoshbetter/TrueMemory/raw/main/assets/charts/leaderboard-bar.png)](https://github.com/buildingjoshbetter/TrueMemory/blob/main/assets/charts/leaderboard-bar.png)

Tested on [LoCoMo](https://github.com/snap-research/locomo) (1,540 questions, 10 conversations), [LongMemEval](https://github.com/xiaowu0162/LongMemEval) (500 questions, multi-session), [BEAM-1M](https://github.com/mohammadtavakoli78/BEAM) (700 questions, 35 conversations at 1M+ tokens), and BEAM-10M (200 questions, 10 conversations at 10M tokens). All systems share the same answer model (GPT-4.1-mini), judge (GPT-4o-mini, 3x majority vote), and scoring pipeline.

### LoCoMo (3-run validated means)

| Tier | Overall | Single-hop | Multi-hop | Temporal | Open-domain |
| --- | --- | --- | --- | --- | --- |
| Edge | 89.6% | 88.7% | 88.5% | 79.2% | 91.4% |
| Base | 92.0% | 91.5% | 91.3% | 82.3% | 93.9% |
| Pro | 93.0% | 92.6% | 90.0% | 86.5% | 95.4% |

### BEAM-1M (Pro tier, 3-run mean)

| Category | Score |
| --- | --- |
| Preference following | 97.1% |
| Contradiction resolution | 91.4% |
| Information extraction | 91.4% |
| Summarization | 89.5% |
| Instruction following | 84.8% |
| Abstention | 82.4% |
| Knowledge update | 77.6% |
| Multi-session reasoning | 67.1% |
| Temporal reasoning | 64.8% |
| Event ordering | 19.5% |
| **Overall** | **76.6%** |

### LongMemEval (Pro tier, 3-run mean)

| Variant | Accuracy | Correct/500 |
| --- | --- | --- |
| Oracle | 92.0% | 460 |
| Strict (\_s) | 87.8% | 439 |

### BEAM-10M (Pro tier, single run)

| Overall | 65.0% (130/200) |
| --- | --- |
| GPU | A100 80GB |
| Conversations | 10 at 10M tokens (~20K messages each) |

[![Accuracy vs Infrastructure Cost](https://github.com/buildingjoshbetter/TrueMemory/raw/main/assets/charts/accuracy-vs-cost.png)](https://github.com/buildingjoshbetter/TrueMemory/blob/main/assets/charts/accuracy-vs-cost.png)

### Reproduce any result yourself

Every benchmark script is self-contained and runs on [Modal](https://modal.com/).

- **[LoCoMo Scripts](https://github.com/buildingjoshbetter/TrueMemory/blob/main/benchmarks/locomo/scripts)** — 8 systems (TrueMemory, Mem0, Zep, Engram, etc.)
- **[LoCoMo Results](https://github.com/buildingjoshbetter/TrueMemory/blob/main/benchmarks/locomo/BENCHMARK_RESULTS.md)** — per-category breakdowns, latency, cost
- **[LoCoMo Eval Config](https://github.com/buildingjoshbetter/TrueMemory/blob/main/benchmarks/locomo/EVAL_CONFIG.md)** — exact models, prompts, parameters
- **[LongMemEval Scripts](https://github.com/buildingjoshbetter/TrueMemory/blob/main/benchmarks/longmemeval)** — oracle + strict variants
- **[LongMemEval Results](https://github.com/buildingjoshbetter/TrueMemory/blob/main/benchmarks/longmemeval/results)** — 6 TM Pro runs + 5 competitor results
- **[BEAM-1M Script](https://github.com/buildingjoshbetter/TrueMemory/blob/main/benchmarks/beam/bench_truememory_pro_beam1m.py)** — 35 conversations at 1M+ tokens
- **[BEAM-10M Script](https://github.com/buildingjoshbetter/TrueMemory/blob/main/benchmarks/beam/bench_truememory_pro_beam10m.py)** — 10 conversations at 10M tokens
- **[BEAM Results](https://github.com/buildingjoshbetter/TrueMemory/blob/main/benchmarks/beam)** — 3 runs (1M) + 1 run (10M)

### Evaluation config

All benchmarks use the same eval pipeline. Nothing is hidden.

| Parameter | LoCoMo | LongMemEval | BEAM-1M | BEAM-10M |
| --- | --- | --- | --- | --- |
| **Dataset** | 10 convs, 1,540 Qs | 500 Qs, multi-session | 35 convs at 1M tokens, 700 Qs | 10 convs at 10M tokens, 200 Qs |
| **Answer model** | `gpt-4.1-mini` | `gpt-4.1-mini` | `gpt-4.1-mini` | `gpt-4.1-mini` |
| **Answer temp** | 0 | 0 | 0 | 0 |
| **Judge model** | `gpt-4o-mini` | `gpt-4o-mini` | `gpt-4o-mini` | `gpt-4o-mini` |
| **Judge voting** | 3x majority | 3x majority | 3x majority | 3x majority |
| **Retrieval top-k** | 100 | 100 | 100 | 100 |
| **Compute** | Modal T4 | Modal A10G | Modal T4 | Modal A100 80GB |

Full details: [LoCoMo](https://github.com/buildingjoshbetter/TrueMemory/blob/main/benchmarks/locomo/EVAL_CONFIG.md) | [LongMemEval](https://github.com/buildingjoshbetter/TrueMemory/blob/main/benchmarks/longmemeval/README.md) | [BEAM](https://github.com/buildingjoshbetter/TrueMemory/blob/main/benchmarks/beam/README.md)

---

## 🐍 Python API

```
from truememory import Memory

m = Memory()

# Store
m.add("Prefers dark mode and TypeScript", user_id="alex")
m.add("Allergic to peanuts", user_id="alex")
m.add("Works at Anthropic as a senior engineer", user_id="alex")

# Search
results = m.search("What are Alex's preferences?", user_id="alex")

# Deep search (multi-round, higher accuracy, slower)
results = m.search_deep("What do we know about Alex's career?", user_id="alex")
```

| Method | Description |
| --- | --- |
| `m.add(content, user_id, metadata)` | Store a memory |
| `m.search(query, user_id, limit)` | Search memories (6-layer pipeline + reranker) |
| `m.search_deep(query, user_id, limit, llm_fn)` | Multi-round agentic search (slower, higher accuracy) |
| `m.search_vectors(query, limit)` | Pure vector cosine similarity search |
| `m.get(id)` | Get a specific memory by ID |
| `m.get_all(user_id, limit, offset)` | Get all memories with pagination |
| `m.update(id, content)` | Update a memory |
| `m.delete(id)` | Delete a memory |
| `m.delete_all(user_id)` | Delete all memories and associated data |
| `m.stats()` | Memory system statistics |

---

## 📖 Docs

| Document | Description |
| --- | --- |
| [Python API Reference](https://github.com/buildingjoshbetter/TrueMemory/blob/main/docs/python-api.md) | Full `Memory` class reference with examples |
| [MCP Tool Reference](https://github.com/buildingjoshbetter/TrueMemory/blob/main/docs/mcp-tools.md) | All 8 MCP tools with parameters and usage |
| [CLI Reference](https://github.com/buildingjoshbetter/TrueMemory/blob/main/docs/cli.md) | `truememory-mcp` and `truememory-ingest` commands |
| [Environment Variables](https://github.com/buildingjoshbetter/TrueMemory/blob/main/docs/env-vars.md) | All `TRUEMEMORY_*` configuration options |
| [Getting Started](https://github.com/buildingjoshbetter/TrueMemory/blob/main/docs/guides/getting-started.md) | Install to first memory, step by step |
| [Tier Selection](https://github.com/buildingjoshbetter/TrueMemory/blob/main/docs/guides/tier-selection.md) | Edge vs Base vs Pro comparison |
| [Debugging](https://github.com/buildingjoshbetter/TrueMemory/blob/main/docs/guides/debugging.md) | Logs, traces, common issues, file locations |

---

## ❓ FAQ

**My session doesn't seem to know anything about me. What's wrong?**

On your first session, TrueMemory runs setup. It won't recall memories until setup is complete. After that, every new session automatically searches your memory and injects up to 25 relevant facts as context. If memories still aren't loading, check that the MCP server is connected (`truememory_stats`) and that you have memories stored (`truememory_search` with a broad query).

**Where is my data stored? Is anything sent to the cloud?**

Everything lives locally in a single SQLite file at `~/.truememory/memories.db`. Edge and Base tiers make zero external network calls. Pro tier sends only your search query text to an LLM API for HyDE expansion. Your memories themselves are never transmitted. Back up anytime with `cp ~/.truememory/memories.db backup.db`.

**How do I switch tiers (Edge → Base → Pro)?**

Call `truememory_configure(tier="base")` (or `"pro"`) in any session, or run `truememory-ingest upgrade-tier base` from the terminal. All tier models are included in the standard install — switching just re-embeds your existing memories with the new model. Pro also needs an API key for HyDE query expansion.

**I switched tiers and search results seem off. How do I fix it?**

After a tier switch, TrueMemory re-embeds all memories with the new model. If this was interrupted, run `truememory_configure(tier="...")` again to retry. If results are still degraded, you can delete `~/.truememory/memories.db` and start fresh. Your conversations are still in your chat history and will be re-extracted.

**Do I need Python installed?**

No. The recommended install (`curl -LsSf .../install.sh | sh`) uses [uv](https://docs.astral.sh/uv/) to manage a sandboxed Python 3.12. Your system Python is never touched. To uninstall cleanly: `uv tool uninstall truememory`.

**Does TrueMemory collect telemetry?**

TrueMemory collects anonymous usage telemetry to help us understand how the product is used and improve it. We track which tools are called and how often, session counts, and basic platform info (OS, tier, version). We **never** track your memory content, search queries, file paths, or API keys. Telemetry is on by default. To opt out:

```
export TRUEMEMORY_TELEMETRY=off
```

---

Find me on X [@Building\_Josh](https://x.com/Building_Josh) · Follow us [@Sauron\_Labs](https://x.com/Sauron_Labs)

---

## 📝 Citation

```
@software{truememory,
  title = {TrueMemory: Neuroscience-Inspired Persistent Memory for AI Agents},
   = {Building\_Josh},
  organization = {Sauron},
  year = {2026},
  url = {https://github.com/buildingjoshbetter/TrueMemory},
  version = {0.6.0}
}
```

---

## ⚖️ License

Licensed under [AGPL-3.0](https://github.com/buildingjoshbetter/TrueMemory/blob/main/LICENSE). Free for personal and research use. Commercial use requires a separate license. Contact [josh@sauronlabs.ai](mailto:josh@sauronlabs.ai).

---

*TrueMemory, a **sauron company*** · [sauronlabs.ai](https://sauronlabs.ai/)