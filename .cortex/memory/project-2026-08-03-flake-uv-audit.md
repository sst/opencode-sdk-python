# Flake/uv bootstrap + opencode 1.18 audit (2026-08-03)

## Decisions

- flake.nix: dev-toolchain devShell (python3 3.13, uv, ruff, mypy, pyright, nodejs_22), nixpkgs pinned to nixos-26.05 rev `6d65bfc1bcef2ef39a239d38e577e92a89fb0f07`, systems x86_64-linux + aarch64-darwin. User choice: "Dev toolchain".
- uv stays canonical as-is: `[tool.rye]` in pyproject.toml left untouched; `.python-version` (3.9.18) governs the venv interpreter; venv via `uv sync --frozen`. User choice: "Keep as-is, uv sync".
- No commits in this effort; user authorized none.

## Gotchas

- uv.lock is stale by uv 0.11 standards (marker-field migration): any bare `uv run`/`uv sync` rewrites it. Pending user decision: migrate the lock or keep `--frozen` discipline.
- nix refuses to evaluate a flake with untracked files in a git worktree: `git add -N` (intent-to-add, unstaged) on flake.nix/flake.lock before `nix flake check`.
- `.stats.yml` recorded Stainless spec URL is a legacy 26-op generation (md5 verified `4ff9376c...`), not the tracking surface.

## Wave B+C close-out (2026-08-03)

- 9 grouped commits on feat/1.18-api-surface (tasks 4-7 + meta fix fec2a78). All gates no-growth vs baseline (2 pre-existing pytest failures, 2 pre-existing _models.py mypy/pyright errors). 122 contract tests for v2, 35/32 for v1-resources/experimental, smoke green.
- Decisions: projectCopy IS v2 scope (project_copy.py, 3 ops); v2 addressing per spec-faithful answer (~48 ops carry location deepObject, session.list flat + project/subpath/cursor, pty.connect pre-flattened + cursor/ticket); D5 flat naming (experimental.console_get, not console.get).
- Gotchas: shared-checkout workers MUST never run git reset/rebase/amend - impl-v1-resources's reset --soft orphaned impl-v2's 3 commits (repaired via byte-faithful cherry-pick). api.md committed CRLF while gen_api_expanded.py writes LF (future regen = full-file diff; normalize to LF before next regen). mypy crashes under nix devShell (py3.13-built binary vs venv py3.9) - use .venv/bin/mypy. impl-wiring left with_raw_response wrappers unwired for the 5 new namespaces (with_raw_response.global_ raises AttributeError - fix pending). global.config.update omits subagent_depth (mirrors fork config.py; paired fix touches config.py - pending user decision). .direnv/ untracked (benign; consider .gitignore).

## Cleanup + follow-up close-out (2026-08-03)

- Cleanup wave: 3 commits (8cb982c api.md LF + .direnv ignore, d79a023 spec-faithful
  subagent_depth on global.config.update + with_raw_response for the 5 new namespaces,
  4732f2e Python 3.13 + mypy-under-nix). Whole-change: baseline-only failures, bare nix
  mypy runs without crashing.
- Decision: list_models NOT re-landed (user-approved 2026-08-03, item 3) - the replay
  actor's experiment is out of scope; client.v2.model.list covers model listing.
- Follow-up wave (items 1+2): COMPLETE (2026-08-03). 5feae1f fix(typing): resolve 3.13 mypy
  findings - _typing.py:51 widened _TYPE_ALIAS_TYPES to tuple[type[Any], ...] (3.13 typeshed
  splits typing/typing_extensions.TypeAliasType), gen_api_expanded.py:171 isinstance narrowing
  (latent bytes-render bug); no ignores, no config changes. 39fe91d docs: dev venv recipe
  (CONTRIBUTING With Nix). Whole-change: baseline-only failures, 2 commits verified.
- Gotcha (now documented): plain `uv sync` in the dev venv prunes dev extras (noxfile,
  httpx_aiohttp imports) and the mypy baseline becomes 7-error noise; restore the full recipe
  before running mypy.
- System note: omp worker sessions have no c2d device and no hub meta peer; their report
  steers cannot reach the wave meta - reports arrive as in-terminal relays. Works, but the
  worker report channel in delegation briefs should be checked (candidate improvement).

## 1.18 audit digest (full evidence: `.cortex/reports/2026-08-03-opencode-1.18-audit-report.md`)

- `spec/openapi-opencode.json` == anomalyco/opencode `packages/sdk/openapi.json` @ v1.18.11 (sha256 `5bbd6493...` after stripping x-codeSamples).
- 1.18 API deltas: only `Config.subagent_depth` (int, minimum 0; absent from SDK - must-add to types/config.py + config_update_params.py + api.md) and `interleaved` widening (already tolerated by `Union[Literal[True], object]`).
- 89 of 188 spec operations unimplemented: global 6, experimental 16, tool 2, worktree 4, v2 61. v2 is upstream's investing surface (9 -> 24 -> 61 ops across 1.15 -> 1.17, stable in 1.18).
- No breaking changes for the implemented surface in 1.18.
- Upstream `openapi-translation-cleanup` may de-advertise `directory`/`workspace` query params the fork's AddressingParams work relies on - watch and test against a real 1.18 server if it lands.
