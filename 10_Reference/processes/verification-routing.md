# Verification & Routing Process

Цель: одинаково и прозрачно решать, куда идёт информация:
- `10_Reference`
- `40_Research`
- `50_Hypotheses`
- `60_Archive`

## 1) Verification checklist
Для каждого документа/инсайта проверить:
1. Источник проверяем и цитируем? (0/1)
2. Есть ли дубли в vault? (0/1)
3. Есть ли связь с текущими целями? (0/1)
4. Есть ли проверяемая причинно-следственная ценность? (0/1)
5. Есть ли риск/безопасностные ограничения? (0/1)

## 2) Scores

### Relevance Score (RS, 0..100)
`RS = 0.35*GoalFit + 0.25*Usage + 0.20*EvidenceQuality + 0.20*Recency`

- GoalFit (0..100): вклад в текущие цели.
- Usage (0..100): частота использования (ссылки/обращения в 30 дней).
- EvidenceQuality (0..100): качество источников и верификации.
- Recency (0..100): насколько свежи данные.

### Stability Score (SS, 0..100)
`SS = 0.50*Consensus + 0.30*Reproducibility + 0.20*ContradictionPenaltyInv`

- Consensus: согласованность с другими источниками.
- Reproducibility: можно ли воспроизвести/проверить вывод.
- ContradictionPenaltyInv: обратная величина противоречивости.

## 3) Routing rules

- **Reference (`10_Reference`)**: `RS >= 70` и `SS >= 70`.
- **Research (`40_Research`)**: `RS >= 50` и `SS < 70` (нужно доисследование).
- **Hypotheses (`50_Hypotheses`)**: `RS >= 50` и есть явная непроверенная причинная гипотеза.
- **Archive (`60_Archive`)**: `RS < 40` или `Usage < 20` в течение 30+ дней, либо superseded.

Пограничные случаи (`RS 40..69`) — weekly review.

## 4) Update cadence
- Daily: triage новых входящих материалов.
- Weekly: review пограничных кейсов + архивирование кандидатов.
- Monthly: пересчёт score для hot topics.

## 5) Metadata template (frontmatter)

```yaml
status: active | review | archived
zone: reference | research | hypothesis | archive
rs: 0
ss: 0
usage_30d: 0
last_verified: YYYY-MM-DD
sources_count: 0
supersedes: []
superseded_by: []
```

## 6) Proven patterns used
- **PARA**: Projects/Areas/Resources/Archives (ясное разделение активного и архивного).
- **Evergreen notes**: постоянное улучшение заметок вместо одноразовых конспектов.
- **Zettelkasten linking**: плотная сетка ссылок для discovery.
- **Johnny.Decimal**: дисциплина структуры и навигации.
