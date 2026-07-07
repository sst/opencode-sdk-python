# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os

import httpx
import pytest
from respx import MockRouter

from opencode_ai import Opencode, AsyncOpencode
from opencode_ai.types import auth_set_params
from tests.wire_helpers import route_request, read_json_body

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")

API_AUTH_PAYLOAD: auth_set_params.ApiAuthParam = {
    "type": "api",
    "key": "sk-test-123",
}

OAUTH_PAYLOAD: auth_set_params.OAuthParam = {
    "type": "oauth",
    "refresh": "refresh-token",
    "access": "access-token",
    "expires": 1234567890,
}


class TestAuthWire:
    @pytest.mark.respx(base_url=base_url)
    def test_set_sends_body_and_path(self, client: Opencode, respx_mock: MockRouter) -> None:
        route = respx_mock.put("/auth/anthropic").mock(return_value=httpx.Response(200, json=True))
        result = client.auth.set("anthropic", auth=API_AUTH_PAYLOAD)
        assert route.called
        request = route_request(route)
        assert request.method == "PUT"
        body = read_json_body(route)
        assert body["type"] == "api"
        assert body["key"] == "sk-test-123"
        assert result is True

    @pytest.mark.respx(base_url=base_url)
    def test_set_sends_oauth_body(self, client: Opencode, respx_mock: MockRouter) -> None:
        route = respx_mock.put("/auth/anthropic").mock(return_value=httpx.Response(200, json=True))
        result = client.auth.set("anthropic", auth=OAUTH_PAYLOAD)
        body = read_json_body(route)
        assert body["type"] == "oauth"
        assert body["refresh"] == "refresh-token"
        assert result is True

    @pytest.mark.respx(base_url=base_url)
    def test_remove_wire_shape(self, client: Opencode, respx_mock: MockRouter) -> None:
        route = respx_mock.delete("/auth/anthropic").mock(return_value=httpx.Response(200, json=True))
        result = client.auth.remove("anthropic")
        assert route.called
        request = route_request(route)
        assert request.method == "DELETE"
        assert request.url.path == "/auth/anthropic"
        assert result is True

    def test_set_empty_id_raises(self, client: Opencode) -> None:
        with pytest.raises(ValueError, match="Expected a non-empty value"):
            client.auth.set("", auth=API_AUTH_PAYLOAD)

    def test_remove_empty_id_raises(self, client: Opencode) -> None:
        with pytest.raises(ValueError, match="Expected a non-empty value"):
            client.auth.remove("")


class TestAsyncAuthWire:
    @pytest.mark.respx(base_url=base_url)
    async def test_set(self, async_client: AsyncOpencode, respx_mock: MockRouter) -> None:
        route = respx_mock.put("/auth/anthropic").mock(return_value=httpx.Response(200, json=True))
        result = await async_client.auth.set("anthropic", auth=API_AUTH_PAYLOAD)
        assert route.called
        request = route_request(route)
        assert request.method == "PUT"
        body = read_json_body(route)
        assert body["type"] == "api"
        assert result is True

    @pytest.mark.respx(base_url=base_url)
    async def test_remove(self, async_client: AsyncOpencode, respx_mock: MockRouter) -> None:
        route = respx_mock.delete("/auth/anthropic").mock(return_value=httpx.Response(200, json=True))
        result = await async_client.auth.remove("anthropic")
        assert route.called
        request = route_request(route)
        assert request.method == "DELETE"
        assert result is True

    async def test_set_empty_id_raises(self, async_client: AsyncOpencode) -> None:
        with pytest.raises(ValueError, match="Expected a non-empty value"):
            await async_client.auth.set("", auth=API_AUTH_PAYLOAD)

    async def test_remove_empty_id_raises(self, async_client: AsyncOpencode) -> None:
        with pytest.raises(ValueError, match="Expected a non-empty value"):
            await async_client.auth.remove("")
