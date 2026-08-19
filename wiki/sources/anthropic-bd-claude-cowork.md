# How Anthropic BD uses Claude Cowork for inbound/outbound

## Bibliographic / source

| Field | Value |
|---|---|
| Title | **How Anthropic's business development team uses Claude to run inbound and outbound at scale** |
| Author | John Albert — BDR, [[wiki/entities/anthropic\|Anthropic]] |
| Publisher | Claude / Anthropic blog |
| Published | **2026-08-07** (page metadata also lists modified 2026-08-10) |
| Category / product | Enterprise AI · [Claude Cowork](https://claude.com/product/cowork) |
| URL | https://claude.com/blog/how-anthropics-business-development-team-uses-claude-to-run-inbound-and-outbound-at-scale |
| Wayback | [2026-08-19 13:46:44](https://web.archive.org/web/20260819134644/https://claude.com/blog/how-anthropics-business-development-team-uses-claude-to-run-inbound-and-outbound-at-scale) |
| Raw capture | `[[raw/anthropic-bd-claude-cowork-inbound-outbound]]` |

## One-line purpose

Первоисточник: как BDR Anthropic гоняет **inbound + outbound at scale** через Claude Cowork — skills, scheduled tasks, CRM/Gmail/Gong connectors — с человеком на каждом исходящем письме.

## Thesis (from the article)

1. **До Cowork** inbound = ~**5 часов/день** на sales inbox (повторяющиеся ответы) плюс свой book; outbound = ручной research по сотням аккаунтов.
2. **После:** повторяемые куски — skills + hourly/overnight schedules; письма — **drafts for review**, не автосенд.
3. **Порядок внедрения:** сначала **sales knowledge base** (частые вопросы + лучшие ответы), потом workflows. Claude сам собрал первую версию KB и дальше флажит stale facts.
4. **Стек inbound:** hourly inbox skill = thin system prompt + KB + voice profile репа → черновики ответов.
5. **Стек outbound:** overnight book research (Salesforce, Apollo, Common Room, Gong, warehouse) → утром brief + score + play на каждый аккаунт; memory file / ledger против дублей.
6. **Админ/CRM:** no-show/dark-prospect watcher (Gmail + Calendar); new-lead first-touch drafts; Salesforce stage updates **с evidence + approval**, причины reject пишутся обратно в skill.
7. **Ad-hoc > очередь к data team:** spend dashboard, «undiscovered usage» (продукт уже используется, opportunity нет), скоринг аккаунтов под вебинар — часто хватает промпта, не отдельного skill.
8. **Командный слой:** проверенные skills → shared plugin; skills делают **достаточно общими**, чтобы разные books/сегменты адаптировали; feedback loop обязателен.

## Workflow map

| Motion | What Claude does | Human gate |
|---|---|---|
| Inbound inbox | Hourly scan + draft reply from KB + voice | Read / edit / send |
| New leads | Scheduled CRM scan + first-touch draft | Same |
| No-show / gone dark | Watch Gmail + Calendar, notify | Follow-up decision |
| Salesforce hygiene | Propose stage change with evidence | Approve / edit / reject + reason |
| Outbound book | Overnight research + score + play (~100 accounts) | Choose who to work |
| Discovery QA | Gong vs playbook → scorecard (top-3 good / top-3 fix / pass-fail / one drill) | Practice next call |
| Usage / events | Ad-hoc prompts: spend trends, unused-product accounts, webinar ICP fit | Outreach decision |

UI screenshots in the article are **synthetic / anonymized** (author's caveat). Localized copies: `assets/external/cdn.prod.website-files.com/`.

## Getting-started advice (author)

1. KB **before** workflows.
2. Дать примеры working messages + ICP; voice skill на стиль репа.
3. **Человек на каждом send.**
4. Шарить skills, когда они уже daily.
5. Не заточить skill под одного репа.
6. Писать dismiss/correct обратно в skill.
7. «Just start experimenting» — больше context/tools → больше рычага.

## Causal map (for pro/plan)

| Cause / lever | Effect |
|---|---|
| Shared, stale-checked FAQ/KB | Drafts не выдумывают product facts |
| Hourly inbox skill | 5h/day ручных ответов → review queue |
| Overnight book research + score | Coverage ~100 accounts без линейного research-time |
| Approval + reject-reason ledger | Skill не повторяет ту же ошибку |
| Shared plugin of proven skills | Команда масштабирует playbook, не личные хаки |
| Human-on-every-send | Скорость без потери trust / compliance |
| Usage-without-opportunity signal | Outbound опирается на already-in-product, не на холодный список |

## Why it matters for `pro/plan`

- Операционный образец **agent-assisted GTM**: не «автопилот продаж», а **KB + skills + schedule + HITL**.
- Прямо усиливает [[wiki/concepts/efficiency-metric]]: убрать 5h/day повторяшки, оставить discovery/education.
- Паттерн [[wiki/concepts/human-in-the-loop-gtm]] применим к 1M Strategy (родители/школы) и к любому inbound (Telegram, sales inbox, waitlist).
- Рядом с [[wiki/concepts/high-agency]]: агент готовит, человек выбирает цель и несёт send-risk.
- Рядом с [[wiki/concepts/barbell-strategy]]: frontier Cowork + вечный принцип «не отправляй то, что не прочитал».
- Sales-заметки: [[10_Reference/Strategy/Sales]].

## Status

- **Ingest depth:** full article body from live HTML `w-richtext` (2026-08-19); thesis-level synthesis, не независимый аудит метрик Anthropic.
- **Confidence:** medium — single first-person vendor blog; числа (5h/day, ~100 accounts) — авторские, без внешней проверки. Скриншоты помечены как demo/synthetic.
- **Capture note:** `web_extract`/Firecrawl на claude.com вернули 400; live `curl` 200 + Wayback snapshot `20260819134644`.

## Next (optional)

- [ ] Сопоставить Cowork skills с Hermes cron/skills (inbox draft, CRM hygiene) без копирования их внутренних промптов
- [ ] Кастдев-плейбук 1M: KB частых возражений родителей до любой outbound-автоматизации
- [ ] Не делать: автосенд клиентам / родителям

## Links

- Entity: [[wiki/entities/anthropic]]
- Concept: [[wiki/concepts/human-in-the-loop-gtm]]
- Tool card: [[10_Reference/tools/claude-cowork]]
- Sales notes: [[10_Reference/Strategy/Sales]]
- Related: [[wiki/concepts/efficiency-metric]], [[wiki/concepts/high-agency]], [[wiki/concepts/barbell-strategy]], [[25_Projects/1M_Strategy/Overview]]
- Raw: [[raw/anthropic-bd-claude-cowork-inbound-outbound]]

## Sources / provenance

- Live: https://claude.com/blog/how-anthropics-business-development-team-uses-claude-to-run-inbound-and-outbound-at-scale
- Wayback: https://web.archive.org/web/20260819134644/https://claude.com/blog/how-anthropics-business-development-team-uses-claude-to-run-inbound-and-outbound-at-scale
- Local capture: `raw/anthropic-bd-claude-cowork-inbound-outbound.md` (ingested 2026-08-19, sha256 `4f057909d799c3d34f4c79cf674c1d7fa06493e8d90b1ae6dc193972118c183b`)
- JSON-LD on page: BlogPosting, datePublished Aug 07 2026, dateModified Aug 10 2026
- User request: Telegram «добавь в базу знаний» + «еще раз»
