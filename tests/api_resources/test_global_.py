# Hand-maintained fork of the Stainless-era opencode SDK. Generated code was replaced by manual maintenance; see CONTRIBUTING.md.

from __future__ import annotations

import os

import httpx
import pytest
from respx import MockRouter

from opencode_ai import Opencode, AsyncOpencode
from tests.wire_helpers import route_request, read_json_body
from opencode_ai._models import construct_type
from opencode_ai.resources.global_ import GlobalResource, AsyncGlobalResource
from opencode_ai.types.event_list_response import EventInstallationUpdated
from opencode_ai.types.global_event_response import GlobalEventResponse
from opencode_ai.types.global_health_response import GlobalHealthResponse
from opencode_ai.types.global_upgrade_response import GlobalUpgradeFailure, GlobalUpgradeSuccess, GlobalUpgradeResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


def test_health_response_constructs() -> None:
    result = construct_type(type_=GlobalHealthResponse, value={"healthy": True, "version": "1.18.11"})
    assert isinstance(result, GlobalHealthResponse)
    assert result.healthy is True
    assert result.version == "1.18.11"


def test_upgrade_success_constructs() -> None:
    result = construct_type(type_=GlobalUpgradeResponse, value={"success": True, "version": "1.18.12"})
    assert isinstance(result, GlobalUpgradeSuccess)
    assert result.version == "1.18.12"


def test_upgrade_failure_constructs() -> None:
    result = construct_type(type_=GlobalUpgradeResponse, value={"success": False, "error": "no update available"})
    assert isinstance(result, GlobalUpgradeFailure)
    assert result.error == "no update available"


def test_global_event_payload_discriminates() -> None:
    payload = {"id": "evt_1", "type": "installation.updated", "properties": {"version": "1.2.3"}}
    result = construct_type(
        type_=GlobalEventResponse,
        value={"directory": "/repo", "project": "proj", "payload": payload},
    )
    assert isinstance(result, GlobalEventResponse)
    assert result.directory == "/repo"
    assert result.project == "proj"
    assert isinstance(result.payload, EventInstallationUpdated)
    assert result.payload.properties.version == "1.2.3"


class TestGlobalWire:
    @pytest.mark.respx(base_url=base_url)
    def test_health_hits_path_without_params(self, client: Opencode, respx_mock: MockRouter) -> None:
        route = respx_mock.get("/global/health").mock(
            return_value=httpx.Response(200, json={"healthy": True, "version": "1.18.11"})
        )
        result = GlobalResource(client).health()
        assert route.called
        request = route_request(route)
        assert request.method == "GET"
        assert request.url.path == "/global/health"
        assert dict(request.url.params) == {}
        assert isinstance(result, GlobalHealthResponse)
        assert result.version == "1.18.11"

    @pytest.mark.respx(base_url=base_url)
    def test_event_hits_path_without_params(self, client: Opencode, respx_mock: MockRouter) -> None:
        route = respx_mock.get("/global/event").mock(
            return_value=httpx.Response(200, headers={"content-type": "text/event-stream"}, content=b"")
        )
        stream = GlobalResource(client).event()
        assert route.called
        request = route_request(route)
        assert request.method == "GET"
        assert request.url.path == "/global/event"
        assert dict(request.url.params) == {}
        stream.response.close()

    @pytest.mark.respx(base_url=base_url)
    def test_config_get_hits_path_without_params(self, client: Opencode, respx_mock: MockRouter) -> None:
        route = respx_mock.get("/global/config").mock(return_value=httpx.Response(200, json={}))
        result = GlobalResource(client).config.get()
        assert route.called
        request = route_request(route)
        assert request.method == "GET"
        assert request.url.path == "/global/config"
        assert dict(request.url.params) == {}
        assert result is not None

    @pytest.mark.respx(base_url=base_url)
    def test_config_update_sends_body_without_params(self, client: Opencode, respx_mock: MockRouter) -> None:
        route = respx_mock.patch("/global/config").mock(return_value=httpx.Response(200, json={"shell": "/bin/zsh"}))
        result = GlobalResource(client).config.update(shell="/bin/zsh")
        assert route.called
        request = route_request(route)
        assert request.method == "PATCH"
        assert request.url.path == "/global/config"
        assert dict(request.url.params) == {}
        body = read_json_body(route)
        assert body["shell"] == "/bin/zsh"
        assert result is not None

    @pytest.mark.respx(base_url=base_url)
    def test_dispose_hits_path(self, client: Opencode, respx_mock: MockRouter) -> None:
        route = respx_mock.post("/global/dispose").mock(return_value=httpx.Response(200, json=True))
        result = GlobalResource(client).dispose()
        assert route.called
        request = route_request(route)
        assert request.method == "POST"
        assert request.url.path == "/global/dispose"
        assert dict(request.url.params) == {}
        assert result is True

    @pytest.mark.respx(base_url=base_url)
    def test_upgrade_sends_body_and_parses_success(self, client: Opencode, respx_mock: MockRouter) -> None:
        route = respx_mock.post("/global/upgrade").mock(
            return_value=httpx.Response(200, json={"success": True, "version": "1.18.12"})
        )
        result = GlobalResource(client).upgrade(target="1.18.12")
        assert route.called
        request = route_request(route)
        assert request.method == "POST"
        assert request.url.path == "/global/upgrade"
        assert dict(request.url.params) == {}
        body = read_json_body(route)
        assert body == {"target": "1.18.12"}
        assert isinstance(result, GlobalUpgradeSuccess)
        assert result.version == "1.18.12"

    @pytest.mark.respx(base_url=base_url)
    def test_upgrade_without_target_sends_empty_body(self, client: Opencode, respx_mock: MockRouter) -> None:
        route = respx_mock.post("/global/upgrade").mock(
            return_value=httpx.Response(200, json={"success": False, "error": "no update available"})
        )
        result = GlobalResource(client).upgrade()
        assert route.called
        body = read_json_body(route)
        assert body == {}
        assert isinstance(result, GlobalUpgradeFailure)


class TestAsyncGlobalWire:
    @pytest.mark.respx(base_url=base_url)
    async def test_health(self, async_client: AsyncOpencode, respx_mock: MockRouter) -> None:
        route = respx_mock.get("/global/health").mock(
            return_value=httpx.Response(200, json={"healthy": True, "version": "1.18.11"})
        )
        result = await AsyncGlobalResource(async_client).health()
        assert route.called
        request = route_request(route)
        assert request.method == "GET"
        assert request.url.path == "/global/health"
        assert isinstance(result, GlobalHealthResponse)

    @pytest.mark.respx(base_url=base_url)
    async def test_event(self, async_client: AsyncOpencode, respx_mock: MockRouter) -> None:
        route = respx_mock.get("/global/event").mock(
            return_value=httpx.Response(200, headers={"content-type": "text/event-stream"}, content=b"")
        )
        stream = await AsyncGlobalResource(async_client).event()
        assert route.called
        assert route_request(route).url.path == "/global/event"
        await stream.response.aclose()

    @pytest.mark.respx(base_url=base_url)
    async def test_config_get(self, async_client: AsyncOpencode, respx_mock: MockRouter) -> None:
        route = respx_mock.get("/global/config").mock(return_value=httpx.Response(200, json={}))
        result = await AsyncGlobalResource(async_client).config.get()
        assert route.called
        request = route_request(route)
        assert request.method == "GET"
        assert request.url.path == "/global/config"
        assert result is not None

    @pytest.mark.respx(base_url=base_url)
    async def test_config_update(self, async_client: AsyncOpencode, respx_mock: MockRouter) -> None:
        route = respx_mock.patch("/global/config").mock(return_value=httpx.Response(200, json={}))
        result = await AsyncGlobalResource(async_client).config.update(shell="/bin/bash")
        assert route.called
        request = route_request(route)
        assert request.method == "PATCH"
        assert read_json_body(route)["shell"] == "/bin/bash"
        assert result is not None

    @pytest.mark.respx(base_url=base_url)
    async def test_dispose(self, async_client: AsyncOpencode, respx_mock: MockRouter) -> None:
        route = respx_mock.post("/global/dispose").mock(return_value=httpx.Response(200, json=True))
        result = await AsyncGlobalResource(async_client).dispose()
        assert route.called
        assert route_request(route).method == "POST"
        assert result is True

    @pytest.mark.respx(base_url=base_url)
    async def test_upgrade(self, async_client: AsyncOpencode, respx_mock: MockRouter) -> None:
        route = respx_mock.post("/global/upgrade").mock(
            return_value=httpx.Response(200, json={"success": True, "version": "1.18.12"})
        )
        result = await AsyncGlobalResource(async_client).upgrade()
        assert route.called
        assert read_json_body(route) == {}
        assert isinstance(result, GlobalUpgradeSuccess)
