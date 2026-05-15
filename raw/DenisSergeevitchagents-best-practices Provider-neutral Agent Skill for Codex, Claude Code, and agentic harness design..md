---
title: "DenisSergeevitch/agents-best-practices: Provider-neutral Agent Skill for Codex, Claude Code, and agentic harness design."
source: "https://github.com/DenisSergeevitch/agents-best-practices"
author:
published:
created: 2026-05-16
description: "Provider-neutral Agent Skill for Codex, Claude Code, and agentic harness design. - DenisSergeevitch/agents-best-practices"
tags:
  - "clippings"
---
## agents-best-practices

[![agents-best-practices icon](https://github.com/DenisSergeevitch/agents-best-practices/raw/main/icon.jpeg)](https://github.com/DenisSergeevitch/agents-best-practices/blob/main/icon.jpeg)

`agents-best-practices` is a general-purpose Agent Skill for Codex, Claude Code, and other tools that support the `SKILL.md` skill format. It helps with designing, generating MVP blueprints for, auditing, refactoring, and explaining agentic harnesses across domains.

It is not limited to coding agents. The same harness patterns apply to research, support, operations, sales, finance, data analysis, procurement, legal workflows, healthcare workflows, education, and other workflow agents.

The skill is provider-neutral and covers OpenAI, Anthropic, and OpenAI-compatible API patterns.

## What Is Inside

The skill is organized around one entrypoint and a set of focused reference files:

- `README.md` describes the skill for public repository visitors.
- `SKILL.md` defines when to use the skill, the core stance, the default answer structure, the reference map, and non-negotiable principles.
- `references/` contains deeper guides for architecture, loops, tools, permissions, context, memory, planning, goals, MVP agent blueprints, skills, connectors, security, evals, observability, provider APIs, and checklists.

Use `SKILL.md` first, then load only the reference files needed for the user's specific harness design problem.

## Installation

### Codex

```
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
git clone https://github.com/DenisSergeevitch/agents-best-practices.git \
  "${CODEX_HOME:-$HOME/.codex}/skills/agents-best-practices"
```

Restart Codex after installation so the skill index reloads.

To update an existing installation:

```
cd "${CODEX_HOME:-$HOME/.codex}/skills/agents-best-practices"
git pull --ff-only
```

### Claude Code

Install it as a personal Claude Code skill:

```
mkdir -p "$HOME/.claude/skills"
git clone https://github.com/DenisSergeevitch/agents-best-practices.git \
  "$HOME/.claude/skills/agents-best-practices"
```

Or install it for one project:

```
mkdir -p .claude/skills
git clone https://github.com/DenisSergeevitch/agents-best-practices.git \
  .claude/skills/agents-best-practices
```

Claude Code watches existing skill directories for changes. If the top-level skills directory did not exist when Claude Code started, restart Claude Code so it can discover the new directory.

## Table of Contents

1. **Agent Harness Architecture**
	How to design the runtime around a model: context, tools, permissions, memory, observability, and stopping conditions.
2. **MVP Agent Blueprint Builder**
	How to turn a domain request into the smallest useful production-safe agent harness blueprint, including autonomy, tools, permissions, context, evals, and launch criteria.
3. **Agentic Loop**
	The core loop: model call, tool call, validation, permission check, execution, observation, then the next step or final answer.
4. **System Prompts and Instructions**
	How to structure instruction layers: global, workspace, domain-specific, task-level, and runtime reminders.
5. **Tools and Permissions**
	How to design tools that are narrow, typed, safe, auditable, and separated by risk class.
6. **Planning Mode**
	How to separate planning from execution with read-only exploration, a plan artifact, approval, and only then mutations.
7. **Goal-Like Loop**
	How to define long-running goals with budgets, checkpoints, validation criteria, and a stop condition.
8. **Context, Memory, and Auto-Compaction**
	How to manage context, retrieval, working state, durable memory, and compaction without losing critical data.
9. **Prompt Caching and Cost-Aware Context**
	How to build stable prompt prefixes, deterministic tool ordering, and a cache-friendly agent runtime.
10. **Skills and Progressive Disclosure**

How to attach reusable workflows: short skill indexes first, full instructions only when needed.

11. **MCP and External Connectors**
	How to connect external systems through governed connectors with namespacing, auth, permissions, audit logs, and least privilege.
12. **Security, Approvals, and Sandboxing**
	Prompt injection handling, secrets, approval flows, draft-versus-commit, and sandboxing for open-world tools.
13. **Observability and Evals**
	How to log agent runs, tool calls, approvals, compactions, failures, and test harnesses against real failure modes.
14. **Provider API Patterns**
	Practical implementation patterns for OpenAI, Anthropic, and OpenAI-compatible APIs without hard-coding the harness to one provider.
15. **Checklists and Coverage Audit**
	Ready-to-use checklists for launch readiness, tool additions, skills and connector integrations, and production review.

## Reference Map

- [`references/mvp-agent-blueprint.md`](https://github.com/DenisSergeevitch/agents-best-practices/blob/main/references/mvp-agent-blueprint.md): MVP harness blueprint structure, domain intake, autonomy levels, tool registry pattern, permission matrix, evals, and launch checklist.
- [`references/architecture.md`](https://github.com/DenisSergeevitch/agents-best-practices/blob/main/references/architecture.md): harness model, component boundaries, authority hierarchy, event model, and maturity levels.
- [`references/agentic-loop.md`](https://github.com/DenisSergeevitch/agents-best-practices/blob/main/references/agentic-loop.md): canonical loop, invariants, budgets, retries, parallelization, and termination rules.
- [`references/system-prompts-instructions.md`](https://github.com/DenisSergeevitch/agents-best-practices/blob/main/references/system-prompts-instructions.md): instruction hierarchy, scoped instructions, runtime reminders, and prompt templates.
- [`references/tools-and-permissions.md`](https://github.com/DenisSergeevitch/agents-best-practices/blob/main/references/tools-and-permissions.md): tool schemas, risk taxonomy, permission decisions, draft-versus-commit, tool results, sandboxing, and secrets.
- [`references/planning-and-goals.md`](https://github.com/DenisSergeevitch/agents-best-practices/blob/main/references/planning-and-goals.md): planning mode, plan artifacts, approval points, goal loops, checkpoints, and stopping conditions.
- [`references/context-memory-compaction.md`](https://github.com/DenisSergeevitch/agents-best-practices/blob/main/references/context-memory-compaction.md): context tiers, memory categories, retrieval, trust labels, cache-aware ordering, compaction, and handoff summaries.
- [`references/prompt-caching-and-cost.md`](https://github.com/DenisSergeevitch/agents-best-practices/blob/main/references/prompt-caching-and-cost.md): stable-prefix design, deterministic serialization, caching tradeoffs, and cost monitoring.
- [`references/skills-and-connectors.md`](https://github.com/DenisSergeevitch/agents-best-practices/blob/main/references/skills-and-connectors.md): Agent Skills, progressive disclosure, MCP, external connectors, tool search, and attachment strategy.
- [`references/security-evals-observability.md`](https://github.com/DenisSergeevitch/agents-best-practices/blob/main/references/security-evals-observability.md): threat models, guardrail layers, approval records, tracing, eval strategy, launch gates, and incident response.
- [`references/provider-api-patterns.md`](https://github.com/DenisSergeevitch/agents-best-practices/blob/main/references/provider-api-patterns.md): provider-neutral API design for OpenAI, Anthropic, Chat Completions-style APIs, adapters, hosted tools, streaming, and state.
- [`references/agent-legibility-feedback-loops.md`](https://github.com/DenisSergeevitch/agents-best-practices/blob/main/references/agent-legibility-feedback-loops.md): source-of-truth knowledge bases, agent-legible environments, validation loops, mechanical invariants, and recurring cleanup.
- [`references/checklists.md`](https://github.com/DenisSergeevitch/agents-best-practices/blob/main/references/checklists.md): design, tools, permissions, context, planning, goals, skills, connectors, evals, launch, and legibility checklists.
- [`references/coverage-audit.md`](https://github.com/DenisSergeevitch/agents-best-practices/blob/main/references/coverage-audit.md): coverage verification for the skill itself.
- [`references/source-links.md`](https://github.com/DenisSergeevitch/agents-best-practices/blob/main/references/source-links.md): official references for Agent Skills, OpenAI, Anthropic, MCP, and governance.

## When To Use This Skill

Use this skill when the user needs help with an agent, agentic workflow, AI worker, autonomous assistant, or harness. It is especially useful when the task involves creating an MVP agent blueprint, tool design, permission boundaries, approval-gated execution, planning mode, long-running goals, memory, compaction, skills, external connectors, security, evals, observability, cost, or provider API choices.

Do not use it for ordinary one-shot writing, translation, or Q&A unless the user is asking how to design an agent that will perform those tasks.

## Core Principle

An agent harness is the control plane around a model. The model proposes actions; the harness validates, authorizes, executes, records, summarizes, and returns observations. Keep the loop simple and make the runtime rigorous.