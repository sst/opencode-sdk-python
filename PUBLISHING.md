# Publishing to PyPI

This guide covers building and publishing `opencode-ai-wg` to PyPI with [uv](https://docs.astral.sh/uv/).

The package uses the hatchling build backend (see `[build-system]` in `pyproject.toml`), so `uv build`
produces both an sdist and a wheel with no extra configuration. Relative links in `README.md` are
rewritten to absolute GitHub links at build time by `hatch-fancy-pypi-readme`, so the description renders
correctly on the PyPI project page.

## Prerequisites

- `uv` installed (`uv --version`; this was written against 0.11.25).
- A PyPI account with permission to publish `opencode-ai-wg`.
- An API token. Create one at https://pypi.org/manage/account/token/. Scope it to the project once the
  project exists; use an account-wide token for the very first upload.

## One-time: pick a version

PyPI rejects re-uploading a version that already exists, so bump the version before every release. There
is a single source of truth: `__version__` in `src/opencode_ai/_version.py`. hatchling reads it at build
time (`[tool.hatch.version]` in `pyproject.toml`, with `version` listed under `[project] dynamic`), so
the distribution version on PyPI and the runtime `opencode_ai.__version__` always match.

```python
# src/opencode_ai/_version.py
__version__ = "1.0.0"   # bump this only
```

Use a matching git tag (for example `v1.0.0`) so releases are traceable.

## Build

Clean any stale artifacts, then build:

```sh
rm -rf dist
uv build
```

This writes two files to `dist/`:

- `opencode_ai_wg-<version>-py3-none-any.whl`
- `opencode_ai_wg-<version>.tar.gz`

Inspect what you are about to ship:

```sh
uv tool run twine check dist/*
```

`twine check` validates the rendered README and metadata without uploading anything. Running it through
`uv tool run` means you do not need twine installed globally.

## Test on TestPyPI first (recommended)

TestPyPI is a separate instance for rehearsing a release. Register a token at
https://test.pypi.org/manage/account/token/, then:

```sh
uv publish --publish-url https://test.pypi.org/legacy/ --token <testpypi-token>
```

Verify the upload installs cleanly from TestPyPI in a throwaway environment. Run this from **outside the
repository** (for example `cd /tmp`); inside the repo, `uv run` imports the local `src/opencode_ai/`
source instead of the downloaded package, so the check would not exercise what you published:

```sh
cd /tmp
uv run --with opencode-ai-wg \
  --index https://test.pypi.org/simple/ \
  --index-strategy unsafe-best-match \
  python -c "import opencode_ai; print(opencode_ai.__version__)"
```

The extra index flags let uv pull `opencode-ai-wg` from TestPyPI while still resolving its dependencies
(httpx, pydantic, and so on) from the real PyPI.

## Publish to PyPI

```sh
uv publish --token <pypi-token>
```

`uv publish` uploads every file in `dist/` by default. To avoid pasting the token each time, export it:

```sh
export UV_PUBLISH_TOKEN=<pypi-token>
uv publish
```

Use `__token__` as the username if you prefer the username/password form; a raw API token works directly
with `--token`.

## Verify

Confirm the release installs from PyPI (again, from outside the repo):

```sh
cd /tmp
uv run --with opencode-ai-wg python -c "import opencode_ai; print(opencode_ai.__version__)"
```

Then tag and push the release:

```sh
git tag v0.2.0
git push origin v0.2.0
```

## Release checklist

1. Bump `__version__` in `src/opencode_ai/_version.py` (the single source of truth).
2. `rm -rf dist && uv build`.
3. `uv tool run twine check dist/*`.
4. Publish to TestPyPI and smoke-test the install.
5. `uv publish` to PyPI.
6. Verify the install from PyPI.
7. Tag the commit (`v<version>`) and push the tag.

## Optional: trusted publishing from CI

PyPI supports [trusted publishing](https://docs.pypi.org/trusted-publishers/), which lets a GitHub
Actions workflow publish without a long-lived token. After configuring a trusted publisher for the
project on PyPI, a workflow can run `uv build` and `uv publish` with no `--token`; uv picks up the
OIDC credentials that GitHub provides. This removes the need to store a PyPI token as a repository
secret.
