# Task 6: v2 API subpackage Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Implement the 61-op `v2` API as a `resources/v2/` subpackage (design decision D1a: `client.v2.session.list(...)`), extend `AddressingParams` (D2), with types, contract tests, and api.md entries.

**Architecture:** `resources/v2/__init__.py` defines `V2Resource(SyncAPIResource)` with `cached_property` accessors returning per-area sub-resources (session, integration, pty, permission, fs, question, provider, credential, health, location, agent, model, command, skill, event, reference). Each area is its own module in the package, following the same per-method conventions as tasks 4-5. This is the frontier task: the largest surface, new addressing vocabulary (`project`/`subpath`/`cursor`), and it defines the v2 contract for the fork.

**Tech Stack:** Python 3.8-compatible typing, httpx, pydantic, pytest/respx.

## Global Constraints

- Branch `feat/1.18-api-surface`; commits grouped (D9) - exactly 4 commits (see step 9).
- Repo root `/workspaces/opencode-sdk-python`; gates via `nix develop --command uv ...`.
- Source of truth: `spec/openapi-opencode.json` (v1.18.11) + `.cortex/plans/2026-08-03-flake-uv-1.18-audit/local-operationIds.txt` (the `v2.*` entries) and `v1.18.11-manifest.json`.
- Addressing (revised 2026-08-03, from the spec; supersedes the earlier flat-only note):
  v2.session.list carries flat directory/workspace/project/subpath/cursor query params (D2: extend AddressingParams with project, subpath, cursor); ~50 other v2 ops carry an optional location deepObject query param (location[directory]/location[workspace]); v2.pty.connect carries pre-flattened location[directory]/location[workspace] plus cursor/ticket. Implement each operation's actual query params per the spec; non-addressing functional params (e.g. fs.find's query, session.messages' limit/order/cursor, permission.saved.list's projectID) are always implemented.
- Do NOT touch other tasks' files.
- Skip project-wide lint; only the named gates.

---

### Task 6: Add the v2 subpackage

**Files:**
- Create: `src/opencode_ai/resources/v2/__init__.py` plus one module per area: `session.py` (25 ops, incl. nested session.permission.*, session.question.*, session.revert.*), `integration.py` (7), `pty.py` (7), `permission.py` (3), `fs.py` (3), `question.py` (1), `provider.py` (2), `credential.py` (2), `project_copy.py` (3), `health.py` (1), `location.py` (1), `agent.py` (1), `model.py` (1), `command.py` (1), `skill.py` (1), `event.py` (1), `reference.py` (1) - 17 modules, 61 ops total. Revision 2026-08-03: counts corrected against the actual spec (session 25 not 19, permission 3 not 7, question 1 not 4; projectCopy 3 added as project_copy.py). The audit's area breakdown in the report was approximate; local-operationIds.txt and the spec are authoritative. projectCopy is IN scope: its operationIds are v2.* even though its HTTP paths start with /experimental/; the experimental worker owns only experimental.* operationIds.
- Create: response/param types under `src/opencode_ai/types/` named `v2_<area>_<op>_response.py` / `v2_<area>_<op>_params.py` style, following existing type-file style
- Modify: `src/opencode_ai/types/addressing_params.py` (D2: add `project: str`, `subpath: str`, `cursor: str`; keep `directory`, `workspace`; keep total=False and the file's style)
- Modify: `src/opencode_ai/resources/__init__.py` (export `V2Resource` and the area classes), `src/opencode_ai/_client.py` (wire `client.v2`)  -> task-7 owns these; do NOT touch them
- Create: `tests/api_resources/test_v2_session.py`, `test_v2_integration.py`, `test_v2_pty.py`, `test_v2_permission.py`, `test_v2_misc.py` (fs/question/provider/credential/health/location/agent/model/command/skill/event/reference grouped)
- api.md: task-7 owns the v2 sections + regen; do NOT touch api.md

**Interfaces:**
- Consumes: the 61 `v2.*` operations (operationId tails, exact paths/params/bodies/responses from the spec; the audit's area breakdown is authoritative for grouping).
- Produces: `client.v2.<area>.<tail>(...)` for all 61, sync + async, with param TypedDicts and response models; `AddressingParams` extended with project/subpath/cursor.

- [ ] **Step 1: Extract the 61 operations from the spec**

Read `spec/openapi-opencode.json`; build the full op table (path, method, params, body, response schema) for every `v2.*` operationId. Cross-check counts against `local-operationIds.txt` (authoritative; the audit's area breakdown in the report is approximate - see the Files list for the corrected 17-area/61-op split). Write the working table to this plan dir (`task-6-ops.md`).

- [ ] **Step 2: Study the templates + decide naming**

Read `resources/auth.py` (structure), `resources/session.py` (addressing + method patterns), one response type file, `tests/wire_helpers.py`. Naming rule: method = snake_case of the operationId tail (e.g. `v2.session.prompt` -> `session.prompt`, `v2.pty.connect-token` -> `pty.connect_token`, `v2.permission.request.list` -> `permission.request_list` - use the tail after `v2.<area>.`; where the tail itself has a dot (`permission.request.list`, `permission.saved.list`, `session.permission.list`, `session.question.list`, `question.request.list`), the method name keeps the full tail in snake_case, e.g. `permission.request_list(...)`. State your final mapping in `task-6-ops.md` before implementing.

- [ ] **Step 3: Extend AddressingParams + write the failing tests first (TDD)**

First extend `types/addressing_params.py` (add `project`, `subpath`, `cursor`). Then write the test files: one respx test per operation covering method+path, query params (directory/workspace/project/subpath/cursor on `v2.session.list`; none elsewhere), and response construction for operations with response schemas. `tests/api_resources/test_v2_misc.py` groups the singleton areas.

Run: `nix develop --command uv run pytest tests/api_resources/test_v2_session.py tests/api_resources/test_v2_integration.py tests/api_resources/test_v2_pty.py tests/api_resources/test_v2_permission.py tests/api_resources/test_v2_misc.py -n 0 -q`
Expected: FAIL - ImportError.

- [ ] **Step 4: Implement the package skeleton**

Write `resources/v2/__init__.py` with `V2Resource` + `cached_property` accessors (one per area, mirroring how `_client.py` wires top-level resources), and stub-free modules per area implementing the methods from step 1's table (sync + async, params via `maybe_transform`, responses via `cast` + `construct_type`). Write the type files as you go.

- [ ] **Step 5: Run tests to verify they pass**

Run: `nix develop --command uv run pytest tests/api_resources/test_v2_session.py tests/api_resources/test_v2_integration.py tests/api_resources/test_v2_pty.py tests/api_resources/test_v2_permission.py tests/api_resources/test_v2_misc.py -n 0 -q`
Expected: PASS.

- [ ] **Step 6: Scoped gates**

Run:
`nix develop --command uv run ruff check src/opencode_ai/resources/v2 src/opencode_ai/types/addressing_params.py src/opencode_ai/types/v2_*.py tests/api_resources/test_v2_*.py`
`nix develop --command uv run mypy src/opencode_ai/resources/v2 src/opencode_ai/types/addressing_params.py`
`nix develop --command uv run pyright src/opencode_ai/resources/v2`
Expected: all exit 0.

- [ ] **Step 7: Commit (grouped, D9 - exactly 3 commits; wiring and api.md are task-7's)**

```bash
git add src/opencode_ai/types/addressing_params.py
git commit -m "feat(types): extend AddressingParams with v2 project/subpath/cursor fields"
git add src/opencode_ai/resources/v2 src/opencode_ai/types/v2_*.py
git commit -m "feat(v2): add v2 API subpackage (61 ops)"
git add tests/api_resources/test_v2_*.py
git commit -m "feat(v2): add contract tests for v2 resources"
```

Expected: 3 commits. NEVER per-module or per-method commits. Do NOT stage __init__.py, _client.py, or api.md - task-7 wires them.

**Acceptance (inviolable):** steps 5, 6 pass; all 61 operations implemented sync + async with the spec's shapes; `AddressingParams` extended (not duplicated); the commit plan followed. Wiring into the client (client.v2) and api.md are task-7's acceptance - do not touch those files.

**Report format:** a diff: `git log --oneline -4` + `git show --stat` per commit, gate outputs, the naming mapping from step 2. If a gate cannot pass, STOP and report with output intact - do not descope.
