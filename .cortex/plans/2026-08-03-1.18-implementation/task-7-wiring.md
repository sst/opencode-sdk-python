# Task 7: Client wiring + api.md Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Wire the five new resources (global_, tool, worktree, experimental, v2) into the client and api.md, after tasks 4-6 have landed their modules, types, and tests.

**Architecture:** Tasks 4-6 deliberately did NOT touch `resources/__init__.py`, `_client.py`, or `api.md` (shared files; concurrent commits would race). This task owns those three files for all five resources: exports in `resources/__init__.py`, `cached_property` accessors in `_client.py` (`client.global_`, `client.tool`, `client.worktree`, `client.experimental`, `client.v2`), and api.md sections plus the expanded-type regeneration.

**Tech Stack:** Python 3.8-compatible typing, uv venv, git.

## Global Constraints

- Branch `feat/1.18-api-surface`; commit ONCE (grouped, D9).
- Repo root `/workspaces/opencode-sdk-python`; gates via `nix develop --command uv ...`.
- Touch ONLY `src/opencode_ai/resources/__init__.py`, `src/opencode_ai/_client.py`, `api.md`. Do NOT touch the resource modules/types/tests from tasks 4-6.
- Skip project-wide lint; only the named gates.

---

### Task 7: Wire the client and api.md

**Files:**
- Modify: `src/opencode_ai/resources/__init__.py` (exports for GlobalResource, ToolResource, WorktreeResource, ExperimentalResource, V2Resource and its area classes)
- Modify: `src/opencode_ai/_client.py` (accessors `global_`, `tool`, `worktree`, `experimental`, `v2`)
- Modify: `api.md` (five new resource sections + regen)

**Interfaces:**
- Consumes: the modules from tasks 4-6 (already committed): resources/global_.py (class GlobalResource), tool.py (ToolResource), worktree.py (WorktreeResource), experimental.py (ExperimentalResource), resources/v2/ (V2Resource with per-area accessors).
- Produces: `client.global_.health(...)`, `client.tool.list()`, `client.worktree.list()`, `client.experimental.console.get()`, `client.v2.session.list(...)` all reachable; api.md documents them.

- [ ] **Step 1: Confirm the consumed modules exist**

Run: `git log --oneline -6` - expect the task-4/5/6 commits on the branch. Then read `src/opencode_ai/resources/__init__.py` and `src/opencode_ai/_client.py` to see the exact export/accessor pattern (how `auth` is wired: import, `__all__` entry or module import, `cached_property` in both SyncOpencode and AsyncOpencode).

- [ ] **Step 2: Wire the exports and accessors**

In `resources/__init__.py`: export the five resource classes following the existing pattern exactly. In `_client.py`: add `cached_property` accessors for `global_`, `tool`, `worktree`, `experimental`, `v2` on BOTH the sync and async clients, mirroring the `auth` accessor. `global_` keeps the trailing underscore (keyword dodge, design D4); the module is `global_`.

- [ ] **Step 3: Verify the wiring with an import smoke**

Run: `nix develop --command uv run python -c "
import opencode_ai
c = opencode_ai.Opencode()
ac = opencode_ai.AsyncOpencode()
assert c.global_ and c.tool and c.worktree and c.experimental and c.v2
assert ac.global_ and ac.tool and ac.worktree and ac.experimental and ac.v2
print('wired')
"`
Expected: prints wired, exit 0.

- [ ] **Step 4: api.md sections + regen**

Add the five resource sections to api.md (methods and types import blocks, mirroring existing sections; v2 gets the client.v2 namespace with its areas), then run `nix develop --command uv run python scripts/gen_api_expanded.py`. Verify the diff only adds the new sections/types and the regenerated regions.

- [ ] **Step 5: Scoped gates**

Run:
`nix develop --command uv run ruff check src/opencode_ai/resources/__init__.py src/opencode_ai/_client.py`
`nix develop --command uv run mypy src/opencode_ai/resources/__init__.py src/opencode_ai/_client.py`
`nix develop --command uv run pyright src/opencode_ai/resources/__init__.py src/opencode_ai/_client.py`
Expected: exit 0. (Note: pre-existing mypy/pyright errors exist in _models.py at baseline; your two files must not add new errors - scope the output to the files you touched.)

- [ ] **Step 6: Contract test smoke across the wave**

Run: `nix develop --command uv run pytest tests/api_resources/test_global_.py tests/api_resources/test_tool.py tests/api_resources/test_worktree.py tests/api_resources/test_experimental.py tests/api_resources/test_v2_session.py tests/api_resources/test_v2_misc.py -n 0 -q`
Expected: PASS (these test files came from tasks 4-6; the wiring must make their client construction work).

- [ ] **Step 7: Commit (grouped, D9 - exactly 1 commit)**

```bash
git add src/opencode_ai/resources/__init__.py src/opencode_ai/_client.py api.md
git commit -m "feat(resources): wire global_, tool, worktree, experimental, v2 into client and api.md"
```

Expected: ONE commit, only the three files.

**Acceptance (inviolable):** steps 3, 5, 6 pass; one grouped commit; all five namespaces reachable on both clients.

**Report format:** a diff: `git show --stat HEAD`, gate outputs, deviations. If a gate cannot pass, STOP and report with output intact - do not descope.
