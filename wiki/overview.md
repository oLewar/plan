# Overview

## Mission
Исследование мира для понимания причинно-следственных связей между событиями и поиска эффективных решений возникающих проблем.

## Current operating assumptions
- Знание накапливается как persistent wiki, а не пересобирается с нуля на каждый вопрос.
- Источники в `raw/` immutable.
- Каждая значимая мысль из исследования должна попадать в wiki-страницы.
- Безопасность — обязательный фильтр всех действий.
- Persistent memory (wiki / Hermes memories / SOUL) is a privileged next-turn input — treat writes as an ASI06 surface ([[wiki/concepts/memory-poisoning]]).
- Agent products can be *composed* (plugins/profiles) rather than forked; DeepSeek Harness is the public case ([[wiki/concepts/everything-is-a-plugin]]).
- Coding-agent *style* can be a sticky playbook router on an existing loop; pstack `/poteto-mode` is the public Cursor case ([[wiki/concepts/playbook-routed-agent-mode]]).
- Coding-agent *place* can be a server-owned PTY runtime; Herdr is the public multiplexer case ([[wiki/concepts/agent-runtime-multiplexer]]).
- A harness can *refine its own supplemental state* from the trajectory; Prime Agent `/refine` is the public case — writes are an ASI06 surface ([[wiki/concepts/continual-harness]]).
- Supervised DL training error decomposes into approximation + optimization + generalization; do not collapse them into one label ([[wiki/concepts/composed-error-analysis]]).
- Local coding-agent inference can persist KV across RAM and SSD; oMLX is the public Apple Silicon case — this Linux host cannot run it ([[wiki/concepts/tiered-kv-cache]]).
- A diagram can be a fail-closed **typed JSON IR** compiled to HTML; Archify is the public case — not a fifth harness axis, not installed here ([[wiki/concepts/typed-ir-artifact-delivery]]).
- MCP is a **transport**, not a sandbox: a tool broker can be unauthenticated `shell=True` on `0.0.0.0`; HexStrike is the public anti-pattern — not installed here ([[wiki/concepts/mcp-tool-broker]]).

## Active hypotheses
1. Качество решений растёт быстрее, если сначала строить causal map, а уже потом выбирать действия.
2. Эффективность повышается, когда query-результаты автоматически компаундятся обратно в wiki.
3. Регулярный lint снижает деградацию базы знаний (противоречия, устаревшие тезисы, orphan-страницы).

## Next milestones
- Внедрить ingest-чеклист как повторяемый workflow.
- Ввести weekly lint-процедуру.
- Наладить приоритезацию backlog по формуле эффективности.
