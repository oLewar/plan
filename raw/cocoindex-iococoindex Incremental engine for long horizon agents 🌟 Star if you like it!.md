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
![Enterprise corpus — codebase, Slack, meeting notes, and documentation — flowing continuously through the CocoIndex incremental sync engine into a production AI agent with always-fresh context. Only the Δ (delta) is reprocessed on every change. Keywords: RAG pipeline, agent memory, enterprise retrieval, AI agent context, live indexing, retrieval-augmented generation, production LLM apps, streaming ETL, incremental ingestion.](https://camo.githubusercontent.com/f59f9e3629159b9d4c744a785ef4f60fdd782e9a76babcf359dd4636551423c0/68747470733a2f2f636f636f696e6465782e696f2f626c6f62732f6769746875622f686f6d65706167652f656e74657270726973652d6865726f2d6c696768742e737667)

## Your agents deserve fresh context.

**Star us ❤️ →**[![Star CocoIndex on GitHub — open-source Python framework for RAG, vector search, and live agent context](https://camo.githubusercontent.com/18e8c31d362be84126e763c979f971a79acee5e597c10bc2dcabe59470a903b6/68747470733a2f2f636f636f696e6465782e696f2f626c6f62732f6769746875622f686f6d65706167652f737461722d62746e2d736d616c6c2d6c696768742e737667)](https://github.com/cocoindex-io/cocoindex "Star CocoIndex on GitHub — open-source incremental indexing framework for AI agents")

·[

![cocoindex.io — the CocoIndex homepage: incremental data pipelines for AI agents](https://camo.githubusercontent.com/52174ddba60973211c9a0ad45545f32dfa56cb5beec4ba643a206d56bb7c77b9/68747470733a2f2f636f636f696e6465782e696f2f626c6f62732f6769746875622f686f6d65706167652f636f636f2d696e6c696e652d6c696768742e737667)

](https://cocoindex.io/ "Visit cocoindex.io — the CocoIndex homepage")·[

![CocoIndex documentation — quickstart, connectors, ops, transformations, target stores, RAG and knowledge graph recipes](https://camo.githubusercontent.com/e9de019e89b10a8e2f3d59b72bef6b2f56ac3fec19557a072fd7a458499b489d/68747470733a2f2f636f636f696e6465782e696f2f626c6f62732f6769746875622f686f6d65706167652f646f63732d696e6c696e652d6c696768742e737667)

](https://cocoindex.io/docs "Read the CocoIndex documentation — guides, quickstart, connectors, transformations, and API reference")·[

![Join the CocoIndex Discord community — help, showcase, release notes, and live chat with maintainers](https://camo.githubusercontent.com/dc8e129b32b844e4ac2ed0dbe5d5627fe2fcaa7918355ae39037eadaea16d383/68747470733a2f2f636f636f696e6465782e696f2f626c6f62732f6769746875622f686f6d65706167652f646973636f72642d696e6c696e652d6c696768742e737667)

](https://discord.com/invite/zpA9S2DR7s "Join the CocoIndex Discord — community chat, showcase, release notes, help and support")

CocoIndex turns codebases, meeting notes, inboxes, Slack, PDFs, and videos into live, continuously fresh context for your AI agents and LLM apps to reason over effectively — with minimal incremental processing. Get your production AI agent ready in 10 minutes with reliable, continuously fresh data — no stale batches, no context gap

**Incremental** · only the delta · **Any scale** · parallel by default · **Declarative** · Python, 5 min

[![cocoindex-io/cocoindex | Trendshift](https://camo.githubusercontent.com/f52d8dec649d65af2212e88080ff34b06c04274a34db2f4a8a4c1dbe822206d5/68747470733a2f2f7472656e6473686966742e696f2f6170692f62616467652f7265706f7369746f726965732f3133393339)](https://trendshift.io/repositories/13939)

[Deutsch](https://readme-i18n.com/cocoindex-io/cocoindex?lang=de) | [English](https://readme-i18n.com/cocoindex-io/cocoindex?lang=en) | [Español](https://readme-i18n.com/cocoindex-io/cocoindex?lang=es) | [français](https://readme-i18n.com/cocoindex-io/cocoindex?lang=fr) | [日本語](https://readme-i18n.com/cocoindex-io/cocoindex?lang=ja) | [한국어](https://readme-i18n.com/cocoindex-io/cocoindex?lang=ko) | [Português](https://readme-i18n.com/cocoindex-io/cocoindex?lang=pt) | [Русский](https://readme-i18n.com/cocoindex-io/cocoindex?lang=ru) | [中文](https://readme-i18n.com/cocoindex-io/cocoindex?lang=zh)

## Built with CocoIndex ❤️[![CocoIndex-code — flagship MCP server for AI coding agents. AST-aware incremental semantic code index that keeps live call graphs, symbols, vectors, and chunks fresh on every commit. 70% fewer tokens per turn, 80-90% cache hits on re-index, sub-second freshness. Supports Python, TypeScript, Rust, and Go. Features: Δ-only incremental processing, semantic search by meaning (not grep), call graphs and blast-radius analysis, global repo view for duplicates and architecture. Build coding agents (generate, refactor) and code-review agents (catch, approve). One install — Claude Code, Cursor, and other MCP-aware agents see your whole repository instantly. Keywords: MCP server, coding agent, code intelligence, AST chunking, semantic code search, call graph, vector embedding, repository context, Claude Code, Cursor, incremental indexing, blast radius.](https://camo.githubusercontent.com/c6f607a66aef2155240db73e037a15a775a6fed5248ea250a6849e9360fcba18/68747470733a2f2f636f636f696e6465782e696f2f626c6f62732f6769746875622f686f6d65706167652f636f636f696e6465782d636f64652d6865726f2d6c696768742e737667)](https://cocoindex.io/cocoindex-code "CocoIndex-code — flagship MCP server for AI coding agents: AST-aware, incremental, semantic code index. Claude Code and Cursor see your whole repo instantly.")

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
<sub>See <a href="https://cocoindex.io/docs/getting_started/ai_coding_agents/">Use with AI coding agents</a> for install steps.</sub>[![Full quickstart — open-book icon linking to the CocoIndex documentation quickstart: pip install, declare sources and targets, run the incremental engine](https://camo.githubusercontent.com/bea2dce577989fc43c0059d56b61928859e0c3c14e6b045c4e2aee3bce9a050e/68747470733a2f2f636f636f696e6465782e696f2f626c6f62732f6769746875622f686f6d65706167652f717569636b73746172742d62746e2d6c696768742e737667)](https://cocoindex.io/docs/getting_started/quickstart "Full CocoIndex quickstart — install, declare sources and targets, run the incremental engine, set up vector search or knowledge graph in 5 minutes")

[

![Learn the concept — lightbulb icon linking to the CocoIndex core-concepts guide: sources, targets, flows, incremental engine, and data lineage](https://camo.githubusercontent.com/2bb3ac1f6a44871fa1f0255abffb69a37b5d2f0f1a6396573fd8193e2539874f/68747470733a2f2f636f636f696e6465782e696f2f626c6f62732f6769746875622f686f6d65706167652f6c6561726e2d636f6e636570742d62746e2d6c696768742e737667)

](https://cocoindex.io/docs/programming_guide/core_concepts "Learn the CocoIndex core concepts — sources, targets, flows, incremental engine, lineage")[![Animated GitHub Star button for the cocoindex-io/cocoindex repository: a cursor clicks the star, it fills yellow, confetti bursts, the star count ticks up, and an 'Appreciate a star if you like it!' caption with a beating heart shows below the button](https://camo.githubusercontent.com/6da6a051c3fd496c420dfefa843dbe3e5db8e459cdec182fae498de840e7e008/68747470733a2f2f636f636f696e6465782e696f2f626c6f62732f6769746875622f686f6d65706167652f636f6d6d2d6769746875622d6c696768742e737667)](https://github.com/cocoindex-io/cocoindex "Star CocoIndex on GitHub — open-source Python framework for live agent context")

## React — for data engineering

![React — for data engineering. The CocoIndex mental model: Target = F(Source). A persistent-state-driven dataflow where you declare the desired target state and the engine keeps it in sync with the latest source data and code, forever, at low latency and low cost. Source files (.py, .md, .pdf, .ts) flow through your Python transformation F into a live target dots-matrix index; only the Δ is reprocessed on every change, and every target dot traces back to its exact source byte. Four core properties: Python not a DAG (sky), declare target state (yellow bullseye), lineage end-to-end (coral connected dots), and incremental at any scale (mint Δ+1). Your code is as simple as the one-off version — the engine does the rest. Keywords: React for data engineering, declarative ETL, persistent state, data lineage, dataflow, Δ only, incremental indexing, CocoIndex.](https://camo.githubusercontent.com/b815bf55dd4b4c4249728e256c71a65e844c81e915cc0e2131085bf6d15f3b42/68747470733a2f2f636f636f696e6465782e696f2f626c6f62732f6769746875622f686f6d65706167652f72656163743464652d6865726f2d6c696768742e737667)

![What happens when either side changes — CocoIndex tracks per-row provenance so the Δ propagates at minimum cost. Two scenarios shown in one illustration: (top) Source change — one file (b.md) is edited and only one target dot re-syncs (coral pulse). (bottom) Code change — the transformation function F is rewritten from v1 to v2 and only the dots whose outputs depend on the changed code re-run (amber/yellow pulses). Source on the left, F in the center (Python code block), target dots-matrix on the right. Keywords: incremental indexing, change data capture, delta processing, fine-grained invalidation, code-aware caching, hash-of-code invalidation, memoization, reproducible pipelines, incremental recomputation.](https://camo.githubusercontent.com/132c32fa8505f92ff43ff145ddeab9be87eb2775d0bc783e0416533013952fec/68747470733a2f2f636f636f696e6465782e696f2f626c6f62732f6769746875622f686f6d65706167652f6569746865722d736964652d6368616e67652d6c696768742e737667)

[**See the React ↔ CocoIndex mental model →**](https://cocoindex.io/react-cocoindex)

## Incremental engine for long-horizon agents

Data transformation for any engineer, designed for AI workloads —  
with a smart incremental engine for *always-fresh, explainable data.*[![Learn the concept — purple button with a lightbulb icon linking to the CocoIndex core-concepts guide: sources, targets, flows, incremental engine, and data lineage](https://camo.githubusercontent.com/2bb3ac1f6a44871fa1f0255abffb69a37b5d2f0f1a6396573fd8193e2539874f/68747470733a2f2f636f636f696e6465782e696f2f626c6f62732f6769746875622f686f6d65706167652f6c6561726e2d636f6e636570742d62746e2d6c696768742e737667)](https://cocoindex.io/docs/programming_guide/core_concepts "Learn the CocoIndex core concepts — sources, targets, flows, incremental engine, lineage")

![CocoIndex's Python-native transformation flows connect 8 source categories (Codebases, Meeting Notes, Web · APIs, File System · Blob Stores, Databases, Message Queues, Images · Video, Voice · Transcripts) through the incremental engine out to 6 target stores (Relational DB, Data Warehouse, Vector DB, Graph DB, Message Queue, Feature Store). A flow.py code block (@coco.fn · def f(src): · chunks = split(src) · target.row(embed(chunks))) shows the shared pipeline; only the Δ is reprocessed — unchanged src hits the cache, changed src re-runs split() and Δ → re-embed. The persistent data-pipeline control plane runs eight always-on subsystems: live caching, pipeline catalog, version tracking, continuously learning, lineage, task scheduling, metrics collection, and failure management. Keywords: data pipeline, ETL, source connectors, vector database, graph database, incremental engine, streaming ingestion, caching, lineage, versioning, scheduling, metrics, retries.](https://camo.githubusercontent.com/6285cf1b2b45e6edbc8e908d536630820041338d80ee26e01c3ef1531354833b/68747470733a2f2f636f636f696e6465782e696f2f626c6f62732f6769746875622f686f6d65706167652f696e6372656d656e74616c2d656e67696e652d6c696768742e737667)

## Why incremental?

Your agents are only as good as the data they see.  
Batch pipelines drift stale. CocoIndex stays live — and only runs the Δ.

![Why incremental? — one illustration combining the four core benefits of CocoIndex's incremental engine. Sub-second fresh (mint): a stopwatch ticking under a second, source changes propagate to the target in under a second so agents see the world as it is, not as it was yesterday. 10× cheaper at scale (yellow): a 10,000-row corpus block where only a thin Δ 0.1% column re-runs and 99.9% stays cached — you skip the other 99.9% of your corpus and pay a fraction of the compute, embedding, and LLM bill. Explainable by default (coral): a lineage thread links a source byte (handbook.md L42) to a target vector — every vector, row, or graph node in the target traces back to its exact source byte for debuggable, auditable, regulator-friendly AI pipelines. Production-grade (purple): a shield stamped with the Rust crab surrounded by retry loops, back-off dots, a DLQ tray, and a no-data-loss check — Rust core with retries, exponential back-off, dead-letter queues, and no-data-loss guarantees, production-ready for long-horizon AI agents. Keywords: incremental indexing, Δ-only reprocessing, sub-second freshness, low-latency RAG, cost-efficient embeddings, data lineage, retrieval-augmented generation, Rust core, retries, back-off, dead letters, no data loss, long-horizon agents.](https://camo.githubusercontent.com/85ce4f41e4efd56ce68f5e57b2d31fab1f50ff899ec4b24d49dc9af5e7a760f7/68747470733a2f2f636f636f696e6465782e696f2f626c6f62732f6769746875622f686f6d65706167652f7768792d696e6372656d656e74616c2d6461726b2e737667)

## What can you build?

[**See all 20+ examples · updated every week →**](https://github.com/cocoindex-io/cocoindex/blob/main/examples "Browse all 20+ CocoIndex examples on GitHub — code, PDF, HN, knowledge graph, podcast, CSV-to-Kafka, image, and more")

**Working starters from [the examples tree](https://github.com/cocoindex-io/cocoindex/blob/main/examples) — clone, plug your source, ship.**

[![Real-time code index — walk a git repo, AST-chunk source files, embed with sentence-transformers, upsert to pgvector / LanceDB, incremental on every commit. Keywords: code search, code embedding, semantic code retrieval, Python.](https://camo.githubusercontent.com/d636fa1a100536ca72333b9d5010b15b2d65cac1d53905eafbe905f31b7233ea/68747470733a2f2f636f636f696e6465782e696f2f626c6f62732f6769746875622f686f6d65706167652f6578616d706c652d636f64652e737667)](https://github.com/cocoindex-io/cocoindex/blob/main/examples/code_embedding "Real-time code index — walk a git repo, chunk source files with an AST-aware splitter, embed with sentence-transformers, and upsert to pgvector / LanceDB. Fully incremental: only files touched by the latest commit re-embed. Good for coding agents, code review, semantic find-by-meaning.")

[![PDF → RAG index — ingest PDFs from local, S3, or GDrive, extract + chunk text, embed chunks, upsert to pgvector / LanceDB. Classic retrieval-augmented-generation stack, incremental. Keywords: RAG, document Q&A, PDF search, vector database.](https://camo.githubusercontent.com/76e4308dd90e3e42e84ecf0c336227fc6057180168d0d5763c6f5654ba08cf3a/68747470733a2f2f636f636f696e6465782e696f2f626c6f62732f6769746875622f686f6d65706167652f6578616d706c652d7064662e737667)](https://github.com/cocoindex-io/cocoindex/blob/main/examples/pdf_embedding "PDF → RAG index — ingest PDFs from local / S3 / Google Drive, extract text, chunk with a recursive splitter, embed each chunk, and upsert into pgvector / LanceDB with a vector index. Classic RAG stack, incremental — only edited PDFs re-embed.")

[![HN trending topics — pull Hacker News threads via Algolia, recursively parse comments, LLM-extract topics with Gemini 2.5 Flash, rank by weighted hit count (thread=5, comment=1), store in Postgres. Incremental. Keywords: Hacker News, trending topics, LLM extraction, Gemini, Postgres, news intelligence, topic ranking.](https://camo.githubusercontent.com/873f3df9c143eeb3fa30f74fd4ec09ac0271aeca8b6757439142e2f27e81a084/68747470733a2f2f636f636f696e6465782e696f2f626c6f62732f6769746875622f686f6d65706167652f6578616d706c652d686e2d7472656e64696e672e737667)](https://github.com/cocoindex-io/cocoindex/blob/main/examples/hn_trending_topics "HN trending topics — fetch Hacker News threads via the Algolia API, recursively pull nested comments, LLM-extract typed topic lists per message with Gemini 2.5 Flash, and rank topics by weighted mention count (thread = 5 points, comment = 1 point).")

[![Conversation → knowledge graph — LLM extracts people, topics, decisions, action items from transcripts and upserts into Neo4j / Kuzu. Live graph, incremental. Keywords: knowledge graph, entity extraction, meeting intelligence, agent memory.](https://camo.githubusercontent.com/75387c4e8717fa9951c9b0a2daa89e954eb6c4c52d68490621a98abf51ee5607/68747470733a2f2f636f636f696e6465782e696f2f626c6f62732f6769746875622f686f6d65706167652f6578616d706c652d6b672e737667)](https://github.com/cocoindex-io/cocoindex/blob/main/examples/conversation_to_knowledge "Conversation → knowledge graph — pull people, topics, decisions, and action items out of meeting transcripts, Slack, podcasts, or support calls with an LLM extractor, and upsert into Neo4j or Kuzu. Incremental: only changed turns re-extract.")

[![Multi-repo summarization — walk N git repos, extract structure, LLM-summarize per-repo + a rolled-up org summary, refresh on every push. Keywords: internal platform, developer experience, monorepo, SDK docs.](https://camo.githubusercontent.com/4cf25d15dba6fdaedff31f52254268705dc6ccdd43d0d474d1b7c5af2b3177e4/68747470733a2f2f636f636f696e6465782e696f2f626c6f62732f6769746875622f686f6d65706167652f6578616d706c652d6d756c7469636f64652e737667)](https://github.com/cocoindex-io/cocoindex/blob/main/examples/multi_codebase_summarization "Multi-repo summarization — walk N git repositories, extract READMEs / public APIs / modules, LLM-summarize each one, and roll up into a single top-level summary. Incremental: only repos with new commits re-run.")

[![Structured extraction — BAML / DSPy typed schema extraction from forms, PDFs, intakes, invoices into Postgres / warehouse. Incremental. Keywords: ETL, LLM extraction, schema-first, patient intake, invoice processing, KYC, contracts.](https://camo.githubusercontent.com/b1d690a48151558218995c53cea289c3057696853c58d81817c1cab1b5134708/68747470733a2f2f636f636f696e6465782e696f2f626c6f62732f6769746875622f686f6d65706167652f6578616d706c652d696e74616b652e737667)](https://github.com/cocoindex-io/cocoindex/blob/main/examples/patient_intake_extraction_baml "Structured extraction — read messy forms, PDFs, invoices, or free-text and extract typed, schema-validated fields with BAML or DSPy, then write rows into Postgres or a warehouse. Incremental: only changed documents re-extract.")

[![Podcast → knowledge graph — transcribe YouTube / Spotify audio with speaker diarization, LLM-extract speakers and statements, resolve entities across episodes, store in SurrealDB / Neo4j. Keywords: podcast, diarization, YouTube, Whisper, SurrealDB, knowledge graph, entity resolution.](https://camo.githubusercontent.com/3d06ee4922c3df55c3441f298290d019b4255f681b71349bac6a6ae30f705ddb/68747470733a2f2f636f636f696e6465782e696f2f626c6f62732f6769746875622f686f6d65706167652f6578616d706c652d706f64636173742e737667)](https://github.com/cocoindex-io/cocoindex/blob/main/examples/conversation_to_knowledge "Podcast → knowledge graph — download YouTube podcast audio, transcribe with speaker diarization (Whisper / AssemblyAI), LLM-extract structured statements and entities per speaker, resolve duplicates across episodes with embeddings, and store the whole graph (speakers, statements, topics) in SurrealDB or Neo4j. Incremental.")

[![CSV → Kafka live — watch a folder of CSV files, publish each row as a JSON message to a Kafka topic via CocoIndex's Kafka target connector. Incremental, sub-second, no producer loop. Keywords: Kafka, CDC, streaming, StreamNative, Confluent, CSV ingestion, event streaming.](https://camo.githubusercontent.com/11b1d74258ca249e1bc06c7518e937ca1d40e82fe4a57663d122f9fb8bcc2508/68747470733a2f2f636f636f696e6465782e696f2f626c6f62732f6769746875622f686f6d65706167652f6578616d706c652d6373762d6b61666b612e737667)](https://github.com/cocoindex-io/cocoindex/blob/main/examples/csv_to_kafka "CSV → Kafka live — watch a folder of CSV files (local or S3) and publish each row as a JSON message keyed by its primary key to a Kafka topic on StreamNative / Confluent / self-hosted. Sub-second incremental — only changed rows publish.")

![Share what you build — a banner with a trail of tiny hearts rising from the bottom behind the text, inviting the CocoIndex community to share projects built with the framework](https://camo.githubusercontent.com/b7cad9c9ac42e42ff906e4d1bf754d7824658cb9634abeb58aaa94343b167f52/68747470733a2f2f636f636f696e6465782e696f2f626c6f62732f6769746875622f686f6d65706167652f73686172652d6275696c642d6c696768742e737667)

Building something with CocoIndex? **We want to see it.**  
Tag [@cocoindex\_io](https://x.com/cocoindex_io "Tag @cocoindex_io on X to showcase your CocoIndex project") on X or drop a link in [#showcase](https://discord.com/invite/zpA9S2DR7s "Share your project in the CocoIndex Discord #showcase channel") on Discord. We'll boost it. 🥥

## Community

| [  ![Join the CocoIndex Discord community — live chat with maintainers and users, showcase your projects, get help building RAG pipelines and knowledge graphs](https://camo.githubusercontent.com/46a24571a18a1a040af34e2b0dbe746e4af78ef3f0c989bfe11492a2baa5266c/68747470733a2f2f636f636f696e6465782e696f2f626c6f62732f6769746875622f686f6d65706167652f636f6d6d2d646973636f72642d6c696768742e737667)  ](https://discord.com/invite/zpA9S2DR7s "Join the CocoIndex Discord — community chat, showcase, help, release notes") | [  ![Subscribe to the CocoIndex YouTube channel — video tutorials, live demos, architecture deep dives, and AI agent recipes](https://camo.githubusercontent.com/6e1f689085ab976b52cf077f57733fce1a4e7baaa30b477f34a01ce116232708/68747470733a2f2f636f636f696e6465782e696f2f626c6f62732f6769746875622f686f6d65706167652f636f6d6d2d796f75747562652d6c696768742e737667)  ](https://www.youtube.com/@cocoindex-io "Subscribe to the CocoIndex YouTube channel — live demos, tutorials, and deep dives") | [  ![Read the CocoIndex blog — engineering deep dives, release notes, RAG and knowledge graph tutorials, and case studies](https://camo.githubusercontent.com/d99f9b0d4a8c4ed6aae0b4fe80f3d4642e86e9306a3f5140944d9480bbdb2bf3/68747470733a2f2f636f636f696e6465782e696f2f626c6f62732f6769746875622f686f6d65706167652f636f6d6d2d626c6f672d6c696768742e737667)  ](https://cocoindex.io/blogs/ "Read the CocoIndex blog — engineering posts, release notes, and tutorials") | [  ![Follow @cocoindex_io on X (formerly Twitter) for release notes, demos, launches, and AI data pipeline updates](https://camo.githubusercontent.com/0530a5926547f305e139c8ae534054f7334d1c8dfc56d07becc4acae71ba49fe/68747470733a2f2f636f636f696e6465782e696f2f626c6f62732f6769746875622f686f6d65706167652f636f6d6d2d782d6c696768742e737667)  ](https://x.com/cocoindex_io "Follow @cocoindex_io on X (Twitter) for release notes, demos, and updates") |
| --- | --- | --- | --- |

[![We love Contributors — section title banner with a pulsing coral heart badge and cream twinkle sparkles. Every typo fix, new connector, and doc tweak makes CocoIndex better. Keywords: open-source contribution, pull request, typo fix, new connector, good first issue, Hacktoberfest, community, coconut heart.](https://camo.githubusercontent.com/f30dbe1e1eda31c2f8c3f495bdedf7ab6dc291cfe67e760aa8364a67ca270174/68747470733a2f2f636f636f696e6465782e696f2f626c6f62732f6769746875622f686f6d65706167652f77652d6c6f76652d636f6e7472696275746f72732e737667)](https://camo.githubusercontent.com/f30dbe1e1eda31c2f8c3f495bdedf7ab6dc291cfe67e760aa8364a67ca270174/68747470733a2f2f636f636f696e6465782e696f2f626c6f62732f6769746875622f686f6d65706167652f77652d6c6f76652d636f6e7472696275746f72732e737667)

**We are *so* excited to meet you.**  
Every typo fix, new connector, doc tweak, or full-on rewrite makes CocoIndex better.  
Come hang out — big PRs and small ones, both welcome.

📝 [**Read the contributing guide**](https://cocoindex.io/docs/contributing/guide) · 🐛 [**good first issues**](https://github.com/cocoindex-io/cocoindex/labels/good%20first%20issue) · 💬 [**Say hi on Discord**](https://discord.com/invite/zpA9S2DR7s)

## CocoIndex Enterprise

![CocoIndex Enterprise — built for enterprise scale. Four headline stats for PB-scale incremental indexing: PB corpus scale incrementally indexed (coral), 10× fewer LLM embedding calls vs. full recompute (yellow), 100% lineage coverage with every byte traceable (mint), Δ only the delta always (sky). Below, a wide 50×8 corpus matrix of 400 dim tiles represents a petabyte-scale store where a single coral Δ slice of 8 tiles re-runs while the other 99.9% stays cached. Keywords: enterprise RAG, petabyte-scale indexing, incremental compute, delta-only, lineage, parallel chunking, zero-copy, failure isolation.](https://camo.githubusercontent.com/f52361a64c3a9875135f23aa992b1824d60591757be61dbcbecc1c492cf7265b/68747470733a2f2f636f636f696e6465782e696f2f626c6f62732f6769746875622f686f6d65706167652f656e74657270726973652d7363616c652d6c696768742e737667)

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

[![Explore CocoIndex Enterprise — bright blue pill button linking to cocoindex.io/enterprise, the PB-scale incremental data pipeline for AI agents](https://camo.githubusercontent.com/ae2b7159b87f803c40991f825297f3d8c3d79edbad3f6d05c388a962423cde84/68747470733a2f2f636f636f696e6465782e696f2f626c6f62732f6769746875622f686f6d65706167652f656e74657270726973652d62746e2e737667)](https://cocoindex.io/enterprise/ "Explore CocoIndex Enterprise — PB-scale incremental data pipelines for AI agents")

<sub>Apache 2.0 · © CocoIndex contributors 🥥</sub>