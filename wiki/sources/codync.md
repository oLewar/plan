# Codync (leepokai/Codync)

## Bibliographic / source

| Field | Value |
|---|---|
| Title | **Codync** |
| Tagline | coding agents as teammates you message (README: «1:1 alternative to Grok Bot and Muse») |
| Author | [[wiki/entities/leepokai\|Po Kai Lee (`leepokai`)]] |
| Repo | [leepokai/Codync](https://github.com/leepokai/Codync) |
| Site | https://www.codync.dev |
| App Store | https://apps.apple.com/app/codync/id6760984418 (iOS 18+; not opened) |
| Homebrew tap | https://github.com/leepokai/homebrew-codync (not ingested) |
| License | MIT (file + API `spdx_id`; copyright 2026 Po Kai Lee) |
| Language | Rust host (`codync-host`); SwiftUI apps; GTK 4 / libadwaita Linux app; TypeScript `cloud/` and `relay/` |
| Version at ingest | **v2.3.0** — `host/Cargo.toml` `version` = GitHub latest release, published 2026-10-02. HEAD `9d838b72073c` is that tag |
| Rust | edition 2024; `rust-version = "1.88"`; pinned toolchain **1.99.0** (`rust-toolchain.toml`) |
| Default branch | `main` |
| Stars / forks | **102** / **14** (GitHub API, 2026-10-02) |
| Open issues | 8 (API; mixes issues and PRs) |
| Created / last push | 2026-03-18 / 2026-10-02 |
| Topics | `acp`, `agent-client-protocol`, `claude-code`, `codex`, `coding-agents`, `gtk4`, `ios`, `linux`, `macos`, `remote-desktop`, `rust`, `swiftui` |
| Tree | **615** blobs / **199** trees, `truncated: false` |
| Domain | phone/desktop client for coding agents; ACP host; not a loop |
| Raw capture | `[[raw/leepokai-Codync-readme]]` |
| Agent contract | root [AGENTS.md](https://github.com/leepokai/Codync/blob/main/AGENTS.md) + [docs/architecture/overview.md](https://github.com/leepokai/Codync/blob/main/docs/architecture/overview.md) |

## One-line purpose

A Rust host on your computer turns installed coding agents into named bots you message from an iPhone, a Mac, a Linux desktop, or a terminal. The host does not replace those agents. It queues one turn at a time and speaks [Agent Client Protocol](https://agentclientprotocol.com) over stdio.

## Thesis

1. **Place, not a loop.** `host/src/agent/mod.rs` says the job is harness discovery, the ACP registry, sign-in, and a per-bot actor. The actor in `host/src/agent/bot.rs` owns one ACP process and runs turns one at a time. Claude Code, Codex, Cursor and the rest stay the loop.
2. **A bot is a queue, not a session.** `Actor` holds a `VecDeque`. User messages on the same lane fold into the next prompt. A bot-to-bot ask, a group turn, and a routine are separate queue items and do not feed that bot's memory (`turn_text = None`).
3. **Chat hides the trace.** The module header copies Grok Bot: the thread shows the user message, the turn's final reply, permission cards, and notices. Tool calls, thoughts, and plans are a «full conversation» sheet.
4. **Instructions are a snapshot, not `/refine`.** The same header: instructions and memory are a frozen snapshot per session and compaction epoch. `NewSession` drops the half-written episode and keeps memory. Name and skill changes ride the next message as a profile update. There is no trajectory→prompt writer.
5. **«~40 agents» is the registry, not the built-in list.** `HARNESSES` in `backends.rs` has **26** named entries (Claude Code through Poolside). Hermes is not one of them. The rest come from `https://cdn.agentclientprotocol.com/registry/v1/latest/registry.json`, refreshed every 24 h, launched via `npx`, `uvx`, or a checksummed archive under `~/.codync/agents`. That JSON is treated as untrusted path input. The live registry was not fetched.
6. **The phone is a client of the host.** Loopback HTTP + SSE for local and SSH-forwarded callers (`DEFAULT_PORT` **19222**, default bind `0.0.0.0` so a phone can use LAN or Tailscale). Remote Apple clients use an end-to-end encrypted channel, direct or via `cloud/`. The overview says end-to-end does not hide routing IDs, timing, or sizes.
7. **Major version is the phone↔host protocol.** README: apps work with hosts of the same major. AGENTS.md: do not bump major (stay on 2.x). Channel wire `v=1` and pairing URL `v=3` are separate numbers. The host has no default cloud URL; a Debug install is not production readiness (overview).

## Architecture snapshot

```
iPhone / remote Apple client
    │ encrypted channel (direct, else cloud/ ComputerRelay)
    ▼
codync-host  (one actor per bot, SQLite in ~/.codync)
    │ ACP over stdio, session/prompt
    ▼
installed coding agent (or an ACP-registry binary fetched on first use)

local app / TUI / SSH -L  ── loopback HTTP + SSE :19222 ──► same host
host alerts ── sealed ticket ──► relay/ APNs worker ──► iPhone
```

| Piece | Where | What it owns |
|---|---|---|
| Per-bot actor | `host/src/agent/bot.rs` (1602 lines) | ACP process, one turn at a time, transcript mapping |
| Built-in harnesses | `host/src/agent/backends.rs` `HARNESSES` | 26 ids; PATH hydration from the login shell |
| ACP registry | `host/src/agent/registry.rs` | CDN JSON, 24 h refresh, download / npx / uvx |
| HTTP API | `host/src/api/mod.rs` | methods + caller checks; shared with `remote/channel.rs` |
| Revisions | `host/src/store.rs` + `hub.rs` | global `rev`; clients catch up with `since` |
| Group room | `host/src/chat/group.rs` | `MAX_ROUNDS = 3`, `MAX_REPLIES = 10`; the group has no harness |
| Built-in MCP | `Actor::mcp_servers` | `connectors`, `team`, `memory`, `routines`; `computer` and `composio` only if enabled |
| Push | `relay/` | APNs tickets; host holds tickets, not the device token |
| Accounts | `cloud/` | Clerk, D1, Durable Object mailbox; chat bytes stay encrypted |
| Clients | `kit/`, `apps/ios`, `apps/macos`, `apps/linux`, `host/src/tui` | SwiftUI, GTK 4, terminal |

### Turn rules checked in `bot.rs`

| Rule | Code |
|---|---|
| One turn at a time | `next_in_queue` only starts a turn while `self.turn.is_none()` |
| Same-lane messages batch | consecutive `Queued::User` on one lane join with `\n\n` |
| Ask / group / routine skip memory | `turn_text = None` before those prompts |
| Restart resume | inflight turn younger than `STALE_RESUME_MS` = **1 hour** is resumed; older is dropped |
| Delegated turns do not silently resume | ask, group, and routine are not marked inflight; a new session must not repeat an interrupted routine |
| Stop kills a stuck ask | `CancelAsk` calls `acp.kill()` so a harness that ignores `session/cancel` cannot block the queue |
| Handshake budget | 20 s if another launch candidate remains, else 180 s |
| Profile injection | non-Claude fresh sessions get `<bot-profile>` prepended; Claude takes `_meta.systemPrompt` |
| Connector change | restarts the agent before the next turn so MCP servers reload |

### Built-in harness ids (26)

`claude`, `codex`, `cursor`, `pi`, `opencode`, `grok`, `gemini`, `copilot`, `qwen`, `goose`, `kimi`, `droid`, `amp`, `kilo`, `cline`, `auggie`, `vibe`, `kiro` (`registry: None`), `devin`, `qoder`, `codebuddy`, `minimax`, `junie`, `antigravity`, `cortex`, `poolside`.

No `hermes`. Support for anything else is «whatever the ACP registry lists», not a row in this file.

## What the README claims that the files do not settle

| Claim | Status |
|---|---|
| «1:1» with Grok Bot / Muse | Positioning. The chat model is copied (module comment). Feature parity was not checked |
| «~40 more» agents | Registry comment says ~40. Built-in table is 26. Live registry not fetched |
| Free Cloudflare relay, no subscription | README + `cloud/` exists. Account terms and quota were not read |
| End-to-end encryption | Channel uses x25519 / chacha20poly1305 in the dependency list. Wire proof not read (`docs/reference/remote-relay.md` is 51 KB and was not opened). Overview: metadata stays visible |
| Private push | README: notification text sealed to the phone key. Not traced past `remote/push.rs` |
| Usage limits from local CLIs, percentages only | README. `usage.rs` not read |
| Default bind `0.0.0.0` | Confirmed in `main.rs`, with a comment that the phone needs LAN/Tailscale. Loopback callers use a bearer token in `~/.codync`. Remote devices use their own keys |

## Why it matters for `pro/plan`

- A phone client in front of an existing agent is a **place** question, closer to [[wiki/concepts/agent-runtime-multiplexer|Herdr]] than to a new loop. Codync owns the queue and the transcript; Herdr owns the PTY. Neither writes the next prompt from the trajectory ([[wiki/concepts/continual-harness]]).
- Hermes is absent from `HARNESSES`. That is **Refuted** for the built-in list, not a claim about the ACP registry.
- Not a fifth harness axis. Do not install. The curl installer (`packaging/install.sh | sh`) was not run. Repo created 2026-03-18 — not added to [[wiki/concepts/barbell-strategy]].

## Status

- Ingest depth: README + AGENTS.md + architecture overview + `host/Cargo.toml` + `rust-toolchain.toml` + `agent/{mod,bot,backends,registry}.rs` + `api/mod.rs` (port/bind only) + `service.rs` (`DEFAULT_PORT`, data dir) + `chat/group.rs` (caps only) + GitHub API repo/tags/release/commits/languages/tree/user. **Not executed. Not installed.**
- Confidence: high on the queue, the 26-id list, the port, and the version. Medium on the relay and the cloud account model (overview only).
- Not fetched: live ACP registry JSON, `docs/reference/remote-relay.md`, `docs/features/*`, `cloud/` and `relay/` source, SwiftUI, screen/WebRTC, voice, weights, installers.

## Links

- Entity: [[wiki/entities/leepokai]]
- Concept: [[wiki/concepts/per-bot-turn-queue]]
- Tool card: [[10_Reference/tools/codync]]
- Raw: [[raw/leepokai-Codync-readme]]

## Sources / provenance

- Repo https://github.com/leepokai/Codync (`main` @ `9d838b72073c`, tag `v2.3.0`, 2026-10-02)
- README body sha256 `0729959c5cd9ca8a7f18c15d421300850c10f7f4cc70462d2e22d97e199c6d0f` (13482 bytes, LF)
- Ingested 2026-10-02. Reference only.
