# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os

import httpx
import pytest
from respx import MockRouter

from opencode_ai import Opencode, AsyncOpencode
from tests.utils import assert_matches_type
from opencode_ai.types import (
    MCPStatus,
    McpAddResponse,
    McpStatusResponse,
    McpConnectResponse,
    McpAuthStartResponse,
    McpAuthRemoveResponse,
    McpDisconnectResponse,
)
from tests.wire_helpers import route_request, read_json_body

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")

STATUS_MAP_SAMPLE: dict[str, object] = {
    "connected-server": {"status": "connected"},
    "disabled-server": {"status": "disabled"},
    "failed-server": {"status": "failed", "error": "boom"},
    "needs-auth-server": {"status": "needs_auth"},
    "needs-registration-server": {"status": "needs_client_registration", "error": "register first"},
}

AUTH_START_SAMPLE: dict[str, object] = {
    "authorizationUrl": "https://example.com/authorize",
    "oauthState": "state-123",
}

AUTH_REMOVE_SAMPLE: dict[str, object] = {"success": True}


class TestMcpWire:
    @pytest.mark.respx(base_url=base_url)
    def test_status_wire_shape(self, client: Opencode, respx_mock: MockRouter) -> None:
        route = respx_mock.get("/mcp").mock(return_value=httpx.Response(200, json=STATUS_MAP_SAMPLE))
        result = client.mcp.status()
        assert route.called
        request = route_request(route)
        assert request.method == "GET"
        assert_matches_type(McpStatusResponse, result, path=["response"])

    @pytest.mark.respx(base_url=base_url)
    def test_status_sends_addressing_query_params(self, client: Opencode, respx_mock: MockRouter) -> None:
        route = respx_mock.get("/mcp").mock(return_value=httpx.Response(200, json=STATUS_MAP_SAMPLE))
        result = client.mcp.status(directory="/tmp/my-project", workspace="my-workspace")
        assert route.called
        request = route_request(route)
        assert dict(request.url.params) == {"directory": "/tmp/my-project", "workspace": "my-workspace"}
        assert_matches_type(McpStatusResponse, result, path=["response"])

    @pytest.mark.respx(base_url=base_url)
    def test_add_sends_body(self, client: Opencode, respx_mock: MockRouter) -> None:
        route = respx_mock.post("/mcp").mock(return_value=httpx.Response(200, json=STATUS_MAP_SAMPLE))
        result = client.mcp.add(
            name="my-server",
            config={
                "type": "local",
                "command": ["node", "server.js"],
            },
        )
        assert route.called
        request = route_request(route)
        assert request.method == "POST"
        body = read_json_body(route)
        assert body == {
            "name": "my-server",
            "config": {"type": "local", "command": ["node", "server.js"]},
        }
        assert_matches_type(McpAddResponse, result, path=["response"])

    @pytest.mark.respx(base_url=base_url)
    def test_add_remote_config_sends_body(self, client: Opencode, respx_mock: MockRouter) -> None:
        route = respx_mock.post("/mcp").mock(return_value=httpx.Response(200, json=STATUS_MAP_SAMPLE))
        result = client.mcp.add(
            name="remote-server",
            config={
                "type": "remote",
                "url": "https://example.com/mcp",
                "oauth": False,
            },
        )
        assert route.called
        body = read_json_body(route)
        assert body == {
            "name": "remote-server",
            "config": {"type": "remote", "url": "https://example.com/mcp", "oauth": False},
        }
        assert_matches_type(McpAddResponse, result, path=["response"])

    @pytest.mark.respx(base_url=base_url)
    def test_auth_start_wire_shape(self, client: Opencode, respx_mock: MockRouter) -> None:
        route = respx_mock.post("/mcp/my-server/auth").mock(
            return_value=httpx.Response(200, json=AUTH_START_SAMPLE)
        )
        result = client.mcp.auth_start("my-server")
        assert route.called
        request = route_request(route)
        assert request.method == "POST"
        assert_matches_type(McpAuthStartResponse, result, path=["response"])

    @pytest.mark.respx(base_url=base_url)
    def test_auth_remove_wire_shape(self, client: Opencode, respx_mock: MockRouter) -> None:
        route = respx_mock.delete("/mcp/my-server/auth").mock(
            return_value=httpx.Response(200, json=AUTH_REMOVE_SAMPLE)
        )
        result = client.mcp.auth_remove("my-server")
        assert route.called
        request = route_request(route)
        assert request.method == "DELETE"
        assert_matches_type(McpAuthRemoveResponse, result, path=["response"])

    @pytest.mark.respx(base_url=base_url)
    def test_auth_callback_sends_body(self, client: Opencode, respx_mock: MockRouter) -> None:
        route = respx_mock.post("/mcp/my-server/auth/callback").mock(
            return_value=httpx.Response(200, json={"status": "connected"})
        )
        result = client.mcp.auth_callback("my-server", code="the-code")
        assert route.called
        request = route_request(route)
        assert request.method == "POST"
        body = read_json_body(route)
        assert body == {"code": "the-code"}
        assert_matches_type(MCPStatus, result, path=["response"])

    @pytest.mark.respx(base_url=base_url)
    def test_auth_authenticate_wire_shape(self, client: Opencode, respx_mock: MockRouter) -> None:
        route = respx_mock.post("/mcp/my-server/auth/authenticate").mock(
            return_value=httpx.Response(200, json={"status": "needs_auth"})
        )
        result = client.mcp.auth_authenticate("my-server")
        assert route.called
        request = route_request(route)
        assert request.method == "POST"
        assert_matches_type(MCPStatus, result, path=["response"])

    @pytest.mark.respx(base_url=base_url)
    def test_connect_wire_shape(self, client: Opencode, respx_mock: MockRouter) -> None:
        route = respx_mock.post("/mcp/my-server/connect").mock(return_value=httpx.Response(200, json=True))
        result = client.mcp.connect("my-server")
        assert route.called
        request = route_request(route)
        assert request.method == "POST"
        assert_matches_type(McpConnectResponse, result, path=["response"])

    @pytest.mark.respx(base_url=base_url)
    def test_disconnect_wire_shape(self, client: Opencode, respx_mock: MockRouter) -> None:
        route = respx_mock.post("/mcp/my-server/disconnect").mock(return_value=httpx.Response(200, json=True))
        result = client.mcp.disconnect("my-server")
        assert route.called
        request = route_request(route)
        assert request.method == "POST"
        assert_matches_type(McpDisconnectResponse, result, path=["response"])

    def test_path_params_auth_start(self, client: Opencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            client.mcp.with_raw_response.auth_start("")

    def test_path_params_auth_remove(self, client: Opencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            client.mcp.with_raw_response.auth_remove("")

    def test_path_params_auth_callback(self, client: Opencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            client.mcp.with_raw_response.auth_callback("", code="the-code")

    def test_path_params_auth_authenticate(self, client: Opencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            client.mcp.with_raw_response.auth_authenticate("")

    def test_path_params_connect(self, client: Opencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            client.mcp.with_raw_response.connect("")

    def test_path_params_disconnect(self, client: Opencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            client.mcp.with_raw_response.disconnect("")


class TestAsyncMcpWire:
    @pytest.mark.respx(base_url=base_url)
    async def test_status_wire_shape(self, async_client: AsyncOpencode, respx_mock: MockRouter) -> None:
        route = respx_mock.get("/mcp").mock(return_value=httpx.Response(200, json=STATUS_MAP_SAMPLE))
        result = await async_client.mcp.status()
        assert route.called
        request = route_request(route)
        assert request.method == "GET"
        assert_matches_type(McpStatusResponse, result, path=["response"])

    @pytest.mark.respx(base_url=base_url)
    async def test_status_sends_addressing_query_params(
        self, async_client: AsyncOpencode, respx_mock: MockRouter
    ) -> None:
        route = respx_mock.get("/mcp").mock(return_value=httpx.Response(200, json=STATUS_MAP_SAMPLE))
        result = await async_client.mcp.status(directory="/tmp/my-project", workspace="my-workspace")
        assert route.called
        request = route_request(route)
        assert dict(request.url.params) == {"directory": "/tmp/my-project", "workspace": "my-workspace"}
        assert_matches_type(McpStatusResponse, result, path=["response"])

    @pytest.mark.respx(base_url=base_url)
    async def test_add_sends_body(self, async_client: AsyncOpencode, respx_mock: MockRouter) -> None:
        route = respx_mock.post("/mcp").mock(return_value=httpx.Response(200, json=STATUS_MAP_SAMPLE))
        result = await async_client.mcp.add(
            name="my-server",
            config={
                "type": "local",
                "command": ["node", "server.js"],
            },
        )
        assert route.called
        body = read_json_body(route)
        assert body == {
            "name": "my-server",
            "config": {"type": "local", "command": ["node", "server.js"]},
        }
        assert_matches_type(McpAddResponse, result, path=["response"])

    @pytest.mark.respx(base_url=base_url)
    async def test_auth_start_wire_shape(self, async_client: AsyncOpencode, respx_mock: MockRouter) -> None:
        route = respx_mock.post("/mcp/my-server/auth").mock(
            return_value=httpx.Response(200, json=AUTH_START_SAMPLE)
        )
        result = await async_client.mcp.auth_start("my-server")
        assert route.called
        request = route_request(route)
        assert request.method == "POST"
        assert_matches_type(McpAuthStartResponse, result, path=["response"])

    @pytest.mark.respx(base_url=base_url)
    async def test_auth_remove_wire_shape(self, async_client: AsyncOpencode, respx_mock: MockRouter) -> None:
        route = respx_mock.delete("/mcp/my-server/auth").mock(
            return_value=httpx.Response(200, json=AUTH_REMOVE_SAMPLE)
        )
        result = await async_client.mcp.auth_remove("my-server")
        assert route.called
        request = route_request(route)
        assert request.method == "DELETE"
        assert_matches_type(McpAuthRemoveResponse, result, path=["response"])

    @pytest.mark.respx(base_url=base_url)
    async def test_auth_callback_sends_body(self, async_client: AsyncOpencode, respx_mock: MockRouter) -> None:
        route = respx_mock.post("/mcp/my-server/auth/callback").mock(
            return_value=httpx.Response(200, json={"status": "connected"})
        )
        result = await async_client.mcp.auth_callback("my-server", code="the-code")
        assert route.called
        body = read_json_body(route)
        assert body == {"code": "the-code"}
        assert_matches_type(MCPStatus, result, path=["response"])

    @pytest.mark.respx(base_url=base_url)
    async def test_auth_authenticate_wire_shape(self, async_client: AsyncOpencode, respx_mock: MockRouter) -> None:
        route = respx_mock.post("/mcp/my-server/auth/authenticate").mock(
            return_value=httpx.Response(200, json={"status": "needs_auth"})
        )
        result = await async_client.mcp.auth_authenticate("my-server")
        assert route.called
        request = route_request(route)
        assert request.method == "POST"
        assert_matches_type(MCPStatus, result, path=["response"])

    @pytest.mark.respx(base_url=base_url)
    async def test_connect_wire_shape(self, async_client: AsyncOpencode, respx_mock: MockRouter) -> None:
        route = respx_mock.post("/mcp/my-server/connect").mock(return_value=httpx.Response(200, json=True))
        result = await async_client.mcp.connect("my-server")
        assert route.called
        request = route_request(route)
        assert request.method == "POST"
        assert_matches_type(McpConnectResponse, result, path=["response"])

    @pytest.mark.respx(base_url=base_url)
    async def test_disconnect_wire_shape(self, async_client: AsyncOpencode, respx_mock: MockRouter) -> None:
        route = respx_mock.post("/mcp/my-server/disconnect").mock(return_value=httpx.Response(200, json=True))
        result = await async_client.mcp.disconnect("my-server")
        assert route.called
        request = route_request(route)
        assert request.method == "POST"
        assert_matches_type(McpDisconnectResponse, result, path=["response"])

    async def test_path_params_auth_start(self, async_client: AsyncOpencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            await async_client.mcp.with_raw_response.auth_start("")

    async def test_path_params_auth_remove(self, async_client: AsyncOpencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            await async_client.mcp.with_raw_response.auth_remove("")

    async def test_path_params_auth_callback(self, async_client: AsyncOpencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            await async_client.mcp.with_raw_response.auth_callback("", code="the-code")

    async def test_path_params_auth_authenticate(self, async_client: AsyncOpencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            await async_client.mcp.with_raw_response.auth_authenticate("")

    async def test_path_params_connect(self, async_client: AsyncOpencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            await async_client.mcp.with_raw_response.connect("")

    async def test_path_params_disconnect(self, async_client: AsyncOpencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            await async_client.mcp.with_raw_response.disconnect("")
