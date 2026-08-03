# Task 1: Spec faithfulness (subagent_depth + with_raw_response) Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Fix the two hand-back findings: (1) `client.global.config.update()` must accept `subagent_depth` (the spec's Config schema has it; the worker mirrored the fork's incomplete pattern); (2) the 5 new namespaces (global_, tool, worktree, experimental, v2) must expose `with_raw_response` wrappers like every existing resource.

**Architecture:** Existing resources (e.g. auth.py, session.py) expose `with_raw_response` and `with_streaming_response` via `cached_property` on the sync resource class. The new modules were written without them. The global update params type omits `subagent_depth` because the worker copied the fork's `types/config_update_params.py`-adjacent pattern.

**Tech Stack:** Python 3.8-compatible typing, pydantic, pytest/respx.

## Global Constraints

- Branch feat/1.18-api-surface; ONE grouped commit at the end.
- Repo root /workspaces/opencode-sdk-python; gates via `nix develop --command uv ...`.
- Touch only: `src/opencode_ai/resources/global_.py`, `tool.py`, `worktree.py`, `experimental.py`, `resources/v2/` (module files), the global update params type file (`src/opencode_ai/types/global_config_update_params.py` or the actual name used), `types/config.py` ONLY if the paired fix needs it, and the test files `tests/api_resources/test_global_.py`, `test_tool.py`, `test_worktree.py`, `test_experimental.py`, `test_v2_*.py`. Do NOT touch api.md, .gitignore, .python-version, flake.nix, uv.lock (other workers own them).
- Skip project-wide lint; only the named gates.

---

### Task 1: Faithfulness fixes

**Files:** per Global Constraints.

**Interfaces:**
- Consumes: spec/openapi-opencode.json `components.schemas.Config` (`subagent_depth: integer, minimum 0`); the with_raw_response pattern in `src/opencode_ai/resources/auth.py`.
- Produces: `global.config.update(..., subagent_depth=...)` typed and accepted; `client.with_raw_response.global_.health(...)` etc. working for all 5 namespaces.

- [ ] **Step 1: Confirm the gaps (fail-first evidence)**

Run:
`grep -n "subagent_depth" src/opencode_ai/types/global_config_update_params.py src/opencode_ai/resources/global_.py; grep -n "with_raw_response" src/opencode_ai/resources/auth.py | head -5; grep -c "with_raw_response" src/opencode_ai/resources/global_.py src/opencode_ai/resources/tool.py src/opencode_ai/resources/worktree.py src/opencode_ai/resources/experimental.py src/opencode_ai/resources/v2/*.py`
Expected: subagent_depth absent from the global update params; auth.py shows the pattern (cached_property returning the wrapper); the 5 new modules show 0.

- [ ] **Step 2: Write the failing tests first**

In the respective test files (follow the existing respx/construct_type conventions):
1. `test_global_.py`: a test that `client.global.config.update(subagent_depth=4)` sends the field (route assertion on the body/query) and that the params TypedDict accepts it (type-level check via a dict literal in the test).
2. For each of the 5 namespaces: a test that `client.with_raw_response.<resource>.<method>` exists and returns a raw response object for one representative method (mirror how existing tests cover with_raw_response - check test_auth.py or test_session.py for the pattern).

Run: `nix develop --command uv run pytest tests/api_resources/test_global_.py tests/api_resources/test_tool.py tests/api_resources/test_worktree.py tests/api_resources/test_experimental.py tests/api_resources/test_v2_session.py -n 0 -q`
Expected: FAIL - missing attribute / missing field.

- [ ] **Step 3: Implement**

1. Add `subagent_depth: int` (optional, minimum 0 semantics via the type style used in the file) to the global config update params TypedDict; thread it through `global_.py`'s `config.update` method exactly like the other params.
2. Add `with_raw_response` (and `with_streaming_response` if the existing pattern has it) `cached_property` wrappers to the sync resource classes of global_, tool, worktree, experimental, and every v2 area class, mirroring auth.py's structure exactly (the wrapper class with the same method signatures).

- [ ] **Step 4: Run tests to verify they pass**

Run: `nix develop --command uv run pytest tests/api_resources/test_global_.py tests/api_resources/test_tool.py tests/api_resources/test_worktree.py tests/api_resources/test_experimental.py tests/api_resources/test_v2_session.py -n 0 -q`
Expected: PASS.

- [ ] **Step 5: Scoped gates**

Run:
`nix develop --command uv run ruff check src/opencode_ai/resources/global_.py src/opencode_ai/resources/tool.py src/opencode_ai/resources/worktree.py src/opencode_ai/resources/experimental.py src/opencode_ai/resources/v2 src/opencode_ai/types/global_config_update_params.py tests/api_resources/test_global_.py tests/api_resources/test_tool.py tests/api_resources/test_worktree.py tests/api_resources/test_experimental.py tests/api_resources/test_v2_session.py`
`nix develop --command uv run mypy src/opencode_ai/resources/global_.py src/opencode_ai/resources/v2`
`nix develop --command uv run pyright src/opencode_ai/resources/global_.py src/opencode_ai/resources/v2`
Expected: exit 0 (only the 2 known baseline _models.py errors may appear if the command spans them - scope to your files).

- [ ] **Step 6: Commit (grouped, ONE commit)**

```bash
git add src/opencode_ai/resources/global_.py src/opencode_ai/resources/tool.py src/opencode_ai/resources/worktree.py src/opencode_ai/resources/experimental.py src/opencode_ai/resources/v2 src/opencode_ai/types/global_config_update_params.py tests/api_resources/test_global_.py tests/api_resources/test_tool.py tests/api_resources/test_worktree.py tests/api_resources/test_experimental.py tests/api_resources/test_v2_session.py
git commit -m "fix(resources): spec-faithful subagent_depth on global.config.update, wire with_raw_response for new namespaces"
```

Expected: ONE commit, only the listed paths.

**Acceptance (inviolable):** steps 4, 5 pass; the spec field and the wrapper pattern are both present; one grouped commit.

**Report format:** a diff: `git show --stat HEAD`, gate outputs, deviations. If a gate cannot pass, STOP and report with output intact - do not descope.
