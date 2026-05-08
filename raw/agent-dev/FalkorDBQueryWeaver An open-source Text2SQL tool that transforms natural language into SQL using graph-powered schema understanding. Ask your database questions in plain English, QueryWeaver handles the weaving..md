---
title: "FalkorDB/QueryWeaver: An open-source Text2SQL tool that transforms natural language into SQL using graph-powered schema understanding. Ask your database questions in plain English, QueryWeaver handles the weaving."
source: "https://github.com/FalkorDB/QueryWeaver"
author:
published:
created: 2026-04-26
description: "An open-source Text2SQL tool that transforms natural language into SQL using graph-powered schema understanding. Ask your database questions in plain English, QueryWeaver handles the weaving. - FalkorDB/QueryWeaver"
tags:
  - "clippings"
---
## QueryWeaver (Text2SQL)

**REST API · MCP · Graph-powered**

QueryWeaver is an **open-source Text2SQL** tool that converts plain-English questions into SQL using **graph-powered schema understanding**. It helps you ask databases natural-language questions and returns SQL and results.

Connect and ask questions:

[![new-qw-ui-gif](https://private-user-images.githubusercontent.com/182233217/532750997-34663279-0273-4c21-88a8-d20700020a07.gif?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NzcyMDU0NDQsIm5iZiI6MTc3NzIwNTE0NCwicGF0aCI6Ii8xODIyMzMyMTcvNTMyNzUwOTk3LTM0NjYzMjc5LTAyNzMtNGMyMS04OGE4LWQyMDcwMDAyMGEwNy5naWY_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjYwNDI2JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI2MDQyNlQxMjA1NDRaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1iZDdkNjQyNjRmMDgwNzcxOTNiOWIzNmUxZGZhNjU3NTdkMGIyNmM2OTY5ZDc0OWIyMDZiMzlkMzc4NDE3Mzk4JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZyZXNwb25zZS1jb250ZW50LXR5cGU9aW1hZ2UlMkZnaWYifQ.nxy0rkv1RkhrYM4dglmnHFibEyvnE1qOjm5Eo5p75nk)](https://private-user-images.githubusercontent.com/182233217/532750997-34663279-0273-4c21-88a8-d20700020a07.gif?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NzcyMDU0NDQsIm5iZiI6MTc3NzIwNTE0NCwicGF0aCI6Ii8xODIyMzMyMTcvNTMyNzUwOTk3LTM0NjYzMjc5LTAyNzMtNGMyMS04OGE4LWQyMDcwMDAyMGEwNy5naWY_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjYwNDI2JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI2MDQyNlQxMjA1NDRaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1iZDdkNjQyNjRmMDgwNzcxOTNiOWIzNmUxZGZhNjU3NTdkMGIyNmM2OTY5ZDc0OWIyMDZiMzlkMzc4NDE3Mzk4JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZyZXNwb25zZS1jb250ZW50LXR5cGU9aW1hZ2UlMkZnaWYifQ.nxy0rkv1RkhrYM4dglmnHFibEyvnE1qOjm5Eo5p75nk)

## Get Started

### Docker

> 💡 Recommended for evaluation purposes (Local Python or Node are not required)

```
docker run -p 5000:5000 -it falkordb/queryweaver
```

Launch: [http://localhost:5000](http://localhost:5000/)

---

Create a local `.env` by copying `.env.example` and passing it to Docker. This is the simplest way to provide all required configuration:

```
cp .env.example .env
# edit .env to set your values, then:
docker run -p 5000:5000 --env-file .env falkordb/queryweaver
```

### Alternative: Pass individual environment variables

If you prefer to pass variables on the command line, use `-e` flags (less convenient for many variables):

```
docker run -p 5000:5000 -it \
  -e APP_ENV=production \
  -e FASTAPI_SECRET_KEY=your_super_secret_key_here \
  -e GOOGLE_CLIENT_ID=your_google_client_id \
  -e GOOGLE_CLIENT_SECRET=your_google_client_secret \
  -e GITHUB_CLIENT_ID=your_github_client_id \
  -e GITHUB_CLIENT_SECRET=your_github_client_secret \
  -e AZURE_API_KEY=your_azure_api_key \
  falkordb/queryweaver
```

> Note: QueryWeaver supports multiple AI providers. You can use `OPENAI_API_KEY`, `GEMINI_API_KEY`, `ANTHROPIC_API_KEY`, or `AZURE_API_KEY`. See the [AI/LLM configuration](#aillm-configuration) section for details.

> For a full list of configuration options, consult `.env.example`.

## Memory TTL (optional)

QueryWeaver stores per-user conversation memory in FalkorDB. By default these graphs persist indefinitely. Set `MEMORY_TTL_SECONDS` to apply a Redis TTL (in seconds) so idle memory graphs are automatically cleaned up.

```
# Expire memory graphs after 1 week of inactivity
MEMORY_TTL_SECONDS=604800
```

The TTL is refreshed on every user interaction, so active users keep their memory.

## MCP server: host or connect (optional)

QueryWeaver includes optional support for the Model Context Protocol (MCP). You can either have QueryWeaver expose an MCP-compatible HTTP surface (so other services can call QueryWeaver as an MCP server), or configure QueryWeaver to call an external MCP server for model/context services.

What QueryWeaver provides

- The app registers MCP operations focused on Text2SQL flows:
	- `list_databases`
		- `connect_database`
		- `database_schema`
		- `query_database`
- To disable the built-in MCP endpoints set `DISABLE_MCP=true` in your `.env` or environment (default: MCP enabled).
- Configuration
- `DISABLE_MCP` — disable QueryWeaver's built-in MCP HTTP surface. Set to `true` to disable. Default: `false` (MCP enabled).

Examples

Disable the built-in MCP when running with Docker:

```
docker run -p 5000:5000 -it --env DISABLE_MCP=true falkordb/queryweaver
```

Calling the built-in MCP endpoints (example)

- The MCP surface is exposed as HTTP endpoints.

### Server Configuration

Below is a minimal example `mcp.json` client configuration that targets a local QueryWeaver instance exposing the MCP HTTP surface at `/mcp`.

```
{
   "servers": {
      "queryweaver": {
         "type": "http",
         "url": "http://127.0.0.1:5000/mcp",
         "headers": {
            "Authorization": "Bearer your_token_here"
         }
      }
   },
   "inputs": []
}
```

## REST API

### API Documentation

Swagger UI: [https://app.queryweaver.ai/docs](https://app.queryweaver.ai/docs)

OpenAPI JSON: [https://app.queryweaver.ai/openapi.json](https://app.queryweaver.ai/openapi.json)

### Overview

QueryWeaver exposes a small REST API for managing graphs (database schemas) and running Text2SQL queries. All endpoints that modify or access user-scoped data require authentication via a bearer token. In the browser the app uses session cookies and OAuth flows; for CLI and scripts you can use an API token (see `tokens` routes or the web UI to create one).

Core endpoints

- GET /graphs — list available graphs for the authenticated user
- GET /graphs/{graph\_id}/data — return nodes/links (tables, columns, foreign keys) for the graph
- POST /graphs — upload or create a graph (JSON payload or file upload)
- POST /graphs/{graph\_id} — run a Text2SQL chat query against the named graph (streaming response)

Authentication

- Add an Authorization header: `Authorization: Bearer <API_TOKEN>`

Examples

1. List graphs (GET)

curl example:

```
curl -s -H "Authorization: Bearer $TOKEN" \
   https://app.queryweaver.ai/graphs
```

Python example:

```
import requests
resp = requests.get('https://app.queryweaver.ai/graphs', headers={'Authorization': f'Bearer {TOKEN}'})
print(resp.json())
```
2. Get graph schema (GET)

curl example:

```
curl -s -H "Authorization: Bearer $TOKEN" \
   https://app.queryweaver.ai/graphs/my_database/data
```

Python example:

```
resp = requests.get('https://app.queryweaver.ai/graphs/my_database/data', headers={'Authorization': f'Bearer {TOKEN}'})
print(resp.json())
```
3. Load a graph (POST) — JSON payload
```
curl -H "Authorization: Bearer $TOKEN" -H "Content-Type: application/json" \
   -d '{"database": "my_database", "tables": [...]}' \
   https://app.queryweaver.ai/graphs
```

Or upload a file (multipart/form-data):

```
curl -H "Authorization: Bearer $TOKEN" -F "file=@schema.json" \
   https://app.queryweaver.ai/graphs
```
4. Query a graph (POST) — run a chat-based Text2SQL request

The `POST /graphs/{graph_id}` endpoint accepts a JSON body with at least a `chat` field (an array of messages). The endpoint streams processing steps and the final SQL back as server-sent-message chunks delimited by a special boundary used by the frontend. For simple scripting you can call it and read the final JSON object from the streamed messages.

Example payload:

```
{
   "chat": ["How many users signed up last month?"],
   "result": [],
   "instructions": "Prefer PostgreSQL compatible SQL"
}
```

curl example (simple, collects whole response):

```
curl -s -H "Authorization: Bearer $TOKEN" -H "Content-Type: application/json" \
   -d '{"chat": ["Count orders last week"]}' \
   https://app.queryweaver.ai/graphs/my_database
```

Python example (stream-aware):

```
import requests
import json

url = 'https://app.queryweaver.ai/graphs/my_database'
headers = {'Authorization': f'Bearer {TOKEN}', 'Content-Type': 'application/json'}
with requests.post(url, headers=headers, json={"chat": ["Count orders last week"]}, stream=True) as r:
      # The server yields JSON objects delimited by a message boundary string
      boundary = '|||FALKORDB_MESSAGE_BOUNDARY|||'
      buffer = ''
      for chunk in r.iter_content(decode_unicode=True, chunk_size=1024):
            buffer += chunk
            while boundary in buffer:
                  part, buffer = buffer.split(boundary, 1)
                  if not part.strip():
                        continue
                  obj = json.loads(part)
                  print('STREAM:', obj)
```

Notes & tips

- Graph IDs are namespaced per-user. When calling the API directly use the plain graph id (the server will namespace by the authenticated user). For uploaded files the `database` field determines the saved graph id.
- The streaming response includes intermediate reasoning steps, follow-up questions (if the query is ambiguous or off-topic), and the final SQL. The frontend expects the boundary string `|||FALKORDB_MESSAGE_BOUNDARY|||` between messages.
- For destructive SQL (INSERT/UPDATE/DELETE etc) the service will include a confirmation step in the stream; the frontend handles this flow. If you automate destructive operations, ensure you handle confirmation properly (see the `ConfirmRequest` model in the code).

## Development

Follow these steps to run and develop QueryWeaver from source.

### Prerequisites

- Python 3.12+
- uv (Python package manager)
- A FalkorDB instance (local or remote)
- Node.js and npm (for the React frontend)

### Install and configure

Quickstart (recommended for development):

```
# Clone the repo
git clone https://github.com/FalkorDB/QueryWeaver.git
cd QueryWeaver

# Install dependencies (backend + frontend) and start the dev server
make install
make run-dev
```

If you prefer to set up manually or need a custom environment, use uv:

```
# Install Python (backend) and frontend dependencies
uv sync

# Create a local environment file
cp .env.example .env
# Edit .env with your values (set APP_ENV=development for local development)
```

### Run the app locally

```
uv run uvicorn api.index:app --host 0.0.0.0 --port 5000 --reload
```

The server will be available at [http://localhost:5000](http://localhost:5000/)

Alternatively, the repository provides Make targets for running the app:

```
make run-dev   # development server (reload, debug-friendly)
make run-prod  # production mode (ensure frontend build if needed)
```

### Frontend build (when needed)

The frontend is a modern React + Vite app in `app/`. Build before production runs or after frontend changes:

```
make install       # installs backend and frontend deps
make build-prod    # builds the frontend into app/dist/

# or manually
cd app
npm ci
npm run build
```

### OAuth configuration

QueryWeaver supports Google and GitHub OAuth. Create OAuth credentials for each provider and paste the client IDs/secrets into your `.env` file.

- Google: set authorized origin and callback `http://localhost:5000/login/google/authorized`
- GitHub: set homepage and callback `http://localhost:5000/login/github/authorized`

#### Environment-specific OAuth settings

For production/staging deployments, set `APP_ENV=production` or `APP_ENV=staging` in your environment to enable secure session cookies (HTTPS-only). This prevents OAuth CSRF state mismatch errors.

```
# For production/staging (enables HTTPS-only session cookies)
APP_ENV=production

# For development (allows HTTP session cookies)
APP_ENV=development
```

**Important**: If you're getting "mismatching\_state: CSRF Warning!" errors on staging/production, ensure `APP_ENV` is set to `production` or `staging` to enable secure session handling.

### AI/LLM configuration

QueryWeaver supports multiple AI providers. Set one API key and QueryWeaver auto-detects which provider to use.

**Priority order:** Ollama > OpenAI > Gemini > Anthropic > Cohere > Azure (default)

| Provider | API Key | Default Models |
| --- | --- | --- |
| Ollama | `OLLAMA_MODEL` | `ollama/<your-model>`, `ollama/nomic-embed-text` |
| OpenAI | `OPENAI_API_KEY` | `openai/gpt-4.1`, `openai/text-embedding-ada-002` |
| Google Gemini | `GEMINI_API_KEY` | `gemini/gemini-3-pro-preview`, `gemini/gemini-embedding-001` |
| Anthropic | `ANTHROPIC_API_KEY` | `anthropic/claude-sonnet-4-5-20250929`, `voyage/voyage-3` \* |
| Cohere | `COHERE_API_KEY` | `cohere/command-a-03-2025`, `cohere/embed-v4.0` |
| Azure OpenAI | `AZURE_API_KEY` | `azure/gpt-4.1`, `azure/text-embedding-ada-002` |

\* Anthropic has no native embeddings. You must set `VOYAGE_API_KEY` or `EMBEDDING_MODEL` for embeddings, otherwise startup will fail with an error.

**Optional: Override default models**

```
COMPLETION_MODEL=gemini/gemini-3-pro-preview
EMBEDDING_MODEL=gemini/gemini-embedding-001
```

Both must match your API key's provider.

#### Docker examples with AI configuration

Using OpenAI:

```
docker run -p 5000:5000 -it \
  -e FASTAPI_SECRET_KEY=your_secret_key \
  -e OPENAI_API_KEY=your_openai_api_key \
  falkordb/queryweaver
```

Using Google Gemini:

```
docker run -p 5000:5000 -it \
  -e FASTAPI_SECRET_KEY=your_secret_key \
  -e GEMINI_API_KEY=your_gemini_api_key \
  falkordb/queryweaver
```

Using Anthropic:

```
docker run -p 5000:5000 -it \
  -e FASTAPI_SECRET_KEY=your_secret_key \
  -e ANTHROPIC_API_KEY=your_anthropic_api_key \
  falkordb/queryweaver
```

Using Azure OpenAI:

```
docker run -p 5000:5000 -it \
  -e FASTAPI_SECRET_KEY=your_secret_key \
  -e AZURE_API_KEY=your_azure_api_key \
  -e AZURE_API_BASE=https://your-resource.openai.azure.com/ \
  -e AZURE_API_VERSION=2024-12-01-preview \
  falkordb/queryweaver
```

## Testing

> Quick note: many tests require FalkorDB to be available. Use the included helper to run a test DB in Docker if needed.

### Prerequisites

- Install dev dependencies: `uv sync`
- Start FalkorDB (see `make docker-falkordb`)
- Install Playwright browsers: `uv run playwright install`

### Quick commands

Recommended: prepare the development/test environment using the Make helper (installs dependencies and Playwright browsers):

```
# Prepare development/test environment (installs deps and Playwright browsers)
make setup-dev
```

Alternatively, you can run the E2E-specific setup script and then run tests manually:

```
# Prepare E2E test environment (installs browsers and other setup)
./setup_e2e_tests.sh

# Run all tests
make test

# Run unit tests only (faster)
make test-unit

# Run E2E tests (headless)
make test-e2e

# Run E2E tests with a visible browser for debugging
make test-e2e-headed
```

### Test types

- Unit tests: focus on individual modules and utilities. Run with `make test-unit` or `uv run python -m pytest tests/ -k "not e2e"`.
- End-to-end (E2E) tests: run via Playwright and exercise UI flows, OAuth, file uploads, schema processing, chat queries, and API endpoints. Use `make test-e2e`.

See `tests/e2e/README.md` for full E2E test instructions.

### CI/CD

GitHub Actions run unit and E2E tests on pushes and pull requests. Failures capture screenshots and artifacts for debugging.

## Troubleshooting

- FalkorDB connection issues: start the DB helper `make docker-falkordb` or check network/host settings.
- Playwright/browser failures: install browsers with `uv run playwright install` and ensure system deps are present.
- Missing environment variables: copy `.env.example` and fill required values.
- **OAuth "mismatching\_state: CSRF Warning!" errors**: Set `APP_ENV=production` (or `staging`) in your environment for HTTPS deployments, or `APP_ENV=development` for HTTP development environments. This ensures session cookies are configured correctly for your deployment type.

## Project layout (high level)

- `api/` – FastAPI backend
- `app/` – React + Vite frontend
- `tests/` – unit and E2E tests

## License

Licensed under the GNU Affero General Public License (AGPL). See [LICENSE](https://github.com/FalkorDB/QueryWeaver/blob/staging/LICENSE.txt).

Copyright FalkorDB Ltd. 2025