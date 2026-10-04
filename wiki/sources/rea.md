# REA (morluto/rea)

## Bibliographic

| Field | Value |
|---|---|
| Title | **REA: Reverse Engineer Anything** |
| Package | `rea-agents` **3.2.1** (npm bin `rea` and `rea-agents`) |
| Owner | [[wiki/entities/morluto]] |
| Repo | [morluto/rea](https://github.com/morluto/rea) |
| License | MIT (GitHub API SPDX `MIT`; `LICENSE` copyright 2026 morluto) |
| Language | TypeScript (ESM). Node `^22.19.0 \|\| >=24.11.0` |
| Created | 2026-04-14 |
| Latest release | `rea-agents-3.2.1`, published 2026-10-03 |
| HEAD | `405732a7f55e` (2026-10-04), past that tag |
| Stars | **1672** (GitHub API `stargazers_count`, 2026-10-04). Forks 170. Not a homepage counter |
| Default branch | `main` |
| Domain | Local reverse-engineering CLI and MCP server for agents |
| Raw capture | [[raw/morluto-rea-readme]] |

## One-line purpose

Один CLI и один MCP-сервер дают агенту локальные средства разобрать приложение: нативный бинарь, managed PE, JS/Electron, пакет или уже открытую страницу — и вернуть evidence, а не исходник.

## What the code does

Read from files on `main` at HEAD `405732a7f55e`, not from the README's feature tables. Not run.

- **Two entry points, one session.** `package.json` bins both names at `scripts/rea.mjs`. `src/cli.ts` builds an Incur CLI and registers setup, analysis, artifact, managed, evidence, process, policy, browser, Electron, JS-runtime, and application commands. It does not start Hopper at import. `src/main.ts` is the long-lived MCP process: stdio via `@modelcontextprotocol/server` **2.0.0**, then `createBinarySession`. `server.json` says the registry transport is stdio and the package argument is `mcp`.
- **Deep providers are Hopper and Ghidra, both constructed.** `src/application/runtime.ts` always does `new HopperProvider` and `new GhidraProvider`, then an `AnalysisProviderRegistry` with `config.analysisProvider`. Artifact graph, macOS native inspection, and managed static analysis are lazy. The generated catalog (`docs/product-catalog.json`) lists **14** providers. Hopper is declared with **37** capabilities, Ghidra with **22**. Ghidra is bring-your-own (`AGENTS.md`: setup must not download Ghidra or Java). Hopper is a separate desktop app; the README's demo/Xvfb story was not re-checked in the bridge.
- **Tool count is a generated catalog, not a slogan.** `docs/product-catalog.json` `tools.total` is **122**, in ten families (direct 39, enhanced 15, native 7, artifact 5, managed 8, browser 9, electron 5, javascript-runtime 2, application 10, session 22). The skill frontmatter repeats 122 and digest `39c2c4c55c1197e5a8c05c829bf9ba024d2508ed3a59b672f95c5ed19c016a5c`. CLI primary commands in that catalog: **75**. This vault did not recompute the digest.
- **The skill routes the target before `open_binary`.** `skills/reverse-engineer-anything/SKILL.md` (version `"23"`, same as `src/generatedPackageMetadata.ts` `skillVersion`) says: ASAR/JS tree → `analyze_javascript_application`; archive/package → `open_binary` or `inspect_artifact`; managed PE → `inspect_managed_artifact`; an already-open page → `list_browser_targets` / `list_electron_targets`; native binary → `open_binary`. It also says to skip REA for ordinary source-repo reading, and that static analysis is not an observation of execution.
- **Setup knows seven clients and writes six.** `src/application/SupportedClients.ts`: Claude Code, Claude Desktop, Codex, Cursor, Gemini CLI, Windsurf (managed), Devin (`format: "unsupported"`). The product catalog marks Devin `detect-only`. Hermes is not in the list. MCP registration is pinned to `rea-agents@<version>` (`src/identity.ts`), not a floating `@latest`, even though the CLI specifier string says `@latest`.
- **Tree.** Recursive `git/trees` on `main`: **1406** blobs, **95** trees, `truncated: false`. README raw size **62567** bytes, LF. No `plugin.json` and no Cordis bundle anywhere in that tree. GitHub topics include `dsh` and `dsh-plugin`; the code that was opened does not implement a DSH plugin.

## Why it matters for `pro/plan`

- This is an analysis backend an agent can call. It is not a harness. Not added to `10_Reference/Agents/tools/harness.md`, and not a fifth axis next to [[wiki/concepts/everything-is-a-plugin]], [[wiki/concepts/playbook-routed-agent-mode]], [[wiki/concepts/agent-runtime-multiplexer]], and [[wiki/concepts/continual-harness]].
- The `dsh` / `cordis` topics do not make it a DeepSeek Harness plugin. [[wiki/sources/deepseek-harness]] is the loop; this repo did not ship a `plugin.json`.
- The reusable split is already on [[wiki/concepts/causal-analysis]]: a decompile, a string, and a filename are not an observation that the program ran. One bullet there. No new concept page. No efficiency-metric bullet: the repo states no cost number this vault can use.
- Not added to [[wiki/concepts/barbell-strategy]]. A 2026-04 product is not a timeless object.

## Status

| | |
|---|---|
| Confidence | **high** on package version, the two entry points, the Hopper+Ghidra construction, the 122-tool catalog total, the seven-client list, and the absence of a DSH plugin in the public tree. **low** on every README claim about demo automation, checksums, and what a real Hopper or Ghidra session returns — those scripts were not run |
| Depth | README `main` + `AGENTS.md` + `package.json` + `LICENSE` + `server.json` + `src/cli.ts` + `src/main.ts` + `src/identity.ts` + `src/application/runtime.ts` + `src/application/SupportedClients.ts` + skill + `docs/product-catalog.json` + GitHub API repo/release/tags/commits/user/recursive tree. Provider wire (`bridge/hopper_bridge.py`, `src/ghidra/GhidraProvider.ts`) was not read |
| Not installed | `rea` / `rea-agents` were not installed, `npx` was not run, Hopper and Ghidra were not downloaded |
| Not a harness | Not added to the harness card |

## Open

- **Hypothesis**: whether a pinned MCP registration plus this routing skill is worth adding beside Hermes `browser_exec` is not answered by reading the tree. See [[wiki/questions/research-backlog]].

## Provenance

- Fetched 2026-10-04 via GitHub API and `raw.githubusercontent.com`. No clone.
- Raw: [[raw/morluto-rea-readme]]. Body sha256 `ff8c0c3b2578111b337fdfbf23263b92e8dccab3d9f11db5d566fc0e5f05a4e5` (62567 bytes after the closing frontmatter fence; LF, matches the raw README).

## Sources

- [[raw/morluto-rea-readme]]
