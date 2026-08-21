# pstack

Cursor plugin: rigorous agent workflows you can parallelize after one agent is trustworthy. Author: Lauren Tan (`poteto`).

- Full wiki source: [[wiki/sources/pstack]]
- Entity: [[wiki/entities/cursor]] / [[wiki/entities/lauren-tan]]
- Concept: [[wiki/concepts/playbook-routed-agent-mode]]
- GitHub: https://github.com/cursor/plugins/tree/main/pstack
- README: https://github.com/cursor/plugins/blob/main/pstack/README.md
- Guide: https://github.com/cursor/plugins/tree/main/pstack/docs/guide
- License: MIT
- Manifest version at ingest: **0.14.2** (2026-08-21)

## What it is

Sticky `/poteto-mode` matches a playbook (22 + shared `opening-a-pr`), copies steps verbatim, routes other skills, splits work by model strength, proves on the real app. Goal is **less, higher-quality code**, not max LoC.

## Install (Cursor only)

```text
/add-plugin pstack
/setup-pstack
/poteto-mode <goal + how you'll know it's done>
```

`/setup-pstack` writes `~/.cursor/rules/pstack-models.mdc` (always-apply). Missing lines keep skill defaults. `inherit-parent` / `auto` = parent chat model.

Do not also expect `/deslop` / `control-cli` / `control-ui` unless `cursor-team-kit` is installed.

## Defaults (public `/setup-pstack` template)

- specified code: **Sol** (`gpt-5.6-sol-max`)
- fast mechanical: **Grok** (`grok-4.6-fast-xhigh`)
- prose / judgment: **Fable** (`claude-fable-5-thinking-max`)
- panels: Fable / Sol / Grok / **Opus 5**

## High-value skills

| Skill | Role |
|---|---|
| `/poteto-mode` | Default entry; sticky router |
| `/setup-pstack` | Per-role models |
| `/how` `/why` `/teach` `/recall` | Understand before edit |
| `/architect` `/arena` `/swarm` `/interrogate` | Design + multi-model review |
| `/tdd` `/no-comments` `/unslop` | Build and clean |
| `/create-verification-skill` | Project-local prove-it-works harness |
| `/automate-me` | Mine transcripts into `<you>-mode` |

## Hermes / Chappy

See [[wiki/sources/pstack]] for integration options. At ingest: **reference only** — Cursor plugin runtime, not a Hermes skill pack. Fusion CLI remains explicit-request-only; do not import `never-block-on-the-human` onto Fusion or onto GTM send.
