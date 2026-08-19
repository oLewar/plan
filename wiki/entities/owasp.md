# OWASP

| Field | Value |
|---|---|
| Type | nonprofit / security standards org |
| Full name | Open Worldwide Application Security Project |
| Site | https://owasp.org/ |
| Vault project | [[wiki/sources/owasp-agent-memory-guard]] — Incubator, ASI06 reference |

## Relevance

- Держит таксономию рисков, на которую ссылаются agent-security проекты (LLM Top 10, ASI / agent security items).
- **ASI06 Memory & Context Poisoning** — слот, который закрывает Agent Memory Guard как reference implementation.
- Для `pro/plan` это якорь «стандарт, а не вендорский блог»: когда оцениваем память Hermes/wiki, сверяемся с ASI06, не только с product copy.

## What this vault currently knows

- One incubated project ingested: AMG (Python runtime guard + scanners + MCP).
- Adjacent mentions elsewhere in research dumps (Argus / agent-skills OWASP Top 10) are **not** yet first-class wiki sources.

## Related

- Source: [[wiki/sources/owasp-agent-memory-guard]]
- Concept: [[wiki/concepts/memory-poisoning]]
- Tool: [[10_Reference/tools/owasp-agent-memory-guard]]

## Sources

- [[wiki/sources/owasp-agent-memory-guard]]
