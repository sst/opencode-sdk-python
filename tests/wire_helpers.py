# Test-only helpers for respx wire-shape assertions.
from __future__ import annotations

import json
from typing import Any

import httpx


def route_request(route: Any) -> httpx.Request:
    """Return the httpx.Request from the most recent call on a respx route."""
    return route.calls.last.request


def read_json_body(route: Any) -> dict:
    """Decode the JSON body of the most recent request on a respx route."""
    return json.loads(route_request(route).content)
