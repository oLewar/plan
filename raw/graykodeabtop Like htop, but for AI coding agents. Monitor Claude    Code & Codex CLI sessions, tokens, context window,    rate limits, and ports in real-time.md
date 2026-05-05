---
title: "graykode/abtop: Like htop, but for AI coding agents. Monitor Claude    Code & Codex CLI sessions, tokens, context window,    rate limits, and ports in real-time."
source: "https://github.com/graykode/abtop"
author:
published:
created: 2026-04-18
description: "Like htop, but for AI coding agents. Monitor Claude    Code & Codex CLI sessions, tokens, context window,    rate limits, and ports in real-time. - graykode/abtop"
tags:
  - "clippings"
---
## abtop

**Like htop, but for your AI coding agents.**

See every Claude Code and Codex CLI session at a glance — token usage, context window %, rate limits, child processes, open ports, and more.

[![demo](https://github.com/graykode/abtop/raw/main/assets/demo.gif)](https://github.com/graykode/abtop/blob/main/assets/demo.gif)

## Why

- Running 3+ agents across projects? See them all in one screen.
- Hitting rate limits? Watch your quota in real-time.
- Agent spawned a server and forgot to kill it? Orphan port detection.
- Context window filling up? Per-session % bars with warnings.

All read-only. No API keys. No auth.

## Install

### macOS / Linux

```
curl --proto '=https' --tlsv1.2 -LsSf https://github.com/graykode/abtop/releases/latest/download/abtop-installer.sh | sh
```

### Cargo

```
cargo install abtop
```

### Other

Pre-built binaries for all platforms are available on the [GitHub Releases](https://github.com/graykode/abtop/releases) page.

## Usage

```
abtop                    # Launch TUI
abtop --once             # Print snapshot and exit
abtop --setup            # Install rate limit collection hook
abtop --theme dracula    # Launch with a specific theme
```

Recommended terminal size: **120x40** or larger. Minimum 80x24 — panels hide gracefully when small.

### Windows

abtop requires Unix tools (`ps`, `lsof`) and is not supported natively on Windows. Use [WSL](https://learn.microsoft.com/en-us/windows/wsl/install) instead:

```
wsl --install
# Inside WSL:
curl --proto '=https' --tlsv1.2 -LsSf https://github.com/graykode/abtop/releases/latest/download/abtop-installer.sh | sh
abtop
```

### tmux

abtop works standalone, but running inside tmux unlocks session jumping — press `Enter` to switch directly to the pane running that agent.

```
tmux new -s work
# pane 0: abtop
# pane 1: claude (project A)
# pane 2: claude (project B)
# → Enter on a session in abtop jumps to its pane
```

## Supported Agents

| Feature | Claude Code | Codex CLI |
| --- | --- | --- |
| Session Discovery | ✅ | ✅ |
| Token Tracking | ✅ | ✅ |
| Context Window % | ✅ | ✅ |
| Status Detection | ✅ | ✅ |
| Current Task | ✅ | ✅ |
| Rate Limit | ✅ | ✅ |
| Git Status | ✅ | ✅ |
| Children / Ports | ✅ | ✅ |
| Subagents | ✅ | ❌ |
| Memory Status | ✅ | ❌ |

## Themes

10 built-in themes, including 4 colorblind-friendly options (`high-contrast`, `protanopia`, `deuteranopia`, `tritanopia`). Press `t` to cycle at runtime, or launch with `--theme <name>`. Your choice is saved to `~/.config/abtop/config.toml`.

| btop (default) | dracula | catppuccin |
| --- | --- | --- |
| [![btop](https://github.com/graykode/abtop/raw/main/assets/themes/btop.png)](https://github.com/graykode/abtop/blob/main/assets/themes/btop.png) | [![dracula](https://github.com/graykode/abtop/raw/main/assets/themes/dracula.png)](https://github.com/graykode/abtop/blob/main/assets/themes/dracula.png) | [![catppuccin](https://github.com/graykode/abtop/raw/main/assets/themes/catppuccin.png)](https://github.com/graykode/abtop/blob/main/assets/themes/catppuccin.png) |

| tokyo-night | gruvbox | nord |
| --- | --- | --- |
| [![tokyo-night](https://github.com/graykode/abtop/raw/main/assets/themes/tokyo-night.png)](https://github.com/graykode/abtop/blob/main/assets/themes/tokyo-night.png) | [![gruvbox](https://github.com/graykode/abtop/raw/main/assets/themes/gruvbox.png)](https://github.com/graykode/abtop/blob/main/assets/themes/gruvbox.png) | [![nord](https://github.com/graykode/abtop/raw/main/assets/themes/nord.png)](https://github.com/graykode/abtop/blob/main/assets/themes/nord.png) |

Colorblind-friendly themes:

| high-contrast | protanopia |
| --- | --- |
| [![high-contrast](https://github.com/graykode/abtop/raw/main/assets/themes/high-contrast.png)](https://github.com/graykode/abtop/blob/main/assets/themes/high-contrast.png) | [![protanopia](https://github.com/graykode/abtop/raw/main/assets/themes/protanopia.png)](https://github.com/graykode/abtop/blob/main/assets/themes/protanopia.png) |

| deuteranopia | tritanopia |
| --- | --- |
| [![deuteranopia](https://github.com/graykode/abtop/raw/main/assets/themes/deuteranopia.png)](https://github.com/graykode/abtop/blob/main/assets/themes/deuteranopia.png) | [![tritanopia](https://github.com/graykode/abtop/raw/main/assets/themes/tritanopia.png)](https://github.com/graykode/abtop/blob/main/assets/themes/tritanopia.png) |

Theme support contributed by [@tbouquet](https://github.com/tbouquet).

## Key Bindings

| Key | Action |
| --- | --- |
| `↑` / `↓` or `k` / `j` | Select session |
| `Enter` | Jump to session terminal (tmux only) |
| `x` | Kill selected session |
| `X` | Kill all orphan ports |
| `t` | Cycle theme |
| `q` | Quit |
| `r` | Force refresh |

## Privacy

abtop reads local files only. No API keys, no auth. Tool names and file paths are shown in the UI, but file contents and prompt text are never displayed. Session summaries are generated via `claude --print`, which makes its own API call — this is the only indirect network usage.