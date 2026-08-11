# Matt Pocock Skills

Composable agent skills for real engineering (alignment, domain language, TDD, architecture) by Matt Pocock.

- Full wiki source note: [[wiki/sources/mattpocock-skills|mattpocock-skills]]
- GitHub: https://github.com/mattpocock/skills
- README: https://github.com/mattpocock/skills/blob/main/README.md
- Homepage: https://aihero.dev/skills
- Catalog: https://skills.sh/mattpocock/skills
- License: MIT

## What it is

Small, editable skill packages for Claude Code / Codex / other agents. Positioned against heavy process frameworks (GSD, BMAD, Spec-Kit): keep control, compose practices, fix common agent failure modes (misalignment, verbosity, blind coding, design entropy).

## Install (from README)

```bash
# Claude Code managed plugin
claude plugins install mattpocock-skills

# Editable install (Codex / others / tinkerers)
npx skills@latest add mattpocock/skills
```

Then run once per repo: `/setup-matt-pocock-skills`.

Do not install plugin + editable copy together (duplicates every skill).

## High-value skills

| Skill | Role |
|---|---|
| `/grill-me` / `/grill-with-docs` | Alignment interview; docs path also builds `CONTEXT.md` + ADRs |
| `/tdd` | Red-green-refactor |
| `/diagnosing-bugs` | Gated diagnosis loop |
| `/to-spec` / `/to-tickets` / `/implement` | Spec → tickets → build with review |
| `/improve-codebase-architecture` | Deep-module survey (HTML report) |
| `/code-review` | Standards × Spec parallel review |
| `/wayfinder` | Multi-session decision map on issue tracker |

## Hermes / Chappy

See [[wiki/sources/mattpocock-skills|source page]] for integration options. At ingest: research/reference only — not installed into Hermes profile.
