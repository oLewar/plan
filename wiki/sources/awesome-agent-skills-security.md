# Awesome Agent Skills Security (LLMSecurity)

## Bibliographic / source

| Field | Value |
|---|---|
| Title | **Awesome Agent Skills Security** |
| Repo | https://github.com/LLMSecurity/awesome-agent-skills-security |
| What it is | A curated link list. Not a tool, not a scanner, not a skill pack |
| Maintainer (citation block) | Yi Liu, 2026. No other maintainer named |
| Org | `LLMSecurity` — GitHub org API: 4 public repos, no name, no blog, no description |
| Created / pushed | 2026-03-09 / 2026-09-29 |
| Stars / forks | 165 / 82 (GitHub API, 2026-09-30) |
| Topics | agent-security, ai-safety, awesome-list, llm-security, mcp, owasp, prompt-injection, tool-use |
| Tree | 3 blobs: `README.md` (234,302 bytes), `CONTRIBUTING.md` (1,725), `.github/pull_request_template.md` (517). No code, no tags |
| License | **CC0 1.0** stated at the bottom of the README. GitHub license API returned `None` — the list has no `LICENSE` file, so the API cannot see it. Trust the README line, not the API null |
| README sha256 | `7e956157801a8795c8076568f69aab9d70a74e463f0cb0b4fe1f8436f11312b5` |
| Raw capture | [[raw/LLMSecurity-awesome-agent-skills-security-readme]] |

## One-line purpose

A map of writing about attacks on, and defenses of, the tools and skills an agent is allowed to call. The security-relevant layer is the skill and the tool schema, not the chat prompt.

## What the list actually contains (counted 2026-09-30, not copied)

Entries are bold-linked items. Attack and defense entries sit under `###` headings; benchmarks, tools, and specs sit in tables. The Contents block is slightly stale: body has a subsection **Compound System Attacks** (4 entries) that Contents does not name.

| Section | Entries | Shape |
|---|---|---|
| Threat frameworks & standards | 10 | bullets. Includes OWASP Agentic AI Threats, OWASP LLM Top 10, **OWASP Agentic Skills Top 10 (AST10) v1.0 (2026)**, MITRE ATLAS, NIST AI RMF, EU AI Act |
| Surveys & systematizations | 52 | bullets |
| Attack research | **150** | 10 subsections, see below |
| Defense research | **213** | 5 subsections |
| Benchmarks & datasets | 41 | table. Sizes are the list's claims (ASB "10 agents, 398 envs", InjecAgent "1,054 cases", AgentHarm "110 behaviors") — not re-counted here |
| Tools & frameworks | 45 | table |
| Agent skill specifications | 7 | table |
| Industry reports & blog posts | 21 | bullets |
| Related awesome lists | 6 | bullets |

Attack subsections: prompt injection via tools 15, tool poisoning & supply chain 38, privilege escalation 13, data exfiltration 23, indirect prompt injection 23, agent deception 16, compound system attacks 4, cross-plugin 5, backdoor 2, jailbreaking & guardrail bypass 11.

Defense subsections: permission & access control 58, runtime monitoring & sandboxing 59, input/output validation 27, formal verification 11, evaluation & red teaming 58.

Inclusion rule, from `CONTRIBUTING.md`: agent/tool/skill security only; papers must be public (arXiv or peer-reviewed, no paywalled-only); tools must be open-source with a commit in the last 6 months; no marketing, no general LLM-safety paper that never touches a tool. Stated review time is one week. Whether they enforce it was not checked.

## Why it matters for `pro/plan`

- The list's own split matches a page already here. [[wiki/concepts/memory-poisoning]] is one write path (ASI06: a note that becomes next turn's privileged input). This list is the wider surface: the tool schema, the skill file, and the plugin boundary. AST10 is their name for that wider layer; ASI06 is one cell of it, not the whole thing.
- [[wiki/concepts/causal-analysis]]: "the model was jailbroken" and "the tool description was poisoned" are different causes. The largest attack bucket here is supply chain (38), not the classic prompt injection (15). A guard on the chat box does not touch a poisoned skill file.
- [[wiki/concepts/efficiency-metric]]: reading this list is cheap. Treating a benchmark's size cell ("1,054 test cases") as a measurement is expensive — those numbers are copied from the papers' own abstracts. Do not cite them as verified.
- Not a harness, not a scanner, not installed. Nothing in the three files is executable. Do not add a skill from a linked repo on the strength of it being listed.

## Status

- **Ingest depth**: README + CONTRIBUTING + repo/tree/tags/org API. No linked paper, tool, or benchmark was opened.
- **Confidence**: high on the counts, the CC0 line, the absent LICENSE file, the Contents/body mismatch, and the maintainer name in the citation block. Medium on org identity — the API profile is empty. Low on any claim inside a listed paper.
- **Do not cite**: a benchmark size from this list as our count; AST10's "critical" rating as a measurement; the Contents block as a complete map of the headings.

## Links

- Concept: [[wiki/concepts/skill-supply-chain]]
- Entity: [[wiki/entities/yi-liu-llmsecurity]]
- Tool card: [[10_Reference/tools/awesome-agent-skills-security]]
- Adjacent: [[wiki/concepts/memory-poisoning]], [[wiki/sources/owasp-agent-memory-guard]], [[wiki/concepts/causal-analysis]], [[wiki/concepts/efficiency-metric]]
