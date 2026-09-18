# Logika (EvilFreelancer/logika)

## Bibliographic / source

| Field | Value |
|---|---|
| Title | **Logika** |
| Tagline | Classical formal logic skill from G. Chelpanov's «Учебник логики» |
| Author | [[wiki/entities/pavel-rykov]] (`EvilFreelancer`; LICENSE «Copyright (c) 2026 Pavel Rykov») |
| Repo | [EvilFreelancer/logika](https://github.com/EvilFreelancer/logika) |
| Catalog | [EvilFreelancer/rpa-skills](https://github.com/EvilFreelancer/rpa-skills) (marketplace; **35★**, not a second ingest) |
| Homepage field | GitHub API `homepage` → rpa-skills (catalog), not a product site |
| License | MIT |
| Language | Markdown skill pack (GitHub `language: None`; languages API `{}`) |
| Version at ingest | **2.0.0** in `SKILL.md` + `.claude-plugin` / `.cursor-plugin` / `.codex-plugin`. **No git tags. No PyPI.** npm `logika@1.0.0` is an **unrelated** «logic operations» package. |
| Default branch / HEAD | `main` @ `6554244dcc4b` («Version bumping», 2026-08-02) |
| Stars / forks / subscribers | **140** / **14** / **2** (GitHub API 2026-09-18) |
| Open issues | **0** |
| Created / last push | 2026-06-26 / 2026-08-02 |
| Tree size | GitHub API `size` 106 KB; recursive tree **16 blobs / 6 trees**, not truncated |
| Domain | agent skill; formal logic; Russian references; argument review/fix |
| Raw capture | durable `40_Research/sources/finance/EvilFreelancer-logika-readme.md` (cron routed inbox here; no `__2` sibling) |
| Agent contract | root [SKILL.md](https://github.com/EvilFreelancer/logika/blob/main/SKILL.md) (GitHub Contents `size` 21457; UTF-8 text 12515 chars) + [AGENTS.md](https://github.com/EvilFreelancer/logika/blob/main/AGENTS.md) |
| Textbook | Chelpanov «Учебник логики» — README says bundled in `source/`; **`.gitignore` is `source/`**. Recursive tree has **no** `source/` blobs. Full book is **not** in the public git snapshot. `docs/konspekt.md` (171 041 B) is. |

## One-line purpose

A **portable SKILL.md** that makes a coding agent act as a Chelpanov-style logician: review Russian argumentation without rewriting, or minimally rewrite it, or solve textbook problems — always naming the *form* of the inference and the fallacy (RU + Latin).

## Thesis (README + SKILL.md + AGENTS.md + plugin.json + tree)

1. **Not a harness, not a CLI, not a model.** Same class as [[wiki/sources/mattpocock-skills]] / pstack-as-plugin: instructions + references the host loop loads. Contrast DSH / Herdr / Prime Agent.
2. **Four modes** (SKILL.md): **Review** (`/logika:review` — analysis-only table); **Fix** (default rewrite, preserve style, no new facts); **Problems** (step-by-step textbook); **Benchmark** (only explicit BQA/MCQA → one JSON object `{"reasoning","answer"}`).
3. **Form vs matter.** Formal validity (conclusion follows) and material truth (premises match the world) are checked **separately**. A valid syllogism can have false premises.
4. **References in Russian, Chelpanov terms:** `concepts.md`, `judgments.md`, `syllogism.md`, `induction.md`, `errors.md`, `laws.md`. Command file `commands/review.md` is the analysis-only slash command.
5. **Version lock across manifests.** AGENTS.md: `version` must match in SKILL.md + three plugin.json; catalog `rpa-skills` **follows, never leads**. At HEAD all four say **2.0.0**.
6. **Install is copy/symlink or marketplace**, not pip. Claude: `/plugin marketplace add EvilFreelancer/rpa-skills` then `/plugin install logika@rpa-skills`. Folder: `~/.claude/skills/logika/`, `~/.cursor/skills/logika/`, `~/.codex/skills/logika/`, `~/.kimi/skills/logika/`. Directory name **must** equal frontmatter `name: logika`.
7. **`source/` is gitignored.** Do not cite the public tree as containing the full textbook. Konspekt of 26 chapters is in-tree (`docs/konspekt.md`).
8. **Hermes is not a listed target.** Process-borrow of the review format is the honest steal; do not copy the skill into `~/.hermes/skills` unless asked.

## Architecture snapshot

```
user text / textbook problem
  → host loop loads SKILL.md (trigger: «проверь логику» / «исправь логику» / English fallacy/syllogism phrases)
  → load references/*.md as needed (review almost always errors.md + syllogism.md)
  → mode output: report XOR rewrite XOR solution XOR single JSON
```

| Piece | Role |
|---|---|
| `SKILL.md` | Canonical contract (RU description drives auto-trigger) |
| `commands/review.md` | `/logika:review` — do not rewrite |
| `references/*.md` | Chelpanov distillations |
| `docs/konspekt.md` | Per-chapter notes (26 chapters) |
| `.claude-plugin/plugin.json` etc. | Marketplace metadata **2.0.0** |

### Contrast vs other vault skills

| | Logika | Matt Pocock skills | pstack |
|---|---|---|---|
| Owns | Formal-logic *procedure* | Engineering *practices* | Sticky playbook *router* |
| Language of refs | Russian (Chelpanov) | English | English |
| Host | Claude/Cursor/Codex/Kimi | Claude plugin or `npx skills` | Cursor `/add-plugin` |
| Loop | Unchanged | Unchanged | Unchanged |

## Why it matters for `pro/plan`

- Mission is causal analysis: Chelpanov's split **формальная / материальная истинность** and **post hoc ≠ cause** is the same hygiene as [[wiki/concepts/causal-analysis]] (failed experiment ≠ one cause; after X ≠ because of X).
- Efficiency: a named-fallacy table is cheaper than an unscoped «is this text ok?» ([[wiki/concepts/efficiency-metric]]).
- Honest steal: review format (verdict + structure + error table + hidden premises) for wiki/GTM drafts — without installing the plugin.
- Do not treat the skill as a substitute for evidence. It checks *form*. Material claims still need sources.

## Status

- Ingest depth: README `main` + SKILL.md + AGENTS.md + three plugin.json **2.0.0** + `commands/review.md` + heads of six `references/` + LICENSE + `.gitignore` + GitHub API repo/user/commits/tree + rpa-skills org metadata. **Textbook body not in tree. Not installed.**
- Confidence: **high** on skill contract and tree; **medium** that marketplace copy in rpa-skills is still 2.0.0 (catalog pushed 2026-09-15; this repo last push 2026-08-02 — AGENTS.md warns catalog can lag).
- This host: skill **not** under `~/.hermes/skills`.

## Links

- Entity: [[wiki/entities/pavel-rykov]]
- Concept: [[wiki/concepts/formal-logic-skill]]
- Tool card: [[10_Reference/tools/logika]]
- Neighbor skills: [[wiki/sources/mattpocock-skills]]

## Sources / provenance

- Repo https://github.com/EvilFreelancer/logika (`main` @ `6554244dcc4b`, 2026-09-18)
- Raw capture sha256 `6d70589be40da4784bdf6560725c75377b0c6635d3f0875eafc34db54f02efc0` (5824 bytes, LF)
- Chelpanov textbook: public domain (author claim); full text **not** verified in this git snapshot
