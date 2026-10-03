# Anysite

Vendor of an MCP (and a REST API) over external web datasets. Not a lab. Not a harness. Not a loop.

| Field | Value |
|---|---|
| Site | https://anysite.io/ |
| MCP endpoint (homepage sample) | `https://mcp.anysite.io/mcp` (key in the query; not called) |
| What it says it is | «Live Web Data for GTM & Marketing Teams» — typed fields (people, companies, posts, prices) pulled at query time, over MCP or API |
| Coverage (homepage claim) | 900+ sources, 5,000+ endpoints: social, e-commerce, news, finance, maps, code. Crunchbase is **not** named on the homepage; the promo names it |
| MCP price (homepage) | flat from $30/month; also $99 and $199 MCP tiers. API from $49 (usage-based credits). 7-day free trial on the plans shown |
| This ingest | [[wiki/sources/anysite-ai-startup-funding]] only |
| Installed here | **no**. Not subscribed. No account. |

Homepage fetched 2026-10-03 (`curl`, HTTP 200). `web_extract` failed. The page is marketing. The $30 MCP tier and the 7-day trial match what the promo says; the promo's free month is a code, not a homepage price.

## Contrast

- Sells a data layer an agent calls. Does not sell an agent loop ([[wiki/concepts/mcp-tool-broker]] is the safety contrast for brokers that execute commands; this page does not claim that, and it was not tested).
- Social scraping and email finding are advertised. The procedure is not recorded ([[10_Reference/tools/anysite]]).

## Sources

- https://anysite.io/ (curl, 2026-10-03)
- `[[wiki/sources/anysite-ai-startup-funding]]`
