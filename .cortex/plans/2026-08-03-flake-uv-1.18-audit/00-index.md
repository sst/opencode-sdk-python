> **Status: COMPLETE** (2026-08-03)

# Flake + uv bootstrap, opencode 1.18 spec audit

Execution skill: `catalyst-v2-writing-execution-plans`. Each implementer receives
only its own task doc plus the Global constraints below.

## Goal

1. Give the repo a reproducible dev environment via `flake.nix` (dev toolchain shell).
2. Keep uv as the project's package tool; prove `uv sync` works inside the shell.
3. Audit `spec/openapi-opencode.json` against the opencode 1.18 API surface and
   produce a prioritized recommendation of SDK changes.

## Architecture / Tech stack

- Repo: Walzen Group fork of the Stainless-generated opencode Python SDK.
  Distribution `opencode-ai-wg`, import `opencode_ai`, generated with Stainless.
- Python: `requires-python >= 3.8`; `.python-version` = 3.9.18 (rye-era pin);
  pyright `pythonVersion = "3.8"`.
- Tooling: `uv.lock` present; `pyproject.toml` still carries `[tool.rye] managed = true`
  and `[tool.rye.scripts]` (unchanged by this effort).
- Nix 2.35.1 installed on the host (`/nix/var/nix/profiles/default/bin/nix`,
  observed `nix --version`).
- Upstream spec record: `.stats.yml` -> `openapi_spec_url:
  https://storage.googleapis.com/stainless-sdk-openapi-specs/opencode%2Fopencode-62d8fccba4eb8dc3a80434e0849eab3352e49fb96a718bb7b6d17ed8e582b716.yml`,
  `openapi_spec_hash: 4ff9376cf9634e91731e63fe482ea532`.
- Local spec: `spec/openapi-opencode.json` (untracked, OpenAPI 3.1.0, 162 paths /
  188 operations / 472 schemas).
- opencode release line current as of 2026-08-01: 1.18.11; project repo is
  anomalyco/opencode (formerly sst/opencode).

## Source spec and resolved questions

- User decision (2026-08-03, quoted): flake devShell = **Dev toolchain**
  (python + uv + ruff + mypy + pyright + prism mock server).
- User decision (2026-08-03, quoted): uv = **Keep as-is, uv sync** - leave
  pyproject.toml / rye config untouched; the flake provides uv and `uv sync`
  creates the venv.
- User directive (2026-08-03): create the `.cortex/` tree (did not exist).
- User directive: audit output is a **recommendation** (report); SDK code changes
  are a later effort pending user approval.
- No external tracking surface (no Plane/Jira/Linear/GitHub Projects): board
  keeper skipped.
- No commits in this effort: changes stay uncommitted unless the user
  explicitly authorizes.

## Global constraints

- Repo root for all paths: `/workspaces/opencode-sdk-python`.
- Do NOT commit anything. Leave changes uncommitted.
- Do NOT modify `pyproject.toml`, `uv.lock`, `requirements*.lock`,
  `.python-version`, `src/`, `docs/`, `api.md`, `.stats.yml` unless your task doc
  explicitly says so.
- Artifacts and reports go under `.cortex/plans/2026-08-03-flake-uv-1.18-audit/`,
  never `/tmp`.
- Skip formatters/linters/project-wide test suites unless your Acceptance gates
  name them.
- `.devcontainer/coding` and `spec/` are pre-existing untracked paths; leave them
  alone.
- User-facing style: i-have-adhd convention (lead with the answer, three lines or
  fewer, cut filler). Embed this pointer in anything written for the user.

## Task table

| Doc | Task | Repo area | Depends on |
|---|---|---|---|
| task-1-flake-uv-shell.md | Create flake.nix (dev toolchain), verify uv sync | repo root: flake.nix, flake.lock | - |
| task-2-audit-opencode-1.18.md | Audit spec vs opencode 1.18, recommendation report | read-only; report under plan dir | - |

## Tracks

- Track A: `flake-uv-shell` (task 1).
- Track B: `audit-1.18` (task 2).

Tracks are independent: task 1 writes only `flake.nix`/`flake.lock`/`.venv` at the
repo root; task 2 writes only under the plan dir. Shared checkout, no worktree.

## Agent allocation

| Task | Executor | Model tier | Model string |
|---|---|---|---|
| task-1 | `flake-uv-shell` (omp worker) | Mid-tier | `opencode-go/deepseek-v4-flash`, thinking max |
| task-2 | `audit-1.18` (omp worker) | Mid-tier | `opencode-go/deepseek-v4-flash`, thinking max |
| wave meta | `meta-w1` (omp) | Mid-tier | `opencode-go/deepseek-v4-flash`, thinking max |

## Pre-work

Board: skipped (no external tracking). `.cortex/` tree created by the
orchestrator. Dispatch via `c2d dispatch` with both workers and the meta-agent in
one call; orchestrator arms each returned wake.

## Whole-change verification (meta-agent's end-to-end check)

Run inside the pinned toolchain at repo root, after both workers settle; do not
re-run the workers' own gates:

```
nix flake check                       # exit 0
nix develop --command bash -c 'uv sync --frozen && uv run python -c "import opencode_ai"'
                                      # exit 0; .venv created; import works
nix develop --command bash -c 'ruff --version && mypy --version && pyright --version && node --version'
                                      # all print versions
git status --short                    # only expected: flake.nix, flake.lock,
                                      # spec/, .devcontainer/coding, .cortex/
```

## Smoke test

```
nix develop --command uv run python -c "import opencode_ai; print(opencode_ai.Opencode)"
```

Expected: prints `<class 'opencode_ai.Opencode'>` (or equivalent class repr),
exit 0. This is the end-to-end scenario: pinned env -> uv-managed venv -> SDK
imports.

## Out of scope

- rye -> uv migration, pyproject/rye config changes
- SDK code changes (resources/types/api.md) - only recommended in the audit report
- CI changes, docker/devcontainer changes
- Commits, releases, PyPI publishing
- Board keeper / external status tracking
