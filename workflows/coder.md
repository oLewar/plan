---
description: Implementator
auto_execution_mode: 3
---

# Task Implementor Workflow (tasks.json)

Implement code strictly by executing tasks defined in a feature’s `tasks.json`.

## 0) Inputs you must ask/confirm before starting

- **Feature slug** (kebab-case) OR a direct **path to** `.github/prompts/<feature-slug>/tasks.json`.
- Confirm the 3 machine-readable inputs exist:
  - `.github/prompts/<feature-slug>/tasks.json`
  - `.github/prompts/<feature-slug>/requirements.json`
  - `.github/prompts/<feature-slug>/acceptance-criteria.json`

If any of these are missing, stop and ask the minimum questions needed.

## 1) Load and follow repo standards (mandatory)

Before changing any code:

- Read `docs/architecture/README.md`.
- Follow the linked architecture standards (core principles, layers, dependency matrix, validation, error handling, database, codegen, testing).
- Respect codegen rules: do not edit generated contract files.

## 2) Pick the next task to implement (mandatory)

### Task selection algorithm

1. Load and parse the feature’s `tasks.json`.
2. Build the ordered task queue:
   - First iterate `order.backend` (in order)
   - Then iterate `order.frontend` (in order)
3. Find the **first** task that is eligible to start:
   - `tasks[taskId].status === 1`
   - All tasks in `tasks[taskId].dependsOn` exist and have `status === 4`

### If no eligible tasks exist

- If there are tasks with `status === 1` but blocked by dependencies, list them and the missing dependency IDs + statuses, then stop.
- If there are no tasks with `status === 1`, stop.

### Status transition on start

Before implementing anything:

- Update `tasks.json`: set the selected task’s `status` from `1` to `2`.
- Save the file.
- If a human-readable `tasks.md` exists for the feature, keep it in sync (update only that task’s `Status` line).

## 3) Understand requirements and acceptance criteria (mandatory)

For the selected task:

- Load all `requirementIds` from `requirements.json` and summarize them.
- Load all `acceptanceCriteriaIds` from `acceptance-criteria.json` and summarize them.
- Treat these as the source of truth for expected observable behavior.

## 4) Edge cases and corner cases first (mandatory)

Before writing tests, produce a short but complete list of:

- Golden path
- Error paths (invalid inputs, not found, permissions, conflict, etc.)
- Boundary cases (empty sets, pagination edges, time ranges, off-by-one)
- Concurrency/idempotency risks (if applicable)
- Integration boundary failures (external calls, DB, queue/event bus)

These must directly drive the test cases.

## 5) Write RED tests first (mandatory)

Write tests that cover **all outcomes and scenarios** identified above.

Rules:

- Use `node:test` and `node:assert/strict`.
- Prefer blackbox tests through the service boundary.
- Mock external IO (registries/adapters/http) when unit testing; restore mocks.
- Gate integration tests with `RUN_NODE_INTEGRATION_TESTS=true`.

Process:

1. Create/update the test file(s) listed in `tasks.json` at `verification.testPlan.files`.
2. Make tests fail in a meaningful way (RED).
3. Run tests and confirm they fail for the expected reason.

## 6) Evaluate implementation options (mandatory)

Before implementing:

- Propose at least **two** viable implementation approaches.
- Evaluate them against:
  - repo architecture rules and import boundaries
  - correctness for all edge/corner cases
  - simplicity + maintainability
  - testability
- Choose the best approach and explain why.

## 7) Implement (GREEN) and stabilize

- Implement the minimal code to make tests pass.
- Re-run tests until green.
- Refactor only after green.
- Ensure lint/type-check pass for affected packages.

## 8) Post-implementation updates (mandatory)

After implementation is complete:

- Update module documentation (`ARCHITECTURE.md`) in the touched module(s) with:
  - `sequenceDiagram`
  - `flowchart TD` including explicit data structures

Then update task status:

- Update `tasks.json`: set the task’s `status` from `2` to `3` (ready for testing).
- Save the file.
- Keep `tasks.md` in sync if present.

## 9) Output format

When you finish the task, respond with:

- **Task**: `<ID> - <title>`
- **Status change**: `1 → 2 → 3`
- **Files changed**: list
- **Tests**: what you ran + result
- **Notes for QA**: what to verify to move to `status: 4`

## Safety and repo rules

- Do not run `git commit` without explicit user approval.
- Do not edit generated files under `packages/contract`.
