# CloakBrowser

CloakBrowser — open-source stealth Chromium для browser automation, который заявляет source-level fingerprint patches и совместимость с Playwright/Puppeteer API.

- GitHub: [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser)
- Homepage: [cloakbrowser.dev](https://cloakbrowser.dev/)
- PyPI: `cloakbrowser`
- npm: `cloakbrowser`
- Docker: `cloakhq/cloakbrowser`
- License: MIT
- Категория: stealth browser / anti-bot browser automation / browser profile manager.

## Что решает

- Запуск автоматизированного Chromium так, чтобы он меньше выглядел как stock Playwright/headless browser.
- Drop-in replacement для Playwright/Puppeteer: часто достаточно заменить import и использовать похожий API.
- Browser Profile Manager как self-hosted альтернатива Multilogin, GoLogin и AdsPower: профили, fingerprint, proxies, persistent sessions, noVNC.

## Ключевые возможности из README

- Source-level C++ patches в Chromium: canvas, WebGL, audio, fonts, GPU, screen, WebRTC, network timing, automation signals, CDP input behavior.
- `humanize=True`: более человекоподобные mouse curves, keyboard timing и scroll patterns.
- Поддержка Python и JavaScript.
- Auto-download stealth Chromium binary при первом запуске.
- Proxy flags: HTTP/SOCKS5, `geoip=True`, timezone/locale matching, WebRTC IP spoofing.
- Persistent profiles через `launch_persistent_context()`.
- Docker smoke test:

```bash
docker run --rm cloakhq/cloakbrowser cloaktest
```

## Минимальные примеры

Python:

```python
from cloakbrowser import launch

browser = launch()
page = browser.new_page()
page.goto("https://example.com")
browser.close()
```

JavaScript:

```javascript
import { launch } from 'cloakbrowser';

const browser = await launch();
const page = await browser.newPage();
await page.goto('https://example.com');
await browser.close();
```

Для сайтов с anti-bot protection README рекомендует residential proxy и флаги:

```python
browser = launch(
    proxy="http://user:***@residential-proxy:port",
    geoip=True,
    headless=False,
    humanize=True,
)
```

## Browser Profile Manager

Self-hosted manager запускается так:

```bash
docker run -p 8080:8080 -v cloakprofiles:/data cloakhq/cloakbrowser-manager
```

После запуска открыть `http://localhost:8080`, создать profile и нажать Launch.

Смежный репозиторий: [CloakHQ/CloakBrowser-Manager](https://github.com/CloakHQ/CloakBrowser-Manager).

## Интеграция с Hermes / Chappy

Текущий статус: **в Hermes сейчас нет встроенной интеграции CloakBrowser**. Проверка показала:

- стандартный Hermes toolset `browser` включён, но это не CloakBrowser;
- в коде `/usr/local/lib/hermes-agent` нет упоминаний `CloakBrowser`, `CloakHQ`, `cloak`;
- в `/root/.hermes` нет конфигурации/плагина CloakBrowser.

### Варианты подключения

1. **Python tool/script поверх CloakBrowser**
   - Установить `cloakbrowser` в окружение Hermes.
   - Написать script/tool, который запускает CloakBrowser через Python API и выполняет ограниченные операции: открыть URL, снять screenshot, получить HTML/text, выполнить JS.
   - Плюс: проще всего для первых экспериментов.
   - Минус: это будет отдельный инструмент, а не замена встроенного Hermes browser toolset.

2. **CDP bridge**
   - Запустить CloakBrowser с `--remote-debugging-port=9242`:

```python
from cloakbrowser import launch_async
browser = await launch_async(args=["--remote-debugging-port=9242"])
```

   - Подключать к `http://127.0.0.1:9242` frameworks, которые умеют CDP.
   - По README: stealth fingerprint patches работают через CDP, но `humanize=True` — wrapper-level feature; для humanize при CDP нужны отдельные patching functions.
   - Потенциально это направление для интеграции с Hermes browser backend, если backend позволяет подключение к внешнему CDP endpoint.

3. **agent-aget CLI wrapper**
   - Репозиторий: [izzzzzi/agent-aget](https://github.com/izzzzzi/agent-aget).
   - `aget` — CLI для браузерных сценариев LLM-агентов: запускает управляемый CloakBrowser stealth Chromium, хранит локальные сессии и возвращает машинно-читаемый JSON.
   - Установка: `npm i -g agent-aget`; диагностика: `aget doctor`; установка/проверка браузера: `aget browser install`, `aget browser status`, `aget browser path`.
   - Базовый workflow: `aget open URL -n NAME` → сохранить `sid` → `aget page snapshot/read/click/fill/wait/get/scroll/screenshot -s SID` → `aget session close -s SID`.
   - Плюс: уже имеет agent-friendly JSON contract, refs `@e1`/`@i1`, batch-команды и session management. Это самый дешёвый путь для первого Hermes/Chappy эксперимента без написания собственного браузерного backend.
   - Минус: молодой проект; перед доверием нужно проверить установку, стабильность сессий, безопасность state dir, качество ошибок и совместимость с текущим Hermes execution environment.

4. **CLI/MCP wrapper вокруг aget или CloakBrowser**
   - Сделать Hermes custom tool/plugin или MCP server с командами вида `cloak_open`, `cloak_click`, `cloak_extract`, `cloak_screenshot`, которые внутри вызывают `aget` или Python CloakBrowser API.
   - Плюс: можно явно включать/выключать инструмент и ограничить сценарии.
   - Минус: больше разработки и тестов, но поверх `aget` объём работы меньше.

5. **CloakBrowser Manager как отдельный сервис**
   - Поднять `cloakhq/cloakbrowser-manager` в Docker.
   - Использовать его для профилей и ручного/полуавтоматического browser access через noVNC.
   - Подходит как первая инфраструктурная проверка, но не даёт полноценного Hermes tool integration автоматически.

## Риски и ограничения

- CloakBrowser не решает CAPTCHA, а пытается предотвращать их появление; README явно говорит, что CAPTCHA-solving и proxy rotation не встроены.
- Для антибот-сайтов часто нужен residential proxy; datacenter IP всё равно может блокироваться.
- Использование stealth/anti-detect браузеров может нарушать ToS сайтов. Нужна явная политика применения: свои сервисы, тестирование, разрешённый scraping, восстановление доступа к публичным материалам без обхода платного/закрытого доступа.
- Первый запуск скачивает кастомный Chromium binary (~200MB); это влияет на provisioning и backup/cache.
- Любая интеграция в Hermes должна иметь safety guardrails: домены, rate limits, запрет на credential stuffing/массовый обход защит, логирование действий.

## Быстрый вывод

Для Chappy самый дешёвый эксперимент: **не заменять встроенный browser toolset сразу**, а поставить `agent-aget` как CLI-адаптер к CloakBrowser и проверить его на 2–3 задачах, где стандартный Hermes browser упирается в bot detection или плохо держит сессию.

Если `aget` стабильно работает, следующий шаг — обернуть его в Hermes custom tool/plugin с ограниченным набором команд и guardrails. Если нет — вернуться к прямому Python CloakBrowser API или CDP/backend integration.

## Минимальный test plan для Chappy

1. Проверить установку:

```bash
npm i -g agent-aget
aget version
aget doctor
aget browser status || aget browser install
```

2. Проверить базовый JSON workflow:

```bash
aget open https://example.com -n smoke
aget page read -s SID --limit 40
aget page snapshot -s SID
aget page screenshot -s SID --path /tmp/aget-smoke.png
aget session close -s SID
```

3. Проверить проблемный сценарий, где обычный browser failed, например страницу с bot detection, но только в рамках разрешённого доступа и без обхода платного/закрытого контента.
4. Оценить: latency, стабильность sid, качество `page read`, качество refs, где хранятся профили/сессии, не протекают ли cookies/tokens в stdout/logs.

## Sources

- [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser)
- [CloakBrowser homepage](https://cloakbrowser.dev/)
- [CloakHQ/CloakBrowser-Manager](https://github.com/CloakHQ/CloakBrowser-Manager)
- [izzzzzi/agent-aget](https://github.com/izzzzzi/agent-aget)
