# Causal analysis

## Purpose
Выявлять причинно-следственные связи между событиями так, чтобы решения были не реактивными, а системными.

## Working model
Для каждого важного события фиксируем:
- событие,
- предполагаемые причины,
- наблюдаемые эффекты,
- альтернативные объяснения,
- уровень уверенности.

## Confidence states
- `Hypothesis`
- `Confirmed`
- `Refuted`
- `Unknown`

## Minimal template
- Event:
- Candidate causes:
- Evidence:
- Counter-evidence:
- Downstream effects:
- Confidence:
- Next best question:

## Related patterns
- **Input→output framing** and task decomposition as everyday causal hygiene ([[wiki/sources/fireside-chat-arman-suleimenov-2026-08-07]]).
- **Willingness-to-pay** as causal evidence that a product reduces real pain (vs compliments).
- **Idea = f(assets)**: enabling causes of success often pre-exist in network/expertise, not in abstract ambition ([[wiki/concepts/idea-as-function-of-assets]]).
- **Usage-without-opportunity**: product already in use + no CRM opportunity is a higher-confidence outbound cause than a cold list ([[wiki/sources/anthropic-bd-claude-cowork]]).
- **Reject-reason ledger**: writing *why* a draft/CRM proposal failed is the causal feedback that stops the same error next cycle ([[wiki/concepts/human-in-the-loop-gtm]]).
- **Poisoned memory → next-turn privileged input**: the cause is a successful *write*, not the current prompt; reset does not break the chain ([[wiki/concepts/memory-poisoning]]).
- **Loop as plugin**: if the driver is a row in a patchable tree, “we use Claude Code / Hermes” is a *composition choice*, not an identity of the product ([[wiki/concepts/everything-is-a-plugin]]).
- **Silent skip of a named gate**: the cause of slop-ship is dropping `architect` / prove-it-works after reading a playbook, not «the model is dumb» ([[wiki/concepts/playbook-routed-agent-mode]]).
- **UI quit ≠ process death**: if the runtime owns PTYs, closing the TUI is not a cause of a stopped agent; if a manager app owns the process, it is ([[wiki/concepts/agent-runtime-multiplexer]]).

## Sources
- `[[wiki/sources/llm-wiki-gist]]`
- `[[wiki/sources/fireside-chat-arman-suleimenov-2026-08-07]]`
- `[[wiki/sources/anthropic-bd-claude-cowork]]`
- `[[wiki/sources/owasp-agent-memory-guard]]`
- `[[wiki/sources/deepseek-harness]]`
- `[[wiki/sources/pstack]]`
- `[[wiki/sources/herdr]]`
