# Hand-maintained fork of the Stainless-era opencode SDK. Generated code was replaced by manual maintenance; see CONTRIBUTING.md.

from __future__ import annotations

import os

import httpx
import pytest
from respx import MockRouter

from opencode_ai import Opencode, AsyncOpencode
from tests.wire_helpers import route_request
from opencode_ai.resources.v2 import V2Resource, AsyncV2Resource

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestV2PermissionWire:
    @pytest.mark.respx(base_url=base_url)
    def test_permission_request_list(self, client: Opencode, respx_mock: MockRouter) -> None:
        v2 = V2Resource(client)
        route = respx_mock.get("/api/permission/request").mock(
            return_value=httpx.Response(
                200, json={"location": {"directory": "/w", "project": {"id": "p1", "directory": "/w"}}, "data": []}
            )
        )
        result = v2.permission.request_list(location={"directory": "/d", "workspace": "wrk_1"})
        assert route.called
        request = route_request(route)
        assert request.method == "GET"
        assert request.url.params.get("location[directory]") == "/d"
        assert result.location.directory == "/w"

    @pytest.mark.respx(base_url=base_url)
    def test_permission_saved_list(self, client: Opencode, respx_mock: MockRouter) -> None:
        v2 = V2Resource(client)
        route = respx_mock.get("/api/permission/saved").mock(return_value=httpx.Response(200, json={"data": []}))
        result = v2.permission.saved_list(project_id="qv")
        assert route.called
        request = route_request(route)
        assert request.method == "GET"
        assert request.url.params.get("projectID") == "qv"
        assert result is not None

    @pytest.mark.respx(base_url=base_url)
    def test_permission_saved_remove(self, client: Opencode, respx_mock: MockRouter) -> None:
        v2 = V2Resource(client)
        route = respx_mock.delete("/api/permission/saved/id_1").mock(return_value=httpx.Response(200, json=None))
        result = v2.permission.saved_remove("id_1")
        assert route.called
        request = route_request(route)
        assert request.method == "DELETE"
        assert result is None


class TestAsyncV2PermissionWire:
    @pytest.mark.respx(base_url=base_url)
    async def test_permission_request_list(self, async_client: AsyncOpencode, respx_mock: MockRouter) -> None:
        v2 = AsyncV2Resource(async_client)
        route = respx_mock.get("/api/permission/request").mock(
            return_value=httpx.Response(
                200, json={"location": {"directory": "/w", "project": {"id": "p1", "directory": "/w"}}, "data": []}
            )
        )
        result = await v2.permission.request_list(location={"directory": "/d", "workspace": "wrk_1"})
        assert route.called
        request = route_request(route)
        assert request.method == "GET"
        assert request.url.params.get("location[directory]") == "/d"
        assert result.location.directory == "/w"

    @pytest.mark.respx(base_url=base_url)
    async def test_permission_saved_list(self, async_client: AsyncOpencode, respx_mock: MockRouter) -> None:
        v2 = AsyncV2Resource(async_client)
        route = respx_mock.get("/api/permission/saved").mock(return_value=httpx.Response(200, json={"data": []}))
        result = await v2.permission.saved_list(project_id="qv")
        assert route.called
        request = route_request(route)
        assert request.method == "GET"
        assert request.url.params.get("projectID") == "qv"
        assert result is not None

    @pytest.mark.respx(base_url=base_url)
    async def test_permission_saved_remove(self, async_client: AsyncOpencode, respx_mock: MockRouter) -> None:
        v2 = AsyncV2Resource(async_client)
        route = respx_mock.delete("/api/permission/saved/id_1").mock(return_value=httpx.Response(200, json=None))
        result = await v2.permission.saved_remove("id_1")
        assert route.called
        request = route_request(route)
        assert request.method == "DELETE"
        assert result is None
