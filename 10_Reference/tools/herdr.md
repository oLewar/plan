# Herdr

Terminal **runtime / multiplexer** for coding agents. Background server owns PTYs; TUI is a client. Does not replace Claude Code, Codex, Hermes, Grok.

- Full wiki source: [[wiki/sources/herdr]]
- Entity: [[wiki/entities/herdr]]
- Concept: [[wiki/concepts/agent-runtime-multiplexer]]
- GitHub: https://github.com/herdrdev/herdr
- Site / docs: https://herdr.dev · https://herdr.dev/docs/
- License: Apache-2.0
- Version at ingest: **v0.8.2** (2026-08-19); stars **33397** (GitHub API 2026-08-29)

## Install (docs; not run here)

```bash
curl -fsSL https://herdr.dev/install.sh | sh
herdr
```

Also: `brew install herdr` · `mise use -g herdr` · Windows `irm https://herdr.dev/install.ps1 | iex`. Detach: `ctrl+b q`. Stop everything: `herdr server stop`.

Config: `~/.config/herdr/config.toml`. Dump defaults: `herdr --default-config`.

## Hermes / Chappy

Official integration (session identity, not lifecycle authority):

```bash
herdr integration install hermes
# writes ~/.hermes/plugins/herdr-agent-state/ and enables it in config.yaml
# restart Hermes; resume: hermes --resume <id>
```

State (`working` / `blocked` / `idle`) still comes from **screen manifests**. Docs disagree on min integration version (`2` vs `5`).

Operate Herdr *from inside a pane* only when `HERDR_ENV=1`:

```bash
npx skills add herdrdev/herdr --skill herdr -g
# or: herdr --skill
```

At ingest: **reference only** — not installed on this host. Do not pipe `install.sh` or write `~/.hermes/config.yaml` without an explicit ask.

## Operating constraints

- Plugins are unsandboxed executables (full CLI/socket). Install only trusted `owner/repo`.
- `pane_history` stores terminal contents (secrets). Off by default.
- `herdr update --handoff` is experimental. Homebrew/mise/Nix cannot use Herdr's updater.
- Nested tmux inside a pane hides the agent from detection.
- Pipe-to-sh installer: review before running.

## Mental model

Server owns the herd; you attach. Details: [[wiki/concepts/agent-runtime-multiplexer]]. Contrast loop-replace ([[wiki/concepts/everything-is-a-plugin]]) and style-wrap ([[wiki/concepts/playbook-routed-agent-mode]]).
