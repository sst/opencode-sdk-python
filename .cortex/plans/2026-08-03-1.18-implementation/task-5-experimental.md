# Task 5: experimental resource Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Implement the 16 `experimental.*` operations as one flat `resources/experimental.py` module (design decision D5), with types, contract tests, and api.md entries.

**Architecture:** One module, class `ExperimentalResource`, 16 methods (sync + async), following `resources/auth.py` as the structural template and the same conventions as task 4 (params TypedDicts, `construct_type` responses, addressing params where the spec advertises them). The experimental surface spans sub-areas (capabilities, console, session, resource, controlPlane, projectCopy, workspace) but stays one module per the fork's flat style; methods are named after the operationId tail.

**Tech Stack:** Python 3.8-compatible typing, httpx, pydantic, pytest/respx.

## Global Constraints

- Branch `feat/1.18-api-surface`; commits grouped (D9) - exactly 2 commits (see step 8).
- Repo root `/workspaces/opencode-sdk-python`; gates via `nix develop --command uv ...`.
- Source of truth: `spec/openapi-opencode.json` (v1.18.11) + `.cortex/plans/2026-08-03-flake-uv-1.18-audit/missing-ops.json`.
- Addressing: ALL experimental operations carry `directory`/`workspace` EXCEPT `experimental.controlPlane.moveSession` (spec has none on it).
- Do NOT touch other tasks' files.
- Skip project-wide lint; only the named gates.

---

### Task 5: Add the experimental resource

**Files:**
- Create: `src/opencode_ai/resources/experimental.py`
- Create: response/param types under `src/opencode_ai/types/` named after the spec schemas (e.g. `experimental_workspace_list_response.py`), following existing type-file style
- Modify: `src/opencode_ai/resources/__init__.py`, `src/opencode_ai/_client.py` (wire `client.experimental`)  -> task-7 owns these; do NOT touch them
- Create: `tests/api_resources/test_experimental.py`
- api.md: task-7 owns the api.md sections + regen; do NOT touch api.md

**Interfaces:**
- Consumes: the 16 spec operations (verify exact paths/params from the spec): `experimental.capabilities.get`, `experimental.console.get`, `experimental.console.listOrgs`, `experimental.console.switchOrg`, `experimental.session.list`, `experimental.session.background`, `experimental.resource.list`, `experimental.controlPlane.moveSession`, `experimental.projectCopy.generateName`, `experimental.workspace.list/create/syncList/status/remove/warp`, `experimental.workspace.adapter.list`.
- Produces: `client.experimental.<tail>(...)` for all 16, sync + async, with param TypedDicts and response models.

- [ ] **Step 1: Extract the 16 operations from the spec**

Read `spec/openapi-opencode.json`; record path, method, query params, body, response schema for each of the 16 operationIds. Cross-check against `missing-ops.json`. Write the working table to this plan dir (`task-5-ops.md`).

- [ ] **Step 2: Study the templates**

Reuse the conventions from task 4 (same repo): `resources/auth.py` structure, addressing pattern from `resources/session.py`, response-type convention, respx test pattern from `tests/api_resources/test_auth.py` + `tests/wire_helpers.py`. Note the camelCase operationId tails (`listOrgs`, `switchOrg`, `generateName`, `syncList`): Python method names follow the operationId tail verbatim (`list_orgs`? NO - see step 3).

- [ ] **Step 3: Method naming decision (follow this exactly)**

Method names are the snake_case form of the operationId tail, per the SDK's existing convention (the spec's `session.prompt` -> `session.prompt`; camelCase tails become snake_case: `console.listOrgs` -> `console.list_orgs`, `console.switchOrg` -> `console.switch_org`, `projectCopy.generateName` -> `project_copy.generate_name`, `workspace.syncList` -> `workspace.sync_list`). The client attribute chain is `client.experimental.console.list_orgs()`, `client.experimental.workspace.sync_list()`, etc. (sub-areas are plain methods on the one module, NOT nested classes - D5). Path params and query params come verbatim from the spec.

- [ ] **Step 4: Write the failing contract tests first (TDD)**

Write `tests/api_resources/test_experimental.py`: one respx test per operation (sync; async mirrored per the existing test files' convention). Assert method+path, query params (directory/workspace where the spec has them; NOT on `control_plane.move_session`), and response construction for the operations with response schemas. For operations with no response schema, assert the call and status handling per the existing convention.

Run: `nix develop --command uv run pytest tests/api_resources/test_experimental.py -n 0 -q`
Expected: FAIL - ImportError.

- [ ] **Step 5: Implement the module and types**

Write `resources/experimental.py` (`class ExperimentalResource(SyncAPIResource)`, async twin, one method per operation), the type files, `__init__.py` export, `_client.py` accessor. Follow task 4's step 4 conventions exactly.

- [ ] **Step 6: Run tests to verify they pass**

Run: `nix develop --command uv run pytest tests/api_resources/test_experimental.py -n 0 -q`
Expected: PASS.

- [ ] **Step 7: Scoped gates**

Run:
`nix develop --command uv run ruff check src/opencode_ai/resources/experimental.py src/opencode_ai/types/experimental_*.py tests/api_resources/test_experimental.py`
`nix develop --command uv run mypy src/opencode_ai/resources/experimental.py`
`nix develop --command uv run pyright src/opencode_ai/resources/experimental.py`
Expected: all exit 0.

- [ ] **Step 7: Commit (grouped, D9 - exactly 1 commit; wiring and api.md are task-7's)**

```bash
git add src/opencode_ai/resources/experimental.py src/opencode_ai/types/experimental_*.py tests/api_resources/test_experimental.py
git commit -m "feat(resources): add experimental resource (16 ops)"
```

Expected: 1 commit. NEVER per-method commits. Do NOT stage __init__.py, _client.py, or api.md - task-7 wires them.

**Acceptance (inviolable):** steps 6, 7 pass; the naming rule from step 3 is applied; addressing per the spec (no directory/workspace on `control_plane.move_session`); 1 grouped commit. Wiring into the client (client.experimental) and api.md are task-7's acceptance - do not touch those files.

**Report format:** a diff: `git log --oneline -2` + `git show --stat` per commit, gate outputs, the ops table from step 1. If a gate cannot pass, STOP and report with output intact - do not descope.
