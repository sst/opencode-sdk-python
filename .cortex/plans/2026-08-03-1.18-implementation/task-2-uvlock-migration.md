# Task 2: uv.lock migration Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Migrate `uv.lock` to the current uv lockfile format so bare `uv run`/`uv sync` no longer rewrites it.

**Architecture:** The lockfile predates uv 0.11's marker-field format; `uv lock --check` reports it stale and any bare `uv run` silently regenerates it. `uv lock` rewrites the file in place. The dependency set must not change, only the format.

**Tech Stack:** uv (0.11.x, from the flake devShell), git.

## Global Constraints

- Branch `feat/1.18-api-surface`; commit ONCE at the end (grouped, D9).
- Repo root `/workspaces/opencode-sdk-python`; gates via `nix develop --command uv ...`.
- Touch ONLY `uv.lock`. Do NOT edit `pyproject.toml`, `requirements*.lock`, or anything else.
- Skip project-wide lint/tests; only the gates below.

---

### Task 2: Migrate the lockfile

**Files:**
- Modify: `uv.lock` (only file)

**Interfaces:**
- Consumes: current `pyproject.toml` (unchanged) and `uv.lock` (stale format).
- Produces: `uv.lock` in current format, `uv lock --check` exit 0, bare `uv run` leaves the lock clean.

- [ ] **Step 1: Confirm staleness**

Run: `nix develop --command uv lock --check`
Expected: exit 1 (stale; capture the message, e.g. marker-field migration).

- [ ] **Step 2: Record the pre-migration dependency surface**

Run: `git show HEAD:uv.lock | grep -E '^name = |^version = ' | paste - - | sort > /tmp/lock-before.txt` then copy that file into this plan dir as `lock-before.txt` (artifacts live under `.cortex/plans/2026-08-03-1.18-implementation/`, never leave them in /tmp).

- [ ] **Step 3: Migrate**

Run: `nix develop --command uv lock`
Expected: exit 0, `uv.lock` rewritten.

- [ ] **Step 4: Verify the format migration, not a dependency change**

Run: `git diff --stat uv.lock` (expect a large format diff), then
`git diff uv.lock | grep -E '^[+-]name = |^[+-]version = ' | grep -v '^[+-][+-]' | sort | uniq -c | sort -rn | head` and compare against `lock-before.txt`.
Also: `git diff uv.lock | grep -E '^[-]version = '` - every removed version must reappear as an added version for the same package name.

Expected: same package set and versions; only format/layout changed. If any package version CHANGED, STOP and report - do not commit a silent dependency bump.

- [ ] **Step 5: Prove bare runs no longer dirty the lock**

Run: `nix develop --command uv lock --check` (exit 0), then
`nix develop --command uv run python -c "import opencode_ai"` (exit 0), then
`git status --short uv.lock` (clean - no modification).

- [ ] **Step 6: Commit (grouped, D9)**

```bash
git add uv.lock
git commit -m "chore(lock): migrate uv.lock to current lockfile format"
```

Expected: ONE commit, only `uv.lock`.

**Acceptance (inviolable):** steps 4 and 5 pass as specified (same dependency surface, lock clean after bare run, `--check` exit 0); one grouped commit.

**Report format:** a diff: `git show --stat HEAD`, the captured staleness message, before/after package-count comparison, gate outputs. If a gate cannot pass, STOP and report with output intact - do not descope.
