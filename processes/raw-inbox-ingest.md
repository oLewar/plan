# Raw Inbox Ingest

`raw/` — это только входящая свалка материалов.

## Контракт
- В `raw/` не допускаются вложенные папки.
- В `raw/` кладём новые файлы только в корень.
- Файлы из `raw/` периодически разбираются и переносятся во внешние разделы.

## Маршрутизация
- `40_Research/sources/agent-dev/`
- `40_Research/sources/finance/`
- `40_Research/sources/ml-research/`
- `10_Reference/sources/general/`

## Локализация изображений
Если в документах есть внешние image URL:
- скачивать в `assets/external/<host>/<hash>.<ext>`
- менять ссылки в markdown на локальные пути

## Автоматизация
Скрипт:
- `/root/.hermes/scripts/plan_raw_ingest.sh`

Запуск:
```bash
/root/.hermes/scripts/plan_raw_ingest.sh
```

Отчёт:
- `40_Research/sources/ingest-report-latest.md`
