# Prompting codebase questions

## Назначение

Пример, как формулировать запросы к coding agent / Claude Code для исследования кодовой базы.

Главный паттерн: **задавать вопросы не только по текущим файлам, но и по связям, истории изменений, issues/PR и версиям релизов**. Хороший prompt направляет агента к конкретным артефактам: файлам, классам, git history, issue, PR, API, release version.

## Пример со скриншота

Источник: скриншот `img_fee5f763d589.jpg`, сохранённый из Telegram. OCR извлечён локально через tesseract; возможны мелкие ошибки распознавания.

```text
Use Claude Code to answer
questions about your codebase

Example prompts:

› How is @RoutingController.py used?

› How do I make a new @app/services/ValidationTemplateFactory?

› Why does recoverFromException take so many arguments? Look through git
history to answer

› Why did we fix issue #18363 by adding the if/else in @src/login.ts API?

› In which version did we release the new @api/ext/PreHooks.php API?
Look at PR #9383, then carefully verify which app versions were impacted

› What did I ship last week?
```

## Что делает эти промпты хорошими

- **Ссылаются на конкретные артефакты**: `@RoutingController.py`, `@src/login.ts`, `@api/ext/PreHooks.php`, PR/issue IDs.
- **Формулируют вопрос как исследование системы**, а не как просьбу угадать ответ.
- **Заставляют использовать историю**: git history, PR, issue, release versions.
- **Просят верификацию влияния**: какие версии были затронуты, зачем внесли изменение, что реально shipped.
- **Подходят для agentic codebase QA**: агент должен читать код, граф зависимостей, историю коммитов и метаданные репозитория.

## Шаблоны промптов

```text
How is @<file-or-symbol> used?
```

```text
How do I make a new @<component-or-service>?
```

```text
Why does <function-or-class> <look strange / take many args / have this branch>?
Look through git history to answer.
```

```text
Why did we fix issue #<issue-id> by <specific code change> in @<file>?
Check the issue, PR, code diff, and commit history.
```

```text
In which version did we release <feature/API/change>?
Look at PR #<pr-id>, then carefully verify which app versions were impacted.
```

```text
What did I ship <time period>?
Summarize merged PRs, commits, changed areas, and user-visible impact.
```

## Принцип

Для вопросов по кодовой базе хороший prompt должен указывать минимум один якорь:

- файл или символ;
- issue/PR/commit;
- временной диапазон;
- релизную версию;
- наблюдаемое странное поведение;
- ожидаемый формат ответа.

Без якоря агент будет делать общий обзор. С якорем он может построить трассу: **код → история → причина → последствия → проверенный вывод**.

## Связанные темы

- [[10_Reference/Agents/readme|Agents readme]]
- [[10_Reference/Agents/tools/review|Code review / repo intelligence tools]]
- [[10_Reference/Agents/tools/search_in_md|Search in markdown / qmd]]
