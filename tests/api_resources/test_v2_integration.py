# Hand-maintained fork of the Stainless-era opencode SDK. Generated code was replaced by manual maintenance; see CONTRIBUTING.md.

from __future__ import annotations

import os

import httpx
import pytest
from respx import MockRouter

from opencode_ai import Opencode, AsyncOpencode
from tests.wire_helpers import route_request, read_json_body
from opencode_ai.resources.v2 import V2Resource, AsyncV2Resource

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestV2IntegrationWire:
    @pytest.mark.respx(base_url=base_url)
    def test_integration_attempt_cancel(self, client: Opencode, respx_mock: MockRouter) -> None:
        v2 = V2Resource(client)
        route = respx_mock.delete("/api/integration/attempt/attempt_id_1").mock(
            return_value=httpx.Response(200, json=None)
        )
        result = v2.integration.attempt_cancel("attempt_id_1", location={"directory": "/d", "workspace": "wrk_1"})
        assert route.called
        request = route_request(route)
        assert request.method == "DELETE"
        assert request.url.params.get("location[directory]") == "/d"
        assert result is None

    @pytest.mark.respx(base_url=base_url)
    def test_integration_attempt_complete(self, client: Opencode, respx_mock: MockRouter) -> None:
        v2 = V2Resource(client)
        route = respx_mock.post("/api/integration/attempt/attempt_id_1/complete").mock(
            return_value=httpx.Response(200, json=None)
        )
        result = v2.integration.attempt_complete("attempt_id_1", location={"directory": "/d", "workspace": "wrk_1"})
        assert route.called
        request = route_request(route)
        assert request.method == "POST"
        assert request.url.params.get("location[directory]") == "/d"
        assert result is None

    @pytest.mark.respx(base_url=base_url)
    def test_integration_attempt_status(self, client: Opencode, respx_mock: MockRouter) -> None:
        v2 = V2Resource(client)
        route = respx_mock.get("/api/integration/attempt/attempt_id_1").mock(
            return_value=httpx.Response(
                200, json={"location": {"directory": "/w", "project": {"id": "p1", "directory": "/w"}}, "data": {}}
            )
        )
        result = v2.integration.attempt_status("attempt_id_1", location={"directory": "/d", "workspace": "wrk_1"})
        assert route.called
        request = route_request(route)
        assert request.method == "GET"
        assert request.url.params.get("location[directory]") == "/d"
        assert result.location.directory == "/w"

    @pytest.mark.respx(base_url=base_url)
    def test_integration_connect_key(self, client: Opencode, respx_mock: MockRouter) -> None:
        v2 = V2Resource(client)
        route = respx_mock.post("/api/integration/integration_id_1/connect/key").mock(
            return_value=httpx.Response(200, json=None)
        )
        result = v2.integration.connect_key(
            "integration_id_1", key="x", location={"directory": "/d", "workspace": "wrk_1"}
        )
        assert route.called
        request = route_request(route)
        assert request.method == "POST"
        body = read_json_body(route)
        assert body["key"] == "x"
        assert request.url.params.get("location[directory]") == "/d"
        assert result is None

    @pytest.mark.respx(base_url=base_url)
    def test_integration_connect_oauth(self, client: Opencode, respx_mock: MockRouter) -> None:
        v2 = V2Resource(client)
        route = respx_mock.post("/api/integration/integration_id_1/connect/oauth").mock(
            return_value=httpx.Response(
                200, json={"location": {"directory": "/w", "project": {"id": "p1", "directory": "/w"}}, "data": {}}
            )
        )
        result = v2.integration.connect_oauth(
            "integration_id_1", method_id="x", inputs={}, location={"directory": "/d", "workspace": "wrk_1"}
        )
        assert route.called
        request = route_request(route)
        assert request.method == "POST"
        body = read_json_body(route)
        assert body["methodID"] == "x"
        assert request.url.params.get("location[directory]") == "/d"
        assert result.location.directory == "/w"

    @pytest.mark.respx(base_url=base_url)
    def test_integration_get(self, client: Opencode, respx_mock: MockRouter) -> None:
        v2 = V2Resource(client)
        route = respx_mock.get("/api/integration/integration_id_1").mock(
            return_value=httpx.Response(
                200, json={"location": {"directory": "/w", "project": {"id": "p1", "directory": "/w"}}, "data": {}}
            )
        )
        result = v2.integration.get("integration_id_1", location={"directory": "/d", "workspace": "wrk_1"})
        assert route.called
        request = route_request(route)
        assert request.method == "GET"
        assert request.url.params.get("location[directory]") == "/d"
        assert result.location.directory == "/w"

    @pytest.mark.respx(base_url=base_url)
    def test_integration_list(self, client: Opencode, respx_mock: MockRouter) -> None:
        v2 = V2Resource(client)
        route = respx_mock.get("/api/integration").mock(
            return_value=httpx.Response(
                200, json={"location": {"directory": "/w", "project": {"id": "p1", "directory": "/w"}}, "data": []}
            )
        )
        result = v2.integration.list(location={"directory": "/d", "workspace": "wrk_1"})
        assert route.called
        request = route_request(route)
        assert request.method == "GET"
        assert request.url.params.get("location[directory]") == "/d"
        assert result.location.directory == "/w"


class TestAsyncV2IntegrationWire:
    @pytest.mark.respx(base_url=base_url)
    async def test_integration_attempt_cancel(self, async_client: AsyncOpencode, respx_mock: MockRouter) -> None:
        v2 = AsyncV2Resource(async_client)
        route = respx_mock.delete("/api/integration/attempt/attempt_id_1").mock(
            return_value=httpx.Response(200, json=None)
        )
        result = await v2.integration.attempt_cancel("attempt_id_1", location={"directory": "/d", "workspace": "wrk_1"})
        assert route.called
        request = route_request(route)
        assert request.method == "DELETE"
        assert request.url.params.get("location[directory]") == "/d"
        assert result is None

    @pytest.mark.respx(base_url=base_url)
    async def test_integration_attempt_complete(self, async_client: AsyncOpencode, respx_mock: MockRouter) -> None:
        v2 = AsyncV2Resource(async_client)
        route = respx_mock.post("/api/integration/attempt/attempt_id_1/complete").mock(
            return_value=httpx.Response(200, json=None)
        )
        result = await v2.integration.attempt_complete(
            "attempt_id_1", location={"directory": "/d", "workspace": "wrk_1"}
        )
        assert route.called
        request = route_request(route)
        assert request.method == "POST"
        assert request.url.params.get("location[directory]") == "/d"
        assert result is None

    @pytest.mark.respx(base_url=base_url)
    async def test_integration_attempt_status(self, async_client: AsyncOpencode, respx_mock: MockRouter) -> None:
        v2 = AsyncV2Resource(async_client)
        route = respx_mock.get("/api/integration/attempt/attempt_id_1").mock(
            return_value=httpx.Response(
                200, json={"location": {"directory": "/w", "project": {"id": "p1", "directory": "/w"}}, "data": {}}
            )
        )
        result = await v2.integration.attempt_status("attempt_id_1", location={"directory": "/d", "workspace": "wrk_1"})
        assert route.called
        request = route_request(route)
        assert request.method == "GET"
        assert request.url.params.get("location[directory]") == "/d"
        assert result.location.directory == "/w"

    @pytest.mark.respx(base_url=base_url)
    async def test_integration_connect_key(self, async_client: AsyncOpencode, respx_mock: MockRouter) -> None:
        v2 = AsyncV2Resource(async_client)
        route = respx_mock.post("/api/integration/integration_id_1/connect/key").mock(
            return_value=httpx.Response(200, json=None)
        )
        result = await v2.integration.connect_key(
            "integration_id_1", key="x", location={"directory": "/d", "workspace": "wrk_1"}
        )
        assert route.called
        request = route_request(route)
        assert request.method == "POST"
        body = read_json_body(route)
        assert body["key"] == "x"
        assert request.url.params.get("location[directory]") == "/d"
        assert result is None

    @pytest.mark.respx(base_url=base_url)
    async def test_integration_connect_oauth(self, async_client: AsyncOpencode, respx_mock: MockRouter) -> None:
        v2 = AsyncV2Resource(async_client)
        route = respx_mock.post("/api/integration/integration_id_1/connect/oauth").mock(
            return_value=httpx.Response(
                200, json={"location": {"directory": "/w", "project": {"id": "p1", "directory": "/w"}}, "data": {}}
            )
        )
        result = await v2.integration.connect_oauth(
            "integration_id_1", method_id="x", inputs={}, location={"directory": "/d", "workspace": "wrk_1"}
        )
        assert route.called
        request = route_request(route)
        assert request.method == "POST"
        body = read_json_body(route)
        assert body["methodID"] == "x"
        assert request.url.params.get("location[directory]") == "/d"
        assert result.location.directory == "/w"

    @pytest.mark.respx(base_url=base_url)
    async def test_integration_get(self, async_client: AsyncOpencode, respx_mock: MockRouter) -> None:
        v2 = AsyncV2Resource(async_client)
        route = respx_mock.get("/api/integration/integration_id_1").mock(
            return_value=httpx.Response(
                200, json={"location": {"directory": "/w", "project": {"id": "p1", "directory": "/w"}}, "data": {}}
            )
        )
        result = await v2.integration.get("integration_id_1", location={"directory": "/d", "workspace": "wrk_1"})
        assert route.called
        request = route_request(route)
        assert request.method == "GET"
        assert request.url.params.get("location[directory]") == "/d"
        assert result.location.directory == "/w"

    @pytest.mark.respx(base_url=base_url)
    async def test_integration_list(self, async_client: AsyncOpencode, respx_mock: MockRouter) -> None:
        v2 = AsyncV2Resource(async_client)
        route = respx_mock.get("/api/integration").mock(
            return_value=httpx.Response(
                200, json={"location": {"directory": "/w", "project": {"id": "p1", "directory": "/w"}}, "data": []}
            )
        )
        result = await v2.integration.list(location={"directory": "/d", "workspace": "wrk_1"})
        assert route.called
        request = route_request(route)
        assert request.method == "GET"
        assert request.url.params.get("location[directory]") == "/d"
        assert result.location.directory == "/w"
