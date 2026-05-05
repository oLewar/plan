---
title: "Machinelearning"
source: "https://t.me/s/ai_machinelearning_big_data/9884"
author:
published: 0:07
created: 2026-04-14
description: "nthropic объяснил** [регрессию Claude Code"
tags:
  - "clippings"
---
[Machinelearning](https://t.me/ai_machinelearning_big_data)

***📌*** **Anthropic объяснил** [регрессию Claude Code](https://t.me/ai_machinelearning_big_data/9866) **и предложил обходные пути.**  
  
Инженер из AMD опубликовал на GitHub [подробный разбор](https://github.com/anthropics/claude-code/issues/42796) деградации Claude Code на сложных задачах, начавшейся в феврале. Автор сгенерировал отчет силами Opus 4.6, проанализировав 17 тыс. блоков размышлений и 234 тыс. вызовов инструментов в 6 852 локальных сессиях.  
  
Главная метрика - отношение чтений файлов к правкам упала с **6,6 до 2,0**. Иначе говоря, модель почти перестала изучать код перед его модификацией: доля правок без предварительного чтения выросла с **6,2% до 33,7%**.  
  
Параллельно был зафиксировал рост зацикливаний (с 8,2 до 21,0 на тысячу вызовов), удвоение использования полной перезаписи файлов вместо точечных правок и вспышку поведенческих симптомов (уклонение от ответственности, преждевременные остановки и склонность к простейшему решению).  
  
Специальный stop-hook, ловящий такие фразы, сработал 173 раза за 17 дней после 8 марта, против нуля за весь предыдущий период.  
  
Автор связал регрессию с заголовком `redact-thinking-2026-02-12`, после появление которого содержимое thinking-блоков перестало приходить клиенту.  
  
Борис Черный, глава команды Claude Code [ответил](https://news.ycombinator.com/item?id=47664442) на Hacker News:  
  

> Заголовок убирает саммари размышлений из интерфейса, чтобы не гонять их по сети ради снижения латентности, но не трогает ни сам ризонинг, ни бюджеты на него.

  
  
Локальный анализ транскриптов поэтому и видит пустые блоки и делает неверный вывод об отсутствии мышления. Если надо, то вернуть отображение можно опцией `showThinkingSummaries:true` в `settings.json`.  
  
***🟡*** **Реальных изменений, влияющих на глубину рассуждений, было два:**  
  

> 9 февраля вместе с Opus 4.6 включили adaptive thinking - модель сама выбирает длину размышлений вместо фиксированного бюджета.  
>   
> 3 марта дефолтный уровень усилий для Opus 4.6 подняли до medium (effort=85) как компромисс между интеллектом, латентностью и стоимостью.

  
  
В ответ на гипотезу о том, что виноват свежий 1M-контекст и работа без `/compact` после 200k токенов, Борис предложил решения, которыми можно вернуть прежнее поведение:  
  
 <video src="https://cdn4.telesco.pe/file/ad96c0e109.webm?token=kLu8sYkvIR8w18MDBdleN-Reu3Dwx3eRNEuUNKm42LfXlGLayEYANXKCfe4wnOhVSD28-Eby2Xg0VKL-DNZYLqBV0ER1IwPMv3j06r7HXKhbmfSYQLOI0e_XHIJY17207bKZPmixi6xp06iErcl-U9t7hQh--buLq8GjJ2XcZzdD6y8wobHUuDsXmifTA7PGLfphavFQOy3XX9t_EdkeItEznonhm3pcLRkKgRphLsvPpVxILw4P38-RQgrC4fwpTrgk6c_LzxnZZ-l8_smqVkGrbt3jat6DhMztwfzMAZqvmGLyrbjEsU_y3S1tQuHCZ5AJ3ADoD3spLm62VcbXQw" width="100%" height="100%" controls=""><img src="https://cdn4.telesco.pe/file/aETPJKYd_yTAYWR9DvMfxaZfl-xHnRgEyFOabjjtbfdx_gWkvnmPefNN-WMbIjl1Vqq0uXKf40Rai35qIyMRXl_d5Jldr48_pB4vbTMigoqGwZhzAuFUT9dQpvEiCgFuej6CNGikvZ8UQlbZsJuJZPj-tCcp-ysDDtl5CBN4-vdFSj0CQ2o_7oH068icp9R_U-fkLH9oZjPEb8ibJPBxZG-nXPmGyj3ZKUakhEDktZWziiUG157mBvff9aLz_3SysHCHxwSGOUyxA9VtP48mrnLIYTJR79AzFt6rN5tzWLJq1DgKZMcmGG8-Gqe-hwXfjyYxGkNKUrIhNauJ2Xg25Q"></video> ***🟢*** `/effort high` или `/effort max` - поднять максимальный бюджет thinking-токенов на задачу;  
  
 <video src="https://cdn4.telesco.pe/file/ad96c0e109.webm?token=kLu8sYkvIR8w18MDBdleN-Reu3Dwx3eRNEuUNKm42LfXlGLayEYANXKCfe4wnOhVSD28-Eby2Xg0VKL-DNZYLqBV0ER1IwPMv3j06r7HXKhbmfSYQLOI0e_XHIJY17207bKZPmixi6xp06iErcl-U9t7hQh--buLq8GjJ2XcZzdD6y8wobHUuDsXmifTA7PGLfphavFQOy3XX9t_EdkeItEznonhm3pcLRkKgRphLsvPpVxILw4P38-RQgrC4fwpTrgk6c_LzxnZZ-l8_smqVkGrbt3jat6DhMztwfzMAZqvmGLyrbjEsU_y3S1tQuHCZ5AJ3ADoD3spLm62VcbXQw" width="100%" height="100%" controls=""><img src="https://cdn4.telesco.pe/file/aETPJKYd_yTAYWR9DvMfxaZfl-xHnRgEyFOabjjtbfdx_gWkvnmPefNN-WMbIjl1Vqq0uXKf40Rai35qIyMRXl_d5Jldr48_pB4vbTMigoqGwZhzAuFUT9dQpvEiCgFuej6CNGikvZ8UQlbZsJuJZPj-tCcp-ysDDtl5CBN4-vdFSj0CQ2o_7oH068icp9R_U-fkLH9oZjPEb8ibJPBxZG-nXPmGyj3ZKUakhEDktZWziiUG157mBvff9aLz_3SysHCHxwSGOUyxA9VtP48mrnLIYTJR79AzFt6rN5tzWLJq1DgKZMcmGG8-Gqe-hwXfjyYxGkNKUrIhNauJ2Xg25Q"></video> ***🟢*** `CLAUDE_CODE_AUTO_COMPACT_WINDOW=400000` - принудительно укоротить рабочее окно контекста.  
  
 <video src="https://cdn4.telesco.pe/file/ad96c0e109.webm?token=kLu8sYkvIR8w18MDBdleN-Reu3Dwx3eRNEuUNKm42LfXlGLayEYANXKCfe4wnOhVSD28-Eby2Xg0VKL-DNZYLqBV0ER1IwPMv3j06r7HXKhbmfSYQLOI0e_XHIJY17207bKZPmixi6xp06iErcl-U9t7hQh--buLq8GjJ2XcZzdD6y8wobHUuDsXmifTA7PGLfphavFQOy3XX9t_EdkeItEznonhm3pcLRkKgRphLsvPpVxILw4P38-RQgrC4fwpTrgk6c_LzxnZZ-l8_smqVkGrbt3jat6DhMztwfzMAZqvmGLyrbjEsU_y3S1tQuHCZ5AJ3ADoD3spLm62VcbXQw" width="100%" height="100%" controls=""><img src="https://cdn4.telesco.pe/file/aETPJKYd_yTAYWR9DvMfxaZfl-xHnRgEyFOabjjtbfdx_gWkvnmPefNN-WMbIjl1Vqq0uXKf40Rai35qIyMRXl_d5Jldr48_pB4vbTMigoqGwZhzAuFUT9dQpvEiCgFuej6CNGikvZ8UQlbZsJuJZPj-tCcp-ysDDtl5CBN4-vdFSj0CQ2o_7oH068icp9R_U-fkLH9oZjPEb8ibJPBxZG-nXPmGyj3ZKUakhEDktZWziiUG157mBvff9aLz_3SysHCHxwSGOUyxA9VtP48mrnLIYTJR79AzFt6rN5tzWLJq1DgKZMcmGG8-Gqe-hwXfjyYxGkNKUrIhNauJ2Xg25Q"></video> ***🟢*** `CLAUDE_CODE_SIMPLE=1` - упрощенный режим для проверки гипотезы об интерференции системного промпта.  
  
Дополнительно есть `CLAUDE_CODE_DISABLE_ADAPTIVE_THINKING=1`, он отключает адаптивный режим и возвращает фиксированный бюджет рассуждений.  
  
***🟡*** **Расследование бага продолжается командой Claude Code.**  
  

> Борис также заверил, что Anthropic протестирует включение high effort по умолчанию для тарифов Teams и Enterprise.  
>   
> Это приведет к большему расходу токенов и росту латентности, но даст гарантированную глубину рассуждений.

  
  
[@ai\_machinelearning\_big\_data](https://t.me/ai_machinelearning_big_data)  
  
[#news](https://t.me/s/ai_machinelearning_big_data/9884?q=%23news) [#ai](https://t.me/s/ai_machinelearning_big_data/9884?q=%23ai) [#ml](https://t.me/s/ai_machinelearning_big_data/9884?q=%23ml)

Please open Telegram to view this post

[VIEW IN TELEGRAM](https://t.me/ai_machinelearning_big_data/9884)

April 14