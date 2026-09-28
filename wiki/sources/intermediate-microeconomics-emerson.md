# Intermediate Microeconomics (Patrick M. Emerson, Oregon State)

## Bibliographic / source

| Field | Value |
|---|---|
| Title | **Intermediate Microeconomics** |
| Author | Patrick M. Emerson |
| Publisher | Oregon State University Open Educational Resources (Pressbooks) |
| URL | https://open.oregonstate.education/intermediatemicroeconomics/ |
| Read from | https://open.oregonstate.education/intermediatemicroeconomics/chapter/module-1/ |
| Copyright | © 2019 Patrick M. Emerson |
| License | [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/). Back-matter page spells it "NonCommerical" — that is their typo; the linked license is NonCommercial |
| Print ISBN | 978-1-955101-18-9 |
| First publication | 2019-10-28 (version **1.00**) |
| Version table | **2.04** on 2024-04-18 (equation fix in module 5). The table stops there |
| Chapter `modified` dates | later than the table: eight modules touched **2025-05-16** or **2025-05-19** (5, 6, 7, 8, 11, 13, 15, 17, 20). Do not treat 2.04 as "last edit" |
| Downloads | EPUB, digital PDF, print PDF, Common Cartridge — from the landing page. Not fetched |
| Grant | Division of Educational Ventures, Oregon State |
| Subject | Microeconomics. One part, **24 modules**, ~130,000 words in the HTML API (2026-09-28) |
| Raw capture | [[raw/oregonstate-intermediate-microeconomics]] |

## One-line purpose

Промежуточный курс микроэкономики: каждый модуль начинается с политического вопроса (налог на гибриды, минимальная зарплата, налог на углерод, патент на лекарство), а теория — инструмент разобрать этот вопрос. Два математических входа, графический и с исчислением, в одном тексте.

## Thesis (from the landing page, the TOC API, and the module headings — not a chapter reading)

1. **Policy question first, model second.** All 24 modules open with "The Policy Question" and close by walking that same question back through the tools ("Policy Example", then "Exploring the Policy Question"). The question is a hook, not a result. Module 19 states the question (school uniforms) and then its learning objectives; it does not answer the uniforms question in the opening.
2. **One book, two tracks.** The landing description says instructors can teach with or without calculus. In the HTML that split is uneven: explicit `Calculus` headings show up in module 7 (long-run cost minimization) and module 8 (short-run and long-run cost; three such headings). Other modules put the algebra in ordinary headings (Cobb-Douglas demand in module 4, monopoly quantity and price in module 15, a "Mathematical Extension" in module 14) or use LaTeX without a calculus label (module 2). Several modules have neither (1, 3, 10, 12, 13, 17, 19–21, 23, 24). "Both tracks everywhere" is the publisher's claim, not what the headings show.
3. **The spine is the standard intermediate sequence, not a survey of current policy.** Consumer theory (1–5) → firm, cost, supply (6–9) → equilibrium and comparative statics (10–11) → inputs (12) → competition, general equilibrium, monopoly, pricing (13–16) → games and oligopoly (17–19) → failures and information (20–22) → risk and time (23–24).
4. **The version log is behind the files.** Accessibility page lists edits through 2.04 (2024-04-18). The chapter API's `modified` field is 2025 for nine modules. Cite the module date, not "version 2.04", when a number matters.

## The 24 modules

Policy question is the chapter's hook, paraphrased from the opening, not a finding. Word counts are the HTML API, 2026-09-28.

| # | Module | Hook (author's question) | Words |
|---|---|---|---|
| 1 | Preference and Indifference Curves | Tax credit for hybrid cars — best way to cut fuel use and carbon? | 4,618 |
| 2 | Utility | Same hybrid-credit question, now with a utility function | 4,129 |
| 3 | Budget Constraints | Same question: a hybrid frees money for other goods | 3,768 |
| 4 | Consumer Choice | Same question, now as a choice under the constraint | 5,512 |
| 5 | Individual Demand and Market Demand | Should a city charge more for downtown parking? | 7,256 |
| 6 | Firms and Their Production Decisions | Is classroom technology the best way to improve education? | 9,168 |
| 7 | Minimizing Costs | Will a higher minimum wage cut employment? | 6,853 |
| 8 | Cost Curves | Should the federal government promote domestic streetcars? | 6,132 |
| 9 | Profit Maximization and Supply | Will a carbon tax harm the economy? | 5,835 |
| 10 | Market Equilibrium: Supply and Demand | Should government run public marketplaces? | 4,840 |
| 11 | Comparative Statics | Should the federal government subsidize solar installations? | 6,897 |
| 12 | Input Markets | Should Oregon and New Jersey ban self-service gas? | 6,612 |
| 13 | Perfect Competition | Should government allow oil companies to merge retail stations? | 2,848 |
| 14 | General Equilibrium | Should government address inequality with taxes and transfers? | 8,622 |
| 15 | Monopoly | Should government patent life-saving drugs? | 5,428 |
| 16 | Pricing Strategies | Should public universities charge everyone the same price? | 9,489 |
| 17 | Game Theory | Do banks need regulation to be saved from themselves? | 9,312 |
| 18 | Oligopoly: Cournot, Bertrand, Stackelberg | How should government have answered big-oil mergers? | 3,892 |
| 19 | Monopolistic Competition | Should public schools require uniforms? | 1,325 |
| 20 | Externalities | Should New York ban large sugary drinks? | 5,409 |
| 21 | Public Goods | Should government regulate near-shore fishing? (the "exploring" prompt then switches to drug monopolies) | 2,800 |
| 22 | Asymmetric Information | Should government mandate buying health insurance? | 2,726 |
| 23 | Uncertainty and Risk | Should the US government provide flood insurance? | 2,906 |
| 24 | Time: Money Now or Money Later? | Should government regulate payday loans? | 3,832 |

Modules 1–4 are one running example (the hybrid tax credit) seen four ways: preferences, utility, budget, choice. Module 19 is an outline relative to the others (~1,300 words against ~9,000 for pricing and game theory).

## Why it matters for `pro/plan`

- Timeless pole of [[wiki/concepts/barbell-strategy]]: the objects (constraint, marginal rate, surplus, externality, asymmetric information) outlast the 2005–2012 policy hooks. The hooks go stale; the decomposition does not.
- A policy fight is usually a fight about **which margin**. This book forces the split: preferences vs budget (1–4), firm cost vs the wage floor (7), carbon tax vs the supply curve (9), patent as a designed monopoly (15), price discrimination vs one tuition (16). That is the same hygiene as [[wiki/concepts/causal-analysis]] — don't collapse "the policy failed" into one cause.
- Deadweight loss, consumer surplus, and producer surplus are defined as headings in module 10. Use those words only in that sense.
- Not a data source. The chapters illustrate with named cases (California carbon rules, Crestor, Eastern Market, the individual mandate). Those are teaching examples, not measurements.
- CC BY-NC-SA: share and adapt with attribution, **non-commercial**, share-alike. Do not drop the graphs into a paid product.

## Status

- **Ingest source**: landing page (web extract; direct curl got CloudFront 403), Pressbooks TOC API, all 24 chapter bodies via `pressbooks/v2/chapters` (headings and word counts only), back-matter pages for license, version table, and citation templates. PDF/EPUB not downloaded. No module read past its opening and its heading list.
- **Depth**: bibliographic + TOC + the policy-question sentence of each module + where calculus headings actually sit. Not a chapter-level reading. No worked problem reproduced.
- **Confidence**: high on license, ISBN, 24 titles, URLs, word counts, and the version table (fetched). High that modules 1–4 share the hybrid-credit hook and that module 19 is short (those are in the HTML). Medium on "both math tracks in every chapter" — **not supported** by the heading census; say so. The 2025 `modified` dates are file timestamps, not a changelog of what changed.
- **Do not cite**: a module's policy question as the book's conclusion; version 2.04 as the last edit; "calculus optional throughout" without the heading caveat.

## Links

- Concept: [[wiki/concepts/margin-and-constraint]]
- Entity: [[wiki/entities/patrick-emerson]]
- Tool card: [[10_Reference/tools/intermediate-microeconomics]]
- Adjacent: [[wiki/concepts/barbell-strategy]], [[wiki/concepts/causal-analysis]], [[wiki/concepts/efficiency-metric]]
