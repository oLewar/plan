# Self-hosted и privacy-first open-source tools

Короткий справочник инструментов, которые заменяют облачные/платные сервисы локальными или self-hosted решениями.

## Список инструментов

### LocalSend
- GitHub: [localsend/localsend](https://github.com/localsend/localsend)
- Категория: передача файлов между устройствами.
- Что решает: передача файлов между Windows, macOS, Linux, Android и iOS без регистрации и облака.
- Почему полезно: быстрый локальный обмен файлами в одной сети без зависимости от мессенджеров, AirDrop, облачных дисков и аккаунтов.

### yt-dlp
- GitHub: [yt-dlp/yt-dlp](https://github.com/yt-dlp/yt-dlp)
- Категория: скачивание видео и аудио.
- Что решает: загрузка видео/аудио с YouTube, Bilibili, Twitter/X и множества других сайтов.
- Почему полезно: универсальный CLI-инструмент для архивации, извлечения аудио, работы с субтитрами и подготовки материалов для локальной обработки.

### Stirling-PDF
- GitHub: [Stirling-Tools/Stirling-PDF](https://github.com/Stirling-Tools/Stirling-PDF)
- Категория: универсальный PDF-инструмент.
- Что решает: объединение, разделение, сжатие, конвертация в Word, добавление водяных знаков, OCR и другие PDF-операции.
- Почему полезно: self-hosted альтернатива набору PDF-функций Adobe без загрузки документов в сторонние облака.

### FreeTube
- GitHub: [FreeTubeApp/FreeTube](https://github.com/FreeTubeApp/FreeTube)
- Категория: десктопный YouTube-плеер.
- Что решает: просмотр YouTube без рекламы, слежки и аккаунта Google.
- Почему полезно: снижает трекинг и отвлечения, подходит для privacy-first потребления видео.

### Syncthing
- GitHub: [syncthing/syncthing](https://github.com/syncthing/syncthing)
- Категория: peer-to-peer синхронизация файлов.
- Что решает: прямая синхронизация файлов между устройствами без централизованного облака.
- Почему полезно: альтернатива Baidu Netdisk, iCloud и другим облачным дискам; данные не проходят через серверы третьих лиц.
- Важное уточнение: Syncthing использует защищённые TLS-соединения между устройствами; это не классический end-to-end cloud encryption, потому что нет облачного посредника, а доверие строится на идентификаторах устройств.

### Vaultwarden
- GitHub: [dani-garcia/vaultwarden](https://github.com/dani-garcia/vaultwarden)
- Категория: self-hosted менеджер паролей, совместимый с Bitwarden-клиентами.
- Что решает: хранение паролей и секретов на своём сервере вместо подписки на 1Password/LastPass.
- Почему полезно: контроль над данными, совместимость с привычными Bitwarden-приложениями, низкие требования к ресурсам.
- Риск: требует аккуратной настройки HTTPS, резервных копий, обновлений и защиты сервера.

### Immich
- GitHub: [immich-app/immich](https://github.com/immich-app/immich)
- Категория: self-hosted фото/видео библиотека.
- Что решает: альтернатива Google Фото: автоматический backup с телефона, распознавание лиц, поиск и AI-функции.
- Почему полезно: контроль над семейным фотоархивом и снижение зависимости от ежемесячной аренды облачного хранилища.
- Риск: фотоархив критичен, поэтому обязательны отдельные резервные копии; Immich активно развивается, перед обновлениями стоит читать release notes.

### AdGuard Home
- GitHub: [AdguardTeam/AdGuardHome](https://github.com/AdguardTeam/AdGuardHome)
- Категория: DNS-level блокировка рекламы и трекеров.
- Что решает: блокировка рекламы на уровне сети/роутера для всех устройств, включая смартфоны и smart TV.
- Почему полезно: единая точка контроля рекламы, трекинга и вредных доменов без настройки каждого устройства отдельно.

### Jellyfin
- GitHub: [jellyfin/jellyfin](https://github.com/jellyfin/jellyfin)
- Категория: self-hosted медиасервер.
- Что решает: личный Netflix для фильмов, сериалов, музыки и другого медиа.
- Почему полезно: локальная медиатека, стриминг на разные устройства, отсутствие ежемесячных платежей платформам.

### Uptime Kuma
- GitHub: [louislam/uptime-kuma](https://github.com/louislam/uptime-kuma)
- Категория: мониторинг доступности сервисов.
- Что решает: следит за сайтами, API, домашними/self-hosted сервисами и отправляет уведомления о сбоях.
- Почему полезно: простая панель мониторинга для личной инфраструктуры и проектов.

## Паттерн применения

Эти инструменты относятся к стратегии **local-first / self-hosted / privacy-first**:

- заменить арендованные облачные сервисы собственным контролируемым стеком;
- снизить зависимость от аккаунтов, рекламы, трекинга и vendor lock-in;
- повысить автономность личной инфраструктуры;
- принять операционные обязанности: обновления, backup, мониторинг и безопасность.

## Быстрый приоритет внедрения

1. **Uptime Kuma** — поставить рано, чтобы видеть состояние остальных self-hosted сервисов.
2. **AdGuard Home** — быстрый сетевой эффект для всех домашних устройств.
3. **Syncthing / LocalSend** — закрыть обмен и синхронизацию файлов.
4. **Vaultwarden** — только после настройки backup, HTTPS и мониторинга.
5. **Immich / Jellyfin / Stirling-PDF** — по мере появления конкретных задач и достаточного диска.
6. **yt-dlp / FreeTube** — как локальные рабочие инструменты для видео и контента.

## Sources

- [LocalSend](https://github.com/localsend/localsend)
- [yt-dlp](https://github.com/yt-dlp/yt-dlp)
- [Stirling-PDF](https://github.com/Stirling-Tools/Stirling-PDF)
- [FreeTube](https://github.com/FreeTubeApp/FreeTube)
- [Syncthing](https://github.com/syncthing/syncthing)
- [Vaultwarden](https://github.com/dani-garcia/vaultwarden)
- [Immich](https://github.com/immich-app/immich)
- [AdGuard Home](https://github.com/AdguardTeam/AdGuardHome)
- [Jellyfin](https://github.com/jellyfin/jellyfin)
- [Uptime Kuma](https://github.com/louislam/uptime-kuma)
