# Hand-maintained fork of the Stainless-era opencode SDK. Generated code was replaced by manual maintenance; see CONTRIBUTING.md.

from __future__ import annotations

import os

import httpx
import pytest
from respx import MockRouter

from opencode_ai import Opencode, AsyncOpencode
from tests.wire_helpers import route_request
from opencode_ai._models import construct_type
from opencode_ai.resources.tool import ToolResource, AsyncToolResource
from opencode_ai.types.tool_ids_response import ToolIDsResponse
from opencode_ai.types.tool_list_response import ToolListResponse, ToolListResponseItem

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")

TOOL_ITEM_PAYLOAD = {"id": "bash", "description": "Run a shell command", "parameters": {"type": "object"}}


def test_list_response_constructs() -> None:
    result = construct_type(type_=ToolListResponse, value=[TOOL_ITEM_PAYLOAD])
    assert isinstance(result, list)
    assert isinstance(result[0], ToolListResponseItem)
    assert result[0].id == "bash"
    assert result[0].parameters == {"type": "object"}


def test_ids_response_constructs() -> None:
    result = construct_type(type_=ToolIDsResponse, value=["bash", "edit"])
    assert result == ["bash", "edit"]


class TestToolWire:
    @pytest.mark.respx(base_url=base_url)
    def test_list_sends_provider_model_and_addressing_params(
        self, client: Opencode, respx_mock: MockRouter
    ) -> None:
        route = respx_mock.get("/experimental/tool").mock(return_value=httpx.Response(200, json=[TOOL_ITEM_PAYLOAD]))
        result = ToolResource(client).list(provider="anthropic", model="claude", directory="/repo", workspace="ws1")
        assert route.called
        request = route_request(route)
        assert request.method == "GET"
        assert request.url.path == "/experimental/tool"
        assert dict(request.url.params) == {
            "provider": "anthropic",
            "model": "claude",
            "directory": "/repo",
            "workspace": "ws1",
        }
        assert isinstance(result[0], ToolListResponseItem)

    @pytest.mark.respx(base_url=base_url)
    def test_list_omits_addressing_params_when_not_given(self, client: Opencode, respx_mock: MockRouter) -> None:
        route = respx_mock.get("/experimental/tool").mock(return_value=httpx.Response(200, json=[]))
        ToolResource(client).list(provider="anthropic", model="claude")
        assert route.called
        assert dict(route_request(route).url.params) == {"provider": "anthropic", "model": "claude"}

    @pytest.mark.respx(base_url=base_url)
    def test_ids_sends_addressing_params(self, client: Opencode, respx_mock: MockRouter) -> None:
        route = respx_mock.get("/experimental/tool/ids").mock(return_value=httpx.Response(200, json=["bash", "edit"]))
        result = ToolResource(client).ids(directory="/repo", workspace="ws1")
        assert route.called
        request = route_request(route)
        assert request.method == "GET"
        assert request.url.path == "/experimental/tool/ids"
        assert dict(request.url.params) == {"directory": "/repo", "workspace": "ws1"}
        assert isinstance(result, list)
        assert result == ["bash", "edit"]

    @pytest.mark.respx(base_url=base_url)
    def test_with_raw_response_ids(self, client: Opencode, respx_mock: MockRouter) -> None:
        route = respx_mock.get("/experimental/tool/ids").mock(return_value=httpx.Response(200, json=["bash", "edit"]))
        response = client.with_raw_response.tool.ids()
        assert route.called
        assert response.is_closed is True
        result = response.parse()
        assert result == ["bash", "edit"]


class TestAsyncToolWire:
    @pytest.mark.respx(base_url=base_url)
    async def test_list(self, async_client: AsyncOpencode, respx_mock: MockRouter) -> None:
        route = respx_mock.get("/experimental/tool").mock(return_value=httpx.Response(200, json=[TOOL_ITEM_PAYLOAD]))
        result = await AsyncToolResource(async_client).list(
            provider="anthropic", model="claude", directory="/repo", workspace="ws1"
        )
        assert route.called
        request = route_request(route)
        assert request.method == "GET"
        assert dict(request.url.params) == {
            "provider": "anthropic",
            "model": "claude",
            "directory": "/repo",
            "workspace": "ws1",
        }
        assert isinstance(result[0], ToolListResponseItem)

    @pytest.mark.respx(base_url=base_url)
    async def test_ids(self, async_client: AsyncOpencode, respx_mock: MockRouter) -> None:
        route = respx_mock.get("/experimental/tool/ids").mock(return_value=httpx.Response(200, json=["bash"]))
        result = await AsyncToolResource(async_client).ids(directory="/repo", workspace="ws1")
        assert route.called
        assert dict(route_request(route).url.params) == {"directory": "/repo", "workspace": "ws1"}
        assert result == ["bash"]
