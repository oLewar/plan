# Prime Agent

Open-source **RLM coding/research harness** from Prime Intellect. Persistent IPython is the model's tool. Built on `pi`. MIT.

- Full wiki source: [[wiki/sources/prime-agent]]
- Entity: [[wiki/entities/prime-intellect]]
- Concept: [[wiki/concepts/continual-harness]]
- GitHub: https://github.com/PrimeIntellect-ai/prime-agent
- Blog: https://www.primeintellect.ai/blog/prime-agent
- Paper: https://arxiv.org/abs/2608.23552
- License: MIT
- Version at ingest: **v0.8.1** (2026-08-26); stars **19049** (GitHub API 2026-08-29)
- Config: `~/.prime/agent/` and project `.prime/agent/`

## Install (docs; not run here)

```bash
curl -fsSL https://app.primeintellect.ai/prime-agent/install.sh | sh
cd /path/to/project
prime-agent
# first run: /login
```

Installer claims SHA-256 verify. Still a pipe-to-sh. macOS/Linux; Windows/Termux docs exist in-tree.

```bash
prime-agent agents
prime-agent attach <agent>
prime-agent --resume [path|id]
prime-agent doctor [--fix]
prime-agent shutdown [--force]
```

## Operating constraints

- Model-generated Python runs **as your user**. Workers isolate crashes, not security.
- `/refine` mutates supplemental prompts/memories/skill descriptions; base prompt is frozen; rollback exists. Treat writes as ASI06 ([[wiki/concepts/memory-poisoning]]).
- A2A only inside parent/sibling/child («nuclear family»).
- Public npm workspace names (`@earendil-works/pi-coding-agent`) are implementation details, not the install path.
- Hermes/Chappy: **reference only** — do not install without an explicit ask.

## Mental model

REPL + daemon + self-editing *supplemental* harness. Contrast loop-replace ([[wiki/concepts/everything-is-a-plugin]]), PTY runtime ([[wiki/concepts/agent-runtime-multiplexer]]), playbook wrap ([[wiki/concepts/playbook-routed-agent-mode]]).
