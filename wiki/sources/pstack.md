# pstack (cursor/plugins)

## Bibliographic / source

| Field | Value |
|---|---|
| Title | **pstack** |
| Author | [[wiki/entities/lauren-tan\|Lauren Tan]] (`poteto`) |
| Org / host | [[wiki/entities/cursor\|Cursor]] official plugins repo |
| Plugin path | [cursor/plugins/tree/main/pstack](https://github.com/cursor/plugins/tree/main/pstack) |
| README | [blob/main/pstack/README.md](https://github.com/cursor/plugins/blob/main/pstack/README.md) |
| Guide | [pstack/docs/guide](https://github.com/cursor/plugins/tree/main/pstack/docs/guide) |
| Manifest | `pstack/.cursor-plugin/plugin.json` **0.14.2** (tree `main` @ `46125561`, 2026-08-21) |
| License | MIT (Copyright 2026 Lauren Tan) |
| Parent repo | [cursor/plugins](https://github.com/cursor/plugins) — Cursor plugin spec + official plugins |
| Parent stars / forks | 4341 / 365 (GitHub API, 2026-08-21) |
| Parent created / last push | 2026-01-23 / 2026-08-21 |
| Domain | coding-agent workflows, Cursor plugins, multi-model review, evidence-gated shipping |
| Raw capture | [[40_Research/sources/agent-dev/cursor-plugins-pstack-readme]] (cron-routed from `raw/` inbox) |

## One-line purpose

Cursor plugin that turns the IDE agent into a **rigorous engineering team**: sticky `/poteto-mode` routes a task to a playbook, other skills fire as steps, multi-model panels review, and work is not done until the **real artifact** is proven.

## Thesis (from README + plugin.json + `/poteto-mode` + `/setup-pstack`)

1. **Throughput without quality is not the goal.** «If you want to go fast, go deep first.» Less code, higher quality; fearless parallelism only after one agent is trustworthy.
2. **One sticky mode, not a pile of slash commands.** `/poteto-mode` matches a playbook, copies its steps **verbatim** into the todo list (silent skip forbidden; `skip: <reason>` required), then routes situational skills. Opt out by saying so.
3. **Best spec is code.** pstack ships **no planning skills**. Cursor Plan mode exists; the author does not believe in planning as the default.
4. **Model by role, not one model for everything.** Defaults: specified sequences → Sol (`gpt-5.6-sol-max`); fast mechanical code → Grok (`grok-4.6-fast-xhigh`); prose/judgment/hardest design → Fable (`claude-fable-5-thinking-max`); review panels → Fable / Sol / Grok / Opus 5. Override via `/setup-pstack` → `~/.cursor/rules/pstack-models.mdc`.
5. **Principles are named, indexed, and must change a decision.** 21 leaf `principle-*` skills. A citation with no decision means the leaf was skipped.
6. **PRs welcome; fork it.** Complementary kit `cursor-team-kit` holds `/deslop`, `control-cli`, `control-ui` — not bundled here.

## Architecture snapshot

```
/add-plugin pstack
  → /setup-pstack  (models rule + optional verify-* skill)
  → /poteto-mode   (sticky; match playbook → copy steps → route skills)
       subagent_type: poteto-agent  (must read poteto-mode SKILL.md in full)
       Comment Sicko via /no-comments
  → prove on the real app, then PR (opening-a-pr at end of every playbook)
```

### Layout (tree `main`, 231 paths under `pstack/`)

| Piece | Role |
|---|---|
| `.cursor-plugin/plugin.json` | Manifest **0.14.2**; `skills: ./skills/`, `agents: ./agents/` |
| `skills/poteto-mode/` | Sticky router + **23** playbook files (README markets **22**; plus `opening-a-pr.md` as the shared closer) |
| `skills/principle-*` | **21** one-principle skills (core / architecture / verification / delegation / meta) |
| Other `skills/*` | Situational: how, why, recall, blast-radius, architect, arena, swarm, interrogate, tdd, unslop, … |
| `agents/poteto-agent.md` | Subagent wrapper; substituting `generalPurpose` skips the principles read and drifts |
| `agents/comment-sicko.md` | Read-only comment reviewer (`subagent_type: "Comment Sicko"`) |
| `docs/guide/` | 10-page first-task guide |
| `automations/benny/` | Dormant Slack-triage pack; **not** registered as slash skills |

### Default model map (`/setup-pstack` template, 2026-08-21)

| Role | Default slug |
|---|---|
| feature, refactoring | `grok-4.6-fast-xhigh` |
| bug-fix / perf-issue / hillclimb | `gpt-5.6-sol-max` |
| judgment and prose; hardest tasks | `claude-fable-5-thinking-max` |
| how explorer; why investigators; swarm workers | `grok-4.6-fast-xhigh` |
| how explainer; why synthesizer | `claude-fable-5-thinking-max` |
| how critics / arena / architect / interrogate panels | fable + sol + grok + `claude-opus-5-thinking-xhigh` |

`inherit-parent` / `auto` = omit Task `model` (Auto users stay on Auto). Panel **list length** = fan-out count.

### Skill inventory (user-facing, non-principle)

`/poteto-mode`, `/setup-pstack`, `/how`, `/why`, `/recall`, `/blast-radius`, `/architect`, `/arena`, `/swarm`, `/interrogate`, `/automate-me`, `/reflect`, `/teach`, `/tdd`, `/no-comments`, `/typescript-best-practices`, `/figure-it-out`, `/show-me-your-work`, `/create-verification-skill`, `/maintain-verification-skill`, `/unslop`, `/bro`, `/technical-writing`

### Playbooks (router table)

investigation, bug-fix, perf-issue, hillclimb, runtime-forensics, trace-forensics, feature, refactoring, prototype, visual-parity, authoring-a-skill, eval, babysit, shipping, autonomous-run, orchestrate, autopilot-full, autopilot-stack, session-pickup, pause-safely, multi-phase-plan, worktree-cleanup; plus **opening-a-pr** (end of every other playbook).

### 21 principles (groups)

- **Core:** laziness-protocol, foundational-thinking, redesign-from-first-principles, subtract-before-you-add, minimize-reader-load, outcome-oriented-execution, experience-first, exhaust-the-design-space, build-the-lever
- **Architecture:** model-the-domain, boundary-discipline, type-system-discipline, make-operations-idempotent, migrate-callers-then-delete-legacy-apis, separate-before-serializing-shared-state
- **Verification:** prove-it-works, fix-root-causes, sequence-verifiable-units
- **Delegation:** guard-the-context-window, never-block-on-the-human
- **Meta:** encode-lessons-in-structure

## Why it matters for `pro/plan`

- Direct neighbor to [[wiki/sources/mattpocock-skills]]: both «real engineering vs slop», but pstack is a **sticky router + playbooks + named principles + multi-model panels**, not a bag of independently invoked skills.
- Evidence gate (`prove-it-works`, project-local `verify-*`) matches the host coding loop: issues → worktrees → retries / evidence, not «it compiles».
- Contrast with [[wiki/concepts/human-in-the-loop-gtm]]: pstack **never-block-on-the-human** for reversible coding work; GTM still requires a person on every customer send. Do not import the coding autonomy rule into outreach.
- Contrast with [[wiki/concepts/everything-is-a-plugin]]: DSH replaces the loop; pstack **wraps Cursor's loop** with skills/agents. Composition of *style*, not of runtime.
- `/automate-me` mines transcripts into a personal `*-mode` — relevant if we ever generate a Chappy-mode skill from real sessions rather than hand-writing SOUL.

## Status

- **Ingest source:** user URL `https://github.com/cursor/plugins/tree/main/pstack` + raw README + `plugin.json` + `/poteto-mode` + `/setup-pstack` + guide `01-setup` + GitHub API tree/commits (2026-08-21).
- **Depth:** README + manifest + router/setup skills + tree inventory. Individual playbook/principle bodies **not** deep-dived.
- **Hermes / Chappy:** reference only. Install path is Cursor `/add-plugin`; `Task` `subagent_type` and `~/.cursor/rules/pstack-models.mdc` are Cursor-specific. Do not install into the Hermes profile.
- **Confidence:** high for public files at capture SHA; medium that live Cursor marketplace copy equals this tree (plugin version can lag git).

## Possible Hermes/Chappy integration paths

1. **Process borrow only** — playbook-match → verbatim steps → `skip: reason`; prove-it-works; multi-model interrogate as a review gate.
2. **Manual port of a few skills** — `how`/`why`/`interrogate`/`tdd`/`unslop` into Hermes `SKILL.md` after rewriting Cursor `Task` APIs.
3. **Do not** copy `never-block-on-the-human` onto Fusion CLI (user rule: Fusion only on explicit request) or onto GTM send.

## Next (optional)

- [ ] Deep-dive `playbooks/bug-fix.md` vs host evidence-gate
- [ ] Compare 21 principles vs local `code-quality-workflows` / `subagent-driven-development`
- [ ] Decide whether a Chappy `*-mode` should be mined (`/automate-me` pattern) or stay hand-written (SOUL.md)

## Links

- Entity: [[wiki/entities/cursor]], [[wiki/entities/lauren-tan]]
- Concept: [[wiki/concepts/playbook-routed-agent-mode]]
- Tool: [[10_Reference/tools/pstack]]
- Neighbor: [[wiki/sources/mattpocock-skills]]
- Raw (durable after inbox route): [[40_Research/sources/agent-dev/cursor-plugins-pstack-readme]]

## Sources / provenance

- README: https://github.com/cursor/plugins/blob/main/pstack/README.md
- Raw: https://raw.githubusercontent.com/cursor/plugins/main/pstack/README.md (sha256 `7b2994ff3caa430bbdd5734e24f7b2f18afeee2dd0893e5dbbce0fca2790ce8d`, 2026-08-21)
- Manifest: https://raw.githubusercontent.com/cursor/plugins/main/pstack/.cursor-plugin/plugin.json (`version` 0.14.2)
- `/poteto-mode`: https://raw.githubusercontent.com/cursor/plugins/main/pstack/skills/poteto-mode/SKILL.md
- `/setup-pstack`: https://raw.githubusercontent.com/cursor/plugins/main/pstack/skills/setup-pstack/SKILL.md
- Guide: https://raw.githubusercontent.com/cursor/plugins/main/pstack/docs/guide/README.md
- Tree + commits via GitHub API `main` @ `461255613064` (docs(pstack): port workflow and boundary guidance #238)
- Parent repo metadata: GitHub API `cursor/plugins` 2026-08-21
