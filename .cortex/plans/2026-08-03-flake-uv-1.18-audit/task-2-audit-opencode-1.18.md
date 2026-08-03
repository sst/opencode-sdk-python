# Task 2: Audit spec vs opencode 1.18, recommendation report

## Context

The repo is a fork of the Stainless-generated opencode Python SDK
(`opencode-ai-wg`, imports as `opencode_ai`). `spec/openapi-opencode.json`
(untracked, OpenAPI 3.1.0, 162 paths / 188 operations / 472 schemas) is a local
copy of the API spec the SDK tracks. The user wants to know what changed with
the opencode 1.18 release line (current: 1.18.11, 2026-08-01) and what the SDK
should do about it. Your deliverable is a recommendation report; no SDK code
changes in this task.

## Target

- Read-only on repo files. You may write working files and the report only
  under `/workspaces/opencode-sdk-python/.cortex/plans/2026-08-03-flake-uv-1.18-audit/`.
- Report file: `.cortex/plans/2026-08-03-flake-uv-1.18-audit/task-2-audit-report.md`.

Non-goals: no edits to `src/`, `spec/`, `api.md`, `docs/`, `pyproject.toml`,
lockfiles, `.stats.yml`. No commits.

## Change

1. **Baseline the local spec.** Parse `/workspaces/opencode-sdk-python/spec/openapi-opencode.json`:
   record OpenAPI version, info block, path/operation counts, and dump a
   manifest of operationIds (e.g. `auth.set`) to
   `.cortex/plans/2026-08-03-flake-uv-1.18-audit/local-operationIds.txt` for
   diffing.
2. **Establish which opencode version the local spec corresponds to.** Fetch the
   upstream Stainless spec URL from `.stats.yml`:
   `https://storage.googleapis.com/stainless-sdk-openapi-specs/opencode%2Fopencode-62d8fccba4eb8dc3a80434e0849eab3352e49fb96a718bb7b6d17ed8e582b716.yml`
   (recorded hash `4ff9376cf9634e91731e63fe482ea532` - compute the download's
   md5 and compare). Compare its path/operation/schema surface with the local
   spec; if identical, the local spec is the upstream one.
3. **Get the opencode 1.18 API surface.** Try in this order, and record exactly
   which source you used (URL + tag/commit):
   a. The anomalyco/opencode GitHub repo (formerly sst/opencode) - look for the
      OpenAPI spec it generates from (repo root, `packages/opencode`, a
      `stainless`/`.stainless` config, release assets of tags `v1.18.x`).
   b. opencode.ai docs: https://opencode.ai/changelog (1.18 entries) and
      https://opencode.ai/docs for endpoint-level changes.
   c. Re-fetch the Stainless spec URL from step 2 - if the bucket serves a
      newer generation, the delta from the local spec is 1.18-era evidence.
   If the exact 1.18 spec cannot be found, say so explicitly and base the audit
   on the best available source (name it), flagging the confidence level.
4. **Diff at three levels**, local spec vs 1.18 source:
   - paths/operations: added, removed, renamed (by path+method and operationId)
   - parameters: new/changed/removed params per operation (e.g. new query
     params, new body fields)
   - schemas (`components.schemas`): added, removed; for changed ones, the
     added/removed fields
   Produce counts plus named exemplars; the full detail lives in the report.
5. **Map deltas to SDK impact.** The SDK mirrors the API one resource module per
   namespace under `src/opencode_ai/resources/` (session.py, event.py, file.py,
   find.py, config.py, project.py, provider.py, question.py, permission.py, mcp.py,
   path.py, vcs.py, command.py, lsp.py, formatter.py, instance.py, auth.py,
   sync.py, pty.py, tui.py, app.py) with types under `src/opencode_ai/types/`.
   `api.md` documents the full SDK surface. For each delta, name the resource
   module(s)/type file(s) that would need regeneration or hand-edits. The fork
   already carries custom work on top of the generated code (e.g. directory/
   workspace addressing params on all v1 methods - see README, and
   `docs/MIGRATION-v1.md`): note where a 1.18 delta collides with that custom
   work.
6. **Recommendation.** A prioritized list: Must (required for 1.18 compat),
   Should, Optional. Include: whether to regenerate from the upstream spec or
   hand-edit, whether `spec/openapi-opencode.json` and `.stats.yml`'s recorded
   hash should be refreshed (and to what), any breaking changes users would hit
   (renamed/removed params, changed types), and anything 1.18 added that the
   fork's custom addressing work needs to absorb.
7. End the report with a three-line-or-fewer summary (i-have-adhd style: lead
   with the answer, cut filler).

## Constraints (from plan index)

- Repo root: `/workspaces/opencode-sdk-python`. All paths absolute.
- Read-only on repo files; only the plan dir is writable.
- Do NOT commit anything.
- Artifacts under `.cortex/plans/2026-08-03-flake-uv-1.18-audit/`, never `/tmp`.
- Skip formatters/linters/project-wide test suites.
- `.devcontainer/coding` and `spec/` are pre-existing untracked paths; leave
  them alone.
- User-facing writing: i-have-adhd convention (lead with the answer, three lines
  or fewer, cut filler).

## Acceptance

1. The report file exists at the path above and contains, in order: baseline
   stats of the local spec; the provenance of the 1.18 source (URL and/or tag);
   delta tables for operations, parameters, and schemas (added/changed/removed,
   with operationIds and schema names quoted); SDK impact mapping to resource
   modules/types; the prioritized recommendation; the closing summary.
2. Every claim about a delta carries evidence: operationId, path+method, schema
   name, or changelog entry (with URL).
3. `git status --short` at the repo root shows nothing outside
   `flake.nix`/`flake.lock` (task 1's files, if present), `spec/`,
   `.devcontainer/coding`, `.cortex/`. You modified no repo file.

If a needed source is unreachable, report it with what you tried; do not
fabricate deltas. Acceptance criteria are not descoped - a partial source makes
the report say so and lowers confidence explicitly.

## Report format

The report file is the deliverable. At the end of your session, summarize it in
three lines or fewer (i-have-adhd). Changes stay uncommitted.
