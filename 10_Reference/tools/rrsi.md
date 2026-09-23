# RRSI

**Regularized** test-time search over an agent harness (prompts, tools, skills, memory, control flow) with the policy model frozen. Apache-2.0. Reference only.

- Full wiki source: [[wiki/sources/rrsi]]
- Entity: [[wiki/entities/google-research]]
- Concept: [[wiki/concepts/regularized-harness-search]]
- GitHub: https://github.com/google-research/rrsi
- Paper: https://arxiv.org/abs/2609.24972
- Project: https://regularized-rsi.com/
- License: Apache-2.0
- Package version: **0.1.0** (`pyproject.toml`). No git tags / GitHub releases (2026-09-23).
- Stars: **174** (GitHub API 2026-09-23)

## Commands (README; not run here)

```bash
git clone https://github.com/google-research/rrsi.git && cd rrsi
pip install -e ".[dev]"
python3 rrsi.py --domain coding smoke
python3 rrsi.py --domain coding baseline
python3 rrsi.py --domain coding run
```

Domains: `coding` (Terminal-Bench 2.1), `workspace` (Harvey LAB), `eng` (EngDesign). Needs Vertex (`RRSI_VERTEX_PROJECTS`) plus per-domain runners (harbor, archipelago, Docker / bwrap). Do not install on this host without an explicit ask.

## Operating constraints

- Search roles default to `claude-opus-4-8` on Anthropic Vertex. Not a Hermes model slot.
- Critic rejects task-id leakage, grader gaming, and undeclared bundles **before** eval.
- Coding `w_s = 0`: inside the noise band, a score bump alone is not accepted.
- Incumbent is a git commit on `evolve/<domain>`, not a memory write.
- Not a fifth harness axis and not a `/refine` replacement for SOUL/memories.

## Mental model

Measure a harness diff, or keep `H_t`. Contrast trajectory CRUD ([[wiki/concepts/continual-harness]]), freeze-a-node lineage ([[wiki/concepts/git-native-experiment-tree]]), loop-as-plugin ([[wiki/concepts/everything-is-a-plugin]]).
