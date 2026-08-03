# Task 5: document the dev venv recipe (item 2, user-approved)

Status: COMPLETE (2026-08-03), commit 39fe91d.

## Target

CONTRIBUTING.md on branch feat/1.18-api-surface at 4732f2e. Single doc change.

## Change

Short section matching the file's existing structure, exact facts from the cleanup wave:

- Dev toolchain entry: `nix develop` (flake.nix: python3 3.13, uv, ruff, mypy, pyright,
  nodejs_22).
- Plain `uv sync --frozen` installs runtime-only deps, not the full dev venv. Complete
  recipe: `uv sync --frozen` + `uv pip install -r requirements-dev.lock` + the two pins
  absent from that lock and required on 3.13: `httpx-aiohttp==0.1.12` and
  `time-machine==3.3.0` (2.9.0 crashes on Python 3.13).
- Warning: plain `uv sync` prunes those extras; reinstall after any sync.
- `.python-version` is 3.13; venv interpreter is the nix python 3.13.14; flake wraps
  mypy with --python-executable so `nix develop --command mypy .` works bare.

Style: catalyst-v2-writing-docs (plain identifiers in prose, humanizer pass, LF,
no em dashes, no "The" headings).

## Commit

One logical commit, never push, append-only history.

## Acceptance

Section present and accurate, LF verified, one commit, nothing pushed.
