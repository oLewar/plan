# Research backlog

## Open questions
1. Какие классы событий в нашем домене наиболее критичны для causal modeling?
2. Какие источники дают наибольший прирост уверенности на единицу времени?
3. Где у нас системные blind spots (темы без источников или слабо связные узлы)?
4. Как автоматизировать lint-отчёт без потери качества?
5. Какие write-path'ы Hermes/Chappy/`pro/plan` эквивалентны ASI06 memory (memories, SOUL, vault ingest, cron outputs) и нужен ли runtime guard?

## Next actions
- Составить топ-10 приоритетных вопросов по текущим целям.
- На каждый вопрос определить минимально достаточный набор источников.
- После каждого ingest обновлять причинные цепочки в `wiki/concepts/` и `wiki/analyses/`.

## Sources
- `[[wiki/sources/llm-wiki-gist]]`
- `[[wiki/sources/owasp-agent-memory-guard]]`
