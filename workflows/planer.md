---
auto_execution_mode: 3
description: Planing agent
---

# Spec Generation Prompt (Repo Standard)

Use this prompt to generate a feature spec **and** a step-by-step, test-first implementation plan that matches this repository’s architecture.

## 0) Input you must ask/confirm before writing the spec

Collect these inputs (ask questions only if they are not already known):

- **Feature name** (human readable)
- **Feature slug** (kebab-case, stable). If there is an issue number, use: `<issue>-<feature-slug>`
- **Scope**: backend, frontend, both
- **Primary domain/module(s)** (e.g. `apps/backend/api/src/auction/user`)
- **Source of truth** (issue link, bug report, product request, etc.)

If anything is unclear, ask _only_ the minimum questions required.

---

## 1) Analysis phase (mandatory)

Before writing any spec files:

0. Read `/docs/architecture/README.md` and treat it as the definitive architecture source-of-truth.
   - Follow the linked documents as needed: core principles, layers, dependency matrix, validation, error handling, database, code generation, HTTP/RPC/events, testing.

1. Read the source-of-truth (issue/PR/discussion) and summarize:
   - Current behavior
   - Expected behavior
   - Impact
2. Map the **current code flow**:
   - Identify entry points (controllers/events/cron)
   - Identify orchestration (services/handlers)
   - Identify integration boundaries (adapters/registries/event-bus)
3. Find and list **prior art** (similar implementations in the repo) with file links.
4. Identify risks and edge cases.

Output of analysis must be a short “Context” section inside the spec (see requirements template below).

---

## 2) Spec output format (mandatory)

Create a folder:

- `.github/prompts/<feature-slug>/`

Inside it create exactly these files:

1. `requirements.md`
2. `design.md`
3. `tasks.md`
4. `requirements.json`
5. `acceptance-criteria.json`
6. `tasks.json`

Important:

- The result of this workflow is the **creation of these files in the repository** at the paths above (not only a chat message).
- Do not paste full file contents into chat as the final output. Create/update the files on disk, then respond with a short summary + the list of file paths.

Do **not** implement code in this step. Only produce the spec files.

---

## 2.1) Machine-readable JSON artifacts (mandatory)

Alongside the markdown spec, you must create machine-readable JSON artifacts with a strict structure.

### General JSON rules

- JSON must be valid (no comments, no trailing commas).
- Do not add extra top-level keys beyond what the templates define.
- IDs must be stable and used as **object keys** for easy linking:
  - Requirement IDs: `R1`, `R2`, …
  - Acceptance criteria IDs: `AC1.1`, `AC1.2`, …
  - Task IDs: `B1`, `B2`, … and `F1`, `F2`, …
- All cross-file references must use these IDs (strings), never implicit ordering.

### `requirements.json` template (mandatory)

```json
{
  "schemaVersion": 1,
  "order": ["R1"],
  "requirements": {
    "R1": {
      "title": "Short title",
      "type": "functional",
      "description": "Requirement description",
      "acceptanceCriteriaIds": ["AC1.1"],
      "notes": [],
      "testableEvidence": []
    }
  }
}
```

Rules:

- `type` must be one of: `functional`, `non-functional`.
- `acceptanceCriteriaIds` must reference keys that exist in `acceptance-criteria.json`.

### `acceptance-criteria.json` template (mandatory)

```json
{
  "schemaVersion": 1,
  "order": ["AC1.1"],
  "acceptanceCriteria": {
    "AC1.1": {
      "requirementId": "R1",
      "text": "Concrete, testable criterion",
      "manualVerificationSteps": [],
      "expectedResults": [],
      "notes": []
    }
  }
}
```

Rules:

- `requirementId` must reference a key that exists in `requirements.json`.
- Prefer the convention that `AC1.x` belongs to `R1`.

### `tasks.json` template (mandatory)

```json
{
  "schemaVersion": 1,
  "order": {
    "backend": ["B1"],
    "frontend": ["F1"]
  },
  "tasks": {
    "B1": {
      "title": "Task title",
      "status": 1,
      "dependsOn": [],
      "goal": "One sentence",
      "requirementIds": ["R1"],
      "acceptanceCriteriaIds": ["AC1.1"],
      "contextLinks": [
        {
          "path": "apps/backend/api/src/.../file.ts",
          "lineRange": "10-42",
          "note": ""
        }
      ],
      "verification": {
        "testPlan": {
          "files": ["apps/backend/api/src/.../__tests__/unit/...node.test.ts"],
          "red": ["What must fail before implementation"],
          "green": ["What must pass after implementation"]
        },
        "manualVerification": {
          "steps": [],
          "expectedResults": []
        }
      },
      "definitionOfDone": ["tests pass", "typescript + lint pass", "diagrams updated", "task status updated to 4"]
    }
  }
}
```

Rules:

- `status` must be `1 | 2 | 3 | 4` with the meanings defined in the tasks template.
- `dependsOn` must reference other task IDs present in this same `tasks.json`.
- A task may move from `status: 1` to `status: 2` only if all `dependsOn` tasks are `status: 4`.
- Each task must have at least one verification path:
  - either `verification.testPlan.files` is non-empty,
  - or `acceptanceCriteriaIds` is non-empty (and the referenced ACs contain manual verification details),
  - or `verification.manualVerification.steps` is non-empty.

---

## 3) `requirements.md` template (mandatory)

Write requirements in a way that is easy to reference later.

### Requirements structure rules

- Each requirement must have a stable ID: `R1`, `R2`, …
- Each acceptance criterion must have a stable ID: `AC1.1`, `AC1.2`, …
- Include explicit anchors so links do not break:
  - `R1` must have `<a id="r1"></a>`
  - `AC1.1` must have `<a id="ac1-1"></a>`

### Required sections

- **Context** (short; based on the analysis phase)
- **Goals**
- **Non-Goals / Out of Scope**
- **Definitions / Glossary** (only if needed)
- **Functional Requirements**
  - For each requirement:
    - ID + title
    - Description
    - Acceptance Criteria list
    - Notes/edge cases
- **Non-Functional Requirements** (observability, performance, security, etc.)
- **Testable Evidence**
  - For each requirement, state how we will verify it via tests (reference test cases you plan to add).

---

## 4) `design.md` template (mandatory)

The design must be compatible with `docs/architecture/README.md`.

### Architecture constraints you must follow

- Decide **sync vs async** scenarios early.
- Follow the **Golden Paths**:
  - Synchronous (HTTP/RPC): `Entry Point` → `Service` → `Registry/Adapter` → `Entry Point`.
  - Asynchronous (Events): `Event Handler` → `Service` → `Registry` → `EventBus (Publish)`.
- Layering must follow `docs/architecture/02-layers.md`:
  - Base layers: `*-schema.ts`, `*-service.ts`, `*-controller.ts` / `*-events.ts`.
  - Optional layers only when needed: `*-registry.ts`, `*-adapter.ts`, `*-handlers.ts`, `*-errors.ts`.
- Import boundaries must follow `docs/architecture/03-dependency-matrix.md`:
  - No cross-module deep imports of sources/registries.
  - Cross-module sync calls only via generated clients (`@repo/client/...`) inside Adapters.
  - Cross-module async calls via events (`*-events.ts`).
- Validation must follow `docs/architecture/08-validation.md`:
  - Input integrity validation only at boundaries: controllers, event handlers, generated RPC clients (AJV).
  - Business invariants only in service/handlers.
  - Do not re-validate JSON schema inside services.
- Error handling must follow `docs/architecture/07-error-handling.md` + `docs/architecture/01-core-principles.md`:
  - Use `@sweet-monads/either` (`left/right`) end-to-end.
  - No `try/catch` in controllers/services/handlers; `try/catch` is required in registries/adapters to convert external failures into `Either`.
  - Do not `throw` in business logic.
- Database access must follow `docs/architecture/09-database.md`:
  - `prisma.*` calls only in registries.
  - Domain boundaries: no cross-domain DB access.
- Code generation must follow `docs/architecture/10-code-generation.md`:
  - JSON Schemas are the source of truth.
  - Never edit generated files.
  - Prefer importing contract types from `@repo/contract/...`.
- Control flow & style must follow `docs/architecture/01-core-principles.md`:
  - `switch/case` allowed only for discrete states (enums/discriminated unions), not arbitrary strings.
  - Avoid deep nesting; prefer guard clauses and object maps for dispatch.
- Testing must follow `docs/architecture/11-testing.md`.

### Required sections

- **Overview**
- **Current System Behavior (brief)**
- **Proposed Behavior**
- **API / Contract changes**
  - endpoints/events/schema changes
  - migration/regeneration notes for `packages/contract`
- **Data model changes** (DB, event payloads, DTOs)
- **Flow design**
  - What calls what (controller → service → handlers → registries/adapters)
  - Idempotency / concurrency concerns
- **Error handling strategy** (Either types, error taxonomy)
- **Observability** (logging, metrics, Sentry breadcrumbs if relevant)
- **Security & permissions**
- **Prior art / similar implementations** (links)
- **Open questions** (if any)

---

## 5) `tasks.md` template (mandatory)

### Task numbering rules

- Backend tasks: `B1`, `B2`, …
- Frontend tasks: `F1`, `F2`, …
- If both exist, maintain independent sequences (B and F each start at 1).

### Task status rules (mandatory)

Every task must include a `Status` field using this numeric model:

- `1` — Open for execution
- `2` — In development
- `3` — Ready for testing
- `4` — Completed

When generating the spec, initialize **all** tasks with `Status: 1`.

During implementation, keep status up to date:

- set to `2` when you start working on the task
- set to `3` when implementation is done and it’s ready to be verified
- set to `4` only after verification is done (tests and/or acceptance criteria satisfied)

### Task dependencies & parallel implementation rules (mandatory)

Every task must include a `DependsOn` field (even if empty). This field explicitly encodes whether the task can be worked on in parallel.

- `DependsOn: []` means the task is independent and can be started in parallel with other eligible tasks.
- `DependsOn: ["B1", "F2"]` means the task is blocked until **all** listed tasks have `Status: 4`.

Scheduling rule:

- A task may be moved from `Status: 1` → `Status: 2` **only when** all tasks in `DependsOn` are `Status: 4`.
- Do not rely on “implied” order. If a task is sequentially blocked, it must be represented in `DependsOn`.
- The dependency graph must be acyclic (no circular dependencies). If you find a cycle, split/reframe tasks.

Example:

- `B1` Create table (`DependsOn: []`)
- `B2` Add filters to table (`DependsOn: ["B1"]`)
- `B3` Add authorization (`DependsOn: []`)

### TDD rules (mandatory)

- Verification of requirements must be done via tests whenever reasonably possible.
- If a task cannot be verified with automated tests, it must include explicit acceptance criteria + manual verification steps.
- Tests must be written **first** (RED), then implementation (GREEN), then refactor.
- Tests must use only **native Node modules**:
  - `node:test`
  - `node:assert/strict`
- Do not use Jest for new tests in this workflow.

If the project uses TypeScript, include in the tasks the exact way tests will be executed (e.g. compile step or Node loader) while still using `node:test` + `node:assert` APIs.

### Each task must include

For every numbered task, use this structure:

- `Bx` / `Fx`: **Title**
  - **Status**: `1 | 2 | 3 | 4` (see status rules above)
  - **DependsOn**: `[]` or `["B1", "F2"]` (see dependency rules above)
  - **Goal**: one sentence
  - **Requirements**:
    - Links to requirement anchors, e.g. `[R1](./requirements.md#r1)`
    - Links to acceptance criteria anchors, e.g. `[AC1.1](./requirements.md#ac1-1)`
  - **Context links** (repo-relative links to files):
    - Example: `[user-service.ts](../../../apps/backend/api/src/auction/user/user-service.ts)`
    - Include line ranges in plain text when useful.
  - **Verification** (mandatory):
    - **Test plan** (required field; may be `N/A`):
      - Which `node:test` test file(s) will be added/updated
      - What should fail before implementation and pass after
    - **Acceptance criteria** (required field; may be `N/A`):
      - Concrete, testable criteria (may reference `ACx.y`), and how to manually verify if no automated test is added
    - At least one of (Test plan, Acceptance criteria) must be non-`N/A`.
  - **Definition of Done**:
    - tests pass
    - typescript + lint pass
    - diagrams updated (see below)
    - task status updated to `4`

### Mandatory “living diagrams” rule

During implementation (after the spec is approved):

- After completing **each** task, you must:
  1. Update that task’s `Status` in `tasks.md` (set to `4` only after verification).
  2. Update **module documentation** in the module folder(s) touched.

Module documentation file name standard:

- `ARCHITECTURE.md` inside the primary module folder(s) being modified.

That file must always contain:

1. A Mermaid **sequence diagram** (`sequenceDiagram`) describing the current real flow.
2. A Mermaid **dataflow diagram** (`flowchart TD`) showing:
   - components
   - events/requests
   - and **explicit data structures** (fields, types, example shapes)

Any code change that affects behavior or data structures must be reflected in these diagrams immediately.

### Stop condition

When generating the spec: stop after creating the 6 files in the repository.

When implementing: execute tasks respecting `DependsOn` (do not start blocked tasks), keep tasks and diagrams up to date, and stop only when all tasks have `Status: 4` and tests are green.
