# LLM Wiki (Karpathy gist)

Source file: `raw/llm-wiki.md`
Original: https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f

## Summary
Ключевая идея: вместо одноразового RAG строить и поддерживать persistent interlinked wiki, которую LLM инкрементально обновляет при поступлении новых источников.

## Core principles extracted
- Wiki — компаундящийся артефакт, а не временный ответ.
- 3 слоя: raw sources, wiki, schema.
- Три режима операций: ingest, query, lint.
- `index.md` и `log.md` — обязательная навигация и история эволюции.
- Query-ответы могут становиться новыми wiki-страницами.

## Implications for `pro/plan`
1. `raw/` фиксируем как immutable.
2. Нормализованная структура `wiki/` обязательна.
3. Вводим AGENTS.md как операционную спецификацию.
4. Фиксируем регулярный lint для предотвращения деградации базы.

## Sources
- `[[raw/llm-wiki]]`
