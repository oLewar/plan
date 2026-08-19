# Claude Cowork

Anthropic product for **skills + scheduled tasks + connectors**, used internally by their BDRs for inbound/outbound.

- Full wiki source: [[wiki/sources/anthropic-bd-claude-cowork]]
- Entity: [[wiki/entities/anthropic]]
- Concept: [[wiki/concepts/human-in-the-loop-gtm]]
- Product: https://claude.com/product/cowork
- Get started: https://support.claude.com/en/articles/13345190-get-started-with-claude-cowork
- BD webinar (author demo): https://www.anthropic.com/webinars/claude-for-business-development-representatives

## What BDRs actually run (article-level)

| Skill / job | Cadence | Connectors named |
|---|---|---|
| Inbox drafter | hourly | inbox + sales KB + voice profile |
| New-lead first touch | daytime schedule | CRM |
| No-show / gone-dark | event | Gmail, Google Calendar |
| Pipeline / Salesforce updater | as needed | Salesforce, Gmail, Gong |
| Overnight book research | nightly | Salesforce, Apollo, Common Room, Gong, warehouse |
| Discovery call coach | after calls | Gong + playbook |
| Ad-hoc: spend, unused usage, event ICP | prompt | usage data + CRM |

## Operating constraints (do not drop)

- Drafts, not auto-send.
- KB + ICP + worked-message examples before automation.
- Reject/edit reasons written back into the skill.
- Promote to shared plugin only after daily use.

## Hermes / Chappy

Reference only at ingest. Do **not** stand up auto-outbound from this host. If we reuse the pattern: Hermes skills + cron for *internal* drafts, human send remains outside the agent.
