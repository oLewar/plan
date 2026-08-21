# Matt Pocock Skills (Skills For Real Engineers)

## Bibliographic / source

| Field | Value |
|---|---|
| Title | **Skills For Real Engineers** |
| Author | Matt Pocock |
| Repo | [mattpocock/skills](https://github.com/mattpocock/skills) |
| README | [blob/main/README.md](https://github.com/mattpocock/skills/blob/main/README.md) |
| Homepage | https://aihero.dev/skills |
| skills.sh | https://skills.sh/mattpocock/skills |
| License | MIT |
| Stars (at ingest) | ~213k (GitHub API, 2026-08-11) |
| Language | Shell (skill packages / agent skill files) |
| Domain | agent skills, coding-agent workflows, engineering discipline |

## One-line purpose

Набор **маленьких, composable agent skills** для «real engineering» (alignment, domain language, TDD, architecture, triage) — не тяжёлые process-framework’и вроде GSD/BMAD/Spec-Kit, а редактируемые практики, которые агент и человек вызывают по задаче.

## Thesis (from README)

1. **Control over process frameworks** — frameworks, которые «владеют процессом», отнимают контроль и усложняют отладку; skills должны быть small / adaptable / composable.
2. **Главный failure mode = misalignment** — agent не понял, что нужно; fix = grilling session (`/grill-me`, `/grill-with-docs`).
3. **Shared language** — `CONTEXT.md` + ADRs сокращают verbosity, улучшают naming/navigation и экономят tokens.
4. **Feedback loops** — types, browser, tests; red-green-refactor (`/tdd`) и disciplined debug (`/diagnosing-bugs`).
5. **Design every day** — agents ускоряют entropy; skills вшивают заботу о deep modules / architecture (`/to-spec`, `/improve-codebase-architecture`).

## Install paths

Две философии (не ставить обе сразу — skills задублируются):

| Mode | How | Ownership |
|---|---|---|
| Claude Code plugin (managed, read-only updates) | `claude plugins install mattpocock-skills` или `/plugin install mattpocock-skills` | subscribe |
| Editable copy (Codex / others / tinkerers) | `npx skills@latest add mattpocock/skills` | fork/edit; update via `npx skills update` |

После установки: один раз на repo запустить **`/setup-matt-pocock-skills`** (issue tracker: GitHub / Linear / local files; triage labels; docs layout). Для installer path README требует включить skill `setup-matt-pocock-skills`.

## Skill inventory (repo tree at ingest)

**Engineering — user-invoked:** `ask-matt`, `grill-with-docs`, `triage`, `improve-codebase-architecture`, `setup-matt-pocock-skills`, `to-spec`, `to-tickets`, `implement`, `wayfinder`

**Engineering — model-invoked:** `prototype`, `diagnosing-bugs`, `research`, `tdd`, `domain-modeling`, `codebase-design`, `code-review`, `resolving-merge-conflicts`, `wizard`

**Productivity — user-invoked:** `grill-me`, `handoff`, `teach`, `to-questionnaire`, `wait-what`

**Productivity — model-invoked:** `grilling`, `writing-for-agents`

Также есть `skills/in-progress/*` и `skills/misc/*` (не все production-ready).

**Rule of composition (README):** user-invoked skills orchestrate; model-invoked hold reusable discipline. User-invoked may call model-invoked, but not another user-invoked.

## Why it matters for `pro/plan` / Hermes / Chappy

- Прямой сосед к локальной модели skills Hermes: portable `SKILL.md` packages vs managed plugins.
- Паттерны **grill → shared language → tickets/spec → implement+tdd → review** хорошо ложатся на autonomous coding (issues → worktrees → evidence gates).
- Концепты для переноса: grilling as alignment, `CONTEXT.md` as domain glossary, ADR capture, architecture survey cadence.
- Не путать с generic «agent skills» dump-репозиториями: здесь акцент на engineering fundamentals + control, не vibe-coding process takeover.
- Сосед по тезису «меньше slop, больше engineering»: [[wiki/sources/pstack]] (sticky playbook router on Cursor, not independently invoked skills).

## Status

- **Ingest source:** user link to README + raw README + GitHub API metadata (2026-08-11).
- **Depth:** README-level summary + skill inventory; individual skill deep-dives not yet done.
- **Hermes install status:** not installed as a managed plugin on this host at ingest time (research note only).
- **Prior mention:** bare URL already listed in `10_Reference/Agents/tools/ref.md`.

## Possible Hermes/Chappy integration paths

1. **Manual port** — copy selected skills (grill-me, tdd, diagnosing-bugs, code-review) into Hermes skill format under `~/.hermes/skills/` after adapting triggers/tool names.
2. **skills.sh installer** — if Hermes/Codex skill layout compatible with `npx skills add`, use editable install into a project worktree (not global Hermes profile by default).
3. **Process borrow only** — keep as wiki reference; apply grill/shared-language/TDD patterns inside existing Fusion/worktree workflows without importing files.

## Next (optional)

- [ ] Deep notes on `grill-with-docs` + `CONTEXT.md` pattern
- [ ] Compare vs local Hermes skills (writing-plans, subagent-driven-development, code-quality-workflows)
- [ ] Decide whether any skill should be ported into Chappy snapshot skills

## Sources / provenance

- README: https://github.com/mattpocock/skills/blob/main/README.md
- Raw: https://raw.githubusercontent.com/mattpocock/skills/main/README.md
- Repo: https://github.com/mattpocock/skills
- Homepage: https://aihero.dev/skills
- GitHub API metadata + `git/trees/main?recursive=1` for SKILL.md inventory (2026-08-11)
