# Hand-maintained fork of the Stainless-era opencode SDK. Generated code was replaced by manual maintenance; see CONTRIBUTING.md.

from __future__ import annotations

import os

import httpx
import pytest
from respx import MockRouter

from opencode_ai import Opencode, AsyncOpencode
from tests.wire_helpers import route_request, read_json_body
from opencode_ai._models import construct_type
from opencode_ai.types.worktree import Worktree
from opencode_ai.resources.worktree import WorktreeResource, AsyncWorktreeResource
from opencode_ai.types.worktree_list_response import WorktreeListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")

WORKTREE_PAYLOAD = {"name": "feature", "branch": "feat/x", "directory": "/repo/.worktrees/feature"}


def test_worktree_constructs() -> None:
    result = construct_type(type_=Worktree, value=WORKTREE_PAYLOAD)
    assert isinstance(result, Worktree)
    assert result.name == "feature"
    assert result.branch == "feat/x"
    assert result.directory == "/repo/.worktrees/feature"


def test_list_response_constructs() -> None:
    result = construct_type(type_=WorktreeListResponse, value=["/repo/.worktrees/feature"])
    assert result == ["/repo/.worktrees/feature"]


class TestWorktreeWire:
    @pytest.mark.respx(base_url=base_url)
    def test_list_sends_addressing_params(self, client: Opencode, respx_mock: MockRouter) -> None:
        route = respx_mock.get("/experimental/worktree").mock(
            return_value=httpx.Response(200, json=["/repo/.worktrees/feature"])
        )
        result = WorktreeResource(client).list(directory="/repo", workspace="ws1")
        assert route.called
        request = route_request(route)
        assert request.method == "GET"
        assert request.url.path == "/experimental/worktree"
        assert dict(request.url.params) == {"directory": "/repo", "workspace": "ws1"}
        assert result == ["/repo/.worktrees/feature"]

    @pytest.mark.respx(base_url=base_url)
    def test_create_sends_body_and_addressing_params(self, client: Opencode, respx_mock: MockRouter) -> None:
        route = respx_mock.post("/experimental/worktree").mock(
            return_value=httpx.Response(200, json=WORKTREE_PAYLOAD)
        )
        result = WorktreeResource(client).create(
            name="feature", start_command="cargo test", directory="/repo", workspace="ws1"
        )
        assert route.called
        request = route_request(route)
        assert request.method == "POST"
        assert request.url.path == "/experimental/worktree"
        assert dict(request.url.params) == {"directory": "/repo", "workspace": "ws1"}
        body = read_json_body(route)
        assert body == {"name": "feature", "startCommand": "cargo test"}
        assert isinstance(result, Worktree)
        assert result.name == "feature"

    @pytest.mark.respx(base_url=base_url)
    def test_create_optional_body_fields_omitted(self, client: Opencode, respx_mock: MockRouter) -> None:
        route = respx_mock.post("/experimental/worktree").mock(
            return_value=httpx.Response(200, json=WORKTREE_PAYLOAD)
        )
        WorktreeResource(client).create()
        assert route.called
        assert read_json_body(route) == {}
        assert dict(route_request(route).url.params) == {}

    @pytest.mark.respx(base_url=base_url)
    def test_remove_sends_body_and_addressing_params(self, client: Opencode, respx_mock: MockRouter) -> None:
        route = respx_mock.delete("/experimental/worktree").mock(return_value=httpx.Response(200, json=True))
        result = WorktreeResource(client).remove(directory="/repo/.worktrees/feature", query_directory="/repo", workspace="ws1")
        assert route.called
        request = route_request(route)
        assert request.method == "DELETE"
        assert request.url.path == "/experimental/worktree"
        assert dict(request.url.params) == {"directory": "/repo", "workspace": "ws1"}
        assert read_json_body(route) == {"directory": "/repo/.worktrees/feature"}
        assert result is True

    @pytest.mark.respx(base_url=base_url)
    def test_reset_sends_body_and_addressing_params(self, client: Opencode, respx_mock: MockRouter) -> None:
        route = respx_mock.post("/experimental/worktree/reset").mock(return_value=httpx.Response(200, json=True))
        result = WorktreeResource(client).reset(directory="/repo/.worktrees/feature", query_directory="/repo", workspace="ws1")
        assert route.called
        request = route_request(route)
        assert request.method == "POST"
        assert request.url.path == "/experimental/worktree/reset"
        assert dict(request.url.params) == {"directory": "/repo", "workspace": "ws1"}
        assert read_json_body(route) == {"directory": "/repo/.worktrees/feature"}
        assert result is True

    @pytest.mark.respx(base_url=base_url)
    def test_with_raw_response_list(self, client: Opencode, respx_mock: MockRouter) -> None:
        route = respx_mock.get("/experimental/worktree").mock(
            return_value=httpx.Response(200, json=["/repo/.worktrees/feature"])
        )
        response = client.with_raw_response.worktree.list()
        assert route.called
        assert response.is_closed is True
        result = response.parse()
        assert result == ["/repo/.worktrees/feature"]


class TestAsyncWorktreeWire:
    @pytest.mark.respx(base_url=base_url)
    async def test_list(self, async_client: AsyncOpencode, respx_mock: MockRouter) -> None:
        route = respx_mock.get("/experimental/worktree").mock(return_value=httpx.Response(200, json=[]))
        result = await AsyncWorktreeResource(async_client).list(directory="/repo", workspace="ws1")
        assert route.called
        request = route_request(route)
        assert request.method == "GET"
        assert dict(request.url.params) == {"directory": "/repo", "workspace": "ws1"}
        assert result == []

    @pytest.mark.respx(base_url=base_url)
    async def test_create(self, async_client: AsyncOpencode, respx_mock: MockRouter) -> None:
        route = respx_mock.post("/experimental/worktree").mock(
            return_value=httpx.Response(200, json=WORKTREE_PAYLOAD)
        )
        result = await AsyncWorktreeResource(async_client).create(name="feature", directory="/repo")
        assert route.called
        assert read_json_body(route) == {"name": "feature"}
        assert dict(route_request(route).url.params) == {"directory": "/repo"}
        assert isinstance(result, Worktree)

    @pytest.mark.respx(base_url=base_url)
    async def test_remove(self, async_client: AsyncOpencode, respx_mock: MockRouter) -> None:
        route = respx_mock.delete("/experimental/worktree").mock(return_value=httpx.Response(200, json=True))
        result = await AsyncWorktreeResource(async_client).remove(directory="/repo/.worktrees/feature")
        assert route.called
        assert read_json_body(route) == {"directory": "/repo/.worktrees/feature"}
        assert result is True

    @pytest.mark.respx(base_url=base_url)
    async def test_reset(self, async_client: AsyncOpencode, respx_mock: MockRouter) -> None:
        route = respx_mock.post("/experimental/worktree/reset").mock(return_value=httpx.Response(200, json=True))
        result = await AsyncWorktreeResource(async_client).reset(directory="/repo/.worktrees/feature")
        assert route.called
        assert read_json_body(route) == {"directory": "/repo/.worktrees/feature"}
        assert result is True
