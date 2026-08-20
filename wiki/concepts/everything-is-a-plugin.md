# Everything is a plugin

## Definition (working)

Product architecture where **the agent loop, tools, model adapter, session log, UI, and sandbox are the same kind of thing**: plugins that register reversible effects on a shared context. There is no privileged core to fork; you extend by mounting another plugin and (if needed) patching config rows by id.

Canonical public case in vault: [[wiki/sources/deepseek-harness]] on [Cordis](https://github.com/cordiverse/cordis).

## Mechanism (from DSH / Cordis)

```
empty tree
  → ordered bundles (distribution of config rows + code)
  → user/profile patches (replace a row by id, or insert)
  → running ctx: services, typed events, waterfalls
unload plugin → effects unwind (registrations dispose)
```

Capability **seam** = three roles, not one package:

1. Service Definition (interface)
2. Service Provider (impl: local FS, E2B, remote sandbox, …)
3. Consumer (usually a model-facing tool)

Swap the provider → Bash, PTY, LSP move with it.

**Model-visible ⟺ logged:** if the model saw it, the session log can reconstruct it. New model-visible input = new session event.

## Contrast

| Style | Core | Extend by |
|---|---|---|
| Privileged loop (typical coding CLI) | agent loop is the product | hooks / tools / skills around the loop |
| Plugin harness (DSH claim) | loop is a plugin | mount + patch; unload is defined |
| Hermes skills | skills/tools around a host loop | SKILL.md + tools; loop not user-replaceable |

Status of “loop is really replaceable in production”: **Hypothesis** until we run DSH and swap `dsh-agent-loop`.

## Causal map

| Cause | Effect |
|---|---|
| Registrations as effects | Unload is safe; no leftover listeners |
| Config rows addressable by id | User overlay without forking vendor bundles |
| Seam split (def/provider/consumer) | One sandbox swap moves a family of tools |
| Model-visible not logged | Replay/UI/fork diverge from what the model saw |
| Treating official packages as mandate | Misses DSH’s own CONTRIBUTING: community plugins are first-class |

## Why it matters for `pro/plan`

- 1M scaling requirement is an **independent harness** ([[25_Projects/1M_Strategy/Architecture]]), not a bigger chat.
- Same efficiency logic as vault: compose skills/cron/wiki rather than one mega-agent ([[wiki/concepts/efficiency-metric]]).
- Risk: preview + breaking changes — copying DSH APIs into Hermes now has high Cost / low Safety.

## Related

- Source: [[wiki/sources/deepseek-harness]]
- Entity: [[wiki/entities/deepseek]]
- Tool: [[10_Reference/tools/deepseek-harness]]
- Adjacent: [[wiki/concepts/high-agency]], [[wiki/concepts/barbell-strategy]] (frontier harness + timeless gates)

## Sources

- [[wiki/sources/deepseek-harness]]
