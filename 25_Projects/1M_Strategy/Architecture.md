---
type: project-architecture
status: draft
created: 2026-05-27
tags:
  - agent-harness
  - orchestration
  - strategy
  - verification
---

# Architecture — Strategy Agent Harness

## Purpose

Построить независимую агентную систему, которая помогает достигать стратегии $1M ARR через быстрый анализ возможностей, генерацию решений, сравнение альтернатив и верификацию результатов.

## Core idea

Система должна состоять из множества узкоспециализированных агентов/контекстов, которые можно заменять готовыми решениями: Codex, Claude Code, Bilge, OpenCode, web-research агенты, X/Twitter-анализаторы, domain-specific evaluators.

Главная ценность не в конкретном агенте, а в **верхнем уровне принятия решений**:
- кому дать задачу;
- как сформулировать задачу;
- какие артефакты требовать;
- как сравнить ответы;
- как верифицировать выводы;
- как превратить результат в следующий рабочий шаг.

## Proposed orchestration loop

### 1. Intent capture

Вход: цель/вопрос/событие.

Выход: нормализованный brief:
- decision to make;
- constraints;
- success criteria;
- required evidence;
- deadline/cost budget.

### 2. Design-doc first

Перед выполнением сложной работы агент должен подготовить design doc:
- proposed solution;
- assumptions;
- alternatives considered;
- risks;
- expected evidence;
- plan of execution;
- how result will be verified.

Это снижает риск “агент сразу пошёл делать не то”.

### 3. Parallel alternatives

Для важных решений запускать несколько независимых агентов:
- positive case / opportunity hunter;
- negative case / red team;
- implementation planner;
- market/customer evaluator;
- technical feasibility evaluator;
- verification/research agent.

### 4. Adversarial comparison

Верхний уровень сравнивает outputs:
- где агенты согласны;
- где противоречат;
- какие предположения не проверены;
- какие evidence links сильные/слабые;
- какой вариант максимизирует `(Impact × Confidence gain × Safety) / Cost`.

### 5. Verification gate

Нельзя принимать важный вывод без gate:
- source/evidence check;
- cost/risk check;
- spec compliance check;
- “what would make this false?” check;
- next experiment definition.

### 6. Decision and memory

Результат фиксируется как:
- decision;
- experiment;
- rejected alternatives;
- open questions;
- reusable workflow/skill if процесс повторяемый.

## Suggested initial roles

- **Strategist** — формирует decision brief и критерии выбора.
- **Opportunity Scout** — ищет сильные рыночные/технологические возможности.
- **Red Team** — ищет причины, почему идея не сработает.
- **Customer Discovery Agent** — формирует ICP, интервью, pricing hypotheses.
- **Technical Architect** — оценивает реализуемость и ограничения.
- **Build Agent** — Codex/Claude Code/OpenCode для реализации.
- **Verifier** — проверяет факты, ссылки, claims и соответствие задаче.
- **Synthesis Judge** — сравнивает outputs и формирует решение.

## Operating principle

Не “один умный агент всё решил”, а **композиция специализированных агентов + строгие gates + память решений**.

## Open architecture questions

1. Насколько верхний уровень должен быть полностью автоматическим, а где нужен human approval?
2. Какие решения требуют 2+ независимых агентов?
3. Какие артефакты стандартизировать первыми: design doc, scorecard, experiment brief, decision memo?
4. Как измерять качество агентов и заменять слабых?
5. Как хранить outputs: Obsidian, git, kanban, session DB, отдельная база?
