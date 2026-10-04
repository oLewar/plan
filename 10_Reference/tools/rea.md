# REA (`rea`)

Local CLI and MCP server that lets an agent inspect a shipped app: native binary (Hopper or bring-your-own Ghidra), managed PE, JavaScript/Electron, a package, or an already-open page. Returns evidence records. Does not recover original source.

- Full wiki source: [[wiki/sources/rea]]
- Entity: [[wiki/entities/morluto]]
- GitHub: https://github.com/morluto/rea
- npm: `rea-agents` (bins `rea`, `rea-agents`)
- License: MIT
- Version at ingest: **3.2.1** (release 2026-10-03); HEAD `405732a7f55e` is past that tag; stars **1672** (GitHub API 2026-10-04)
- MCP: stdio, `npx -y rea-agents@<version> mcp` (`src/identity.ts`). SDK `@modelcontextprotocol/server` 2.0.0

## Install (docs; not run here)

This host does not have `rea`. Do not pipe `install.sh`. Do not run `npx rea-agents setup` from this note.

```bash
npx --yes rea-agents@latest setup
npx -y rea-agents@latest doctor
```

Global: `npm install --global rea-agents`, then `rea setup`. Node `^22.19.0 || >=24.11.0`. Setup writes MCP config for Claude Code, Claude Desktop, Codex, Cursor, Gemini CLI, and Windsurf. Devin is detected and not written. Hermes is not in `SupportedClients.ts`.

## Operating constraints

- Hopper and Ghidra are separate programs. `src/application/runtime.ts` constructs both providers; Ghidra is bring-your-own (the repo says setup must not download it or Java). Hopper has its own license; demo mode is a README claim, not something this vault ran.
- Generated catalog: 122 MCP tools, 75 CLI commands, 14 providers. Skill `reverse-engineer-anything` version 23 tells the agent which tool matches the target, and says static analysis is not an execution trace.
- GitHub topics include `dsh` and `dsh-plugin`. The public tree has no `plugin.json`. This is not a DeepSeek Harness plugin and not a harness axis.
- Reference only. Not installed.
