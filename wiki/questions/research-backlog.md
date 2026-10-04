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
14. Стоит ли ставить tgrep как grep-backend для агента на больших worktree (Hypothesis: candidate pruning beats `rg` on 100k+ files; loses on high match-volume / small Linux trees)? Не ставить, пока нет явного запроса. Copilot CLI integration не проверяли.
15. Стоит ли ставить OpenResearch/`orx` как outer research workspace (Hypothesis: freeze-on-answer + stacked bushes beats spreadsheet+tmux for eval lineage)? Не ставить: нет Hermes-адаптера; pipe-to-sh + official telemetry; remote bind/auth **Unknown**. Process-borrow правил — да.
16. Нужен ли отдельный `browser-harness` CLI рядом с Hermes `browser_exec` (Hypothesis: writable `agent_helpers.py` compounds; Safety: local Chrome = user cookies + opt-out PostHog `task` field)? Не ставить. Process-borrow AX-tree clicks — да.
17. Стоит ли Jev/TypeSafe как browser policy (Hypothesis: indexed ops beat free CDP Python for form/nav)? Не ставить: paid TypeSafe + text-model keys; 7.1 s Flights is 3-pair author data. DONE-check steal — да. Adjacent backends: [[wiki/sources/jev-usage-examples]] — compaction/MCP/Canny closer to evidence gates than the Flights demo; still not install.
18. Портировать ли logika/Chelpanov review format в Hermes (Hypothesis: named fallacies beat unscoped «проверь текст» for wiki/GTM drafts)? Не копировать SKILL.md в `~/.hermes/skills` без запроса. Шаблон отчёта — process-borrow.
19. Заимствовать ли RRSI selection (noise floor + token budget + leakage critic, coding `w_s=0`) вместо ungated `/refine` (Hypothesis: measured reject beats trajectory→SOUL)? Не ставить и не направлять цикл на `SOUL.md` / memories. Process-borrow чеклиста — да. PDF ещё не читали. Числа README — author claims.
20. Ставить ли CLM как локальный System One вместо hosted Jev (Hypothesis: same wire, no API key, cache makes repeated actions cheap)? Не ставить: нужен vLLM+GPU; 9× / 87.6% / 81.6% — author claims. T-Rex 5/5 survival is with the planner shield on (CLM agrees 0.658, Jev 0.987). Process-borrow: don't quote a shielded score as the model's.
21. Читать ли ноутбуки pageman/sutskever-30 как учебник (Hypothesis: seeing the op in NumPy beats another framework tutorial)? Не ставить и не клонировать без запроса. Бейдж 30/30 — число файлов: цикл с обновлением весов в 6 (`02`,`05`,`09`,`18`,`26`,`27`), сохранённых выводов 0. Paper 22 — нарисованный степенной закон, не замер. Process-borrow: карта механизмов — да; цитировать как воспроизведение статьи — нет.
22. Ставить ли Julia 1 как локальный ranker вместо hosted Jev (Hypothesis: same question names, CPU, no API key)? Не качать веса без запроса. Это не `POST /v1/systemone` — другой рантайм (`engine.predict`, mmBERT + marker head). 73.15% / 94% / 86% — авторский прогон; колонка Jev скопирована из протокола, не парный реран. Banking77 64% (H200, 1 abstain) и 60% (CPU, 3 abstain) — shortlist 72→16, не native 72-way. Process-borrow: не цитировать softmax после сужения и не принимать display-rounding 1.0 за уверенность.
23. Читать ли Emerson, *Intermediate Microeconomics* (Oregon State OER) как карту «какой рычаг двигает политика» (Hypothesis: naming the margin beats arguing the outcome)? Не качать PDF без запроса. Вопрос модуля — крючок, не вывод. «Исчисление необязательно в каждой главе» — заявка издателя: заголовки `Calculus` нашлись в модулях 7 и 8. Журнал версий кончается на 2.04 (2024-04-18), файлы девяти модулей помечены 2025. CC BY-NC-SA: в платный продукт графики не переносить. Process-borrow: раскладывать спор на ограничение и предельную замену — да; цитировать вопрос главы как ответ — нет.
24. Читать ли остальные лекции MIT 6.254 (Ozdaglar, весна 2010) после лекции 5 (Hypothesis: существование равновесия — дешёвая лицензия смотреть, а не место, где оно лежит)? Лекцию 6 (разрывные игры и доказательство Glicksberg) не качали. Glicksberg в лекции 5 сформулирован и не доказан. Промежуточные формулы из текстовой реконструкции PDF не цитировать: глифы разъехались. CC BY-NC-SA, имя MIT в лицензию не входит. Process-borrow: проверять условия (конечные действия, либо вогнутость на компакте) до слов «равновесная цена» — да; выдавать существование за единственность или за координату — нет.
25. Ставить ли UniMate и качать ли превью-чекпойнты (Hypothesis: один flow-matching на много топологий скелета дешевле отдельной модели на каждую)? Не ставить без запроса. Сэмплинг требует `dataset/features/<dataset>/` рядом с чекпойнтом — веса одни ничего не анимируют. Truebones в скачивание не входит (коммерческий пак). Подписи релиза не обязаны совпадать со страницей проекта. In-between / edit / expand — один Euler с подстановкой, не dopri5, и только при `diff_model=flow`. Тегов нет. Process-borrow: закреплённый кадр — копия, не выбор модели; «real time» и 13 006 — заявки README, не наш прогон.
26. Ставить ли что-то из Awesome Agent Skills Security как сканер скиллов (Hypothesis: список атак заменяет проверку своего write-path)? Не ставить: это каталог ссылок, не инструмент. 150 атак / 213 защит / 41 бенчмарк — счётчик пунктов README на 2026-09-30, не наш прогон. Размеры бенчмарков в таблице — заявки статей. Truebones-стиль: CC0 на список не лицензирует чужие репозитории. Process-borrow: отличать отравленный skill-файл от jailbreak чата — да; ставить репозиторий потому что он в списке — нет.
27. Ставить ли Codync как телефон к уже запущенным агентам (Hypothesis: очередь на ACP дешевле своего loop)? Не ставить без запроса. Встроенный список — 26 CLI, Hermes в нём нет; «~40» — комментарий к реестру ACP, реестр не скачивали. Порт по умолчанию 19222 на `0.0.0.0`. Process-borrow: бот — очередь перед чужим агентом, не новая ось; «1:1 с Grok Bot» не проверено.
28. Проверять ли цифры промо Anysite про AI-funding (Hypothesis: концентрация в мега-раундах объясняет «деньги ×2, сделки +20%»)? Только если появится файл отчёта. Не подписываться, чтобы проверить. 7 740 / $138 млрд / 43% / ×2 / +20% / +59% / +41% / +423% / 30 компаний / Anthropic $65 млрд / Cursor $4 млрд — заявки автора, файла нет.
29. Какую одну книгу из списка Gallier открыть первой (Hypothesis: список из 19 названий — не очередь чтения)? Не выбрано. PDF не скачивать, пока нет явного запроса. Строка «In progress» на индексе — подпись страницы, не статус каждой книги. 2218 и 401 страниц — строки автора, не наш подсчёт.

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
- `[[wiki/sources/tgrep]]`
- `[[wiki/sources/openresearch]]`
- `[[wiki/sources/browser-harness]]`
- `[[wiki/sources/jev-ultrafast]]`
- `[[wiki/sources/jev-usage-examples]]`
- `[[wiki/sources/logika]]`
- `[[wiki/sources/rrsi]]`
- `[[wiki/sources/clm]]`
- `[[wiki/sources/julia-1]]`
- `[[wiki/sources/sutskever-30-implementations]]`
- `[[wiki/sources/intermediate-microeconomics-emerson]]`
- `[[wiki/sources/mit-6-254-game-theory-ozdaglar]]`
- `[[wiki/sources/unimate]]`
- `[[wiki/sources/awesome-agent-skills-security]]`
- `[[wiki/sources/codync]]`
- `[[wiki/sources/anysite-ai-startup-funding]]`
- `[[wiki/sources/jean-gallier-books]]`
