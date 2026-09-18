# Formal-logic skill

## Definition (working)

A **portable agent skill** that does not add tools. It adds a **procedure**:

- split **formal** validity (conclusion follows from premises) from **material** truth (premises match the world);
- name the inference form (syllogism figure/mood, immediate inference, Mill method, analogy, …);
- name every fallacy in **Russian + Latin**;
- emit either an analysis-only report, a minimal rewrite, a textbook solution, or (only for explicit BQA/MCQA) a single JSON object.

Canonical public case in this vault: [[wiki/sources/logika]] (Chelpanov «Учебник логики», Pavel Rykov). Same *packaging* family as [[wiki/sources/mattpocock-skills]]; different *content*.

## Mechanism (from logika SKILL.md)

```
text
  → identify thesis / premises / conclusions
  → classify each inference
  → load references/{errors,syllogism,…}.md
  → review XOR fix XOR solve XOR JSON
rewrite rules: no new facts; weaken «все»/«доказано» rather than invent grounds
```

| This is | This is not |
|---|---|
| A SKILL.md + Russian reference pack | A theorem prover / SAT solver |
| Form-checking | Evidence-gathering ([[wiki/concepts/causal-analysis]] still needs sources) |
| Host-loop plugin (Claude/Cursor/Codex/Kimi) | A harness axis |
| Chelpanov 19th/early-20th textbook distillations | Modern symbolic logic / probability |

## Contrast

| Style | What it constrains | Who runs it |
|---|---|---|
| Playbook-routed mode ([[wiki/concepts/playbook-routed-agent-mode]]) | *Process* steps of a coding task | Cursor sticky `/mode` |
| Matt Pocock skills | Engineering practices (grill, TDD, …) | Claude plugin / `npx skills` |
| **Formal-logic skill** | *Form* of an argument in (usually Russian) prose | Same hosts; Hermes not listed |
| Continual harness | Next-turn supplemental H | `/refine` |

Status of «loading Chelpanov refs makes the model a reliable logician»: **Hypothesis** (skill claim; no eval in this vault). Status of «full textbook is in the public repo»: **Refuted** at tree depth (`.gitignore` has `source/`; no `source/` blobs).

## Causal map

| Cause | Effect |
|---|---|
| Checking only material claims | Valid-looking text with *quaternio terminorum* / post hoc slips through |
| Checking only form | Formally valid argument from false premises ships as «логика корректна» |
| Rewrite mode inventing facts | Material falsehoods added; SKILL.md forbids this |
| Treating `/logika` JSON as default | Benchmark mode leaks into ordinary review |
| Catalog `rpa-skills` not bumped | Marketplace install can lag the skill repo (AGENTS.md: catalog follows) |

## Why it matters for `pro/plan`

- Direct fit to mission: **post hoc ≠ cause**, **скрытая посылка**, **форма vs материя** are the same splits used in [[wiki/concepts/causal-analysis]] (empty run vs answered-but-bad; after X vs because of X).
- Efficiency: a named-error table is cheaper than an open-ended «проверь текст» ([[wiki/concepts/efficiency-metric]]).
- Honest steal: the review template (verdict, structure, table, hidden premises) for wiki/GTM drafts. Do not install into `~/.hermes/skills` unless asked.
- GTM neighbor: HITL send still needs a human; this skill only gates *argument form* ([[wiki/concepts/human-in-the-loop-gtm]]).

## Related

- Source: [[wiki/sources/logika]]
- Entity: [[wiki/entities/pavel-rykov]]
- Tool: [[10_Reference/tools/logika]]
- Adjacent: [[wiki/concepts/causal-analysis]], [[wiki/concepts/playbook-routed-agent-mode]], [[wiki/sources/mattpocock-skills]]

## Sources

- [[wiki/sources/logika]]
