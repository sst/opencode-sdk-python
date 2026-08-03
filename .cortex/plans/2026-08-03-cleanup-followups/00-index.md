> **Status: COMPLETE** (2026-08-03)

# Follow-up cleanup: spec faithfulness + LF/direnv + Python 3.13

## Goal

Close the six open items from the wave B+C hand-back, per user decisions (2026-08-03): items 1-2 fix, 3 LF, 4 add to .gitignore, 5 fix properly (no workaround) AND add Python 3.13 compatibility; item 6 (push/PR) held.

## Tasks

| Doc | Task | Files | Worker |
|---|---|---|---|
| task-1-spec-faithfulness.md | subagent_depth on global.config.update + with_raw_response wrappers for the 5 new namespaces | resources/global_.py + global update params types, types/config.py if needed, the 5 new resource modules, their test files | impl-faithfulness (deepseek max) |
| task-2-mechanical.md | api.md LF normalization + .gitignore add .direnv/ | api.md, .gitignore | impl-mechanical (deepseek max) |
| task-3-python313.md | .python-version to 3.13, venv regen, fix mypy-under-nix properly, full gates on 3.13 | .python-version, uv.lock, flake.nix (mypy package if needed), gate config | impl-python313 (deepseek max) |

## Global constraints

- Branch feat/1.18-api-surface; grouped commits (1 per task); no push.
- Repo root /workspaces/opencode-sdk-python; gates via nix develop --command uv ...
- Do NOT touch pyproject.toml dependencies; requires-python stays >= 3.8.
- Skip project-wide lint except named gates; the meta runs the final whole-change.
- Artifacts under this plan dir or .cortex/reports/; reports follow the reports convention.
- Pre-existing baseline failures (2 pytest u2028 SSE, 2 mypy/pyright _models.py errors) must not grow.

## Whole-change verification (meta)

pytest -q (no growth beyond baseline), ruff check ., mypy ., pyright, smoke import, git log = 3 new commits, api.md LF-verified, .gitignore has .direnv/, `nix develop --command mypy .` works without workaround on the 3.13 venv.

## Out of scope

- Push/PR (held), pydantic pin decision, interleaved tightening, with_raw_response docs beyond code.
