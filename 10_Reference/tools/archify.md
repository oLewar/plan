# Archify

Agent skill: **typed JSON IR → self-contained HTML/SVG diagrams** (architecture, workflow, sequence, dataflow, lifecycle). Fail-closed `deliver`. Not a Mermaid theme, not a harness.

- Full wiki source: [[wiki/sources/archify]]
- Entity: [[wiki/entities/archify]]
- Concept: [[wiki/concepts/typed-ir-artifact-delivery]]
- GitHub: https://github.com/tt-a1i/archify
- Site: https://tt-a1i.github.io/archify/
- License: MIT
- Version at ingest: **v2.16.0** (2026-08-30); HEAD `2bfb471` (2026-08-31); stars **37516** (GitHub API 2026-08-31)

## Install (docs; not run here)

```bash
npx skills add tt-a1i/archify -g
# Cursor explicit:
npx -y skills add tt-a1i/archify --skill archify --agent cursor --global --copy --yes
```

```bash
cd archify   # inside the skill package
node bin/archify.mjs doctor
node bin/archify.mjs validate architecture candidate.json --quality showcase --json
node bin/archify.mjs deliver architecture candidate.json out.html --quality showcase --json
node bin/archify.mjs visual-check out.html --json   # evidence only; not a perceptual pass
node bin/archify.mjs compare architecture base.json head.json delta.html --json
```

DSH community plugin (frozen **Archify 2.14**, not 2.16):

```bash
dsh plugin --profile web add @tt-a1i/archify-dsh@0.1.0
```

Disable reminder GET: `ARCHIFY_UPDATE_CHECK_DISABLED=1`.

## Hermes / Chappy

Could drop in as a portable `SKILL.md` (Node ≥18, no runtime npm deps). **Not verified, not installed.** At ingest: **reference only**. Do not write `~/.hermes/config.yaml` or copy into `~/.hermes/skills/`.

## Operating constraints

- Showcase = 9 artifact checks, 0 warnings. Two repair rounds on `supportedFixes`, then stop.
- Failed `deliver` preserves the previous HTML — do not `visual-check` that path as if it were the candidate.
- Reach / route / delta receipts are authored topology, not runtime impact or merge safety.
- `--repo-root` evidence is architecture-only and public-commit-pinned.
- `@tt-a1i/archify-dsh@0.1.0` ≠ latest skill; it is a 2.14 snapshot for `dsh@0.1.0-rc.6`.
- Update checker may GET Pages; it must not install. Treat as optional network.

## Mental model

**Verified diagram compiler** (IR + gates), not an agent harness. Contrast loop-replace ([[wiki/concepts/everything-is-a-plugin]]), PTY runtime ([[wiki/concepts/agent-runtime-multiplexer]]), `/refine` ([[wiki/concepts/continual-harness]]), local weights ([[wiki/concepts/tiered-kv-cache]]).
