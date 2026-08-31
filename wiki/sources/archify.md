# Archify (tt-a1i/archify)

## Bibliographic / source

| Field | Value |
|---|---|
| Title | **Archify** |
| Tagline | Turn a codebase or system description into a polished, interactive system map — directly in chat |
| Author / maintainer | GitHub user [`tt-a1i`](https://github.com/tt-a1i) (no public name/bio). LICENSE: `Copyright (c) 2026 tt-a1i (Archify)` + `Copyright (c) 2025 Cocoon AI` for original `architecture-diagram-generator` |
| Fork / based_on | SKILL.md `based_on: Cocoon-AI/architecture-diagram-generator (MIT, v1.0)` |
| Repo | [tt-a1i/archify](https://github.com/tt-a1i/archify) |
| Site | https://tt-a1i.github.io/archify/ · [guide](https://tt-a1i.github.io/archify/guide.html) · [Proof Lab](https://tt-a1i.github.io/archify/gallery.html) · [start](https://tt-a1i.github.io/archify/start.html) |
| License | MIT (`LICENSE` + GitHub API `spdx_id`) |
| Language | JavaScript (Node, `"type": "module"`). Runtime **Node ≥18**; DSH bundle needs **`^22.19.0 \|\| >=24.0.0`** |
| Version at ingest | Packaged skill **2.16.0** (`archify/package.json`, `archify/skill-release.json`, GitHub release 2026-08-30). SKILL.md metadata version `"2.16"`. HEAD `main` @ `2bfb471` is *after* the release tag (visual-check wording, 2026-08-31) |
| Default branch / HEAD | `main` @ `2bfb47132c05` («Clarify visual-check as automated browser evidence (#233)», 2026-08-31). Release tree SHA in stable manifest: `a198a3e0d03cd08eb582062a52dc4b0bd5b0aa4f` |
| Stars / forks | **37516** / **2418** (GitHub API 2026-08-31) |
| Open issues | **85** (API mixes issues+PRs) |
| Created / last push | 2026-04-15 / 2026-08-31 |
| Domain | agent skill; typed JSON-IR diagrams; architecture-as-code; fail-closed HTML delivery |
| Raw capture | inbox `raw/tt-a1i-archify-readme.md`; durable [[40_Research/sources/agent-dev/tt-a1i-archify-readme]] |
| DSH plugin | `@tt-a1i/archify-dsh@0.1.0` — community, **not** an official DeepSeek product |

## One-line purpose

Agent-authored **typed JSON IR** compiled by a **zero-dependency** Node CLI into self-contained HTML/SVG diagrams (architecture / workflow / sequence / dataflow / lifecycle), with schema+layout gates and atomic last-good delivery.

## Thesis (from README + SKILL.md + package + DSH README)

1. **Not a Mermaid theme.** Mermaid may be *read* for topology, then rewritten as fresh Archify JSON. Automatic Mermaid parsing, general auto-layout, hosted sharing, and WYSIWYG editing are **out of scope**.
2. **Agent chooses layout; compiler enforces contracts.** Hierarchy, spacing, routes, emphasis are authored. Automatic endpoints spread deterministically. Showcase quality = **9 artifact checks**, 0 composition errors, 0 warnings — a 4-check receipt is «basic», never showcase.
3. **Fail closed.** `deliver` writes a same-directory candidate, checks it, atomically replaces the target only if every gate passes; failures delete the candidate and keep the previous HTML byte-for-byte. Two correction rounds on `diagnostics[].supportedFixes`; then stop and report.
4. **Three separate claims.** `deliver` = deterministic artifact checks. `visual-check` = bounded browser measurements (1440×900 … 2048×1320), receipt stays `visualReview: "pending"`. Perceptual polish needs a human / image-capable reviewer. Do not run `visual-check` after a failed deliver — that path is the *old* last-good file.
5. **Truthful interaction.** Focus, upstream/downstream reach, exact routes, role lens, and stories reuse authored nodes/edges. Reachability is **not** blast radius, breakage, or runtime impact.
6. **Source evidence is opt-in.** Architecture may pin a public repo + full commit SHA + 1–3 paths per component (`--repo-root`). Verified `SRC n` beacons are viewer-only and stripped from canonical exports. Ordinary artifacts stay source-free.
7. **Portable HTML.** One file. Exports: PNG/JPEG/WebP/SVG/WebM + 1200×630 Share / Route / Reach cards. Viewer state (focus, motion, camera) must not enter canonical exports.
8. **Optional update awareness is not auto-update.** Packaged checker GETs a *fixed* Pages URL (`skill-updates/archify/stable.json`). Never downloads/installs. ~72h (±20%) on success; failures retry 6h then 24h. Server sees IP/time, not version/agent/project. Disable: `ARCHIFY_UPDATE_CHECK_DISABLED=1`. User is the only update owner.
9. **DSH snapshot lags the skill.** `@tt-a1i/archify-dsh@0.1.0` embeds **Archify 2.14** from tag `archify-dsh-v0.1.0`. Later changes (including the update notifier) are **intentionally excluded** until a new DSH version. Targets `dsh@0.1.0-rc.6`.
10. **Stars ≠ install here.** ~37k stars in ~4.5 months; ingest is reference-only unless the user asks to install the skill.

## Architecture snapshot

```
plain description | repo | pasted Mermaid
        │
        ▼
  agent writes typed JSON IR
  (schemas/*.schema.json, additionalProperties: false)
        │
        ├─ validate --json  → diagnostics[] + supportedFixes
        ├─ preview (opt-in, 127.0.0.1, last-good iframe)
        └─ deliver --json   → candidate → gates → atomic rename + SHA-256
                │
                ├─ standalone HTML (inline SVG + viewer)
                ├─ visual-check --json  (browser evidence, not a pass)
                └─ compare architecture base.json head.json  (Before/Delta/After)
```

| Piece | Role |
|---|---|
| `archify/SKILL.md` | Portable agent skill (Cursor / Claude Code / Codex / OpenCode / Raven ZIP) |
| `archify/bin/archify.mjs` | Zero-dep CLI: `doctor`, `demo`, `guide`, `brands`, `validate`, `preview`, `deliver`, `compare`, `visual-check`, `migrate` |
| `archify/schemas/` | Five diagram schemas + `common.schema.json` |
| `archify/renderers/` | architecture / workflow / sequence / dataflow / lifecycle |
| `archify/assets/template.html` | Self-contained viewer shell (~678 KB) |
| `docs/skill-updates/archify/stable.json` | Notification-only manifest (v2.16.0, artifact sha256 `4c59fa…8946`) |
| `integrations/deepseek-harness/` | Skill-only Cordis bundle `@tt-a1i/archify-dsh` |
| `archify.zip` | Packaged skill (~1.3 MB in tree) |

### Diagram types (prompt router)

| Type | Best for | IR arrays |
|---|---|---|
| **architecture** | Components, services, storage, boundaries | `components`, `boundaries`, `connections` |
| **workflow** | CI/CD, approvals, tool calls, runbooks | `lanes`, `phases`, `groups`, `mainPath`, `nodes`, `edges` |
| **sequence** | API calls, cache miss, auth, async | `participants`, `segments`, `messages`, `activations` |
| **dataflow** | Pipelines, lineage, PII, consumers | `stages`, `nodes`, `flows` |
| **lifecycle** | States, retries, waits, terminals | `lanes`, `states`, `transitions` |

New workflows: `schema_version: 2` (`readable-v2` compiler). Keep v1 only to freeze legacy geometry. Optional architecture profile `deployment-ownership` fails closed on missing owners / region / private DB / named crossings — never inferred.

### Visual presets

`classic` (default, omit `meta.visual_preset`) · `signal-flow` · `blueprint` · `editorial`. Presets change CSS, not topology/IDs. Dark/light is independent of preset. `meta.locale` is `en` \| `zh-CN` for **viewer chrome only**; authored copy is never translated.

### Install surfaces (docs; not run here)

| Surface | Method |
|---|---|
| skills CLI | `npx skills add tt-a1i/archify -g` |
| Cursor explicit | `npx -y skills add tt-a1i/archify --skill archify --agent cursor --global --copy --yes` |
| Try without install | `npx skills use tt-a1i/archify@archify --agent codex` |
| Claude Code | `~/.claude/skills/` or `.claude/skills/` |
| Codex | `~/.agents/skills/` or `.agents/skills/` |
| OpenCode | `~/.config/opencode/skills/`, `.opencode/skills/`, or `.agents/skills/` |
| Raven | Extract `archify.zip` → `~/.raven/workspace/skills/archify` (not a start.html switcher target) |
| DSH | `dsh plugin --profile web add @tt-a1i/archify-dsh@0.1.0` |

Runtime deps in `package.json` are empty; `ajv` / `parse5` / `saxes` / `simple-icons` are **devDependencies**. Installed ZIP is meant to run without `node_modules`.

## Contrast vs vault harness axes

| | Archify | [[wiki/sources/deepseek-harness]] | [[wiki/sources/herdr]] | [[wiki/sources/prime-agent]] | [[wiki/sources/omlx]] |
|---|---|---|---|---|---|
| Owns | **Typed IR → verified HTML** | Plugin loop | PTYs | `/refine` supplemental H | Weights + KV |
| On DSH | Skill-only filesystem provider (`archify-plugin`), frozen 2.14 | Host | n/a | n/a | n/a |
| Hermes | Could be a skill drop-in; **not installed** | Separate product | Official session plugin | Reference harness | Client of `:8000` |

Archify is a **communication artifact skill**, not a fifth harness axis. Do not invent a new island next to DSH / pstack / Herdr / Prime Agent.

## Why it matters for `pro/plan`

- Causal split: a pretty picture can still be a **lie** (invented edges, reachability sold as blast radius, `visual-check` sold as a pass, failed deliver inspected as success).
- Efficiency: one validated HTML + share card vs a slide deck; Cost is Node + skill install + two repair rounds, not a hosted SaaS.
- Vault already wants living diagrams (`30_Tasks/workflows/planer.md` Mermaid rule). Archify is the **fail-closed** alternative to Mermaid-in-markdown — still **not** auto-adopted.
- DSH already in vault: community plugin proves «everything is a plugin» for *skills*, and the **2.14 vs 2.16** freeze is a version-drift lesson (same class as AMG ROADMAP vs pyproject).
- Optional update GET is an ASI-adjacent network surface: IP visible, no project data by design — still disable with `ARCHIFY_UPDATE_CHECK_DISABLED=1` if the host must stay silent.
- Adjacent to [[wiki/concepts/typed-ir-artifact-delivery]], [[wiki/concepts/everything-is-a-plugin]], [[wiki/concepts/efficiency-metric]].

## Status

- **Ingest depth:** README `main` + `archify/SKILL.md` + `archify/package.json` + `skill-release.json` + `docs/skill-updates/archify/stable.json` + DESIGN.md/PRODUCT.md heads + schemas README + DSH README/`package.json` + CHANGELOG 2.16.0 + GitHub API repo/releases/commits/recursive tree. **Not executed.** `doctor` / `deliver` / visual-check not run. Renderer source not read.
- **Confidence:** high on install surfaces, five types, fail-closed deliver, update-check contract, DSH 2.14 freeze (files + README). Medium on Proof Lab «11 scenarios / 99 checks» (author receipts in docs, not re-run). Stars are GitHub API, not homepage counters.
- **Hermes/Chappy:** **reference only**. Do not `npx skills add`, do not copy into `~/.hermes/skills/`, do not write `~/.hermes/config.yaml`.
- **Reading status:** not used in production on this host.

## Next (optional)

- [ ] Smoke `node archify/bin/archify.mjs doctor` from a cloned/ZIP tree — only if user asks to install
- [ ] Decide Hermes skill path vs leaving diagrams in Mermaid
- [ ] If DSH is ever smoked: confirm `@tt-a1i/archify-dsh@0.1.0` still pins 2.14

## Sources / provenance

- README `main` 2026-08-31, sha256 `0e0c937ef9291adebbaea1522023aebabb8675ea8405304e38d211c6da7ad006` (18697 bytes)
- GitHub API: https://api.github.com/repos/tt-a1i/archify
- Latest release: https://github.com/tt-a1i/archify/releases/tag/v2.16.0 (published 2026-08-30T11:17:04Z)
- Stable manifest: https://tt-a1i.github.io/archify/skill-updates/archify/stable.json (`publishedAt` 2026-08-30T11:13:26Z; artifact sha256 `4c59fa6557a2385beaaef8c7219cc414573acc9f0c30a932d5053b0b20689a46`)
- HEAD: `2bfb47132c057195d8dddb3e25ae966dd7c7a72e`
- Related: [[wiki/entities/archify]], [[wiki/concepts/typed-ir-artifact-delivery]], [[10_Reference/tools/archify]]
