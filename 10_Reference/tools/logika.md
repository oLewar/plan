# Logika

Portable **formal-logic skill** (Chelpanov): review Russian argumentation, minimally rewrite it, or solve textbook problems. No extra tools. Host loop unchanged.

- Full wiki source: [[wiki/sources/logika]]
- Entity: [[wiki/entities/pavel-rykov]]
- Concept: [[wiki/concepts/formal-logic-skill]]
- GitHub: https://github.com/EvilFreelancer/logika
- Catalog: https://github.com/EvilFreelancer/rpa-skills
- License: MIT
- Version at ingest: **2.0.0** (SKILL.md + Claude/Cursor/Codex plugin.json); **no git tags**; HEAD `6554244dcc4b` (2026-08-02); stars **140** (API 2026-09-18)
- npm `logika` is a **different** package

## Install (docs; not run here)

This Hermes host has **no** logika skill. Do not copy into `~/.hermes/skills` unless asked.

```text
/plugin marketplace add EvilFreelancer/rpa-skills
/plugin install logika@rpa-skills
```

Or symlink the repo to `~/.claude/skills/logika/` / `~/.cursor/skills/logika/` / `~/.codex/skills/logika/`. Directory name must be `logika`.

```text
/logika:review <текст>   # analysis only
/logika <текст>          # fix (rewrite)
```

## Hermes / Chappy

At ingest: **reference only**. Honest steal: review template (verdict, structure, error table with RU+Latin names, hidden premises) and the form/matter split.

Full Chelpanov text is **not** in the public git tree (`source/` gitignored). `docs/konspekt.md` is.

## Operating constraints

- Benchmark JSON mode only for explicit BQA/MCQA.
- Fix mode must not invent facts; weaken the claim instead.
- Marketplace copy in rpa-skills can lag this repo (catalog follows).
- Checks *form*. Material truth still needs sources ([[wiki/concepts/causal-analysis]]).

## Mental model

**Procedure skill**, not a loop. Contrast engineering skills ([[wiki/sources/mattpocock-skills]]), playbook router ([[wiki/concepts/playbook-routed-agent-mode]]), harness axes.
