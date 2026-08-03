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


class TestV2PtyWire:
    @pytest.mark.respx(base_url=base_url)
    def test_pty_connect(self, client: Opencode, respx_mock: MockRouter) -> None:
        v2 = V2Resource(client)
        route = respx_mock.get("/api/pty/pty_id_1/connect").mock(return_value=httpx.Response(200, json=True))
        result = v2.pty.connect("pty_id_1", directory="/d", workspace="/d", cursor="qv", ticket="qv")
        assert route.called
        request = route_request(route)
        assert request.method == "GET"
        assert request.url.params.get("location[directory]") == "/d"
        assert request.url.params.get("location[workspace]") == "/d"
        assert request.url.params.get("cursor") == "qv"
        assert request.url.params.get("ticket") == "qv"
        assert result is True

    @pytest.mark.respx(base_url=base_url)
    def test_pty_connect_token(self, client: Opencode, respx_mock: MockRouter) -> None:
        v2 = V2Resource(client)
        route = respx_mock.post("/api/pty/pty_id_1/connect-token").mock(
            return_value=httpx.Response(
                200, json={"location": {"directory": "/w", "project": {"id": "p1", "directory": "/w"}}, "data": {}}
            )
        )
        result = v2.pty.connect_token("pty_id_1", location={"directory": "/d", "workspace": "wrk_1"})
        assert route.called
        request = route_request(route)
        assert request.method == "POST"
        assert request.url.params.get("location[directory]") == "/d"
        assert result.location.directory == "/w"

    @pytest.mark.respx(base_url=base_url)
    def test_pty_create(self, client: Opencode, respx_mock: MockRouter) -> None:
        v2 = V2Resource(client)
        route = respx_mock.post("/api/pty").mock(
            return_value=httpx.Response(
                200, json={"location": {"directory": "/w", "project": {"id": "p1", "directory": "/w"}}, "data": {}}
            )
        )
        result = v2.pty.create(location={"directory": "/d", "workspace": "wrk_1"})
        assert route.called
        request = route_request(route)
        assert request.method == "POST"
        assert request.url.params.get("location[directory]") == "/d"
        assert result.location.directory == "/w"

    @pytest.mark.respx(base_url=base_url)
    def test_pty_get(self, client: Opencode, respx_mock: MockRouter) -> None:
        v2 = V2Resource(client)
        route = respx_mock.get("/api/pty/pty_id_1").mock(
            return_value=httpx.Response(
                200, json={"location": {"directory": "/w", "project": {"id": "p1", "directory": "/w"}}, "data": {}}
            )
        )
        result = v2.pty.get("pty_id_1", location={"directory": "/d", "workspace": "wrk_1"})
        assert route.called
        request = route_request(route)
        assert request.method == "GET"
        assert request.url.params.get("location[directory]") == "/d"
        assert result.location.directory == "/w"

    @pytest.mark.respx(base_url=base_url)
    def test_pty_list(self, client: Opencode, respx_mock: MockRouter) -> None:
        v2 = V2Resource(client)
        route = respx_mock.get("/api/pty").mock(
            return_value=httpx.Response(
                200, json={"location": {"directory": "/w", "project": {"id": "p1", "directory": "/w"}}, "data": []}
            )
        )
        result = v2.pty.list(location={"directory": "/d", "workspace": "wrk_1"})
        assert route.called
        request = route_request(route)
        assert request.method == "GET"
        assert request.url.params.get("location[directory]") == "/d"
        assert result.location.directory == "/w"

    @pytest.mark.respx(base_url=base_url)
    def test_pty_remove(self, client: Opencode, respx_mock: MockRouter) -> None:
        v2 = V2Resource(client)
        route = respx_mock.delete("/api/pty/pty_id_1").mock(return_value=httpx.Response(200, json=None))
        result = v2.pty.remove("pty_id_1", location={"directory": "/d", "workspace": "wrk_1"})
        assert route.called
        request = route_request(route)
        assert request.method == "DELETE"
        assert request.url.params.get("location[directory]") == "/d"
        assert result is None

    @pytest.mark.respx(base_url=base_url)
    def test_pty_update(self, client: Opencode, respx_mock: MockRouter) -> None:
        v2 = V2Resource(client)
        route = respx_mock.put("/api/pty/pty_id_1").mock(
            return_value=httpx.Response(
                200, json={"location": {"directory": "/w", "project": {"id": "p1", "directory": "/w"}}, "data": {}}
            )
        )
        result = v2.pty.update("pty_id_1", location={"directory": "/d", "workspace": "wrk_1"})
        assert route.called
        request = route_request(route)
        assert request.method == "PUT"
        assert request.url.params.get("location[directory]") == "/d"
        assert result.location.directory == "/w"


class TestAsyncV2PtyWire:
    @pytest.mark.respx(base_url=base_url)
    async def test_pty_connect(self, async_client: AsyncOpencode, respx_mock: MockRouter) -> None:
        v2 = AsyncV2Resource(async_client)
        route = respx_mock.get("/api/pty/pty_id_1/connect").mock(return_value=httpx.Response(200, json=True))
        result = await v2.pty.connect("pty_id_1", directory="/d", workspace="/d", cursor="qv", ticket="qv")
        assert route.called
        request = route_request(route)
        assert request.method == "GET"
        assert request.url.params.get("location[directory]") == "/d"
        assert request.url.params.get("location[workspace]") == "/d"
        assert request.url.params.get("cursor") == "qv"
        assert request.url.params.get("ticket") == "qv"
        assert result is True

    @pytest.mark.respx(base_url=base_url)
    async def test_pty_connect_token(self, async_client: AsyncOpencode, respx_mock: MockRouter) -> None:
        v2 = AsyncV2Resource(async_client)
        route = respx_mock.post("/api/pty/pty_id_1/connect-token").mock(
            return_value=httpx.Response(
                200, json={"location": {"directory": "/w", "project": {"id": "p1", "directory": "/w"}}, "data": {}}
            )
        )
        result = await v2.pty.connect_token("pty_id_1", location={"directory": "/d", "workspace": "wrk_1"})
        assert route.called
        request = route_request(route)
        assert request.method == "POST"
        assert request.url.params.get("location[directory]") == "/d"
        assert result.location.directory == "/w"

    @pytest.mark.respx(base_url=base_url)
    async def test_pty_create(self, async_client: AsyncOpencode, respx_mock: MockRouter) -> None:
        v2 = AsyncV2Resource(async_client)
        route = respx_mock.post("/api/pty").mock(
            return_value=httpx.Response(
                200, json={"location": {"directory": "/w", "project": {"id": "p1", "directory": "/w"}}, "data": {}}
            )
        )
        result = await v2.pty.create(location={"directory": "/d", "workspace": "wrk_1"})
        assert route.called
        request = route_request(route)
        assert request.method == "POST"
        assert request.url.params.get("location[directory]") == "/d"
        assert result.location.directory == "/w"

    @pytest.mark.respx(base_url=base_url)
    async def test_pty_get(self, async_client: AsyncOpencode, respx_mock: MockRouter) -> None:
        v2 = AsyncV2Resource(async_client)
        route = respx_mock.get("/api/pty/pty_id_1").mock(
            return_value=httpx.Response(
                200, json={"location": {"directory": "/w", "project": {"id": "p1", "directory": "/w"}}, "data": {}}
            )
        )
        result = await v2.pty.get("pty_id_1", location={"directory": "/d", "workspace": "wrk_1"})
        assert route.called
        request = route_request(route)
        assert request.method == "GET"
        assert request.url.params.get("location[directory]") == "/d"
        assert result.location.directory == "/w"

    @pytest.mark.respx(base_url=base_url)
    async def test_pty_list(self, async_client: AsyncOpencode, respx_mock: MockRouter) -> None:
        v2 = AsyncV2Resource(async_client)
        route = respx_mock.get("/api/pty").mock(
            return_value=httpx.Response(
                200, json={"location": {"directory": "/w", "project": {"id": "p1", "directory": "/w"}}, "data": []}
            )
        )
        result = await v2.pty.list(location={"directory": "/d", "workspace": "wrk_1"})
        assert route.called
        request = route_request(route)
        assert request.method == "GET"
        assert request.url.params.get("location[directory]") == "/d"
        assert result.location.directory == "/w"

    @pytest.mark.respx(base_url=base_url)
    async def test_pty_remove(self, async_client: AsyncOpencode, respx_mock: MockRouter) -> None:
        v2 = AsyncV2Resource(async_client)
        route = respx_mock.delete("/api/pty/pty_id_1").mock(return_value=httpx.Response(200, json=None))
        result = await v2.pty.remove("pty_id_1", location={"directory": "/d", "workspace": "wrk_1"})
        assert route.called
        request = route_request(route)
        assert request.method == "DELETE"
        assert request.url.params.get("location[directory]") == "/d"
        assert result is None

    @pytest.mark.respx(base_url=base_url)
    async def test_pty_update(self, async_client: AsyncOpencode, respx_mock: MockRouter) -> None:
        v2 = AsyncV2Resource(async_client)
        route = respx_mock.put("/api/pty/pty_id_1").mock(
            return_value=httpx.Response(
                200, json={"location": {"directory": "/w", "project": {"id": "p1", "directory": "/w"}}, "data": {}}
            )
        )
        result = await v2.pty.update("pty_id_1", location={"directory": "/d", "workspace": "wrk_1"})
        assert route.called
        request = route_request(route)
        assert request.method == "PUT"
        assert request.url.params.get("location[directory]") == "/d"
        assert result.location.directory == "/w"
