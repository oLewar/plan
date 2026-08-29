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

## Active hypotheses
1. Качество решений растёт быстрее, если сначала строить causal map, а уже потом выбирать действия.
2. Эффективность повышается, когда query-результаты автоматически компаундятся обратно в wiki.
3. Регулярный lint снижает деградацию базы знаний (противоречия, устаревшие тезисы, orphan-страницы).

## Next milestones
- Внедрить ingest-чеклист как повторяемый workflow.
- Ввести weekly lint-процедуру.
- Наладить приоритезацию backlog по формуле эффективности.
