# Task 4: global_/tool/worktree resources Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Implement the 12 non-v2, non-experimental missing operations as three new resource modules: `global` (6 ops), `tool` (2 ops), `worktree` (4 ops), with types, contract tests, and api.md entries.

**Architecture:** The fork's resources are flat Stainless-style modules: one file per namespace, `SyncAPIResource`/`AsyncAPIResource` subclasses, methods taking params TypedDicts, responses built with `construct_type`/`cast`. The new modules follow `resources/auth.py` (smallest existing resource) as the structural template and `resources/session.py` for the addressing pattern. `global` is a Python keyword: module `resources/global_.py`, class `GlobalResource`, client attribute `client.global_` (design decision D4).

**Tech Stack:** Python 3.8-compatible typing, httpx, pydantic, pytest/respx.

## Global Constraints

- Branch `feat/1.18-api-surface`; commits grouped per the commit plan below (D9).
- Repo root `/workspaces/opencode-sdk-python`; gates via `nix develop --command uv ...`.
- Source of truth: `spec/openapi-opencode.json` (v1.18.11) plus the operation manifests at `.cortex/plans/2026-08-03-flake-uv-1.18-audit/local-operationIds.txt` and `missing-ops.json`.
- Addressing: `global.*` carries NO directory/workspace params (spec has none); `tool.*` and `worktree.*` DO (spec advertises them; the fork's v1 convention applies).
- Do NOT touch other tasks' files (config types, uv.lock, README, CONTRIBUTING, .stats.yml, experimental/v2 areas).
- Skip project-wide lint; only the named gates.

---

### Task 4: Add global_, tool, worktree resources

**Files:**
- Create: `src/opencode_ai/resources/global_.py`, `resources/tool.py`, `resources/worktree.py`
- Create: response/param types under `src/opencode_ai/types/` named after the spec schemas each operation uses (e.g. `global_config_get_response.py`), mirroring how existing resources name their types
- Modify: `src/opencode_ai/resources/__init__.py` (export the new resource classes)  -> task-7 owns this; do NOT touch it
- Modify: `src/opencode_ai/_client.py` (wire `client.global_`, `client.tool`, `client.worktree` as `cached_property` accessors)  -> task-7 owns this; do NOT touch it
- Create: `tests/api_resources/test_global_.py`, `test_tool.py`, `test_worktree.py`
- api.md: task-7 owns the api.md sections + regen; do NOT touch api.md

**Interfaces:**
- Consumes: spec operations `global.health/event/config.get/config.update/dispose/upgrade` (6), `tool.list/tool.ids` (2), `worktree.list/create/remove/reset` (4) - verify exact paths/params from the spec; `AddressingParams` (existing, unchanged).
- Produces: `client.global_.health(...)`, `client.global_.event(...)`, `client.global_.config.get(...)`, `client.global_.config.update(...)`, `client.global_.dispose(...)`, `client.global_.upgrade(...)`; `client.tool.list()`, `client.tool.ids()`; `client.worktree.list/create/remove/reset(...)` - each with sync and async variants, plus per-operation param TypedDicts and response models.

- [ ] **Step 1: Extract the 12 operations from the spec**

Read `spec/openapi-opencode.json`: for each of the 12 operationIds, record path, method, query params (name/in/required), request body schema, response schema. Cross-check against `missing-ops.json`. Write the working table to this plan dir (`task-4-ops.md`).

- [ ] **Step 2: Study the templates**

Read `src/opencode_ai/resources/auth.py` (structure) and `resources/session.py` lines showing the addressing-param pattern (how `directory`/`workspace` are threaded as query params - see `addressing_params` import and `maybe_transform` usage). Read one existing response type file (e.g. `types/session_delete_response.py`) for the response-model convention, and `tests/api_resources/test_auth.py` + `tests/wire_helpers.py` for the test convention.

- [ ] **Step 3: Write the failing contract tests first (TDD)**

For each of the three modules, write `tests/api_resources/test_global_.py`, `test_tool.py`, `test_worktree.py` following the respx pattern: `route_request`/`MockRouter`, assert method+path, assert query params (including `directory`/`workspace` where the spec advertises them - for tool/worktree), assert response construction via `construct_type` with a minimal payload from the spec schema. One test per operation (sync; async variants can share the sync path assertions - mirror how test_auth.py handles async).

Run: `nix develop --command uv run pytest tests/api_resources/test_global_.py tests/api_resources/test_tool.py tests/api_resources/test_worktree.py -n 0 -q`
Expected: FAIL - ImportError (modules/attributes do not exist yet).

- [ ] **Step 4: Implement the three modules**

Write `resources/global_.py` (module docstring MUST note the keyword dodge: "global is a Python keyword; the resource is exposed as client.global_"), `resources/tool.py`, `resources/worktree.py`, mirroring the template: `class GlobalResource(SyncAPIResource)` with a `with_streaming_response`/`with_raw_response` cached property per existing convention, one method per operation (sync) plus the async class, params via `maybe_transform`, responses via `cast` + `construct_type` with the new response types.

Write the response/param type files under `src/opencode_ai/types/` named per step 1's schemas, following the existing type files' style (pydantic `BaseModel` responses, TypedDict params, `__all__` exports, `PropertyInfo` where the existing files use it).

Wire `resources/__init__.py` exports and `_client.py` accessors (`global_`, `tool`, `worktree`), exactly matching how `auth` is wired.

- [ ] **Step 5: Run tests to verify they pass**

Run: `nix develop --command uv run pytest tests/api_resources/test_global_.py tests/api_resources/test_tool.py tests/api_resources/test_worktree.py -n 0 -q`
Expected: PASS.

- [ ] **Step 6: Scoped gates**

Run:
`nix develop --command uv run ruff check src/opencode_ai/resources/global_.py src/opencode_ai/resources/tool.py src/opencode_ai/resources/worktree.py src/opencode_ai/types/global_config_get_response.py src/opencode_ai/types/tool_list_response.py src/opencode_ai/types/worktree_list_response.py tests/api_resources/test_global_.py tests/api_resources/test_tool.py tests/api_resources/test_worktree.py` (adjust the type filenames to what you actually created; list ALL new files)
`nix develop --command uv run mypy src/opencode_ai/resources/global_.py src/opencode_ai/resources/tool.py src/opencode_ai/resources/worktree.py`
`nix develop --command uv run pyright src/opencode_ai/resources/global_.py src/opencode_ai/resources/tool.py src/opencode_ai/resources/worktree.py`
Expected: all exit 0. (Pyright with `pythonVersion = "3.8"` - no `|` unions, use `Optional`/`Union`.)

- [ ] **Step 7: Commit (grouped, D9 - exactly 3 commits; wiring and api.md are task-7's)**

```bash
git add src/opencode_ai/resources/global_.py src/opencode_ai/types/global_*.py tests/api_resources/test_global_.py
git commit -m "feat(resources): add global_ resource (6 ops)"
git add src/opencode_ai/resources/tool.py src/opencode_ai/types/tool_*.py tests/api_resources/test_tool.py
git commit -m "feat(resources): add tool resource (2 ops)"
git add src/opencode_ai/resources/worktree.py src/opencode_ai/types/worktree_*.py tests/api_resources/test_worktree.py
git commit -m "feat(resources): add worktree resource (4 ops)"
```

Expected: 3 commits, each grouping all files of one logical unit (resource + its types + its tests). NEVER per-method commits. Do NOT stage __init__.py, _client.py, or api.md - task-7 wires them.

**Acceptance (inviolable):** steps 5, 6 pass; the commit plan is followed; every new method exists in sync + async form with the spec's params (addressing per the spec). Wiring into the client (client.global_, client.tool, client.worktree) and api.md are task-7's acceptance - do not touch those files.

**Report format:** a diff: `git log --oneline -4` + `git show --stat` per commit, gate outputs, the ops table from step 1. If a gate cannot pass, STOP and report with output intact - do not descope.
