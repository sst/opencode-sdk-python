# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os

import httpx
import pytest
from respx import MockRouter

from opencode_ai import Opencode, AsyncOpencode
from tests.utils import assert_matches_type
from opencode_ai.types import FormatterStatusResponse
from tests.wire_helpers import route_request

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")

FORMATTER_STATUS_SAMPLE: dict[str, object] = {
    "name": "prettier",
    "extensions": [".ts", ".tsx"],
    "enabled": True,
}


class TestFormatterWire:
    @pytest.mark.respx(base_url=base_url)
    def test_status_wire_shape(self, client: Opencode, respx_mock: MockRouter) -> None:
        route = respx_mock.get("/formatter").mock(return_value=httpx.Response(200, json=[FORMATTER_STATUS_SAMPLE]))
        result = client.formatter.status()
        assert route.called
        request = route_request(route)
        assert request.method == "GET"
        assert_matches_type(FormatterStatusResponse, result, path=["response"])

    @pytest.mark.respx(base_url=base_url)
    def test_status_sends_query_params(self, client: Opencode, respx_mock: MockRouter) -> None:
        route = respx_mock.get("/formatter").mock(return_value=httpx.Response(200, json=[FORMATTER_STATUS_SAMPLE]))
        result = client.formatter.status(directory="/tmp/project", workspace="ws_123")
        assert route.called
        request = route_request(route)
        assert dict(request.url.params) == {"directory": "/tmp/project", "workspace": "ws_123"}
        assert_matches_type(FormatterStatusResponse, result, path=["response"])


class TestAsyncFormatterWire:
    @pytest.mark.respx(base_url=base_url)
    async def test_status_wire_shape(self, async_client: AsyncOpencode, respx_mock: MockRouter) -> None:
        route = respx_mock.get("/formatter").mock(return_value=httpx.Response(200, json=[FORMATTER_STATUS_SAMPLE]))
        result = await async_client.formatter.status()
        assert route.called
        request = route_request(route)
        assert request.method == "GET"
        assert_matches_type(FormatterStatusResponse, result, path=["response"])

    @pytest.mark.respx(base_url=base_url)
    async def test_status_sends_query_params(self, async_client: AsyncOpencode, respx_mock: MockRouter) -> None:
        route = respx_mock.get("/formatter").mock(return_value=httpx.Response(200, json=[FORMATTER_STATUS_SAMPLE]))
        result = await async_client.formatter.status(directory="/tmp/project", workspace="ws_123")
        assert route.called
        request = route_request(route)
        assert dict(request.url.params) == {"directory": "/tmp/project", "workspace": "ws_123"}
        assert_matches_type(FormatterStatusResponse, result, path=["response"])
