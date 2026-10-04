# Mixture of Self-Improving Branches for Agent Harness Optimization

## Bibliographic

| Field | Value |
|---|---|
| Title | Mixture of Self-Improving Branches for Agent Harness Optimization |
| arXiv | [2609.37834v1](https://arxiv.org/html/2609.37834v1) [cs.AI] |
| Date | 29 Sep 2026 (v1, as printed on the HTML) |
| License | CC BY 4.0 (stated on the HTML page) |
| Authors | Haoyu Dong, Yuhang Zhou, Zihao Lin, Yifan Wu, Bo Peng, Mingyi Wang, Xiangjun Fan, Lizhu Zhang, Zhuokai Zhao |
| Affiliations | The footnote lists Meta, Duke University, and University of California, Davis. It does not assign a person to a number. * = work done while at Meta. † = co-last authors. Correspondence: Haoyu Dong (haoyu.dong151@duke.edu), Zhuokai Zhao (zhuokai@meta.com) |
| First author | [[wiki/entities/haoyu-dong]] |
| Proposer / action models (as named) | Coding proposer: Claude Opus 4.6. Action models: Gemini 3 Flash and Claude Sonnet 4.5, in separate settings |
| Baseline named in the paper | Meta-Harness (Lee et al., 2026). The vault's README capture of that repo is `[[40_Research/sources/agent-dev/stanford-iris-labmeta-harness Reference code for the Meta-Harness paper.]]`. This note did not re-read it |
| Raw capture | [[raw/arxiv-2609.37834]] |
| PDF | Not downloaded |

## One-line purpose

Поиск harness вокруг замороженной модели ведут две ветки с разными development-подмножествами и своим `SKILL.md`; роутер выбирает одну голову до исполнения, не глядя на тест.

## Thesis

Read from the HTML (sections 1–5 and Appendix A), not from the abstract alone. Every number below is an **author claim**. This vault did not re-run the search.

- **Method.** A branch is its own development subset, candidate history, and proposal guidance (`SKILL.md`). All branches start from the same seeds, the full development set, and the same guidance. The shared proposer is Claude Opus 4.6. Each iteration it writes one new harness per branch and the branch scores it on its own subset. A frontier is the top q harnesses by mean reward on that subset. A case leaves every subset when every frontier harness solves it. Otherwise a branch keeps the case, and the others drop it, when its frontier solves the case by at least Δ more heads than the next branch. Guidance is rewritten from that branch's own recent history. Defaults in the experiments: B = 2, N = 20, q = 5, Δ = 2, subset update every iteration, guidance update every 5 iterations.
- **Deployment.** The head of a branch is the harness with the highest mean reward on that branch's *final* subset. Subset scores are not comparable across branches, so a router (the action model, instruction tuned with GEPA on cases solved by exactly one head) picks one head per new input *before* execution. It does not see test labels.
- **Result the authors report (development-selected, held-out test).** Versus Meta-Harness: Math–Gemini 3 Flash 46.0% → 62.0% (relative +34.8%); Math–Claude Sonnet 4.5 29.0% → 30.5% (relative +5.2%); Terminal-Bench 2.0 44.8% → 50.0% (relative +11.6%); SWE-bench Lite 63.6% → 66.0% (relative +3.8%). The abstract's "34.8% on Olympiad-level mathematical reasoning" is the Gemini setting, not both math runs. Splits: math 250 dev / 200 test; Terminal-Bench 2.0 a random 30 / 58 of 88; SWE-bench Lite a random 50 / 250 of 300.
- **What the authors say the ablations show (Math–Gemini only).** Both components: 62.0%. Pruning only: 54.0%. Guidance updates only: 50.0%. Neither (two independent fixed-set searches): 51.0%. Updating the subset every 5 or 3 iterations instead of every iteration: 53.0% and 56.0%. They also say the router beats the stronger single head by 4.0 and 1.7 points on Math–Gemini and Terminal-Bench 2.0, and falls short by one test case on Math–Sonnet and SWE-bench Lite.
- **Limitation the paper states.** Unequal total token use and few repeated evaluations limit what can be said about efficiency and reliability. Routing is slightly below the stronger head in two settings. The ablations support the combined design but do not show that each observed trajectory change caused the later test gain. Appendix A (author table, Claude Sonnet 4.5 as the action model): task-solving tokens are 1.21×, 1.71×, and 1.50× Meta-Harness on math, Terminal-Bench 2.0, and SWE-bench Lite. Full-run totals they print: math 172.90M vs 79.92M; Terminal-Bench 2.0 4,001.39M vs 2,366.80M; SWE-bench Lite 2,951.48M vs 1,907.17M.

## Why it matters for `pro/plan`

- This is harness *search*, not a harness you can run. No code was fetched, so there is no tool card and no line on `harness.md`. It is not a fifth axis next to [[wiki/concepts/everything-is-a-plugin]], [[wiki/concepts/playbook-routed-agent-mode]], [[wiki/concepts/agent-runtime-multiplexer]], and [[wiki/concepts/continual-harness]].
- It is a different search from [[wiki/concepts/regularized-harness-search]] (RRSI). That one keeps one incumbent and rejects an edit for leakage, noise, or tokens. This one splits the development set so two lineages specialize, then routes. The paper does not cite RRSI. Do not merge the two claims.
- The reusable split is already on [[wiki/concepts/causal-analysis]]: a higher routed score is not "the harness got better." One bullet on [[wiki/concepts/efficiency-metric]]: two branches cost more tokens than one Meta-Harness run, by the authors' own table.
- Not added to [[wiki/concepts/barbell-strategy]]. The paper is dated 2026-09-29; the vault does not already treat this method as a timeless object.

## Status

| | |
|---|---|
| Confidence | **medium** on the method as printed in the HTML (Algorithm 1, the prune rule, the schedule). **low** on every percentage — author-reported, not re-run, and the conclusion says repeated evaluations were limited |
| Depth | HTML of v1: abstract, sections 1–5, related work, Appendix A. Appendices B–E were mapped, not copied. PDF not downloaded |
| Not a tool | A paper. No repository URL in the HTML that was fetched. Not installed |
| Not a harness | Not added to the harness card |

## Open

- **Hypothesis**: whether splitting the development set beats a single regularized incumbent (RRSI) on the same tasks is not answered here. The two papers do not compare. See [[wiki/questions/research-backlog]].

## Provenance

- Fetched 2026-10-04: `https://arxiv.org/html/2609.37834v1` only (HTTP 200, 341269 bytes). PDF `https://arxiv.org/pdf/2609.37834` was not requested.
- Raw: [[raw/arxiv-2609.37834]]. Body sha256 `a84fd48a7edb900506af84551776ca792d8c8d45dec482b0bed5cbb066ea6c42` (bytes after the closing frontmatter fence).

## Sources

- [[raw/arxiv-2609.37834]]
