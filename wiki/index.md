# Wiki Index

Обновляется при каждом ingest/query/lint.

## Vault navigation
- [[00_System/Index|System Index]]
- [[10_Reference/Index|Reference Index]]
- [[20_Personal/Index|Personal Index]]
- [[25_Projects/Index|Projects Index]]
- [[30_Tasks/Backlog|Tasks Backlog]]
- [[30_Tasks/In-Progress|Tasks In-Progress]]
- [[40_Research/Index|Research Index]]
- [[50_Hypotheses/Index|Hypotheses Index]]
- [[60_Archive/Index|Archive Index]]

## Core
- [[wiki/overview|overview]] — текущая карта домена, гипотезы, контекст.

## Sources
- [[wiki/sources/llm-wiki-gist|LLM Wiki (Karpathy gist)]] — базовый паттерн структуры и процессов wiki.
- [[wiki/sources/the-plausibility-of-life-kirschner-gerhart|The Plausibility of Life (Kirschner & Gerhart)]] — evo-devo / facilitated variation; почему сложная жизнь «правдоподобна».
- [[wiki/sources/fireside-chat-arman-suleimenov-2026-08-07|Fireside Chat с Арманом Сулейменовым (2026-08-07)]] — nFactorial, vibe coding, барбелл-стратегия, high agency, idea=f(assets).
- [[wiki/sources/mattpocock-skills|Matt Pocock Skills]] — composable agent skills for real engineering (grill, TDD, architecture, tickets).
- [[wiki/sources/x-algorithm|X For You Feed Algorithm (xai-org/x-algorithm)]] — For You ranking/visibility; defaults: copy +20, reply/quote +5, follow +4, like +0.5; report −234.
- [[wiki/sources/anthropic-bd-claude-cowork|Anthropic BD × Claude Cowork]] — inbound/outbound at scale: KB → hourly drafts → HITL send; overnight book research.
- [[wiki/sources/owasp-agent-memory-guard|OWASP Agent Memory Guard]] — ASI06 runtime guard: mediate memory writes; 0.3.0; local, no API keys.
- [[wiki/sources/deepseek-harness|DeepSeek Harness (dsh)]] — plugin agent harness on Cordis; developer preview; `npx @deepseek-ai/dsh web`.
- [[wiki/sources/pstack|pstack (cursor/plugins)]] — Cursor plugin: sticky `/poteto-mode`, 21 principles, multi-model panels; MIT 0.14.2.
- [[wiki/sources/herdr|Herdr (herdrdev/herdr)]] — agent-runtime multiplexer; Apache-2.0; v0.8.2; server owns PTYs; Hermes is a first-class agent.
- [[wiki/sources/prime-agent|Prime Agent (PrimeIntellect-ai/prime-agent)]] — self-improving RLM harness; MIT v0.8.1; persistent IPython + `/refine`.
- [[wiki/sources/mathematical-introduction-to-deep-learning|Mathematical Introduction to Deep Learning (arXiv:2310.20360)]] — Jentzen/Kuckuck/von Wurstemberger; v3 737 pp.; ANN + composed error + PINNs.
- [[wiki/sources/omlx|oMLX (jundot/omlx)]] — Apple Silicon LLM server; continuous batching + RAM/SSD KV cache; OpenAI/Anthropic API; v0.6.4.

## Entities
- [[wiki/entities/omlx|oMLX / Jun Kim (`jundot`)]] — Apple Silicon inference server; Apache-2.0; Hermes listed as Integrations client.
- [[wiki/entities/prime-intellect|Prime Intellect]] — lab; Prime Agent + prime-rl / verifiers (latter not ingested).
- [[wiki/entities/herdr|Herdr]] — YC F26 runtime; org `herdrdev`; founder Can (`ogulcancelik`).
- [[wiki/entities/deepseek|DeepSeek]] — lab; models + public harness `dsh`.
- [[wiki/entities/owasp|OWASP]] — ASI06 / agent-security standards home; AMG incubator.
- [[wiki/entities/anthropic|Anthropic]] — Claude lab; internal BDR playbook on Cowork skills/schedules.
- [[wiki/entities/arman-suleimenov|Арман Сулейменов]] — founder nFactorial, education angel investor, mental-models operator.
- [[wiki/entities/nfactorial-school|nFactorial School]] — selective build+launch+monetize incubator / education community.
- [[wiki/entities/xai|xAI]] — AI lab; publisher of public X For You algorithm stack.
- [[wiki/entities/cursor|Cursor]] — AI code editor; host of official `cursor/plugins` (pstack).
- [[wiki/entities/lauren-tan|Lauren Tan (`poteto`)]] — pstack author; React Compiler / Cursor.

## Concepts
- [[wiki/concepts/causal-analysis|Causal analysis]] — причинно-следственные связи и уровни уверенности.
- [[wiki/concepts/efficiency-metric|Efficiency metric]] — как измеряем эффективность решений.
- [[wiki/concepts/vibe-coding|Vibe coding]] — LLM-first сборка прототипов: скорость vs fundamentals/users.
- [[wiki/concepts/barbell-strategy|Barbell strategy]] — frontier tools + timeless principles; избегать «средней» зоны.
- [[wiki/concepts/high-agency|High agency]] — инициатива/миссия/pushback как дефицит при commodity-интеллекте.
- [[wiki/concepts/idea-as-function-of-assets|Idea = f(assets)]] — идея как функция уже имеющихся преимуществ.
- [[wiki/concepts/shokunin|Shokunin]] — lifelong craftsmanship как антидот к tool-democratization.
- [[wiki/concepts/multi-action-feed-ranking|Multi-action feed ranking]] — multi-action prediction + explicit weights; X defaults not like-optimized; ranking ≠ visibility.
- [[wiki/concepts/human-in-the-loop-gtm|Human-in-the-loop GTM]] — KB + skills + schedule + human send; CRM writes need evidence and reject-ledger.
- [[wiki/concepts/memory-poisoning|Memory poisoning (ASI06)]] — persistent memory as privileged next-turn input; write-gate ≠ prompt-filter.
- [[wiki/concepts/everything-is-a-plugin|Everything is a plugin]] — no privileged agent loop; compose profiles/bundles/patches; unload = unwind effects.
- [[wiki/concepts/playbook-routed-agent-mode|Playbook-routed agent mode]] — sticky mode matches a playbook, copies steps verbatim, routes skills; pstack `/poteto-mode`.
- [[wiki/concepts/agent-runtime-multiplexer|Agent-runtime multiplexer]] — server owns PTYs + semantic agent state; UI is a client; Herdr.
- [[wiki/concepts/continual-harness|Continual harness]] — agent CRUD on supplemental prompts/memories/skills/subagents; `/refine`; base prompt frozen.
- [[wiki/concepts/composed-error-analysis|Composed error analysis]] — overall ANN error = approximation + optimization + generalization.
- [[wiki/concepts/tiered-kv-cache|Tiered KV cache]] — hot RAM + cold SSD paged KV; prefix restore after restart; oMLX.

## Reference standards
- [[10_Reference/Agents/prompting-codebase-questions|Prompting codebase questions]] — примеры промптов для coding agent / Claude Code по кодовой базе.
- [[10_Reference/tools/self-hosted-open-source-tools|Self-hosted и privacy-first open-source tools]] — LocalSend, yt-dlp, Stirling-PDF, FreeTube, Syncthing, Vaultwarden, Immich, AdGuard Home, Jellyfin, Uptime Kuma.
- [[10_Reference/tools/cloakbrowser|CloakBrowser]] — stealth Chromium для browser automation и возможные варианты интеграции с Hermes/Chappy.
- [[10_Reference/tools/mattpocock-skills|Matt Pocock Skills]] — skills pack (Claude Code plugin / skills.sh) для engineering discipline.
- [[10_Reference/tools/x-algorithm|X For You Feed Algorithm]] — open-source X ranking/visibility stack (xai-org/x-algorithm).
- [[10_Reference/Strategy/marketing|Marketing]] — маркетинговые принципы, naming, аудитория, elevator pitch и заметки по AI search optimization / AEO / GEO.
- [[10_Reference/tools/claude-cowork|Claude Cowork]] — skills/schedules/connectors; Anthropic BD inbound+outbound pattern (HITL).
- [[10_Reference/tools/owasp-agent-memory-guard|OWASP Agent Memory Guard]] — Python runtime + CLI/Action/MCP for ASI06 memory writes.
- [[10_Reference/tools/deepseek-harness|DeepSeek Harness]] — `dsh` CLI/Web UI; Cordis plugins; npm RC.
- [[10_Reference/tools/pstack|pstack]] — Cursor `/add-plugin pstack`; `/poteto-mode` + `/setup-pstack`.
- [[10_Reference/tools/herdr|Herdr]] — `herdr` TUI/server; `herdr integration install hermes`; reference only.
- [[10_Reference/tools/prime-agent|Prime Agent]] — `prime-agent` CLI; RLM REPL + daemon; reference only.
- [[10_Reference/tools/omlx|oMLX]] — `omlx serve` on Apple Silicon; `:8000/v1`; reference only (wrong OS here).

## Analyses
- [[wiki/analyses/repo-operating-model|Operating model for pro/plan]] — целевая модель структуры и процессов репозитория.
- [[25_Projects/Kaizen/Index|Kaizen]] — контур постоянного улучшения эффективности через наблюдения, эксперименты и стандарты.
- [[25_Projects/1M_Strategy/Overview|1M Strategy]] — активная стратегия выхода на $1M ARR через детский learning/focus продукт и агентный harness.

## Open Questions
- [[wiki/questions/research-backlog|Research backlog]] — что нужно доисследовать дальше.

## Lint Reports
- (пока пусто)

## AI Signal Monitor
- [[40_Research/ai-signal-monitor/x-ai-accounts]] — AI Signal Monitor — X Accounts
- [[40_Research/ai-signal-monitor/reddit-ai-origin-topics]] — AI Signal Monitor — Reddit Origin Topics
- [[40_Research/ai-signal-monitor/github-fast-star-repos]] — AI Signal Monitor — Fast-Star GitHub Repos

## AI Signal Monitor Daily Reports
- [[40_Research/ai-signal-monitor/daily/2026-06-17]] — daily AI signal summary
- [[40_Research/ai-signal-monitor/daily/2026-06-18]] — daily AI signal summary
- [[40_Research/ai-signal-monitor/daily/2026-06-19]] — daily AI signal summary
- [[40_Research/ai-signal-monitor/daily/2026-06-20]] — daily AI signal summary
- [[40_Research/ai-signal-monitor/daily/2026-06-21]] — daily AI signal summary
- [[40_Research/ai-signal-monitor/daily/2026-06-22]] — daily AI signal summary
