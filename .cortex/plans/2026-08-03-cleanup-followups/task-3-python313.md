# Task 3: Python 3.13 + mypy under nix Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Move the dev environment to Python 3.13 (the SDK already declares 3.13 support; user directive) and fix the mypy-under-nix crash properly - no workaround. The crash: the nix devShell's mypy is a 3.13-built binary that fails when the uv venv interpreter is 3.9 (`.python-version` = 3.9.18); the wave used `.venv/bin/mypy` as a workaround, which is now unacceptable.

**Architecture:** `.python-version` governs the uv venv interpreter. Moving it to 3.13 makes the venv and the nix-provided toolchain agree, which should remove the crash; the full gate suite then runs on 3.13, giving real 3.13 coverage. `requires-python` in pyproject.toml stays `>= 3.8`; pyright's `pythonVersion = "3.8"` stays (syntax floor unchanged).

**Tech Stack:** uv, nix, mypy/pyright/ruff/pytest on 3.13.

## Global Constraints

- Branch feat/1.18-api-surface; ONE grouped commit.
- Repo root /workspaces/opencode-sdk-python; gates via `nix develop --command uv ...`.
- Touch: `.python-version`, `uv.lock` (regen only if uv requires it), `flake.nix` ONLY if the mypy package needs adjustment, nothing else. Do NOT touch pyproject.toml dependency ranges, api.md, .gitignore, src/ (other workers own them).
- If 3.13 surfaces real incompatibilities in src/ or tests, STOP and report them with output - do not fix product code in this task (that would collide with the other workers' scope).
- Baseline failures (2 pytest u2028 SSE, 2 mypy/pyright _models.py) must not grow.

---

### Task 3: 3.13 migration + mypy fix

**Files:**
- Modify: `.python-version` (3.9.18 -> 3.13)
- Modify: `uv.lock` (regen if uv requires), `flake.nix` (only if needed)
- No src/ changes expected

**Interfaces:**
- Consumes: current `.python-version`, uv.lock, flake.nix.
- Produces: venv on Python 3.13; `nix develop --command mypy .` works without `.venv/bin/` workaround; full gates green on 3.13 (no growth vs baseline).

- [ ] **Step 1: Reproduce the crash on the current state**

Run: `nix develop --command mypy . 2>&1 | head -20`
Expected: the known crash/failure (the reason the wave used `.venv/bin/mypy`). Capture the exact error as the fail-first evidence.

- [ ] **Step 2: Switch the interpreter**

Set `.python-version` to `3.13` (a bare `3.13` lets uv resolve the latest 3.13.x; if a specific 3.13.x is already cached/available, pin it - prefer explicitness but do not block on a version uv cannot fetch). Then:
Run: `nix develop --command uv sync --frozen 2>&1 | tail -5`
If uv refuses the frozen lock for the new interpreter, run `nix develop --command uv lock` (regen) then `uv sync`; inspect `git diff uv.lock` and confirm only interpreter/marker-related changes, no dependency version drift - if versions changed, report before committing.

- [ ] **Step 3: Verify the venv is 3.13 and the crash is gone**

Run:
`nix develop --command uv run python --version` (expect 3.13.x)
`nix develop --command mypy . 2>&1 | tail -5` (expect: 2 errors in _models.py ONLY - the baseline pair - and a clean run otherwise; NO crash)
If mypy still crashes with a 3.13 venv, investigate the real mechanism (mypy package in nixpkgs vs venv site-packages) and fix it in flake.nix (e.g. mypy needs the same python as the venv, or needs `--python-executable` - the FIX must be a config change, never a documented workaround). Report what you changed and why.

- [ ] **Step 4: Full gates on 3.13**

Run:
`nix develop --command uv run pytest -q 2>&1 | tail -3` (expect: 2 failed / N passed / 657 skipped - the 2 must be the u2028 SSE baseline pair)
`nix develop --command uv run ruff check .` (exit 0)
`nix develop --command uv run pyright` (expect only the 2 baseline _models.py errors)
`nix develop --command uv run mypy .` (same baseline pair, no crash)
If any failure is NOT in the baseline set, STOP and report with the full output - a 3.13 incompatibility is a finding, not something to paper over.

- [ ] **Step 5: Commit (grouped, ONE commit)**

```bash
git add .python-version uv.lock flake.nix
git commit -m "build: dev environment on Python 3.13, fix mypy under nix"
```

Expected: ONE commit; if flake.nix was untouched, commit the two files only.

**Acceptance (inviolable):** steps 3 and 4 pass (3.13 venv, no mypy crash, gates no-growth on 3.13); one grouped commit.

**Report format:** a diff: `git show --stat HEAD`, the before/after mypy behavior, gate outputs on 3.13. If a gate cannot pass, STOP and report with output intact - do not descope.
