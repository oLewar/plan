# Git-native experiment tree

## Definition (working)

A research project as a **tree of git branches**, not a spreadsheet of hyperparameter runs:

- Each **node** is a branch (`orx/<slug>` in the public case) that exists to establish a baseline or test one hypothesis.
- The **run command + environment is a fixed contract** inherited by children. The only legal difference between nodes is **committed code/config**.
- Once a run **answers** the node (any number, including a disappointment or `nan`), the branch is **frozen**. Repair in place only when the run answered *nothing* (OOM, missing dep, crash before the metric).
- Shape is **stacked bushes**: a small fan of co-equal options for one decision, then **descend onto that round's winner**. A flat fan off the root never accumulates wins; a noodle of single children fakes depth.

Canonical public case in this vault: [[wiki/sources/openresearch]] (`orx` / `orx-experiment-tree`). Status of «this tree is what OpenResearch actually enforces in the runner»: **Confirmed** at skill + clap + `src/local/git.rs` worktree paths; freeze/immutability of answered nodes is the **agent contract**, not independently traced as a git hook.

## Mechanism (from OpenResearch SKILL.md + `orx-experiment-tree`)

```
baseline (root)  — run command set once
    └ bush: LR 2e-5 | LR 3e-5     (siblings; co-equal options)
         └ winner ── bush: arch-A | arch-B
              └ promote / stop
run → immutable archive of recorded commit
uncommitted files never included
```

Per-completion loop (`orx exp wait --project` is a sleep-until-change signal, **not** the source of truth):

| Move | When |
|---|---|
| Repair | Run answered nothing; same node, cap two empties then ask |
| Refill | Mediocre; launch next sibling |
| Promote | Clear win; next bush hangs off *this* node |
| Stop | Goal met, or ~3 failed/regressed runs |

Session worktrees are private (`data_dir/worktrees/<projectId>/<sessionId>`). One branch has one worktree owner. After freeze: never merge/rebase that history; put a merge on a **child**.

## Contrast

| | Git-native experiment tree (OpenResearch) | Continual harness ([[wiki/concepts/continual-harness]]) | Agent-runtime multiplexer ([[wiki/concepts/agent-runtime-multiplexer]]) |
|---|---|---|---|
| What freezes | A measured *node* | Base system prompt | Nothing about experiments |
| What mutates | Child branches (code) | Supplemental H from trajectory | Which PTYs exist |
| Who authorizes a variant | Human/agent creating a child | `/refine` (weak write-gate) | Human attaching a CLI |
| Owns the loop? | **No** — wraps Claude/Codex/OpenCode/Cursor | Yes (IPython) | No — owns place |

Not a fifth harness axis. Plugin loop (DSH), style wrap (pstack), place (Herdr), supplemental-H CRUD (Prime Agent) stay the four. This is **lineage of measured variants**.

Status of «OpenResearch is strictly better than a spreadsheet + tmux for this host»: **Hypothesis** until installed and smoked. Status of «Hermes can be a registry harness»: **Refuted** at current `registry()` (four CLIs only).

## Causal map

| Cause | Effect |
|---|---|
| Vary env/`LR=… python` instead of committed config | Logged summaries stop being comparable; cardinal rule 2 broken |
| Fan every idea off the root | Wins never stack; tree looks busy and does not progress |
| Edit a node after a number lands | Lineage lies: the archived commit is no longer the code that «that» result came from |
| Infer a result from run status | Status ≠ evidence; logs are the channel (`orx-evidence`) |
| Uncommitted dirty tree at launch | Runner archives HEAD; the dirty files never ran |
| Trajectory-write of skills (`/refine`) | Different mechanism: next *prompt* changes, not next *branch* ([[wiki/concepts/memory-poisoning]]) |

## Why it matters for `pro/plan`

- Efficiency: one frozen baseline + stacked children is cheaper than re-deriving «what did we already try» from chat ([[wiki/concepts/efficiency-metric]]).
- Causal hygiene: «the experiment failed» is not one cause. Split **empty run** (repair), **answered-but-bad** (freeze + child), **status-without-log** (not evidence).
- Honest steal for Chappy: freeze-on-answer and fixed eval command — not wrapping Hermes in `orx up` (no adapter; playbook hides `orx` from the user).
- 1M eval runtime: parallel worktrees + first-completion wait is closer to a research factory than a single chat ([[25_Projects/1M_Strategy/Overview]]).

## Related

- Source: [[wiki/sources/openresearch]]
- Entity: [[wiki/entities/alphaxiv]]
- Tool: [[10_Reference/tools/openresearch]]
- Adjacent: [[wiki/concepts/continual-harness]], [[wiki/concepts/agent-runtime-multiplexer]], [[wiki/concepts/everything-is-a-plugin]], [[wiki/concepts/playbook-routed-agent-mode]], [[wiki/concepts/memory-poisoning]], [[wiki/concepts/efficiency-metric]], [[wiki/concepts/causal-analysis]]

## Sources

- [[wiki/sources/openresearch]]
