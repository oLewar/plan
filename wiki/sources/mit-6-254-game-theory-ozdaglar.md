# Game Theory with Engineering Applications (MIT 6.254, Spring 2010)

## Bibliographic / source

| Field | Value |
|---|---|
| Course | **6.254 Game Theory with Engineering Applications**, Spring 2010, graduate |
| Instructor | Prof. Asuman Ozdaglar (slides sign "Asu Ozdaglar") |
| Department | Electrical Engineering and Computer Science, MIT |
| Course home | https://ocw.mit.edu/courses/6-254-game-theory-with-engineering-applications-spring-2010/ |
| Lecture notes index | https://ocw.mit.edu/courses/6-254-game-theory-with-engineering-applications-spring-2010/pages/lecture-notes/ |
| Syllabus | https://ocw.mit.edu/courses/6-254-game-theory-with-engineering-applications-spring-2010/pages/syllabus/ |
| This ingest | Lecture **5**, "Existence of a Nash equilibrium", dated **February 18, 2010** on the title slide |
| Lecture page | https://ocw.mit.edu/courses/6-254-game-theory-with-engineering-applications-spring-2010/resources/mit6_254s10_lec05/ |
| PDF | https://ocw.mit.edu/courses/6-254-game-theory-with-engineering-applications-spring-2010/bf82ebe9ffcd2401d5c59df93ee9a200_MIT6_254S10_lec05.pdf — 276,303 bytes, sha256 `fd77248515269fd9f6bcd254d9691a34ecd1c23c10344603772689decc48abe7`, **28 pages** (`/Type /Page` count). `file(1)` said 4 pages; that is the outline count, not the sheets. **Not committed** |
| Reading named on the slides | Fudenberg and Tirole, Chapter 1. That book was not fetched |
| License | [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/) via https://ocw.mit.edu/terms/ (terms page last updated 2026-08-11). MIT's own reading of "non-commercial": do not sell the materials or a course built on them. MIT name and seal are not part of the license |
| Meetings | 2 lectures / week × 1.5 h, 1 recitation / week × 1 h |
| Grading | midterm 30%, homework 20%, project 50%. "About 6" problem sets. Project: 2–3 papers, a report, a presentation |
| Prerequisites | probability (6.041 or equivalent) and mathematical maturity. Analysis (18.100) and optimization (6.251 / 6.255) "helpful, not required" |
| Raw capture | [[raw/mit-ocw-6-254-lec05]] |

## One-line purpose

Graduate course that treats game theory as a tool for engineered networks (routing, pricing, resource allocation), not as a survey of economic institutions. Lecture 5 is the existence lecture: a finite game always has a *mixed* Nash equilibrium; an infinite game has a *pure* one only under extra shape conditions, and the second example on the slides has none.

## Thesis (lecture 5 read; the other 20 lectures are titles only)

1. **Existence is a license to look, not a location.** The slides say it directly: without existence, studying the equilibrium's properties is "difficult (perhaps meaningless)"; with the theorem, "we can simply try to locate the equilibria." The theorem does not say where the equilibrium is or that it is unique.
2. **Finite game → mixed equilibrium, via a fixed point.** Nash's theorem as stated here: every finite game has a mixed-strategy Nash equilibrium (matching pennies is the named implication). The proof maps the best-response correspondence and invokes Kakutani: the mixed-strategy space is a product of simplices (compact, convex, nonempty); best responses are nonempty (Weierstrass, because payoff is linear in own mixture), convex-valued (linearity again), and closed-graph (continuity). A fixed point of that correspondence is a mixed Nash equilibrium.
3. **Infinite pure-strategy sets need concavity, and the course's own example fails it.** Debreu–Glicksberg–Fan, as stated: compact convex strategy sets, payoff continuous in the opponents' actions and continuous and concave (quasi-concave suffices) in one's own → a *pure* Nash equilibrium exists. Nash is recovered as the special case where strategy sets are simplices and utility is linear in the mixture. Example 2 of the pricing-congestion game is the counterweight: a small kink in one latency function, and every candidate pure-price pair has a profitable deviation. Compactness alone is not enough.
4. **The set of equilibria can be closed without being continuous.** If payoffs depend continuously on a parameter λ in a compact set, the Nash correspondence has a closed graph. The slides add, with emphasis, that this does **not** imply the equilibrium set is continuous in λ. A nearby game can have a nearby equilibrium; it need not have *only* nearby equilibria, and the set can jump.
5. **Dropping concavity does not drop mixed equilibrium, but the proof leaves the lecture.** Glicksberg's theorem, stated and not proved: nonempty compact metric strategy spaces and payoffs continuous in the whole profile → a mixed equilibrium exists. The slide flags why the proof waits: mixed strategies over a continuum are infinite-dimensional. The circle example (two players pick a point, one's payoff is distance, the other's is minus that) has no pure equilibrium; uniform mixing on the circle is a mixed one. "It can be shown" — the slides do not show it.

## The example that opens the lecture

Pricing-congestion game, cited as Acemoglu and Ozdaglar 2007 (paper not fetched). Parallel links, a unit of traffic that is many infinitesimal users, each link owned by a provider who posts a price. Users route by Wardrop: only on minimum effective-cost links (price plus latency), and only if that cost is within a reservation utility R.

- Example 1: two links, latencies 0 and (3/2)x², R = 1, d = 1. Best responses cross once, at prices (1, 1/2). Unique pure equilibrium. The slides assume interior Wardrop flow at that point and point to the paper for the proof of the assumption.
- Example 2: one latency is flat then steep. The slides list the candidate pure profiles and a profitable deviation for each. No pure Nash equilibrium.

Formulas in the reconstructed text are scrambled by the PDF's per-glyph encoding. The prices (1, 1/2), the two latency shapes, and the "no pure equilibrium" conclusion are readable. Do not lift an intermediate expression from the reconstruction.

## Course map (titles from the lecture-notes index; only lecture 5 was read)

| Lec | Topic | Notes |
|---|---|---|
| 1 | Introduction | |
| 2 | Strategic form games | |
| 3 | Strategic form games: solution concepts | |
| 4 | Strategic form games: solution concepts; correlated rationalizability | two PDFs |
| **5** | **Existence of a Nash equilibrium** | **this ingest** |
| 6 | Continuous and discontinuous games | two PDFs |
| 7 | Supermodular games | |
| 8 | Supermodular and potential games | |
| 9 | Computation of Nash equilibrium in finite games | |
| 10 | Evolution and learning in games | |
| 11 | Learning in games | |
| 12 | Extensive form games I | |
| 13 | Extensive form games II | |
| 14 | Nash bargaining solution | |
| 15 | Repeated games I | |
| 16 | Repeated games II | |
| 17 | Bayesian Nash equilibria | |
| 18 | Bayesian Nash and perfect Bayesian equilibria | |
| 19 | Mechanism design I | |
| 20 | Mechanism design II | |
| 21 | Social choice and voting theory | |

Syllabus groups the same material as eight blocks (strategic form, learning/evolution/computation, extensive games, repeated games, incomplete information, mechanism design, network games) and is labeled **tentative**. Lecture 6 is the sequel that promises discontinuous games and the proof of Glicksberg. Not read.

## Why it matters for `pro/plan`

- Same split as [[wiki/concepts/margin-and-constraint]], one floor down. Emerson asks which margin a policy moves. This lecture asks whether a margin *has a resting point*: finite actions always do in mixed strategies; a price set on a continuum does not, unless own-payoff is concave. A model with no equilibrium is not a model you can cite an equilibrium of.
- [[wiki/concepts/causal-analysis]]: "the providers priced at (1, 1/2)" is a different claim from "a pure equilibrium exists." Example 2 is the case where the second claim is false and any sentence about "the" price is unsupported.
- [[wiki/concepts/efficiency-metric]]: computing an equilibrium (lecture 9, unread) is a different cost from proving one exists. Existence is the cheap license; location is the expensive step. The closed-graph remark is the warning against treating a small parameter change as a small equilibrium change.
- Timeless pole of [[wiki/concepts/barbell-strategy]], next to Emerson. The 2007 congestion paper will date; Kakutani's hypotheses will not.
- Not a harness, not a solver, not installed. CC BY-NC-SA: do not drop the slides into a paid product. Do not use the MIT name beyond the attribution the license requires.

## Status

- **Ingest source**: course home, syllabus, lecture-notes index (web extract), and the lecture 5 PDF (text reconstructed from content streams; formulas not trusted). Lectures 1–4 and 6–21 not downloaded. Problem sets, exams, and the reading list not fetched. Fudenberg–Tirole and Acemoglu–Ozdaglar 2007 not fetched.
- **Depth**: bibliographic + the 21-lecture title map + the statement-level reading of lecture 5 (theorems, the two examples, the closed-graph caveat). Not a reproduction of the proofs. Not a check that the reconstruction matches every subscript.
- **Confidence**: high on course metadata, license, the 21 titles, the 28-page count, and the theorem *statements* (Nash, Kakutani's hypotheses, Debreu–Glicksberg–Fan, Glicksberg stated-not-proved). High that example 1 claims a unique pure equilibrium at (1, 1/2) and example 2 claims none. Medium on intermediate formulas — the PDF emits one glyph per text operator and the line joiner scrambles subscripts. Low on anything in lectures 6–21.
- **Do not cite**: a formula copied from the text reconstruction; Glicksberg's theorem as proved in this lecture; the syllabus schedule as what was actually taught ("tentative"); existence as uniqueness or as a location.

## Links

- Concept: [[wiki/concepts/equilibrium-existence]]
- Entity: [[wiki/entities/asuman-ozdaglar]]
- Tool card: [[10_Reference/tools/mit-6-254]]
- Adjacent: [[wiki/concepts/margin-and-constraint]], [[wiki/concepts/causal-analysis]], [[wiki/concepts/efficiency-metric]], [[wiki/concepts/barbell-strategy]], [[wiki/sources/intermediate-microeconomics-emerson]]
