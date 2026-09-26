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
- **Trajectory → harness write**: `/refine` makes the *previous run* a cause of the *next prompt*; same loop stores tactics *and* exploits ([[wiki/concepts/continual-harness]]).
- **Three-term training error**: «модель плохая» может быть approximation (класс слишком узкий), optimization (не нашли параметр) или generalization (выборка ≠ распределение) — разные причины ([[wiki/concepts/composed-error-analysis]]).
- **Slow local LLM ≠ one cause**: missing Metal kernels (silent generic fallback), cold KV miss, or model not pinned — different fixes ([[wiki/concepts/tiered-kv-cache]]).
- **Pretty diagram ≠ true map**: invented edges, reach sold as blast radius, or `visual-check` sold as a pass are different lies; fail-closed IR delivery keeps last-good HTML ([[wiki/concepts/typed-ir-artifact-delivery]]).
- **MCP ≠ sandbox**: the cause of host RCE is a generic `execute_command` + bind/auth, not «the model has tools»; lookup tables branded as agents are a separate lie ([[wiki/concepts/mcp-tool-broker]]).
- **Empty grep ≠ missing symbol**: cold `tgrep serve`, incomplete on-disk index, membership-flag mismatch, 64 MiB cap, or an index-bypass flag are different causes ([[wiki/concepts/trigram-index-search]]).
- **Failed experiment ≠ one cause**: empty run (repair same node), answered-but-bad (freeze + child), status-without-log (not evidence), dirty uncommitted tree (never ran) ([[wiki/concepts/git-native-experiment-tree]]).
- **Browser failed ≠ one cause**: inspect-tick off, stale daemon, Snap Chromium, Cloud timeout, domain-skills never enabled ([[wiki/concepts/self-healing-cdp-harness]]).
- **DONE ≠ success**: the model's stop token is not the page predicate; independent checks own the claim ([[wiki/concepts/indexed-action-space]]).
- **Survived ≠ the model played**: a planner that writes Safe/Unsafe into the prompt plus a shield that replaces the argmax is a different cause from the ranker's own choice ([[wiki/concepts/contrastive-action-ranker]]).
- **Notebook exists ≠ the paper reproduced**: a file with the mechanism and no saved outputs is a map of the op, not a fit ([[wiki/concepts/numpy-paper-toy]]).
- **High score ≠ the fact was known**: the ranker only compares options the caller supplied; a shortlist can drop the right one before the softmax, and a displayed 1.0 can be rounding ([[wiki/concepts/supplied-option-ranker]]).
- **After X ≠ because of X**: post hoc / hidden premise / form-valid-with-false-premises are different errors ([[wiki/concepts/formal-logic-skill]]).
- **Harness improved ≠ one cause**: leakage (task ids), within-noise score bump, token-expensive real gain, and structural novelty inside the band are different accepts ([[wiki/concepts/regularized-harness-search]]).

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
