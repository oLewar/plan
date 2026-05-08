# Operating model for `pro/plan`

## Goal
Превратить репозиторий в живую систему исследований: накапливаем знания, связываем факты, принимаем решения по эффективности.

## Adopted structure
- `raw/` — неизменяемые источники.
- `wiki/` — curated knowledge graph в markdown.
- `AGENTS.md` — правила поведения агента и процессы ingest/query/lint.

## Process loop
1. Ingest new source.
2. Update linked wiki pages and synthesis.
3. Answer questions from wiki and сохранять ценные ответы обратно в wiki.
4. Run lint periodically.
5. Commit changes atomically to `main`.

## Expected benefits
- Меньше повторной "пересборки" знаний.
- Явное накопление причинно-следственных моделей.
- Повышение качества решений за счёт compounding-эффекта.

## Sources
- `[[wiki/sources/llm-wiki-gist]]`
