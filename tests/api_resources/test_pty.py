# Hand-maintained fork of the Stainless-era opencode SDK. Generated code was replaced by manual maintenance; see CONTRIBUTING.md.

from __future__ import annotations

import os

import httpx
import pytest
from respx import MockRouter

from opencode_ai import Opencode, AsyncOpencode
from tests.utils import assert_matches_type
from opencode_ai.types import (
    Pty,
    PtyListResponse,
    PtyDeleteResponse,
    PtyShellsResponse,
    PtyConnectResponse,
    PtyConnectTokenResponse,
)
from tests.wire_helpers import route_request, read_json_body

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")

PTY_SAMPLE: dict[str, object] = {
    "id": "pty_123",
    "title": "bash",
    "command": "bash",
    "args": ["-l"],
    "cwd": "/tmp",
    "status": "running",
    "pid": 42,
}

SHELLS_SAMPLE: list[dict[str, object]] = [
    {"path": "/bin/bash", "name": "bash", "acceptable": True},
]

CONNECT_TOKEN_SAMPLE: dict[str, object] = {"ticket": "ticket-123", "expires_in": 60}


class TestPtyWire:
    @pytest.mark.respx(base_url=base_url)
    def test_list_wire_shape(self, client: Opencode, respx_mock: MockRouter) -> None:
        route = respx_mock.get("/pty").mock(return_value=httpx.Response(200, json=[PTY_SAMPLE]))
        result = client.pty.list()
        assert route.called
        request = route_request(route)
        assert request.method == "GET"
        assert_matches_type(PtyListResponse, result, path=["response"])

    @pytest.mark.respx(base_url=base_url)
    def test_create_sends_body(self, client: Opencode, respx_mock: MockRouter) -> None:
        route = respx_mock.post("/pty").mock(return_value=httpx.Response(200, json=PTY_SAMPLE))
        result = client.pty.create(
            command="bash",
            args=["-l"],
            cwd="/tmp",
            title="bash",
            env={"FOO": "bar"},
        )
        assert route.called
        request = route_request(route)
        assert request.method == "POST"
        body = read_json_body(route)
        assert body == {
            "command": "bash",
            "args": ["-l"],
            "cwd": "/tmp",
            "title": "bash",
            "env": {"FOO": "bar"},
        }
        assert_matches_type(Pty, result, path=["response"])

    @pytest.mark.respx(base_url=base_url)
    def test_retrieve_wire_shape(self, client: Opencode, respx_mock: MockRouter) -> None:
        route = respx_mock.get("/pty/pty_123").mock(return_value=httpx.Response(200, json=PTY_SAMPLE))
        result = client.pty.retrieve("pty_123")
        assert route.called
        request = route_request(route)
        assert request.method == "GET"
        assert_matches_type(Pty, result, path=["response"])

    @pytest.mark.respx(base_url=base_url)
    def test_update_sends_body(self, client: Opencode, respx_mock: MockRouter) -> None:
        route = respx_mock.put("/pty/pty_123").mock(return_value=httpx.Response(200, json=PTY_SAMPLE))
        result = client.pty.update(
            "pty_123",
            title="renamed",
            size={"rows": 24, "cols": 80},
        )
        assert route.called
        request = route_request(route)
        assert request.method == "PUT"
        body = read_json_body(route)
        assert body == {"title": "renamed", "size": {"rows": 24, "cols": 80}}
        assert_matches_type(Pty, result, path=["response"])

    @pytest.mark.respx(base_url=base_url)
    def test_delete_wire_shape(self, client: Opencode, respx_mock: MockRouter) -> None:
        route = respx_mock.delete("/pty/pty_123").mock(return_value=httpx.Response(200, json=True))
        result = client.pty.delete("pty_123")
        assert route.called
        request = route_request(route)
        assert request.method == "DELETE"
        assert_matches_type(PtyDeleteResponse, result, path=["response"])

    @pytest.mark.respx(base_url=base_url)
    def test_connect_wire_shape(self, client: Opencode, respx_mock: MockRouter) -> None:
        route = respx_mock.get("/pty/pty_123/connect").mock(return_value=httpx.Response(200, json=True))
        result = client.pty.connect("pty_123", cursor="abc", ticket="ticket-123")
        assert route.called
        request = route_request(route)
        assert request.method == "GET"
        assert dict(request.url.params) == {"cursor": "abc", "ticket": "ticket-123"}
        assert_matches_type(PtyConnectResponse, result, path=["response"])

    @pytest.mark.respx(base_url=base_url)
    def test_connect_sends_addressing_query_params(self, client: Opencode, respx_mock: MockRouter) -> None:
        route = respx_mock.get("/pty/pty_123/connect").mock(return_value=httpx.Response(200, json=True))
        result = client.pty.connect(
            "pty_123",
            cursor="abc",
            ticket="ticket-123",
            directory="/tmp/my-project",
            workspace="my-workspace",
        )
        assert route.called
        request = route_request(route)
        assert dict(request.url.params) == {
            "cursor": "abc",
            "ticket": "ticket-123",
            "directory": "/tmp/my-project",
            "workspace": "my-workspace",
        }
        assert_matches_type(PtyConnectResponse, result, path=["response"])

    @pytest.mark.respx(base_url=base_url)
    def test_connect_token_wire_shape(self, client: Opencode, respx_mock: MockRouter) -> None:
        route = respx_mock.post("/pty/pty_123/connect-token").mock(
            return_value=httpx.Response(200, json=CONNECT_TOKEN_SAMPLE)
        )
        result = client.pty.connect_token("pty_123")
        assert route.called
        request = route_request(route)
        assert request.method == "POST"
        assert_matches_type(PtyConnectTokenResponse, result, path=["response"])

    @pytest.mark.respx(base_url=base_url)
    def test_shells_wire_shape(self, client: Opencode, respx_mock: MockRouter) -> None:
        route = respx_mock.get("/pty/shells").mock(return_value=httpx.Response(200, json=SHELLS_SAMPLE))
        result = client.pty.shells()
        assert route.called
        request = route_request(route)
        assert request.method == "GET"
        assert_matches_type(PtyShellsResponse, result, path=["response"])

    def test_path_params_retrieve(self, client: Opencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `pty_id` but received ''"):
            client.pty.with_raw_response.retrieve("")

    def test_path_params_update(self, client: Opencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `pty_id` but received ''"):
            client.pty.with_raw_response.update("")

    def test_path_params_delete(self, client: Opencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `pty_id` but received ''"):
            client.pty.with_raw_response.delete("")

    def test_path_params_connect(self, client: Opencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `pty_id` but received ''"):
            client.pty.with_raw_response.connect("")

    def test_path_params_connect_token(self, client: Opencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `pty_id` but received ''"):
            client.pty.with_raw_response.connect_token("")


class TestAsyncPtyWire:
    @pytest.mark.respx(base_url=base_url)
    async def test_list_wire_shape(self, async_client: AsyncOpencode, respx_mock: MockRouter) -> None:
        route = respx_mock.get("/pty").mock(return_value=httpx.Response(200, json=[PTY_SAMPLE]))
        result = await async_client.pty.list()
        assert route.called
        request = route_request(route)
        assert request.method == "GET"
        assert_matches_type(PtyListResponse, result, path=["response"])

    @pytest.mark.respx(base_url=base_url)
    async def test_create_sends_body(self, async_client: AsyncOpencode, respx_mock: MockRouter) -> None:
        route = respx_mock.post("/pty").mock(return_value=httpx.Response(200, json=PTY_SAMPLE))
        result = await async_client.pty.create(
            command="bash",
            args=["-l"],
            cwd="/tmp",
            title="bash",
            env={"FOO": "bar"},
        )
        assert route.called
        body = read_json_body(route)
        assert body == {
            "command": "bash",
            "args": ["-l"],
            "cwd": "/tmp",
            "title": "bash",
            "env": {"FOO": "bar"},
        }
        assert_matches_type(Pty, result, path=["response"])

    @pytest.mark.respx(base_url=base_url)
    async def test_retrieve_wire_shape(self, async_client: AsyncOpencode, respx_mock: MockRouter) -> None:
        route = respx_mock.get("/pty/pty_123").mock(return_value=httpx.Response(200, json=PTY_SAMPLE))
        result = await async_client.pty.retrieve("pty_123")
        assert route.called
        request = route_request(route)
        assert request.method == "GET"
        assert_matches_type(Pty, result, path=["response"])

    @pytest.mark.respx(base_url=base_url)
    async def test_update_sends_body(self, async_client: AsyncOpencode, respx_mock: MockRouter) -> None:
        route = respx_mock.put("/pty/pty_123").mock(return_value=httpx.Response(200, json=PTY_SAMPLE))
        result = await async_client.pty.update(
            "pty_123",
            title="renamed",
            size={"rows": 24, "cols": 80},
        )
        assert route.called
        body = read_json_body(route)
        assert body == {"title": "renamed", "size": {"rows": 24, "cols": 80}}
        assert_matches_type(Pty, result, path=["response"])

    @pytest.mark.respx(base_url=base_url)
    async def test_delete_wire_shape(self, async_client: AsyncOpencode, respx_mock: MockRouter) -> None:
        route = respx_mock.delete("/pty/pty_123").mock(return_value=httpx.Response(200, json=True))
        result = await async_client.pty.delete("pty_123")
        assert route.called
        request = route_request(route)
        assert request.method == "DELETE"
        assert_matches_type(PtyDeleteResponse, result, path=["response"])

    @pytest.mark.respx(base_url=base_url)
    async def test_connect_wire_shape(self, async_client: AsyncOpencode, respx_mock: MockRouter) -> None:
        route = respx_mock.get("/pty/pty_123/connect").mock(return_value=httpx.Response(200, json=True))
        result = await async_client.pty.connect("pty_123", cursor="abc", ticket="ticket-123")
        assert route.called
        request = route_request(route)
        assert request.method == "GET"
        assert dict(request.url.params) == {"cursor": "abc", "ticket": "ticket-123"}
        assert_matches_type(PtyConnectResponse, result, path=["response"])

    @pytest.mark.respx(base_url=base_url)
    async def test_connect_sends_addressing_query_params(
        self, async_client: AsyncOpencode, respx_mock: MockRouter
    ) -> None:
        route = respx_mock.get("/pty/pty_123/connect").mock(return_value=httpx.Response(200, json=True))
        result = await async_client.pty.connect(
            "pty_123",
            cursor="abc",
            ticket="ticket-123",
            directory="/tmp/my-project",
            workspace="my-workspace",
        )
        assert route.called
        request = route_request(route)
        assert dict(request.url.params) == {
            "cursor": "abc",
            "ticket": "ticket-123",
            "directory": "/tmp/my-project",
            "workspace": "my-workspace",
        }
        assert_matches_type(PtyConnectResponse, result, path=["response"])

    @pytest.mark.respx(base_url=base_url)
    async def test_connect_token_wire_shape(self, async_client: AsyncOpencode, respx_mock: MockRouter) -> None:
        route = respx_mock.post("/pty/pty_123/connect-token").mock(
            return_value=httpx.Response(200, json=CONNECT_TOKEN_SAMPLE)
        )
        result = await async_client.pty.connect_token("pty_123")
        assert route.called
        request = route_request(route)
        assert request.method == "POST"
        assert_matches_type(PtyConnectTokenResponse, result, path=["response"])

    @pytest.mark.respx(base_url=base_url)
    async def test_shells_wire_shape(self, async_client: AsyncOpencode, respx_mock: MockRouter) -> None:
        route = respx_mock.get("/pty/shells").mock(return_value=httpx.Response(200, json=SHELLS_SAMPLE))
        result = await async_client.pty.shells()
        assert route.called
        request = route_request(route)
        assert request.method == "GET"
        assert_matches_type(PtyShellsResponse, result, path=["response"])

    async def test_path_params_retrieve(self, async_client: AsyncOpencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `pty_id` but received ''"):
            await async_client.pty.with_raw_response.retrieve("")

    async def test_path_params_update(self, async_client: AsyncOpencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `pty_id` but received ''"):
            await async_client.pty.with_raw_response.update("")

    async def test_path_params_delete(self, async_client: AsyncOpencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `pty_id` but received ''"):
            await async_client.pty.with_raw_response.delete("")

    async def test_path_params_connect(self, async_client: AsyncOpencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `pty_id` but received ''"):
            await async_client.pty.with_raw_response.connect("")

    async def test_path_params_connect_token(self, async_client: AsyncOpencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `pty_id` but received ''"):
            await async_client.pty.with_raw_response.connect_token("")
