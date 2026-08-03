# Design: opencode 1.18 follow-up implementation

Date: 2026-08-03. Repo: `/workspaces/opencode-sdk-python` (Walzen-Group fork of the Stainless-generated opencode Python SDK, `opencode-ai-wg` / `opencode_ai`).

## Scope (user-approved)

1. Add `Config.subagent_depth` (the only 1.18 compat gap in the implemented surface).
2. Migrate `uv.lock` to the current uv format (user: "Migrate lock now").
3. Scrub outdated Stainless documentation and record spec provenance (user: "all of the stainless documentations etc are outdated").
4. Implement the 28 non-v2 missing operations: `global` (6), `experimental` (16), `tool` (2), `worktree` (4).
5. Implement the 61-op `v2` API as a `resources/v2/` subpackage.

Scope note: the 89 operations are NEW surface, not repair. The audit verified the existing v1 surface (99 ops) is complete and correct against 1.18 (see `.cortex/reports/2026-08-03-opencode-1.18-audit-report.md`).

## Resolved design decisions

- **D1 (user-approved): `resources/v2/` subpackage.** `client.v2.session.list(...)`, one module per API area. Mirrors the API's `/api/*` grouping and the existing per-namespace module pattern.
- **D2 (user-approved): shared `AddressingParams`.** Extend `src/opencode_ai/types/addressing_params.py` with optional `project`, `subpath`, `cursor` (total=False, additive). Precedent: the fork already extended it with `directory`/`workspace`. Revised 2026-08-03: the v2 surface's addressing is per-operation (session.list flat params; ~50 ops a location deepObject param; pty.connect pre-flattened location + cursor/ticket) - implement per spec, do not force a single shape.
- **D3 (user-approved): contract tests.** respx-based tests under `tests/api_resources/`, following `tests/wire_helpers.py` (`route_request`) and `assert_matches_type`/`construct_type` conventions. Not exhaustive prism scenarios.
- **D4 (orchestrator): `global` keyword collision.** `global` is a Python keyword; the resource module is `resources/global_.py`, class `GlobalResource`, exposed as `client.global_` (PEP 8 keyword dodge; document in the module docstring).
- **D5 (orchestrator): experimental layout.** One flat `resources/experimental.py` module, 16 methods (sync + async), matching the fork's flat per-namespace style.
- **D6 (orchestrator): addressing application.** Follow the spec: `global.*` (6 ops) and `experimental.controlPlane.moveSession` carry NO directory/workspace params; all other new v1 ops do. `v2.session.list` carries directory/workspace/project/subpath/cursor.
- **D7 (orchestrator): keyword/module naming.** Modules and types named after their spec family (`v2_session_list_response.py` style). No `|` union syntax; keep 3.8-compatible typing (pyright `pythonVersion = "3.8"`, `from __future__ import annotations`).
- **D8 (user): new branch.** All implementation work on branch `feat/1.18-api-surface`, created from `main` before dispatch. No pushes unless the user asks.
- **D9 (user): grouped commits.** Commits ARE authorized for this wave, but grouped by logical unit (one commit per task or per coherent task-group, never per-method/per-file granularity). Each task doc names its expected commits.
- **D10 (user): remove stale Stainless docs.** We maintain the SDK without Stainless; stale Stainless artifacts are REMOVED, not annotated: the "File generated from our OpenAPI spec by Stainless" headers (src + tests), README/CONTRIBUTING/api.md generation claims, and `.stats.yml` (with `scripts/mock` + `scripts/test` repointed at `spec/openapi-opencode.json`). Historical mentions in CHANGELOG stay.

## Sequencing and model allocation (user-approved)

- **Wave A** (Small/fast, `opencode-go/deepseek-v4-flash` thinking max, 3 workers, fresh meta): task-1 subagent_depth, task-2 uv.lock migration, task-3 Stainless docs scrub.
- **Wave B** (Mid-tier, deepseek-v4-flash thinking max, 2 workers, fresh meta): task-4 v1 resources (global/tool/worktree), task-5 experimental.
- **Wave C** (Frontier, `claude-opus-4-8` default effort - 1 of the 2-opus cap, 1 worker, fresh meta): task-6 v2 subpackage.

Rationale: A first because task-1's `api.md` hand-edit must land before B/C regenerate api.md; B and C are file-disjoint so they run in parallel.

## Delivery conventions

- Branch `feat/1.18-api-surface` from `main`; grouped commits per D9; no push unless the user asks.
- User-facing prose and repo docs (README/CONTRIBUTING/api.md edits): invoke `catalyst-v2-writing-docs` and pass through humanizer; i-have-adhd short form.
- Wave reports land under `.cortex/reports/` (user expectation; incident 2026-08-03-report-delivery tracks the convention).
- Toolchain: `nix develop --command uv ...` at repo root; venv interpreter 3.9.18 per `.python-version`.

## Out of scope

- pyproject.toml / `[tool.rye]` changes
- Regeneration via Stainless (input spec is stale; all edits hand-written)
- Commits, releases, PyPI publishing (commit policy per D9; release/push need a separate user call)
- The `interleaved` tightening (optional; deferred)
