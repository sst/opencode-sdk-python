# Task 1: Config.subagent_depth Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add the `subagent_depth` field (the only opencode 1.18 API delta) to the SDK's Config types, tests, and api.md.

**Architecture:** `Config` (pydantic response model) and `ConfigUpdateParams` (TypedDict) are hand-maintained in `src/opencode_ai/types/`. The field is a plain optional integer with `minimum: 0` in the spec. api.md's expanded type regions regenerate from source via `scripts/gen_api_expanded.py`.

**Tech Stack:** Python 3.8-compatible typing, pydantic v1/v2 (project supports pydantic >=1.9,<3), uv venv, pytest/respx.

## Global Constraints

- Branch `feat/1.18-api-surface`; commit ONCE at the end (grouped, D9).
- Repo root `/workspaces/opencode-sdk-python`; all gates via `nix develop --command uv ...`.
- Do NOT touch other tasks' files (`uv.lock`, README, CONTRIBUTING, .stats.yml, resources/).
- Skip project-wide lint; run only the named gates.

---

### Task 1: Add subagent_depth

**Files:**
- Modify: `src/opencode_ai/types/config.py` (class `Config`, currently ~line 382; `ConfigUpdateParams` also lives in `types/config_update_params.py`)
- Modify: `src/opencode_ai/types/config_update_params.py` (class `ConfigUpdateParams`, TypedDict total=False)
- Modify: `api.md` (Config type section; refresh via `scripts/gen_api_expanded.py`)
- Modify: `tests/api_resources/test_config.py` (add a model test)

**Interfaces:**
- Consumes: `spec/openapi-opencode.json` -> `components.schemas.Config` (field `subagent_depth`, `type: integer`, `minimum: 0`, not required).
- Produces: `Config.subagent_depth: Optional[int]` (pydantic) and `ConfigUpdateParams` field `subagent_depth: int`; api.md documents both.

- [ ] **Step 1: Confirm the spec field and existing field-style conventions**

Run:
`python3 -c "import json; d=json.load(open('spec/openapi-opencode.json')); print(d['components']['schemas']['Config']['properties']['subagent_depth'])"`
Expected: `{'type': 'integer', 'minimum': 0}` (or with description).

Then read `src/opencode_ai/types/config.py` around `class Config` and note how existing scalar fields are declared (plain `Optional[int] = None` vs `Field(ge=...)`). Mirror the file's dominant convention. Also read `types/config_update_params.py` `ConfigUpdateParams` to find its field style.

- [ ] **Step 2: Write the failing test**

In `tests/api_resources/test_config.py` add (matching the file's existing `construct_type` style):

```python
def test_config_subagent_depth() -> None:
    config = cast(Config, construct_type(Config, {"subagent_depth": 4}))
    assert config.subagent_depth == 4

    config_missing = cast(Config, construct_type(Config, {}))
    assert config_missing.subagent_depth is None
```

(Import `Config` and `construct_type` per the file's existing imports; check `tests/api_resources/test_config.py` for the exact import lines and mirror them. If the file has a `MINIMAL_*` fixture pattern for Config, reuse it instead of the bare dict.)

- [ ] **Step 3: Run test to verify it fails**

Run: `nix develop --command uv run pytest tests/api_resources/test_config.py::test_config_subagent_depth -n 0 -q`
Expected: FAIL - `AttributeError: 'Config' object has no attribute 'subagent_depth'` (or typing error at `config.subagent_depth`).

- [ ] **Step 4: Implement in both type modules**

In `src/opencode_ai/types/config.py`, class `Config`: add the field with the file's dominant style, e.g. `subagent_depth: Optional[int] = None` (add the import for `Optional` if missing - the file already imports typing helpers; check).

In `src/opencode_ai/types/config_update_params.py`, `ConfigUpdateParams`: add `subagent_depth: int` (TypedDict, total=False, no default).

- [ ] **Step 5: Run test to verify it passes**

Run: `nix develop --command uv run pytest tests/api_resources/test_config.py -n 0 -q`
Expected: PASS (whole file, since other tests must keep passing).

- [ ] **Step 6: Scoped type/lint gates**

Run:
`nix develop --command uv run ruff check src/opencode_ai/types/config.py src/opencode_ai/types/config_update_params.py tests/api_resources/test_config.py`
`nix develop --command uv run mypy src/opencode_ai/types/config.py src/opencode_ai/types/config_update_params.py`
Expected: both exit 0.

- [ ] **Step 7: Refresh api.md and verify the diff**

Run: `nix develop --command uv run python scripts/gen_api_expanded.py`
Then: `git diff api.md | grep subagent_depth`
Expected: `subagent_depth` appears in the regenerated Config type block, and the rest of the api.md diff is limited to the regenerated regions (no unrelated churn; if the script reformats unrelated sections, report it - do not commit unrelated churn silently).

- [ ] **Step 8: Commit (grouped, D9)**

```bash
git add src/opencode_ai/types/config.py src/opencode_ai/types/config_update_params.py tests/api_resources/test_config.py api.md
git commit -m "feat(types): add subagent_depth to Config and config update params"
```

Expected: ONE commit, only the five files above.

**Acceptance (inviolable):** steps 5, 6, 7 pass as specified; one grouped commit; `git show --stat HEAD` lists exactly the five files.

**Report format:** a diff, not a narrative: `git show --stat HEAD`, gate outputs, deviations. If a gate cannot pass, STOP and report with output intact - do not descope.
