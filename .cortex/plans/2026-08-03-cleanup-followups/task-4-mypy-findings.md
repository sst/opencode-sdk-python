# Task 4: fix the 3.13 mypy findings (item 1, user-approved)

Status: COMPLETE (2026-08-03), commit 5feae1f.

## Target

src/opencode_ai/_utils/_typing.py:51 and scripts/gen_api_expanded.py:171 - the two
mypy findings surfaced by the Python 3.13 migration. Branch feat/1.18-api-surface
at 4732f2e.

## Change

1. Reproduce the red run first (test-first, catalyst-v2-testing): `nix develop --command mypy .`
   shows 4 errors = 2 baseline (_models.py) + 2 target-version findings; record it.
2. Root-cause each finding (3.13 target-version artifacts). Prefer real typing fixes
   (correct types, proper generics, isinstance narrowing, version guards); a
   `# type: ignore` only with a one-line justification, never for both findings.
3. Green: `nix develop --command mypy .` = only the 2 baseline errors, no crash;
   `uv run mypy .` = only the 2 baseline errors; `uv run ruff check .` clean.
4. Targeted pytest on the fixed files (worker-level gate only).

## Commit

One logical commit, never push, append-only history.

## Acceptance

Bare nix mypy = 2 baseline errors only; ruff clean; no regression in targeted tests.
Whole-change check is the wave meta's duty.
