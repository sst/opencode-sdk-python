# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os

import httpx
import pytest
from respx import MockRouter

from opencode_ai import Opencode, AsyncOpencode
from tests.utils import assert_matches_type
from opencode_ai.types import Path
from tests.wire_helpers import route_request

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")

PATH_SAMPLE: dict[str, object] = {
    "home": "/home/user",
    "state": "/home/user/.local/state/opencode",
    "config": "/home/user/.config/opencode",
    "worktree": "/home/user/project",
    "directory": "/home/user/project",
}


class TestPathWire:
    @pytest.mark.respx(base_url=base_url)
    def test_get_wire_shape(self, client: Opencode, respx_mock: MockRouter) -> None:
        route = respx_mock.get("/path").mock(return_value=httpx.Response(200, json=PATH_SAMPLE))
        result = client.path.get()
        assert route.called
        request = route_request(route)
        assert request.method == "GET"
        assert_matches_type(Path, result, path=["response"])


class TestAsyncPathWire:
    @pytest.mark.respx(base_url=base_url)
    async def test_get_wire_shape(self, async_client: AsyncOpencode, respx_mock: MockRouter) -> None:
        route = respx_mock.get("/path").mock(return_value=httpx.Response(200, json=PATH_SAMPLE))
        result = await async_client.path.get()
        assert route.called
        request = route_request(route)
        assert request.method == "GET"
        assert_matches_type(Path, result, path=["response"])
