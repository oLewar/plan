# Skill supply chain (the tool description is the payload)

## Definition (working)

An agent does not only read the user's message. It also reads tool schemas, skill files, and plugin manifests, and then acts with whatever those files permit. A poisoned skill is a write into that second channel. The harm is not that the text is rude. The harm is that the agent treats it as instructions and the runtime treats the resulting call as authorized.

Working source: [[wiki/sources/awesome-agent-skills-security]], a curated list, not a primary paper. Their largest attack bucket (38 of 150, counted 2026-09-30) is tool poisoning and supply chain, ahead of prompt injection via tools (15). OWASP's Agentic Skills Top 10 (AST10, v1.0, 2026) is the standards entry that scopes this layer; AST01 (malicious skills) and AST02 (supply-chain compromise) are the ones the list marks critical. That rating is theirs.

```
what the agent will obey
        │
        ├─ user message            → prompt injection (the box people filter)
        ├─ tool schema / skill file → supply chain (loaded before the turn)
        ├─ another plugin's output → cross-plugin (one tool attacks the next)
        └─ a note written last turn → memory (ASI06; already a page here)
                 └─ a filter on the first row does not see the other three
```

## Why it matters for `pro/plan`

- [[wiki/concepts/memory-poisoning]] is the bottom row: a successful write becomes next turn's privileged input. This page is the two rows above it. Same shape, different file. A skill copied in from a README is a supply-chain write whether or not anyone called it an attack.
- [[wiki/concepts/causal-analysis]]: "the agent exfiltrated" does not say which row fired. A poisoned tool description, a cross-plugin handoff, and a jailbreak of the chat are three causes. The list existing does not tell you which one a given incident was.
- [[wiki/concepts/efficiency-metric]]: the cheap check is the source of the skill (who wrote the file, when it last changed) before it is installed. The expensive check is a benchmark suite after it is already loaded. This list's own contribution rule — open-source, commit in the last 6 months, no paywalled-only papers — is a source check, not a detection method.
- Not a claim that any listed attack works, or that any listed defense stops it. No linked paper was opened.

## Related

- Source: [[wiki/sources/awesome-agent-skills-security]]
- The memory row, already written: [[wiki/concepts/memory-poisoning]]
- Don't collapse the cause: [[wiki/concepts/causal-analysis]]
- Check the source before the suite: [[wiki/concepts/efficiency-metric]]
