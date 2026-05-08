# GitHub Activity Monitor (без стягивания репозиториев)

## Цель
Проверять «живость» репозиториев по частоте коммитов и свежести последнего коммита **через GitHub API**, без `git clone`.

## Источники
- Watchlist: `40_Research/github-repos-list.md`
- Скрипт: `scripts/github_repo_activity.py`
- Отчёт: `40_Research/github-activity/latest.md`

## Как работает
1. Читает `owner/repo` из watchlist.
2. Для каждого репозитория запрашивает:
   - последний коммит (дата/sha/автор),
   - число коммитов за окно `N` дней (по умолчанию 30).
3. Считает активность (daily/weekly/monthly/stale).
4. Пишет markdown/JSON отчёты в vault.

## Команды

```bash
cd /root/pro/plan
python3 scripts/github_repo_activity.py \
  --input 40_Research/github-repos-list.md \
  --window-days 30 \
  --output-md 40_Research/github-activity/latest.md \
  --output-json 40_Research/github-activity/latest.json
```

## Токен (рекомендуется)
Для повышения лимитов GitHub API:
- экспортировать `GITHUB_TOKEN` в окружение.

Без токена тоже работает, но с более жёсткими rate limits.

## Интерпретация
- `daily`: >= 20 commits / 30d
- `weekly`: 4..19 commits / 30d
- `monthly`: 1..3 commits / 30d
- `stale`: 0 commits / 30d

## Использование в роутинге
Этот сигнал идёт в verification-routing как часть `Recency/Usage` для материалов, связанных с конкретным репозиторием.
