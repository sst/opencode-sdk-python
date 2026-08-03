> **Status: COMPLETE** (2026-08-03)

# opencode 1.18 implementation (subagent_depth, de-Stainless, v1+v2 coverage)

Execution skill: `catalyst-v2-writing-execution-plans` + superpowers
`writing-plans` (user-mandated). Each implementer receives only its own task doc
plus Global constraints below. Task docs follow the superpowers format (header,
checkbox steps, TDD).

## Goal

Land the 1.18 follow-up: `Config.subagent_depth`, uv.lock migration, full
removal of stale Stainless documentation, and coverage of the 89 missing spec
operations (`global`/`tool`/`worktree`/`experimental`/`v2`) as new surface.

## Architecture / Tech stack

- Repo: Walzen Group fork of the Stainless-generated opencode SDK
  (`opencode-ai-wg`, imports `opencode_ai`). Hand-maintained; no Stainless
  regeneration.
- Python >= 3.8 syntax (pyright strict, `pythonVersion = "3.8"`); venv
  interpreter 3.9.18 via uv; toolchain entered via `nix develop --command uv ...`
  (flake.nix already in the repo, nixos-26.05 pin).
- Tests: respx contract tests under `tests/api_resources/` (`tests/wire_helpers.py`
  `route_request`, `assert_matches_type`, `construct_type`).
- api.md: hand-edited method docs + `uv run python scripts/gen_api_expanded.py`
  for the expanded type regions.
- Source of truth for operation shapes:
  `spec/openapi-opencode.json` (v1.18.11 surface) and the audit's operation
  manifests: `.cortex/plans/2026-08-03-flake-uv-1.18-audit/local-operationIds.txt`,
  `missing-ops.json`, `v1.18.11-manifest.json`.

## Revision notes

- 2026-08-03 (mid-flight): Wave A verified (3 commits; whole-change shows 2
  pre-existing pytest failures + 2 pre-existing mypy/pyright errors in
  _models.py, reproduced identically at baseline 1247e99 - not wave A's; fix
  decision pending user). Wave B+C restructured: tasks 4-6 parallel with wiring
  moved to task-7 (shared-file race). Wave A phase detail recorded under Tracks.
- 2026-08-03 (close-out): Wave B+C complete, 9 commits incl. fec2a78 (meta
  fix of 6 pyright test errors, authorized). No-growth verified on all gates
  (2 baseline pytest failures, 2 baseline mypy/pyright errors). Open items
  recorded in memory: global.config.update omits subagent_depth; with_raw_response
  not wired for new namespaces; api.md CRLF vs LF mismatch; .direnv untracked;
  mypy crashes under nix (use .venv/bin/mypy); v2 location addressing per
  spec-faithful user answer (~48 ops).

## Source spec and resolved questions

## Source spec and resolved questions

Design doc: `design.md` in this dir (decisions D1-D10, all user-approved or
orchestrator-recorded). Key user directives (quoted): dev-toolchain flake,
"Keep as-is, uv sync", "Migrate lock now", "all of the stainless documentations
etc are outdated" -> remove, "develop that on a new branch",
"keep commits grouped properly instead of doing too many little ones".

## Global constraints

- Branch: `feat/1.18-api-surface`, created from `main` BEFORE any implementation.
  All work on that branch. No push unless the user asks.
- Commits authorized and grouped (D9): one commit per task or per coherent
  task-group; NEVER per-method/per-file commits. Task docs name their commits.
- Repo root: `/workspaces/opencode-sdk-python`. All paths absolute.
- Do NOT modify `pyproject.toml`, `.python-version`, or other tasks' files.
- Toolchain: every gate runs inside `nix develop --command ...` at repo root
  (or with the uv venv active). Skip project-wide lint/test suites EXCEPT the
  gates named in each task's Acceptance.
- File headers, README/CONTRIBUTING/api.md prose: remove Stainless-generation
  claims (D10); prose passes `catalyst-v2-writing-docs` + humanizer; user-facing
  text is i-have-adhd short form.
- Artifacts under `.cortex/plans/2026-08-03-1.18-implementation/` or
  `.cortex/reports/`, never `/tmp`. Wave reports land in `.cortex/reports/`.
- `.devcontainer/coding`, `spec/`, `.cortex/` stay untracked/ignored as-is.

## Task table

| Doc | Task | Area | Wave | Model |
|---|---|---|---|---|
| task-1-subagent-depth.md | Config.subagent_depth + test + api.md entry | types/config.py, config_update_params.py, api.md | A | deepseek-v4-flash (max) |
| task-2-uvlock-migration.md | Migrate uv.lock to current format | uv.lock only | A | deepseek-v4-flash (max) |
| task-3-destainless.md | Remove stale Stainless docs + repoint prism scripts | headers, README, CONTRIBUTING, api.md, .stats.yml, scripts/mock, scripts/test | A | deepseek-v4-flash (max) |
| task-4-v1-resources.md | global_/tool/worktree resources (12 ops) | resources/global_.py, tool.py, worktree.py + types + tests + api.md | B | deepseek-v4-flash (max) |
| task-5-experimental.md | experimental resource (16 ops) | resources/experimental.py + types + tests + api.md | B | deepseek-v4-flash (max) |
| task-6-v2-subpackage.md | v2 subpackage (61 ops) + AddressingParams extension | resources/v2/, types/v2_*, tests (no wiring) | C | claude-opus-4-8 (default) |
| task-7-wiring.md | Wire global_/tool/worktree/experimental/v2 into client + api.md | __init__.py, _client.py, api.md | B+C tail | deepseek-v4-flash (max) |

## Tracks

- Wave A (two phases, one meta-agent): phase 1 = task-3 (destainless) +
  task-2 (uvlock), fully disjoint files; phase 2 = task-1 (subagent-depth)
  after phase 1 settles. Reason: task-1 and task-3 both touch config.py,
  test_config.py, and api.md; concurrent commits on a shared checkout would
  interleave, so the global header sweep lands before the content edits.
- Wave B + C (combined, one meta-agent): impl-v1-resources (task-4), impl-experimental
  (task-5), impl-v2 (task-6, opus) run in PARALLEL - their file sets are disjoint
  (per-resource modules, types, tests). The shared files (resources/__init__.py,
  _client.py, api.md) are owned by task-7 (impl-wiring), which dispatches after
  all three settle. Reason: concurrent commits to the shared wiring files would
  interleave on a shared checkout; the tail task removes the race.

## Agent allocation

Locked (per `catalyst-v2-model-picking`): Wave A/B workers and every
meta-agent: `opencode-go/deepseek-v4-flash` thinking max (omp). Wave C worker:
`claude-opus-4-8` default effort (Claude Code; 1 of the 2-opus cap). Fresh
meta-agent per wave. No board keeper (no external tracking).

## Pre-work

1. Orchestrator creates branch `feat/1.18-api-surface` from `main`.
2. Dispatch per wave via `c2d dispatch` (workers + meta in one call); arm every
   returned wake.
3. Incident 2026-08-03-report-delivery verdict (if landed) folds into delivery
   conventions; check `design.md` for updates.

## Whole-change verification (per-wave meta-agent, end-to-end)

Run in pinned toolchain at repo root after each wave's workers settle (do not
re-run worker gates):

```
uv run pytest -q                 # full suite green
uv run ruff check .              # exit 0
uv run mypy .                    # exit 0
uv run pyright                   # exit 0
git status --short               # only expected changes on feat/1.18-api-surface
git log --oneline -N             # commits grouped per plan (D9)
```

Wave C additionally verifies the v2 surface imports and its contract tests run.

## Smoke test (end of Wave C)

```
nix develop --command uv run python -c "
import opencode_ai
c = opencode_ai.Opencode()
assert c.v2.session.list and c.global_.health and c.experimental.console_get and c.tool.list and c.worktree.list
print('all new surfaces importable')
"
```

Expected: prints "all new surfaces importable", exit 0.

## Out of scope

- pyproject.toml / `[tool.rye]` changes
- Stainless regeneration, pushes, releases, PyPI
- `interleaved` tightening, docs for v1-to-v2 migration (deferred)
- Board keeper / external tracking
