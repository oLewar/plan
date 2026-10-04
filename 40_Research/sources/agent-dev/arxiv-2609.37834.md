---
source_url: https://arxiv.org/html/2609.37834v1
arxiv_id: 2609.37834
arxiv_version: v1
ingested: 2026-10-04
pdf_downloaded: false
sha256: a84fd48a7edb900506af84551776ca792d8c8d45dec482b0bed5cbb066ea6c42
---

# Mixture of Self-Improving Branches for Agent Harness Optimization

arXiv:2609.37834v1 [cs.AI] 29 Sep 2026
License on the HTML page: CC BY 4.0
HTML: https://arxiv.org/html/2609.37834v1
PDF was not downloaded.

## Authors

Haoyu Dong, Yuhang Zhou, Zihao Lin, Yifan Wu, Bo Peng, Mingyi Wang, Xiangjun Fan, Lizhu Zhang, Zhuokai Zhao

Footnote on the page, not tied to a person: 1 Meta; 2 Duke University; 3 University of California, Davis. * Work done while at Meta. † Co-last authors. Correspondence: Haoyu Dong <haoyu.dong151@duke.edu>, Zhuokai Zhao <zhuokai@meta.com>.

## Abstract (verbatim)

Harness optimization provides a practical setting for recursive self-improvement (RSI), where agent-generated modifications inform subsequent changes through execution feedback. Recent work such as Meta-Harness implements this process through iterative code generation and evaluation, but retains a fixed development set and proposal policy. These constraints channel evolution along a single search trajectory, increasing the risk of converging to a local optimum. We make the improvement process itself adaptive by organizing search into branches with evolving development subsets and proposal policies. Each branch retains development cases solved by more of its leading harnesses than by those of other branches, drops cases solved by every leading harness across all branches, and revises its proposal policy using its own search history. To deploy the resulting complementary harnesses, we propose a router to select one development-selected branch head for each new input before execution. Across mathematical reasoning and agentic coding benchmarks, our system achieves relative improvements over Meta-Harness of 34.8% on Olympiad-level mathematical reasoning, 11.6% on Terminal-Bench 2.0, and 3.8% on SWE-bench Lite, with harness selection and router configuration based solely on development data. These results show that evolving branch objectives and proposal policies can yield complementary harnesses whose strengths a router combines without access to test outcomes.

## Section map

- 1 Introduction — A harness is retrieval, tools, and control flow around a model; Meta-Harness searches that code on one fixed development set and one fixed proposal policy.
- 2 Related Work — Places the method next to Meta-Harness, Self-Harness, quality-diversity search (AlphaEvolve, AgenticGEO), prompt/program optimizers (DREvo, SkillOpt), and input-level routing.
- 3 Branching Search with Evolving Objectives and Policies — Two branches, shared proposer, per-branch development subset, frontier coverage votes, ownership margin, and a SKILL.md guidance update; a router picks one head before execution.
- 4 Experiments — Four settings: math with Gemini 3 Flash, math with Claude Sonnet 4.5, Terminal-Bench 2.0, SWE-bench Lite. Development-selected routed system vs fixed harnesses and Meta-Harness.
- 4.1 Experimental Setup — Splits, baselines, and the default schedule: B=2, N=20, frontier q=5, margin Δ=2, prune every iteration, guidance every 5.
- 4.2 Performance of Development-Selected Systems — Author table: routed system above Meta-Harness in all four settings; the abstract's 34.8% is Math–Gemini (46.0% → 62.0%), not every math run.
- 4.3 How Branches Develop Different Search Trajectories — On Math–Gemini the branches keep different mechanisms; combined coverage is 4.0–9.0 points above the stronger head.
- 4.4 Router Analysis — Router beats the stronger head on two settings and misses it by one case on two others; it recovers 75% of Math–Gemini exclusive successes.
- 4.5 Method Ablation Studies — On Math–Gemini, pruning plus guidance updates is 62.0%; either alone is 50.0% or 54.0%; neither is 51.0%. Less frequent pruning scores lower.
- 4.6 Test Performance Analysis — A retrospective top-of-pool by test score; the authors treat it as a reference, not the deployed system. On Math–Gemini the router (62.0%) is above that pool's best single harness (58.0%).
- 5 Conclusion — Development-selected heads with routing beat development-selected Meta-Harness. The authors' own limit: unequal token use and few repeated runs, and ablations do not show that each trajectory change caused the later test gain.
- AI use statement — Generative tools drafted text and helped the experiments; the authors say they did not use them to invent the method or the hypotheses.
- Appendix A Token Accounting — Full-run tokens, task-solving vs harness-authoring. With two branches, task-solving tokens are 1.21×, 1.71×, and 1.50× Meta-Harness on the three benchmarks.
- Appendix B Development-Set Changes and Head Selection — Subset histories and one recorded head replacement (Math–Gemini, iteration 13) after four cases leave a branch.
- Appendix C Proposal-Guidance Updates — The update prompts and examples of how a branch rewrites its own SKILL.md.
- Appendix D Router Analysis — Router instructions, and ablations of code / examples / expert outputs with and without GEPA.
- Appendix E Discovered Harness Mechanisms — One paragraph each for Math–Gemini, Math–Sonnet, Terminal-Bench 2.0, and SWE-bench Lite.

## What this capture is not

Not the PDF. Not a code checkout. Numbers above are the paper's own reported figures, copied from the HTML, not a re-run.
