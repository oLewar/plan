# OWASP Agent Memory Guard

## Bibliographic / source

| Field | Value |
|---|---|
| Title | **OWASP Agent Memory Guard** (AMG) |
| Org | [[wiki/entities/owasp\|OWASP Foundation]] — Incubator project |
| Leaders | Vaishnavi Gudur (creator/lead), Anshul Rajkumar (co-leader) |
| Repo | [OWASP/www-project-agent-memory-guard](https://github.com/OWASP/www-project-agent-memory-guard) |
| Site | https://owasp.org/www-project-agent-memory-guard/ |
| PyPI | [`agent-memory-guard`](https://pypi.org/project/agent-memory-guard/) · companion [`langchain-agent-memory-guard`](https://pypi.org/project/langchain-agent-memory-guard/) |
| License | Apache-2.0 |
| Language | Python ≥3.9 (`amg` CLI) |
| Version at ingest | **0.3.0** (`pyproject.toml` / `CITATION.cff`, 2026-08-19) |
| Stars / forks / issues | 140 / 38 / 14 (GitHub API, 2026-08-19) |
| Created / last push | 2026-02-16 / 2026-08-18 |
| Domain | agent memory security, ASI06 memory poisoning, runtime guardrails |
| Raw capture | `[[raw/owasp-www-project-agent-memory-guard-readme]]` |

## One-line purpose

Runtime-слой между агентом и persistent memory: каждый read/write проходит detectors + declarative policy (`allow` / `redact` / `quarantine` / `block`), чтобы **memory poisoning переживал reset контекста** и не становился privileged input на следующем ходе.

## Thesis (from README + package metadata)

1. **Другая поверхность, не input-filter.** Классические defenses смотрят user prompt. Poisoning живёт *в памяти* и переживает context reset, потому что память переживает.
2. **ASI06 reference.** Официальный OWASP Incubator; reference implementation для **ASI06 (Memory & Context Poisoning)**.
3. **Локально, без API keys.** README: median latency **59 µs**; no external calls.
4. **Policy, не один regex.** YAML: `protected_keys`, `immutable_keys`, правила на finding → action.
5. **Forensics + rollback.** Каждый decision → `SecurityEvent`; SHA-256 baselines на immutable keys; snapshots → known-good state.
6. **Provenance классов источника.** `external_tool` / `user_input` / `agent_authored` / `system` едут с каждым event (SIEM).
7. **Self-reinforcement loop.** Слишком много похожих `agent_authored` writes в одно key за cooldown — отдельный detector.

## Architecture snapshot

```
agent → MemoryGuard.write → detectors → policy → Action
                              ↓
                         MemoryStore ← allow/redact/quarantine/block
                              ↓
                         SnapshotStore → rollback / forensics
```

### Detectors present in `src/agent_memory_guard/detectors/` (tree, 2026-08-19)

| Module | Role (from names + README) |
|---|---|
| `injection.py` | prompt injection in memory writes |
| `memory_persistence_injection.py` | injection that survives persistence / reset |
| `leakage.py` | secrets / PII before store |
| `protected_keys.py` | tamper of `system.*` / identity keys |
| `anomaly.py` | size / rapid-change anomalies |
| `self_reinforcement.py` | self-similar agent_authored churn |
| `cross_task.py` | cross-task bleed |
| `excessive_autonomy.py` | autonomy / over-reach |
| `privilege_escalation.py` | privilege escalation via memory |
| `tool_abuse.py` | tool-output as injection vector |
| `ml_injection.py` | optional ML path (`[ml]` extra: transformers/torch) |

### Surfaces beyond the library

| Surface | Path / package |
|---|---|
| Core lib + CLI `amg` | `src/agent_memory_guard/` |
| LangChain history wrapper | `GuardedChatMessageHistory` |
| LangChain middleware (model+tool outputs) | `langchain-agent-memory-guard` |
| AutoGen / mem0 / CrewAI / LlamaIndex | `integrations/` + in-tree adapters |
| Redis store | `storage/redis_store.py` + extra `redis` |
| MCP server | `mcp-server/` |
| CI scanner → SARIF | composite GitHub Action `action.yml` + `scanner/` |
| Semgrep rule | `semgrep/agent-memory-unguarded` |
| Live lab | https://vgudur-amg-memory-poisoning-lab.hf.space/ |
| Colab | `examples/notebooks/poison_and_protect.ipynb` |

## Benchmark (README claim — not re-run here)

55 payloads / 4 categories. Author numbers:

| Metric | Value |
|---|---|
| Recall | 92.5% |
| Precision | 100% |
| FPR | 0% |
| Median latency | 59 µs |
| F1 | 0.961 |

By category: prompt injection 15/15; protected-key tampering 8/8; sensitive leakage 10/12; size anomaly 4/5.

Reproduce locally: `python benchmarks/security_benchmark.py`. Treat as **vendor-reported** until we run it.

## Policy sketch (README)

```yaml
version: 1
default_action: allow
protected_keys: [system.*, identity.role]
immutable_keys: [identity.user_id]
rules:
  - { name: block_prompt_injection, on: prompt_injection, action: block }
  - { name: redact_secrets,        on: sensitive_data,    action: redact }
  - { name: block_protected_keys,  on: protected_key,     action: block }
  - { name: quarantine_size,       on: size_anomaly,      action: quarantine }
```

## Version / roadmap drift (important)

- Packaged version is **0.3.0** (`pyproject.toml`).
- `ROADMAP.md` still lists LlamaIndex/CrewAI/Redis/Prometheus as **v0.3.0 Planned** — tree already has CrewAI/LlamaIndex adapters, `redis_store.py`, MCP, extra detectors, GH Action. Roadmap is stale relative to code.
- `CHANGELOG.md` formatting is broken (nested list indent); last dated unreleased note 2026-05-14. Do not treat changelog as source of truth.
- README «Who's using it» names OWASP + Microsoft research + unnamed enterprise teams — not an audited adopter list.

## Why it matters for `pro/plan`

- Прямой threat model для **persistent wiki / Hermes memories / SOUL / cron state**: всё, что агент записывает, на следующем ходе читается как privileged context.
- Паттерн [[wiki/concepts/memory-poisoning]]: memory ≠ trusted; нужен gate на write, не только на user prompt.
- Совместим с [[wiki/concepts/efficiency-metric]]: Safety в знаменателе формулы — дешёвый local guard (µs, no API) vs дорогой инцидент.
- Рядом с [[wiki/concepts/human-in-the-loop-gtm]]: HITL на send; AMG — HITL-эквивалент на *memory write* (policy вместо человека, плюс quarantine).
- Hermes/Chappy: не ставить в runtime на этом ingest. Кандидаты на оценку — wrap writes в `memories/`, snapshot scripts, plan-vault ingest, MCP if we ever expose memory tools.

## Status

- **Ingest depth:** README + GitHub API metadata + repo tree + `pyproject.toml` 0.3.0 + leaders/CITATION/action.yml/ROADMAP/CHANGELOG. **Not** code-walk of detector regexes; **not** re-run of the 55-payload benchmark.
- **Confidence:** medium-high for architecture/API shape; **low–medium** for 92.5%/0% FPR and «Microsoft uses it».
- **Hermes install:** not installed.

## Next (optional)

- [ ] Прогнать `benchmarks/security_benchmark.py` и сверить таблицу
- [ ] Сопоставить detectors с Hermes write paths (`memories/USER.md`, `SOUL.md`, vault ingest)
- [ ] Решить: research-only vs wrap Chappy memory writes

## Links

- Entity: [[wiki/entities/owasp]]
- Concept: [[wiki/concepts/memory-poisoning]]
- Tool card: [[10_Reference/tools/owasp-agent-memory-guard]]
- Related: [[wiki/concepts/efficiency-metric]], [[wiki/concepts/causal-analysis]], [[wiki/concepts/human-in-the-loop-gtm]]
- Raw: [[raw/owasp-www-project-agent-memory-guard-readme]]

## Sources / provenance

- Repo: https://github.com/OWASP/www-project-agent-memory-guard
- README raw: https://raw.githubusercontent.com/OWASP/www-project-agent-memory-guard/main/README.md
- Local capture: `raw/owasp-www-project-agent-memory-guard-readme.md` (ingested 2026-08-19, sha256 `6a26eed2ebd7ecc6d68817570259eba5ddfeaa419206fe11016b64fb54c782fd`)
- GitHub API repo + recursive tree (2026-08-19); `pyproject.toml` version 0.3.0
- User request: Telegram «добавь в базу знаний» + URL
