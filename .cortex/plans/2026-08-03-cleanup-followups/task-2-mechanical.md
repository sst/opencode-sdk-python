# Task 2: Mechanical (api.md LF + .direnv gitignore) Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Normalize api.md to LF line endings (the regen script writes LF; the file was committed with CRLF, so the next regen would be a full-file diff) and add `.direnv/` to `.gitignore`.

**Architecture:** `scripts/gen_api_expanded.py` writes LF. `.envrc` is already gitignored; `.direnv/` (the direnv cache dir) is not.

**Tech Stack:** git, file(1)/sed for line-ending checks.

## Global Constraints

- Branch feat/1.18-api-surface; ONE grouped commit.
- Repo root /workspaces/opencode-sdk-python.
- Touch ONLY `api.md` and `.gitignore`. Do NOT touch anything else (other workers own src/, .python-version, flake.nix, uv.lock).
- Skip project-wide lint/tests.

---

### Task 2: LF + gitignore

**Files:**
- Modify: `api.md` (line endings only)
- Modify: `.gitignore` (one line)

**Interfaces:**
- Consumes: current api.md (CRLF) and .gitignore.
- Produces: api.md with LF endings, byte-identical content otherwise; `.gitignore` containing `.direnv/`.

- [ ] **Step 1: Confirm the current state**

Run:
`file api.md; git diff --stat api.md`
Expected: shows CRLF line endings (file(1) reports CRLF or the diff shows ^M), no uncommitted changes.

- [ ] **Step 2: Normalize and verify content is unchanged**

Run:
`python3 - <<'EOF'
p = 'api.md'
s = open(p, 'rb').read()
assert b'\r\n' in s, 'no CRLF found - check state first'
open(p, 'wb').write(s.replace(b'\r\n', b'\n'))
EOF`
`file api.md; git diff --stat api.md`
Expected: file(1) reports LF; the diff is the full file (line-ending change) - verify with `git diff --ignore-space-at-eol api.md | head -20` that content lines are unchanged (diff should be empty with whitespace-insensitive comparison).

- [ ] **Step 3: .gitignore**

Append `.direnv/` to `.gitignore` (check it is not already present; also confirm `.direnv` without slash is not already covered - add `.direnv/`).

- [ ] **Step 4: Prove the regen is now clean**

Run: `nix develop --command uv run python scripts/gen_api_expanded.py && git diff --stat api.md`
Expected: the regen produces NO diff (or only the intended expanded regions, not the full file) - this proves LF normalization worked. If the regen changes content, report it; do not commit unexpected content changes silently.

- [ ] **Step 5: Commit (grouped, ONE commit)**

```bash
git add api.md .gitignore
git commit -m "chore: normalize api.md to LF, ignore .direnv"
```

Expected: ONE commit, two files.

**Acceptance (inviolable):** steps 2 and 4 pass (LF, regen clean); one grouped commit.

**Report format:** a diff: `git show --stat HEAD`, the file(1) output before/after, regen diff stat. If a gate cannot pass, STOP and report with output intact - do not descope.
