# Efficiency metric

## Definition
Ключевая метрика: эффективность = максимум ценности при минимуме времени, риска и когнитивной перегрузки.

## Practical scoring
Оцениваем каждый шаг по 1..5:
- Impact (влияние на цель)
- Confidence gain (уменьшение неопределённости)
- Safety (контроль риска)
- Cost (время/сложность)

Приоритет:
`Priority = (Impact × Confidence gain × Safety) / Cost`

## Decision rule
При прочих равных делать шаг с более высоким Priority.

## Related signals (from later sources)
- **Payment / revenue** as high-confidence impact signal for product experiments ([[wiki/sources/fireside-chat-arman-suleimenov-2026-08-07]], [[wiki/entities/nfactorial-school]]).
- **Asset fit** raises expected efficiency: prefer ideas that reuse existing audience/community/domain edge ([[wiki/concepts/idea-as-function-of-assets]]).
- **Barbell allocation** of learning time: frontier tools + timeless principles, skip mid-noise ([[wiki/concepts/barbell-strategy]]).
- **HITL GTM**: cut 5h/day inbox grind via hourly drafts, keep human send (trust/safety stays in the denominator) ([[wiki/sources/anthropic-bd-claude-cowork]], [[wiki/concepts/human-in-the-loop-gtm]]).
- **Memory write-gate**: cheap local ASI06 check (AMG claims µs, no API) keeps Safety from collapsing when agents persist notes/goals ([[wiki/sources/owasp-agent-memory-guard]], [[wiki/concepts/memory-poisoning]]).
- **Plugin composition vs fork**: swapping a capability provider (sandbox/FS/LLM) is cheaper than maintaining a privileged loop fork — *if* unload/effects are real ([[wiki/sources/deepseek-harness]], [[wiki/concepts/everything-is-a-plugin]]).
- **Playbook-routed mode**: copying named steps verbatim is cheap insurance against silent skip of evidence gates; false «done» is the expensive failure ([[wiki/sources/pstack]], [[wiki/concepts/playbook-routed-agent-mode]]).
- **Runtime vs viewer**: one blocked-sidebar glance is cheaper than polling terminals; false `blocked` that auto-answers is the expensive failure ([[wiki/sources/herdr]], [[wiki/concepts/agent-runtime-multiplexer]]).
- **Continual harness**: cheap to persist a lesson from the trajectory; expensive if `/refine` writes an ungated cheat/poison into next-turn memory ([[wiki/sources/prime-agent]], [[wiki/concepts/continual-harness]]).
- **Composed error**: чинить не тот член (optimizer vs capacity vs data) = высокий Cost при нулевом Confidence gain ([[wiki/sources/mathematical-introduction-to-deep-learning]], [[wiki/concepts/composed-error-analysis]]).
- **SSD KV restore vs recompute**: cheap on prefix hit after restart; expensive if kernels were never built (silent 30× claim on GLM-5.2) ([[wiki/sources/omlx]], [[wiki/concepts/tiered-kv-cache]]).
- **Fail-closed diagram vs Mermaid loop**: one validated HTML + share card is cheap; a lying architecture slide is expensive causal noise ([[wiki/sources/archify]], [[wiki/concepts/typed-ir-artifact-delivery]]).
- **Offensive MCP broker**: README 24× scan tables look high-Impact; unauthenticated `shell=True` on `0.0.0.0` drives Safety→0 on a shared host ([[wiki/sources/hexstrike-ai]], [[wiki/concepts/mcp-tool-broker]]).
- **Trigram index vs scan**: cheap on large selective queries after `serve`; expensive if you pay TCP delivery on tens of thousands of matches, or wait on a cold empty index ([[wiki/sources/tgrep]], [[wiki/concepts/trigram-index-search]]).
- **Git-native experiment tree**: cheap to freeze a measured baseline and stack children; expensive if you rewrite the node that produced the number, or infer from status without logs ([[wiki/sources/openresearch]], [[wiki/concepts/git-native-experiment-tree]]).
- **CDP helper lane**: AX-tree click is cheaper than screenshot-only computer-use; a second local daemon for sequential work is the expensive Allow-prompt ([[wiki/sources/browser-harness]], [[wiki/concepts/self-healing-cdp-harness]]).
- **Indexed ops**: one TypeSafe round-trip + text LLM only on TYPE_TEXT is cheap vs serial plan-then-click; treating 7.1 s as a SLA is expensive noise ([[wiki/sources/jev-ultrafast]], [[wiki/concepts/indexed-action-space]]). Other Jev backends (compaction, Canny done-gate) are cheaper process-borrows than standing up TypeSafe ([[wiki/sources/jev-usage-examples]]). A local System One ranker (CLM) is cheaper than hosted Jev only when the candidate list is already the decision and the encoder is warm; a shielded survival rate is not that saving ([[wiki/sources/clm]], [[wiki/concepts/contrastive-action-ranker]]).
- **Named-fallacy table**: cheaper than unscoped «проверь текст»; inventing facts in fix-mode is the expensive material error ([[wiki/sources/logika]], [[wiki/concepts/formal-logic-skill]]).
- **Regularized harness search**: cheap to reject a within-noise or leaky harness diff before another full eval; expensive if the loop is pointed at SOUL/memories (that is the overfit the critic exists to catch) ([[wiki/sources/rrsi]], [[wiki/concepts/regularized-harness-search]]).
- **NumPy paper toy**: cheap to see one op (attention, gate, skip) on synthetic data; expensive to treat "30/30 files" as 30 reproductions, or to port all 30 before reading the 6 that update weights ([[wiki/sources/sutskever-30-implementations]], [[wiki/concepts/numpy-paper-toy]]).

## Sources
- `[[wiki/sources/llm-wiki-gist]]`
- `[[wiki/sources/fireside-chat-arman-suleimenov-2026-08-07]]`
- `[[wiki/sources/anthropic-bd-claude-cowork]]`
- `[[wiki/sources/owasp-agent-memory-guard]]`
- `[[wiki/sources/deepseek-harness]]`
- `[[wiki/sources/pstack]]`
- `[[wiki/sources/herdr]]`
- `[[wiki/sources/prime-agent]]`
- `[[wiki/sources/mathematical-introduction-to-deep-learning]]`
- `[[wiki/sources/omlx]]`
- `[[wiki/sources/archify]]`
- `[[wiki/sources/hexstrike-ai]]`
- `[[wiki/sources/tgrep]]`
- `[[wiki/sources/openresearch]]`
- `[[wiki/sources/browser-harness]]`
- `[[wiki/sources/jev-ultrafast]]`
- `[[wiki/sources/jev-usage-examples]]`
- `[[wiki/sources/logika]]`
