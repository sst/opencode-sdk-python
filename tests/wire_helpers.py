# Test-only helpers for respx wire-shape assertions.
from __future__ import annotations

import json
from typing import cast

import httpx
import respx


def route_request(route: respx.Route) -> httpx.Request:
    """Return the httpx.Request from the most recent call on a respx route."""
    return route.calls.last.request


def read_json_body(route: respx.Route) -> dict[str, object]:
    """Decode the JSON body of the most recent request on a respx route."""
    return cast("dict[str, object]", json.loads(route_request(route).content))
