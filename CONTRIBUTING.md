## Setting up the environment

### With Rye

We use [Rye](https://rye.astral.sh/) to manage dependencies because it will automatically provision a Python environment with the expected Python version. To set it up, run:

```sh
$ ./scripts/bootstrap
```

Or [install Rye manually](https://rye.astral.sh/guide/installation/) and run:

```sh
$ rye sync --all-features
```

You can then run scripts using `rye run python script.py` or by activating the virtual environment:

```sh
# Activate the virtual environment - https://docs.python.org/3/library/venv.html#how-venvs-work
$ source .venv/bin/activate

# now you can omit the `rye run` prefix
$ python script.py
```

### Without Rye

Alternatively if you don't want to install `Rye`, you can stick with the standard `pip` setup by ensuring you have the Python version specified in `.python-version`, create a virtual environment however you desire and then install dependencies using this command:

```sh
$ pip install -r requirements-dev.lock
```

### With Nix

`nix develop` enters a dev shell with python3 3.13, uv, ruff, mypy, pyright, and nodejs_22. The venv uses the flake's python 3.13.14, and .python-version is 3.13. The flake binds mypy to the venv interpreter with --python-executable, so `nix develop --command mypy .` works bare.

`uv sync --frozen` installs only the runtime dependencies. The full dev venv adds the dev extras on top: run `uv pip install -r requirements-dev.lock`, then the two pins missing from that lock and required on Python 3.13: httpx-aiohttp==0.1.12 and time-machine==3.3.0 (the 2.9.0 pin crashes on Python 3.13).

A plain `uv sync` removes those extras, so reinstall them after any sync.

## Modifying/Adding code

The SDK is maintained by hand from the opencode OpenAPI spec (spec/openapi-opencode.json). Edit
src/opencode_ai/resources/* and src/opencode_ai/types/* directly to change the API surface. After
changing a resource, regenerate the expanded API reference:

```sh
$ uv run python scripts/gen_api_expanded.py
```

Then run the checks:

```sh
$ uv run ruff check .
$ uv run mypy .
$ uv run pyright
$ uv run pytest
```

Keep api.md in sync so the documentation matches the code.

## Adding and running examples

Files in the `examples/` directory can be freely edited or added to.

```py
# add an example to examples/<your-example>.py

#!/usr/bin/env -S rye run python
…
```

```sh
$ chmod +x examples/<your-example>.py
# run the example against your api
$ ./examples/<your-example>.py
```

## Using the repository from source

If you’d like to use the repository from source, you can either install from git or link to a cloned repository:

To install via git:

```sh
$ pip install git+ssh://git@github.com/Walzen-Group/opencode-sdk-python.git
```

Alternatively, you can build from source and install the wheel file:

Building this package will create two files in the `dist/` directory, a `.tar.gz` containing the source files and a `.whl` that can be used to install the package efficiently.

To create a distributable version of the library, all you have to do is run this command:

```sh
$ uv build
# or
$ rye build
```

Then to install:

```sh
$ pip install ./path-to-wheel-file.whl
```

## Running tests

Most tests require you to [set up a mock server](https://github.com/stoplightio/prism) against the OpenAPI spec to run the tests.

```sh
# you will need npm installed
$ npx prism mock path/to/your/openapi.yml
```

```sh
$ ./scripts/test
```

## Linting and formatting

This repository uses [ruff](https://github.com/astral-sh/ruff) to lint and format the code.

To lint:

```sh
$ ./scripts/lint
```

To format and fix all ruff issues automatically:

```sh
$ ./scripts/format
```

## Publishing and releases

Releases are cut by hand with `uv`. See [the publishing guide](./PUBLISHING.md) for the full flow: bump
`__version__` in `src/opencode_ai/_version.py`, `uv build`, rehearse on TestPyPI, then `uv publish` to
PyPI.
