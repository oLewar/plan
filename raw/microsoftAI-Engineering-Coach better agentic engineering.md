---
title: "microsoft/AI-Engineering-Coach: better agentic engineering"
source: "https://github.com/microsoft/AI-Engineering-Coach"
author:
published:
created: 2026-05-25
description: "better agentic engineering. Contribute to microsoft/AI-Engineering-Coach development by creating an account on GitHub."
tags:
  - "clippings"
---
## AI Engineer Coach

**better agentic engineering.**  
Analyze your AI coding assistant usage — any harness, one dashboard.

585890575-d60203ce-c678-4fdd-918e-f6c04bff04df.mp4<video src="https://private-user-images.githubusercontent.com/20464460/588526924-9f0239bf-20e0-459f-b137-17cce0edd1b2.mp4?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3Nzk2OTk3MzgsIm5iZiI6MTc3OTY5OTQzOCwicGF0aCI6Ii8yMDQ2NDQ2MC81ODg1MjY5MjQtOWYwMjM5YmYtMjBlMC00NTlmLWIxMzctMTdjY2UwZWRkMWIyLm1wND9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNjA1MjUlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjYwNTI1VDA4NTcxOFomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTJlMmE5YjU5NjUwZjFlNjNmMDM3MmNhZDllYjQxZTNkMDg1MjJiMzg2NGU1YWRhNjhhN2Y2OTU5MTMwMGRiMWUmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JnJlc3BvbnNlLWNvbnRlbnQtdHlwZT12aWRlbyUyRm1wNCJ9.RgSUHJ59rtIFJnjuZad3TYFvegK9us24wgk4EjTrY8w" controls="controls"></video>

---

## What it does

AI Engineer Coach reads your local AI session logs and turns them into actionable insights — no data leaves your machine.

- **Track progress** -- practice scores, weekly trends, daily activity charts
- **Detect anti-patterns** -- 45 rules across prompt quality, session hygiene, code review, tool mastery, and context management
- **Measure output** -- AI-generated code volume by language, workspace, model, and harness
- **Discover skills** -- find repeated prompts and turn them into reusable skills
- **Score context health** — agentic readiness checks, instruction-file audits, workspace context maps
**Screenshots**

[![Timeline](https://github.com/microsoft/AI-Engineering-Coach/raw/main/assets/screen-timeline.png)](https://github.com/microsoft/AI-Engineering-Coach/blob/main/assets/screen-timeline.png)

[![Code Output](https://github.com/microsoft/AI-Engineering-Coach/raw/main/assets/screen-output.png)](https://github.com/microsoft/AI-Engineering-Coach/blob/main/assets/screen-output.png)

[![Premium Request Consumption](https://github.com/microsoft/AI-Engineering-Coach/raw/main/assets/screen-consumption.png)](https://github.com/microsoft/AI-Engineering-Coach/blob/main/assets/screen-consumption.png)

[![Activity Patterns - Projects](https://github.com/microsoft/AI-Engineering-Coach/raw/main/assets/screen-patterns-projects.png)](https://github.com/microsoft/AI-Engineering-Coach/blob/main/assets/screen-patterns-projects.png)

[![Activity Patterns - Work Hours](https://github.com/microsoft/AI-Engineering-Coach/raw/main/assets/screen-patterns-workhours.png)](https://github.com/microsoft/AI-Engineering-Coach/blob/main/assets/screen-patterns-workhours.png)

[![Anti-Patterns](https://github.com/microsoft/AI-Engineering-Coach/raw/main/assets/screen-antipatterns.png)](https://github.com/microsoft/AI-Engineering-Coach/blob/main/assets/screen-antipatterns.png)

[![Skill Finder](https://github.com/microsoft/AI-Engineering-Coach/raw/main/assets/screen-skill-finder.png)](https://github.com/microsoft/AI-Engineering-Coach/blob/main/assets/screen-skill-finder.png)

[![Context Quality](https://github.com/microsoft/AI-Engineering-Coach/raw/main/assets/screen-context-quality.png)](https://github.com/microsoft/AI-Engineering-Coach/blob/main/assets/screen-context-quality.png)

[![Context Management](https://github.com/microsoft/AI-Engineering-Coach/raw/main/assets/screen-context-management.png)](https://github.com/microsoft/AI-Engineering-Coach/blob/main/assets/screen-context-management.png)

[![Learning Center](https://github.com/microsoft/AI-Engineering-Coach/raw/main/assets/screen-learning.png)](https://github.com/microsoft/AI-Engineering-Coach/blob/main/assets/screen-learning.png)

[![Achievements](https://github.com/microsoft/AI-Engineering-Coach/raw/main/assets/screen-achievements.png)](https://github.com/microsoft/AI-Engineering-Coach/blob/main/assets/screen-achievements.png)

[![Agentic SDLC](https://github.com/microsoft/AI-Engineering-Coach/raw/main/assets/screen-sdlc.png)](https://github.com/microsoft/AI-Engineering-Coach/blob/main/assets/screen-sdlc.png)

[![Share Your Stats](https://github.com/microsoft/AI-Engineering-Coach/raw/main/assets/screen-share.png)](https://github.com/microsoft/AI-Engineering-Coach/blob/main/assets/screen-share.png)

---

## Quick Start

```
git clone https://github.com/microsoft/ai-engineering-coach.git
cd ai-engineering-coach
npm install
npm run package
```

Then install the `.vsix`:

**macOS / Linux**

```
code --install-extension ai-engineer-coach-*.vsix
```

**Windows / PowerShell**

```
code --install-extension (Get-ChildItem . -Filter 'ai-engineer-coach-*.vsix' | Select-Object -First 1).FullName
```
1. Open the command palette (`Cmd+Shift+P` / `Ctrl+Shift+P`)
2. Run **AI Engineer Coach: Open Dashboard**
3. Navigate pages from the sidebar, filter by workspace or harness

---

## Pages

### Observe

| Page | Description |
| --- | --- |
| **Dashboard** | Practice scores with week-over-week trends, daily activity chart, top workspace stats |
| **Timeline** | Gantt-style session timeline with per-day drill-down and overlap detection |
| **Coding Moments** | Screenshot gallery from AI coding sessions with story reels and workspace filtering |

### Measure

| Page | Description |
| --- | --- |
| **Output** | Generated code volume by language, model usage table *(token breakdown temporarily hidden)* |
| **Burndown** | Monthly AI token budget progress with projections *(temporarily disabled)* |
| **Patterns** | 7×24 activity heatmap and work-life balance signals |

### Improve

| Page | Description |
| --- | --- |
| **Anti-Patterns** | Five practice score cards with severity ratings, concrete actions, and example prompts. 45 editable markdown rules plus a coverage heatmap |
| **Rule Editor** | Create, edit, and tune detection rules visually or as raw markdown. Live-test against your data |
| **Rule Playground** | Interactive REPL for the rule DSL with field browser, function catalog, and metric list |
| **Data Explorer** | Browse session fields, view distributions, run ad-hoc filters |
| **Skill Finder** | Discover repeated prompt patterns and matching community skills from the open-source catalog |
| **Context Health** | Overall context score, agentic readiness checklist, workspace context map, AI-powered instruction-file review |

### Level Up

| Page | Description |
| --- | --- |
| **Learning Center** | Personalized quizzes and code-comparison rounds generated from your actual usage |
| **Achievements** | XP-based progression with Bronze → Silver → Gold → Diamond tiers |
| **Agentic SDLC** | How you use AI across the full software-development lifecycle |
| **Share** | Generate a shareable stat card |

---

## Privacy

- **Read-only** — the extension never modifies your session files
- **Local analysis** — all parsing and analytics run entirely on your machine
- **No proprietary telemetry** — the extension does not phone home or collect usage data
- **Optional AI features** — some features (rule compiler, skill finder, context review) use the VS Code built-in Copilot language model API when explicitly invoked by the user

---

## Code of Conduct

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/). For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.

## Trademarks

This project may contain trademarks or logos for projects, products, or services. Authorized use of Microsoft trademarks or logos is subject to and must follow [Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general). Use of Microsoft trademarks or logos in modified versions of this project must not cause confusion or imply Microsoft sponsorship. Any use of third-party trademarks or logos are subject to those third-party's policies.

## License

[MIT](https://github.com/microsoft/AI-Engineering-Coach/blob/main/LICENSE)

## Disclaimer

This project is an open-source community effort by Microsoft employees. It is **not** an official Microsoft product and is not part of any Microsoft service or support offering. It is provided as-is with no warranties or guarantees.