---
title: "Leonxlnx/taste-skill: Taste-Skill (High-Agency Frontend) - gives your AI good taste. stops the AI from generating boring, generic, \"slop\""
source: "https://github.com/Leonxlnx/taste-skill"
author:
published:
created: 2026-04-19
description: "Taste-Skill (High-Agency Frontend) - gives your AI good taste. stops the AI from generating boring, generic, \"slop\"  - Leonxlnx/taste-skill: Taste-Skill (High-Agency Frontend) - gives your AI good taste. stops the AI from generating boring, generic, \"slop\""
tags:
  - "clippings"
---
## Taste Skill

A collection of skills that improve how AI tools write frontend code. Instead of generating generic, boring interfaces, the AI builds modern, premium designs with proper animations, spacing, and visual quality.

## Taste Skill v2 Beta

A major update is in progress. If you want early access, sign up for the beta:

[Join the Waitlist](https://tasteskillv2.vercel.app/)

## Feedback & Contributions

I'd love to hear your thoughts! If you have suggestions or find any bugs:

- Open a Pull Request or Issue right here on GitHub
- DM me on [x.com/lexnlin](https://x.com/lexnlin)
- Email me at [hello@learn2vibecode.dev](mailto:hello@learn2vibecode.dev)

## Installing

Works via CLI for all major AI coding agents (Cursor, Antigravity, Claude Code, Codex, Windsurf, Copilot, etc.):

```
npx skills add https://github.com/Leonxlnx/taste-skill
```

## Skills

| Skill | Description |
| --- | --- |
| **taste-skill** | The main design skill for premium frontend code. Covers layout, typography, colors, spacing, and motion. |
| **gpt-taste** | Premium Awwwards-level frontend/UI skill with deterministic randomization checks and strict GSAP animation requirements. |
| **redesign-skill** | For upgrading existing projects by auditing and fixing design problems first. |
| **soft-skill** | Focuses on an expensive, soft UI look with premium fonts, whitespace, depth, and smooth spring animations. |
| **output-skill** | Stops the AI from being lazy. Prevents placeholder comments, skipped code blocks, and half-finished outputs. |
| **minimalist-skill** | For clean, editorial-style interfaces inspired by tools like Notion and Linear. Monochrome, crisp borders. |
| **brutalist-skill** | ⚠️  `BETA` Raw mechanical interfaces fusing Swiss typographic print with CRT terminal aesthetics. |
| **stitch-skill** | Google Stitch-compatible semantic design rules for premium AI UI generation. Includes DESIGN.md for export. |

## Settings (taste-skill only)

The taste skill has three settings at the top of the file. Change these numbers (1-10) depending on what you're building:

- **DESIGN\_VARIANCE** — How experimental the layout is. (1-3: Clean/centered | 8-10: Asymmetric/modern)
- **MOTION\_INTENSITY** — How much animation there is. (1-3: Simple hover | 8-10: Magnetic/scroll-triggered)
- **VISUAL\_DENSITY** — How much content fits on one screen. (1-3: Spacious/luxury | 8-10: Dense dashboards)

## Examples

Created with taste-skill:

[![](https://github.com/Leonxlnx/taste-skill/raw/main/examples/floria-top.webp)](https://github.com/Leonxlnx/taste-skill/blob/main/examples/floria-top.webp) [![](https://github.com/Leonxlnx/taste-skill/raw/main/examples/floria-bottom.webp)](https://github.com/Leonxlnx/taste-skill/blob/main/examples/floria-bottom.webp)

## Support the project

If you find **taste-skill** useful, consider sponsoring the development.

[Sponsor on GitHub](https://github.com/sponsors/Leonxlnx)

### Current Sponsors

[![u2393696078-rgb](https://github.com/u2393696078-rgb.png "u2393696078-rgb")](https://github.com/u2393696078-rgb) [![mccun934](https://github.com/mccun934.png "mccun934")](https://github.com/mccun934) [![ghughes7](https://github.com/ghughes7.png "ghughes7")](https://github.com/ghughes7) [![AtharvaJaiswal005](https://github.com/AtharvaJaiswal005.png "AtharvaJaiswal005")](https://github.com/AtharvaJaiswal005)

## Research

Background research that informed how these skills were built. See the [research](https://github.com/Leonxlnx/taste-skill/blob/main/research) folder.

## Common Questions

**How is this different from other AI design skills?** Taste Skill includes 7 specialized variants instead of a single file, a 3-dial parameterization system for adjustable output, and anti-repetition rules backed by original research. It is framework-agnostic and works across all major agents.

**Does it work with React, Vue, Svelte, etc.?** Yes. Taste Skill is framework-agnostic. The rules focus on design decisions, not framework-specific code patterns.

**What is a SKILL.md file?** A portable instruction file that AI coding agents detect and follow automatically. No configuration is needed, just install it and your agent reads it.