# Codync

Phone and desktop **client** for coding agents you already have. Rust host queues one turn per bot over ACP. Does not replace Claude Code, Codex, Cursor, or Hermes. **Hermes is not in the built-in harness list.**

- Full wiki source: [[wiki/sources/codync]]
- Entity: [[wiki/entities/leepokai]]
- Concept: [[wiki/concepts/per-bot-turn-queue]]
- GitHub: https://github.com/leepokai/Codync
- Site: https://www.codync.dev
- License: MIT
- Version at ingest: **v2.3.0** (2026-10-02); HEAD `9d838b72073c` is that tag; stars **102** (GitHub API 2026-10-02)
- Host: `codync-host`, default port **19222**, data dir `~/.codync` (`CODYNC_HOME` overrides)

## Install (docs; not run here)

This host does not have `codync-host`. Do not pipe the installer.

```bash
curl -fsSL https://raw.githubusercontent.com/leepokai/Codync/main/packaging/install.sh | sh
codync-host serve          # foreground, default 0.0.0.0:19222
codync-host tui
codync-host pair
```

Mac cask: `brew install --cask leepokai/codync/codync`. iPhone: App Store id `6760984418`. Linux host formula: `brew install leepokai/codync/codync-host`.

## Operating constraints

- Default bind is all interfaces, so a phone on the LAN can connect. Loopback helpers use a bearer token in `~/.codync`. Remote devices use their own keys (`codync-host devices`).
- Built-in backends are 26 named CLIs. Anything else is downloaded from the ACP registry on first use (`npx`, `uvx`, or a binary under `~/.codync/agents`).
- The host injects its own MCP servers into the agent (`team`, `memory`, `routines`, and `computer` if the bot has screen access).
- Major version must match between phone and host. Stay on 2.x unless you mean a protocol break.
- Reference only. Not installed.

## Mental model

The bot is a queue in front of someone else's agent. Details: [[wiki/concepts/per-bot-turn-queue]]. Contrast PTY place ([[wiki/concepts/agent-runtime-multiplexer]]) and loop-replace ([[wiki/concepts/everything-is-a-plugin]]).
