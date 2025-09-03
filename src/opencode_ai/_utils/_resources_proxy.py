from __future__ import annotations

from typing import Any
from typing_extensions import override

from ._proxy import LazyProxy


class ResourcesProxy(LazyProxy[Any]):
    """A proxy for the `opencode_ai.resources` module.

    This is used so that we can lazily import `opencode_ai.resources` only when
    needed *and* so that users can just import `opencode_ai` and reference `opencode_ai.resources`
    """

    @override
    def __load__(self) -> Any:
        import importlib

        mod = importlib.import_module("opencode_ai.resources")
        return mod


resources = ResourcesProxy().__as_proxied__()
