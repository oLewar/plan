# Human-in-the-loop GTM

## Definition (working)

Агентная go-to-market петля, где модель **исследует, черновит и предлагает CRM-изменения**, а человек **читает, правит и нажимает send / approve**. Автономный сенд клиенту — антипаттерн.

## Mechanism (from Anthropic BD)

```
curated KB (FAQ + best answers, stale-flagged)
    → thin skill (prompt + KB + voice/ICP examples)
    → schedule (hourly inbox / overnight book)
    → draft or proposed CRM update + evidence
    → human approve / edit / reject
    → write the reason back into the skill
    → promote stable skills to a shared plugin
```

Отдельная ветка: **ad-hoc prompts** (usage without opportunity, event ICP scoring) — не всё должно стать skill с первого раза.

## Design rules

1. **KB before workflows** — иначе drafts галлюцинируют продукт.
2. **Person on every send** — скорость без делегирования trust.
3. **Evidence on CRM writes** — stage change = факт из Gmail/Gong, не «модель так решила».
4. **Feedback is training data** — dismiss без причины не улучшает skill.
5. **Share only after daily use** — не плодить личные одноразовые автоматизации как стандарт команды.
6. **Keep skills general** — books/сегменты разные; skill должен адаптироваться, а не копировать один routine.

## Causal link

| If missing | Failure mode |
|---|---|
| No KB | Confident wrong product answers |
| No human send gate | Brand/legal/relationship risk at scale |
| No reject ledger | Same bad hook every morning |
| Skill too personal | Can't share; team stays artisan |
| Automate before ICP examples | Outbound looks generic |

## Why it matters for `pro/plan`

- Переносимый паттерн для [[25_Projects/1M_Strategy/Overview]]: сначала KB возражений родителей/школ, потом любой outreach-agent.
- Совместим с [[wiki/concepts/efficiency-metric]]: режем cost повторяшек, не режем safety/trust.
- Дополняет [[wiki/concepts/high-agency]]: агент не выбирает цель сделки, человек остаётся principal.
- Совместим с [[wiki/concepts/barbell-strategy]]: frontier Cowork + вечный «не отправляй непрочитанное».
- Не импортировать pstack **never-block-on-the-human** на customer send: coding autonomy ≠ GTM send ([[wiki/concepts/playbook-routed-agent-mode]]).

## Status

- `Hypothesis` как универсальный GTM-стандарт; `Confirmed` только как описание практики Anthropic BD в одном блоге (2026-08-07).
- Не доказано, что те же skills сработают вне их CRM/ICP/бренда.

## Sources

- [[wiki/sources/anthropic-bd-claude-cowork]]
- Related: [[wiki/entities/anthropic]], [[10_Reference/tools/claude-cowork]], [[10_Reference/Strategy/Sales]], [[wiki/concepts/efficiency-metric]], [[wiki/concepts/high-agency]]
