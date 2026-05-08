---
title: "cocoindex-io/cocoindex: Incremental engine for long horizon agents 🌟 Star if you like it!"
source: "https://github.com/cocoindex-io/cocoindex"
author:
published:
created: 2026-05-05
description: "Incremental engine for long horizon agents 🌟 Star if you like it! - cocoindex-io/cocoindex"
tags:
  - "clippings"
---
![Enterprise corpus — codebase, Slack, meeting notes, and documentation — flowing continuously through the CocoIndex incremental sync engine into a production AI agent with always-fresh context. Only the Δ (delta) is reprocessed on every change. Keywords: RAG pipeline, agent memory, enterprise retrieval, AI agent context, live indexing, retrieval-augmented generation, production LLM apps, streaming ETL, incremental ingestion.](../assets/external/camo.githubusercontent.com/10074a527fa81dcf.svg)

## Your agents deserve fresh context.

**Star us ❤️ →**[![Star CocoIndex on GitHub — open-source Python framework for RAG, vector search, and live agent context](../assets/external/camo.githubusercontent.com/09a3d3e1cd7e9125.svg)](https://github.com/cocoindex-io/cocoindex "Star CocoIndex on GitHub — open-source incremental indexing framework for AI agents")

·[

![cocoindex.io — the CocoIndex homepage: incremental data pipelines for AI agents](../assets/external/camo.githubusercontent.com/cd326a2de69148eb.svg)

](https://cocoindex.io/ "Visit cocoindex.io — the CocoIndex homepage")·[

![CocoIndex documentation — quickstart, connectors, ops, transformations, target stores, RAG and knowledge graph recipes](../assets/external/camo.githubusercontent.com/2db33181ec64bfb9.svg)

](https://cocoindex.io/docs "Read the CocoIndex documentation — guides, quickstart, connectors, transformations, and API reference")·[

![Join the CocoIndex Discord community — help, showcase, release notes, and live chat with maintainers](../assets/external/camo.githubusercontent.com/c4cae17c46e2aaf0.svg)

](https://discord.com/invite/zpA9S2DR7s "Join the CocoIndex Discord — community chat, showcase, release notes, help and support")

CocoIndex turns codebases, meeting notes, inboxes, Slack, PDFs, and videos into live, continuously fresh context for your AI agents and LLM apps to reason over effectively — with minimal incremental processing. Get your production AI agent ready in 10 minutes with reliable, continuously fresh data — no stale batches, no context gap

**Incremental** · only the delta · **Any scale** · parallel by default · **Declarative** · Python, 5 min

[![cocoindex-io/cocoindex | Trendshift](../assets/external/camo.githubusercontent.com/8e5c287ee73f79fb.svg)](https://trendshift.io/repositories/13939)

[Deutsch](https://readme-i18n.com/cocoindex-io/cocoindex?lang=de) | [English](https://readme-i18n.com/cocoindex-io/cocoindex?lang=en) | [Español](https://readme-i18n.com/cocoindex-io/cocoindex?lang=es) | [français](https://readme-i18n.com/cocoindex-io/cocoindex?lang=fr) | [日本語](https://readme-i18n.com/cocoindex-io/cocoindex?lang=ja) | [한국어](https://readme-i18n.com/cocoindex-io/cocoindex?lang=ko) | [Português](https://readme-i18n.com/cocoindex-io/cocoindex?lang=pt) | [Русский](https://readme-i18n.com/cocoindex-io/cocoindex?lang=ru) | [中文](https://readme-i18n.com/cocoindex-io/cocoindex?lang=zh)

## Built with CocoIndex ❤️[![CocoIndex-code — flagship MCP server for AI coding agents. AST-aware incremental semantic code index that keeps live call graphs, symbols, vectors, and chunks fresh on every commit. 70% fewer tokens per turn, 80-90% cache hits on re-index, sub-second freshness. Supports Python, TypeScript, Rust, and Go. Features: Δ-only incremental processing, semantic search by meaning (not grep), call graphs and blast-radius analysis, global repo view for duplicates and architecture. Build coding agents (generate, refactor) and code-review agents (catch, approve). One install — Claude Code, Cursor, and other MCP-aware agents see your whole repository instantly. Keywords: MCP server, coding agent, code intelligence, AST chunking, semantic code search, call graph, vector embedding, repository context, Claude Code, Cursor, incremental indexing, blast radius.](../assets/external/camo.githubusercontent.com/e6f3144b213de98a.svg)](https://cocoindex.io/cocoindex-code "CocoIndex-code — flagship MCP server for AI coding agents: AST-aware, incremental, semantic code index. Claude Code and Cursor see your whole repo instantly.")

[**See all 20+ examples · updated every week →**](https://github.com/cocoindex-io/cocoindex/blob/main/examples)

### Get started

```
pip install -U cocoindex
```

Declare *what* should be in your target — CocoIndex keeps it in sync forever, recomputing only the Δ.

```
import cocoindex as coco
from cocoindex.connectors import localfs, postgres
from cocoindex.ops.text import RecursiveSplitter

@coco.fn(memo=True)                          # ← cached by hash(input) + hash(code)
async def index_file(file, table):
    for chunk in RecursiveSplitter().split(await file.read_text()):
        table.declare_row(text=chunk.text, embedding=embed(chunk.text))

@coco.fn
async def main(src):
    table = await postgres.mount_table_target(PG, table_name="docs")
    table.declare_vector_index(column="embedding")
    await coco.mount_each(index_file, localfs.walk_dir(src).items(), table)

coco.App(coco.AppConfig(name="docs"), main, src="./docs").update_blocking()
```

Run once to backfill. Re-run anytime — only the changed files re-embed.

Building with an AI coding agent?  
Drop in our [**CocoIndex skill**](https://github.com/cocoindex-io/cocoindex/blob/main/skills/cocoindex) so your agent writes correct v1 code — concepts, APIs, patterns, all in one file.  
<sub>See <a href="https://cocoindex.io/docs/getting_started/ai_coding_agents/">Use with AI coding agents</a> for install steps.</sub>[![Full quickstart — open-book icon linking to the CocoIndex documentation quickstart: pip install, declare sources and targets, run the incremental engine](../assets/external/camo.githubusercontent.com/5cc8ca37e7f14ca8.svg)](https://cocoindex.io/docs/getting_started/quickstart "Full CocoIndex quickstart — install, declare sources and targets, run the incremental engine, set up vector search or knowledge graph in 5 minutes")

[

![Learn the concept — lightbulb icon linking to the CocoIndex core-concepts guide: sources, targets, flows, incremental engine, and data lineage](../assets/external/camo.githubusercontent.com/e9915841cb889379.svg)

](https://cocoindex.io/docs/programming_guide/core_concepts "Learn the CocoIndex core concepts — sources, targets, flows, incremental engine, lineage")[![Animated GitHub Star button for the cocoindex-io/cocoindex repository: a cursor clicks the star, it fills yellow, confetti bursts, the star count ticks up, and an 'Appreciate a star if you like it!' caption with a beating heart shows below the button](../assets/external/camo.githubusercontent.com/5c6a2c5cba8843fc.svg)](https://github.com/cocoindex-io/cocoindex "Star CocoIndex on GitHub — open-source Python framework for live agent context")

## React — for data engineering

![React — for data engineering. The CocoIndex mental model: Target = F(Source). A persistent-state-driven dataflow where you declare the desired target state and the engine keeps it in sync with the latest source data and code, forever, at low latency and low cost. Source files (.py, .md, .pdf, .ts) flow through your Python transformation F into a live target dots-matrix index; only the Δ is reprocessed on every change, and every target dot traces back to its exact source byte. Four core properties: Python not a DAG (sky), declare target state (yellow bullseye), lineage end-to-end (coral connected dots), and incremental at any scale (mint Δ+1). Your code is as simple as the one-off version — the engine does the rest. Keywords: React for data engineering, declarative ETL, persistent state, data lineage, dataflow, Δ only, incremental indexing, CocoIndex.](../assets/external/camo.githubusercontent.com/8afa7ee7e9622762.svg)

![What happens when either side changes — CocoIndex tracks per-row provenance so the Δ propagates at minimum cost. Two scenarios shown in one illustration: (top) Source change — one file (b.md) is edited and only one target dot re-syncs (coral pulse). (bottom) Code change — the transformation function F is rewritten from v1 to v2 and only the dots whose outputs depend on the changed code re-run (amber/yellow pulses). Source on the left, F in the center (Python code block), target dots-matrix on the right. Keywords: incremental indexing, change data capture, delta processing, fine-grained invalidation, code-aware caching, hash-of-code invalidation, memoization, reproducible pipelines, incremental recomputation.](../assets/external/camo.githubusercontent.com/d6d03480d4a5c682.svg)

[**See the React ↔ CocoIndex mental model →**](https://cocoindex.io/react-cocoindex)

## Incremental engine for long-horizon agents

Data transformation for any engineer, designed for AI workloads —  
with a smart incremental engine for *always-fresh, explainable data.*[![Learn the concept — purple button with a lightbulb icon linking to the CocoIndex core-concepts guide: sources, targets, flows, incremental engine, and data lineage](../assets/external/camo.githubusercontent.com/e9915841cb889379.svg)](https://cocoindex.io/docs/programming_guide/core_concepts "Learn the CocoIndex core concepts — sources, targets, flows, incremental engine, lineage")

![CocoIndex's Python-native transformation flows connect 8 source categories (Codebases, Meeting Notes, Web · APIs, File System · Blob Stores, Databases, Message Queues, Images · Video, Voice · Transcripts) through the incremental engine out to 6 target stores (Relational DB, Data Warehouse, Vector DB, Graph DB, Message Queue, Feature Store). A flow.py code block (@coco.fn · def f(src): · chunks = split(src) · target.row(embed(chunks))) shows the shared pipeline; only the Δ is reprocessed — unchanged src hits the cache, changed src re-runs split() and Δ → re-embed. The persistent data-pipeline control plane runs eight always-on subsystems: live caching, pipeline catalog, version tracking, continuously learning, lineage, task scheduling, metrics collection, and failure management. Keywords: data pipeline, ETL, source connectors, vector database, graph database, incremental engine, streaming ingestion, caching, lineage, versioning, scheduling, metrics, retries.](../assets/external/camo.githubusercontent.com/c5e82f7b930b39a1.svg)

## Why incremental?

Your agents are only as good as the data they see.  
Batch pipelines drift stale. CocoIndex stays live — and only runs the Δ.

![Why incremental? — one illustration combining the four core benefits of CocoIndex's incremental engine. Sub-second fresh (mint): a stopwatch ticking under a second, source changes propagate to the target in under a second so agents see the world as it is, not as it was yesterday. 10× cheaper at scale (yellow): a 10,000-row corpus block where only a thin Δ 0.1% column re-runs and 99.9% stays cached — you skip the other 99.9% of your corpus and pay a fraction of the compute, embedding, and LLM bill. Explainable by default (coral): a lineage thread links a source byte (handbook.md L42) to a target vector — every vector, row, or graph node in the target traces back to its exact source byte for debuggable, auditable, regulator-friendly AI pipelines. Production-grade (purple): a shield stamped with the Rust crab surrounded by retry loops, back-off dots, a DLQ tray, and a no-data-loss check — Rust core with retries, exponential back-off, dead-letter queues, and no-data-loss guarantees, production-ready for long-horizon AI agents. Keywords: incremental indexing, Δ-only reprocessing, sub-second freshness, low-latency RAG, cost-efficient embeddings, data lineage, retrieval-augmented generation, Rust core, retries, back-off, dead letters, no data loss, long-horizon agents.](../assets/external/camo.githubusercontent.com/427d050af52d9b30.svg)

## What can you build?

[**See all 20+ examples · updated every week →**](https://github.com/cocoindex-io/cocoindex/blob/main/examples "Browse all 20+ CocoIndex examples on GitHub — code, PDF, HN, knowledge graph, podcast, CSV-to-Kafka, image, and more")

**Working starters from [the examples tree](https://github.com/cocoindex-io/cocoindex/blob/main/examples) — clone, plug your source, ship.**

[![Real-time code index — walk a git repo, AST-chunk source files, embed with sentence-transformers, upsert to pgvector / LanceDB, incremental on every commit. Keywords: code search, code embedding, semantic code retrieval, Python.](../assets/external/camo.githubusercontent.com/0f05d8b483151df0.svg)](https://github.com/cocoindex-io/cocoindex/blob/main/examples/code_embedding "Real-time code index — walk a git repo, chunk source files with an AST-aware splitter, embed with sentence-transformers, and upsert to pgvector / LanceDB. Fully incremental: only files touched by the latest commit re-embed. Good for coding agents, code review, semantic find-by-meaning.")

[![PDF → RAG index — ingest PDFs from local, S3, or GDrive, extract + chunk text, embed chunks, upsert to pgvector / LanceDB. Classic retrieval-augmented-generation stack, incremental. Keywords: RAG, document Q&A, PDF search, vector database.](../assets/external/camo.githubusercontent.com/aa638f00a9fceea2.svg)](https://github.com/cocoindex-io/cocoindex/blob/main/examples/pdf_embedding "PDF → RAG index — ingest PDFs from local / S3 / Google Drive, extract text, chunk with a recursive splitter, embed each chunk, and upsert into pgvector / LanceDB with a vector index. Classic RAG stack, incremental — only edited PDFs re-embed.")

[![HN trending topics — pull Hacker News threads via Algolia, recursively parse comments, LLM-extract topics with Gemini 2.5 Flash, rank by weighted hit count (thread=5, comment=1), store in Postgres. Incremental. Keywords: Hacker News, trending topics, LLM extraction, Gemini, Postgres, news intelligence, topic ranking.](../assets/external/camo.githubusercontent.com/a80adf37e8b25fb1.svg)](https://github.com/cocoindex-io/cocoindex/blob/main/examples/hn_trending_topics "HN trending topics — fetch Hacker News threads via the Algolia API, recursively pull nested comments, LLM-extract typed topic lists per message with Gemini 2.5 Flash, and rank topics by weighted mention count (thread = 5 points, comment = 1 point).")

[![Conversation → knowledge graph — LLM extracts people, topics, decisions, action items from transcripts and upserts into Neo4j / Kuzu. Live graph, incremental. Keywords: knowledge graph, entity extraction, meeting intelligence, agent memory.](../assets/external/camo.githubusercontent.com/3575b261c1ee89d9.svg)](https://github.com/cocoindex-io/cocoindex/blob/main/examples/conversation_to_knowledge "Conversation → knowledge graph — pull people, topics, decisions, and action items out of meeting transcripts, Slack, podcasts, or support calls with an LLM extractor, and upsert into Neo4j or Kuzu. Incremental: only changed turns re-extract.")

[![Multi-repo summarization — walk N git repos, extract structure, LLM-summarize per-repo + a rolled-up org summary, refresh on every push. Keywords: internal platform, developer experience, monorepo, SDK docs.](../assets/external/camo.githubusercontent.com/296eaff2f29d5e12.svg)](https://github.com/cocoindex-io/cocoindex/blob/main/examples/multi_codebase_summarization "Multi-repo summarization — walk N git repositories, extract READMEs / public APIs / modules, LLM-summarize each one, and roll up into a single top-level summary. Incremental: only repos with new commits re-run.")

[![Structured extraction — BAML / DSPy typed schema extraction from forms, PDFs, intakes, invoices into Postgres / warehouse. Incremental. Keywords: ETL, LLM extraction, schema-first, patient intake, invoice processing, KYC, contracts.](../assets/external/camo.githubusercontent.com/67035dd97da1103f.svg)](https://github.com/cocoindex-io/cocoindex/blob/main/examples/patient_intake_extraction_baml "Structured extraction — read messy forms, PDFs, invoices, or free-text and extract typed, schema-validated fields with BAML or DSPy, then write rows into Postgres or a warehouse. Incremental: only changed documents re-extract.")

[![Podcast → knowledge graph — transcribe YouTube / Spotify audio with speaker diarization, LLM-extract speakers and statements, resolve entities across episodes, store in SurrealDB / Neo4j. Keywords: podcast, diarization, YouTube, Whisper, SurrealDB, knowledge graph, entity resolution.](../assets/external/camo.githubusercontent.com/72208cc41ef72776.svg)](https://github.com/cocoindex-io/cocoindex/blob/main/examples/conversation_to_knowledge "Podcast → knowledge graph — download YouTube podcast audio, transcribe with speaker diarization (Whisper / AssemblyAI), LLM-extract structured statements and entities per speaker, resolve duplicates across episodes with embeddings, and store the whole graph (speakers, statements, topics) in SurrealDB or Neo4j. Incremental.")

[![CSV → Kafka live — watch a folder of CSV files, publish each row as a JSON message to a Kafka topic via CocoIndex's Kafka target connector. Incremental, sub-second, no producer loop. Keywords: Kafka, CDC, streaming, StreamNative, Confluent, CSV ingestion, event streaming.](../assets/external/camo.githubusercontent.com/4b9685b0d81d4085.svg)](https://github.com/cocoindex-io/cocoindex/blob/main/examples/csv_to_kafka "CSV → Kafka live — watch a folder of CSV files (local or S3) and publish each row as a JSON message keyed by its primary key to a Kafka topic on StreamNative / Confluent / self-hosted. Sub-second incremental — only changed rows publish.")

![Share what you build — a banner with a trail of tiny hearts rising from the bottom behind the text, inviting the CocoIndex community to share projects built with the framework](../assets/external/camo.githubusercontent.com/2933ec84ecb78ac4.svg)

Building something with CocoIndex? **We want to see it.**  
Tag [@cocoindex\_io](https://x.com/cocoindex_io "Tag @cocoindex_io on X to showcase your CocoIndex project") on X or drop a link in [#showcase](https://discord.com/invite/zpA9S2DR7s "Share your project in the CocoIndex Discord #showcase channel") on Discord. We'll boost it. 🥥

## Community

| [  ![Join the CocoIndex Discord community — live chat with maintainers and users, showcase your projects, get help building RAG pipelines and knowledge graphs](../assets/external/camo.githubusercontent.com/6539eba3a15eca07.svg)  ](https://discord.com/invite/zpA9S2DR7s "Join the CocoIndex Discord — community chat, showcase, help, release notes") | [  ![Subscribe to the CocoIndex YouTube channel — video tutorials, live demos, architecture deep dives, and AI agent recipes](../assets/external/camo.githubusercontent.com/26deef768a497089.svg)  ](https://www.youtube.com/@cocoindex-io "Subscribe to the CocoIndex YouTube channel — live demos, tutorials, and deep dives") | [  ![Read the CocoIndex blog — engineering deep dives, release notes, RAG and knowledge graph tutorials, and case studies](../assets/external/camo.githubusercontent.com/c1cd7c20b9c181cf.svg)  ](https://cocoindex.io/blogs/ "Read the CocoIndex blog — engineering posts, release notes, and tutorials") | [  ![Follow @cocoindex_io on X (formerly Twitter) for release notes, demos, launches, and AI data pipeline updates](../assets/external/camo.githubusercontent.com/a538d51c3667f724.svg)  ](https://x.com/cocoindex_io "Follow @cocoindex_io on X (Twitter) for release notes, demos, and updates") |
| --- | --- | --- | --- |

[![We love Contributors — section title banner with a pulsing coral heart badge and cream twinkle sparkles. Every typo fix, new connector, and doc tweak makes CocoIndex better. Keywords: open-source contribution, pull request, typo fix, new connector, good first issue, Hacktoberfest, community, coconut heart.](../assets/external/camo.githubusercontent.com/4beea02169ca492d.svg)](https://camo.githubusercontent.com/f30dbe1e1eda31c2f8c3f495bdedf7ab6dc291cfe67e760aa8364a67ca270174/68747470733a2f2f636f636f696e6465782e696f2f626c6f62732f6769746875622f686f6d65706167652f77652d6c6f76652d636f6e7472696275746f72732e737667)

**We are *so* excited to meet you.**  
Every typo fix, new connector, doc tweak, or full-on rewrite makes CocoIndex better.  
Come hang out — big PRs and small ones, both welcome.

📝 [**Read the contributing guide**](https://cocoindex.io/docs/contributing/guide) · 🐛 [**good first issues**](https://github.com/cocoindex-io/cocoindex/labels/good%20first%20issue) · 💬 [**Say hi on Discord**](https://discord.com/invite/zpA9S2DR7s)

## CocoIndex Enterprise

![CocoIndex Enterprise — built for enterprise scale. Four headline stats for PB-scale incremental indexing: PB corpus scale incrementally indexed (coral), 10× fewer LLM embedding calls vs. full recompute (yellow), 100% lineage coverage with every byte traceable (mint), Δ only the delta always (sky). Below, a wide 50×8 corpus matrix of 400 dim tiles represents a petabyte-scale store where a single coral Δ slice of 8 tiles re-runs while the other 99.9% stays cached. Keywords: enterprise RAG, petabyte-scale indexing, incremental compute, delta-only, lineage, parallel chunking, zero-copy, failure isolation.](../assets/external/camo.githubusercontent.com/9814e542a48e8333.svg)

### Large corpus — built for enterprise scale.

Incremental compute is the only way to keep large corpora fresh without re-embedding them every cycle.  
CocoIndex scales from a single repo to petabyte-scale stores — parallel by default, delta-only by design.

### Process once. Reconcile forever.

When a source changes, CocoIndex identifies the affected records, propagates the change  
across joins and lookups, updates the target, and retires stale rows —  
without touching anything that didn't change.

### Built on a Rust engine.

The core is Rust — production-grade from day zero.  
Parallel chunking, zero-copy transforms where possible, and failure isolation  
so one bad record doesn't stall the flow.

[![Explore CocoIndex Enterprise — bright blue pill button linking to cocoindex.io/enterprise, the PB-scale incremental data pipeline for AI agents](../assets/external/camo.githubusercontent.com/9b23c7ae61af1344.svg)](https://cocoindex.io/enterprise/ "Explore CocoIndex Enterprise — PB-scale incremental data pipelines for AI agents")

<sub>Apache 2.0 · © CocoIndex contributors 🥥</sub>