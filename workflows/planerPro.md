---
auto_execution_mode: 3
description: Spec+Plan agent (Lean, JSON-first)
---

# Goal
Generate a feature spec + test-first plan that matches repo architecture (vertical feature slices, JSON Schema contracts, railway-oriented Either).

# Inputs (use assumptions if missing; ask ONLY if blocked)
Provide (best-effort from context/sourceRef):
- featureName
- featureSlug (kebab-case, stable; if issue: "<issue>-<slug>")
- scope: backend|frontend|both
- modules[] (primary folders)
- sourceRef (issue/PR/text)

# Repo constraints (must follow)
1) Read `docs/architecture/summary.json` (preferred) OR `docs/architecture/README.md` if summary missing.
2) Contracts: JSON Schemas are source of truth; generated code must not be edited.
3) Flow (sync): controller/rpc -> service -> registry/adapter -> controller
   Flow (async): event handler -> service -> registry -> publish
4) Errors: use `@sweet-monads/either` end-to-end.
   - no throw in business logic
   - no try/catch in controller/service/handlers
   - try/catch REQUIRED in registries/adapters to convert external failures into Either
5) Validation only at boundaries (controller/event handler/generated client). No schema re-validation inside service.

# Output files (JSON is source of truth)
Create `.github/prompts/<featureSlug>/` with:
1) `context.json`
2) `spec.json`
3) `tasks.json`

Do NOT implement code.

# JSON formats (strict; valid JSON; no extra top-level keys)

## context.json
{
  "schemaVersion": 1,
  "feature": { "name": "", "slug": "", "scope": "", "modules": [], "sourceRef": "" },
  "currentBehavior": "",
  "expectedBehavior": "",
  "entryPoints": [{ "path": "", "note": "" }],
  "priorArt": [{ "path": "", "note": "" }],
  "integrationBoundaries": [{ "type": "db|http|rpc|event|queue|cache|other", "path": "", "note": "" }],
  "risksAndEdgeCases": [],
  "assumptions": [],
  "openQuestions": []
}

## spec.json
{
  "schemaVersion": 1,
  "requirementsOrder": ["R1"],
  "requirements": {
    "R1": {
      "title": "",
      "type": "functional",
      "description": "",
      "acceptanceCriteria": {
        "AC1.1": { "text": "", "manualVerificationSteps": [], "expectedResults": [], "notes": [] }
      },
      "notes": [],
      "testableEvidence": []
    }
  },
  "contracts": {
    "schemas": [
      { "id": "", "kind": "http|rpc|event|dto", "path": "", "change": "add|modify|none", "notes": [] }
    ],
    "regenerationNotes": []
  },
  "design": {
    "overview": "",
    "proposedFlow": [
      { "from": "controller|eventHandler", "to": "service|handler|registry|adapter|eventBus", "note": "" }
    ],
    "dataModelChanges": [],
    "errorTaxonomy": [{ "code": "", "when": "", "mapsTo": "left|right", "notes": [] }],
    "observability": { "logs": [], "metrics": [], "traces": [] },
    "security": { "authz": [], "sensitiveData": [], "notes": [] }
  }
}

## tasks.json
{
  "schemaVersion": 1,
  "order": { "backend": ["B1"], "frontend": [] },
  "tasks": {
    "B1": {
      "title": "",
      "status": 1,
      "dependsOn": [],
      "goal": "",
      "requirementIds": ["R1"],
      "acceptanceCriteriaIds": ["AC1.1"],
      "contextLinks": [{ "path": "", "lineRange": "", "note": "" }],
      "verification": {
        "testPlan": { "files": [], "red": [], "green": [] },
        "manualVerification": { "steps": [], "expectedResults": [] }
      },
      "definitionOfDone": ["tests pass", "ts + lint pass", "docs updated", "status=4"]
    }
  }
}

# Workflow
1) Repo-scan: summarize current + expected behavior, entry points, prior art, risks -> context.json
2) Write spec.json (requirements+AC, contracts, design) using stable IDs
3) Write tasks.json (TDD-first; explicit dependsOn; at least one verification path)
4) Final response: short summary + list of file paths