# Anysite — AI-startup funding post

## Bibliographic

| Field | Value |
|---|---|
| Title | none — pasted promo, not a titled article |
| Author | **Unknown** |
| Channel | **Unknown** (user called it a Telegram promo) |
| How it arrived | pasted by the user, 2026-10-03 |
| Date of post | **Unknown** |
| Product URL | https://anysite.io/ (utm stripped; the post's link was an influencer campaign URL) |
| Report file | **absent** — not attached |
| Prompt | **absent** — not attached |
| Methodology | **absent** — the post names Claude + MCP + Anysite and stops |
| Raw capture | `[[raw/anysite-ai-startup-funding-post]]` |
| Vendor | [[wiki/entities/anysite]] |
| Tool card | [[10_Reference/tools/anysite]] |

## One-line purpose

A Telegram promo claims that Claude, wired over MCP to Anysite, produced a funding breakdown of thousands of AI startups in a couple of hours, then sells the trial.

## Thesis

### Method (author-claimed; not reproduced)

- Opened Claude.
- Connected it over MCP to Anysite (https://anysite.io/).
- Claimed a couple of hours of work, a breakdown of 7 740 AI startups, and 20 use cases.
- Named inputs: a Claude prompt, plus Crunchbase and news via Anysite. Neither the prompt nor the report file was attached.

### Claims (author-claimed; source file absent; confidence low)

Every dollar figure and every growth rate below is an author claim. Do not cite them as measurements.

- Anthropic, xAI, and Project Prometheus took $138 billion — 43% of all AI-startup money since 2020.
- In 2025 AI dollars doubled while deal count rose only 20%; money went into mega-rounds.
- By deal count the fastest growers were voice agents (+59%) and robots (+41%); by investment, Legal AI at +423% year over year.
- Public revenue was found for only 30 companies. Anthropic $65 billion a year, Cursor $4 billion.

The reusable split (dollars vs deal count) is [[wiki/concepts/capital-concentration]]. The companies named already have entity pages where the vault has them ([[wiki/entities/anthropic]], [[wiki/entities/xai]], [[wiki/entities/cursor]]); this post does not update those pages.

### Commercial offer (marketing, from the post)

- 7-day free trial of Anysite.
- A promo code for one free month of the MCP $30 tier. The code is not stored here.
- Advertised extras: social-network parsing, email finding, and closing GTM and outbound. How is not written down.

## Status

| | |
|---|---|
| Confidence | **low** on every dollar figure, every growth rate, the startup count, the use-case count, and the hours — the report file was not attached |
| Depth | pasted promo only; homepage marketing fetched separately and kept on the entity page |
| Not a harness | MCP client over someone else's datasets. Not added to the harness card. Not added to barbell. |

## Provenance

- Body: user paste, 2026-10-03. Utm query stripped from the URL inside the body. sha256 of the body after frontmatter is on the raw capture.
- Homepage: `curl` of https://anysite.io/ returned HTTP 200 on 2026-10-03 (`web_extract` failed). Product claims from that page are on [[wiki/entities/anysite]], not mixed into the four funding bullets.
- Not done: no account, no API call, no trial, no promo redemption, no Crunchbase pull, no report file.

## Sources

- `[[raw/anysite-ai-startup-funding-post]]`
