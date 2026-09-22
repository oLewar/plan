# Indexed action space

## Definition (working)

A browser-agent **policy** where each observation is a **numbered table of live elements**, and the model may only pick:

1. an **operation** from a closed set (`CLICK`, `TYPE_TEXT`, `SELECT`, `SCROLL_*`, `WAIT`, `DONE`, `BLOCKED`);
2. a **target index** drawn from elements that actually support that operation.

Text generation is a **side path**: a small LLM runs only if the chosen operation is `TYPE_TEXT`. The executor maps indices back to **code-owned DOM node ids**. Model output never becomes CSS selectors, coordinates, shell, or JavaScript.

Canonical public case in this vault: [[wiki/sources/jev-ultrafast]] (TypeSafe Jev + Browser Harness CDP). TypeSafe the product is **not** ingested.

## Mechanism (from Jev `agent.py` + `model.py` + `docs/design.md`)

```
page → snapshot.js (one call, WeakMap identities)
    → TypeSafe one request: operation + speculative target heads
    → execute only the matching head
    → if TYPE_TEXT: helper JSON {text} → CDP insertText
DONE is not proof; an independent predicate checks the page
```

| This is | This is not |
|---|---|
| Finite choice over observed nodes | Free Python / raw CDP from the policy model |
| One network round-trip for op+target | Serial «what then where» calls |
| Independent verify of the *page* | Trusting the model's DONE token |
| A policy on CDP | The CDP harness itself ([[wiki/concepts/self-healing-cdp-harness]]) |

## Contrast

| | Indexed action space (Jev) | Self-healing CDP harness | Continual harness |
|---|---|---|---|
| Model emits | Op + index (+ optional text JSON) | Python against helpers | REPL / `/refine` writes |
| Who executes | Code, with occlusion/freshness guards | Agent-written Python + core helpers | The agent loop |
| Proof | Separate checker | Host agent / human | Eval / author claims |
| Sits on | Browser Harness | Chrome CDP | IPython / workers |

Not a fifth harness axis. Not a replacement for Hermes `browser_exec`.

Status of «7.1 s Flights is a general browser SLA»: **Refuted** as a general claim (author: 3 pairs, one task, p = 0.25). Status of «model cannot emit selectors in this codebase»: **Confirmed** at `browser.py` / AGENTS.md depth (executor uses `window.__jevFast.nodes.get`).

## Causal map

| Cause | Effect |
|---|---|
| Treating DONE as success | False complete; flights example forbids this |
| Prepared field strings in the policy | Demo is no longer «one goal»; older prepared recording is a different artifact |
| Invalidating on every DOM mutation | Protocol-call explosion (author: 1092 → 101 after snapshot+scoped guards) |
| Helper JSON with commentary | Executor rejects; no type |
| Shadow/iframe/canvas task | MVP cannot proceed → BLOCKED is honest, not a model failure |
| Shared Chrome profile | Side effects / cookies of the user, same as the underlying harness |

## Why it matters for `pro/plan`

- Causal hygiene: **choice ≠ generation**. Bound the action space when the failure mode is hallucinated selectors ([[wiki/concepts/causal-analysis]]).
- Efficiency: skip pixels in the default loop; pay a text LLM only for fields ([[wiki/concepts/efficiency-metric]]).
- Honest steal: independent DONE check + «no selectors from the model» — without standing up TypeSafe or pinning `browser-harness==0.1.13` on this host.
- The same *closed question + code owns workflow* pattern shows up outside the browser: compaction, MCP tools, Codex routing, desktop AX, games, LP gates. Catalog: [[wiki/sources/jev-usage-examples]]. Those are judgment backends, not a fifth harness axis.

## Related

- Source: [[wiki/sources/jev-ultrafast]]
- Examples: [[wiki/sources/jev-usage-examples]]
- Runtime it requires: [[wiki/sources/browser-harness]], [[wiki/concepts/self-healing-cdp-harness]]
- Entity: [[wiki/entities/browser-use]]
- Tool: [[10_Reference/tools/jev-ultrafast]]
- Adjacent: [[wiki/concepts/playbook-routed-agent-mode]] (verbatim steps ≠ typed ops), [[wiki/concepts/everything-is-a-plugin]]

## Sources

- [[wiki/sources/jev-ultrafast]]
- [[wiki/sources/jev-usage-examples]]
