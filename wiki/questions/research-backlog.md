# Research backlog

## Open questions
1. Какие классы событий в нашем домене наиболее критичны для causal modeling?
2. Какие источники дают наибольший прирост уверенности на единицу времени?
3. Где у нас системные blind spots (темы без источников или слабо связные узлы)?
4. Как автоматизировать lint-отчёт без потери качества?
5. Какие write-path'ы Hermes/Chappy/`pro/plan` эквивалентны ASI06 memory (memories, SOUL, vault ingest, cron outputs) и нужен ли runtime guard?
6. Можно ли в DeepSeek Harness реально заменить `agent-loop` / sandbox provider без форка (Hypothesis: everything-is-a-plugin)? Стоит ли это vs Hermes skills?
7. Стоит ли портировать pstack-паттерн (verbatim playbook steps + named principles + multi-model interrogate) в Hermes/Chappy, или достаточно process-borrow? Fusion остаётся explicit-request-only.
8. Нужен ли Herdr как outer runtime для параллельных Hermes/Claude/Codex pane (Hypothesis: agent-runtime multiplexer beats tmux here)? Не ставить, пока нет явного запроса и smoke-test.
9. Стоит ли заимствовать Continual Harness (`/refine` + harness CRUD) vs держать SOUL/memories human-gated (Hypothesis: ungated refine poisons skills — Factorio RCON)? Paper PDF ещё не читали.
10. Стоит ли читать Jentzen et al. (arXiv:2310.20360) дальше TOC — с Ch.14–15 (composed error) как минимальный рычаг, или Cost 737 стр. не окупается vs текущих harness-осей?
11. Нужен ли oMLX как local OpenAI backend для Hermes/Claude Code на Mac (Hypothesis: SSD KV restore beats recompute for long sessions)? На этом Linux-хосте не ставить. One-click Hermes integration не проверяли.
12. Стоит ли ставить Archify как Hermes skill vs оставить Mermaid в vault (Hypothesis: fail-closed JSON IR beats pretty-but-lying diagrams)? Не ставить, пока нет явного запроса. DSH-бандл = 2.14, skill HEAD = 2.16.
13. Нужен ли offensive MCP-broker (HexStrike) как lab backend (Hypothesis: named scanner wrappers without `execute_command` + loopback + auth can be useful; as shipped Safety≈0)? Не ставить на этот хост. v7.0 / hexstrike.com desktop — Unknown, not in tree.

## Next actions
- Составить топ-10 приоритетных вопросов по текущим целям.
- На каждый вопрос определить минимально достаточный набор источников.
- После каждого ingest обновлять причинные цепочки в `wiki/concepts/` и `wiki/analyses/`.

## Sources
- `[[wiki/sources/llm-wiki-gist]]`
- `[[wiki/sources/owasp-agent-memory-guard]]`
- `[[wiki/sources/deepseek-harness]]`
- `[[wiki/sources/pstack]]`
- `[[wiki/sources/herdr]]`
- `[[wiki/sources/prime-agent]]`
- `[[wiki/sources/mathematical-introduction-to-deep-learning]]`
- `[[wiki/sources/omlx]]`
- `[[wiki/sources/archify]]`
- `[[wiki/sources/hexstrike-ai]]`
