# QMD setup and usage (`pro/plan`)

## Status
- Installed: `qmd 2.1.0`
- Collections:
  - `plan-wiki` → `/root/pro/plan/wiki`
  - `plan-raw` → `/root/pro/plan/raw`
- Contexts:
  - `qmd://plan-wiki/` = `Curated wiki layer with synthesized knowledge`
  - `qmd://plan-raw/` = `Immutable raw sources layer`

## Important note
QMD работает на CPU (без GPU ускорения), потому что в окружении нет Vulkan/CUDA. Это нормально, но `embed`/`query` будут медленнее.

## Verification routing integration

Перед маршрутизацией новых материалов применять процесс:
- [[processes/verification-routing]]

QMD используем для сигнала Usage/Recency:
- `qmd search ... --json` для оценки востребованности тем.
- `qmd ls <collection>` для контроля покрытия разделов.

## Daily commands

```bash
cd /root/pro/plan

# 1) Обновить индекс после изменений в markdown
qmd collection update plan-wiki
qmd collection update plan-raw

# 2) Обновить вектора для новых/изменённых документов
qmd embed

# 3) Поиск
qmd search "causal" -c plan-wiki -n 10
qmd search "harness" -c plan-raw -n 10

# 4) Гибридный поиск (лучше качество)
qmd query "какие подходы лучше для causal analysis" -n 10

# 5) Получить документ целиком
qmd get qmd://plan-wiki/concepts/causal-analysis.md --full
```

## Agent-friendly output

```bash
qmd search "efficiency" -c plan-wiki --json -n 10
qmd query "risk mitigation" --json -n 10
qmd search "orphan pages" --all --files --min-score 0.3
```

## Recommended process integration

1. После каждого ingest/query-цикла:
   - `qmd collection update plan-wiki`
   - `qmd collection update plan-raw`
2. Ежедневно (или при большом изменении источников):
   - `qmd embed`
3. Перед ответами на сложные вопросы:
   - `qmd query ...` + сохранение результатов в `wiki/analyses/`.

## Smoke test (already passed)
Команда:
```bash
qmd search "causal" -c plan-wiki -n 5 --json
```
вернула релевантные результаты, включая:
- `qmd://plan-wiki/concepts/causal-analysis.md`
- `qmd://plan-wiki/index.md`
- `qmd://plan-wiki/log.md`
