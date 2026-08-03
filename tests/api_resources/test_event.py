# Hand-maintained fork of the Stainless-era opencode SDK. Generated code was replaced by manual maintenance; see CONTRIBUTING.md.

from __future__ import annotations

import os
from typing import Any, cast

import httpx
import pytest
from respx import MockRouter

from opencode_ai import Opencode, AsyncOpencode
from opencode_ai.types import EventListResponse
from tests.wire_helpers import route_request
from opencode_ai._models import construct_type
from opencode_ai.types.event_list_response import EventUnknown, EventInstallationUpdated

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


def test_unknown_event_type_does_not_raise() -> None:
    payload = {"type": "some.future.kind.not.in.spec", "properties": {"x": 1}}
    event = construct_type(type_=EventListResponse, value=payload)
    assert event is not None
    # Must land on the permissive fallback with the original data intact --
    # not silently be coerced into an unrelated known variant.
    assert isinstance(event, EventUnknown)
    assert event.type == "some.future.kind.not.in.spec"
    assert event.properties == {"x": 1}


def test_known_event_type_still_resolves_correctly() -> None:
    payload = {"id": "evt_1", "type": "installation.updated", "properties": {"version": "1.2.3"}}
    event = construct_type(type_=EventListResponse, value=payload)
    assert isinstance(event, EventInstallationUpdated)
    assert event.properties.version == "1.2.3"


class TestEvent:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Opencode) -> None:
        event_stream = client.event.list()
        event_stream.response.close()

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Opencode) -> None:
        response = client.event.with_raw_response.list()

        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = response.parse()
        stream.close()

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Opencode) -> None:
        with client.event.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = response.parse()
            stream.close()

        assert cast(Any, response.is_closed) is True


class TestEventWire:
    @pytest.mark.respx(base_url=base_url)
    def test_list_sends_directory_and_workspace_query(self, client: Opencode, respx_mock: MockRouter) -> None:
        route = respx_mock.get("/event").mock(
            return_value=httpx.Response(200, headers={"content-type": "text/event-stream"}, content=b"")
        )
        stream = client.event.list(directory="/repo", workspace="ws1")
        assert route_request(route).url.params.get("directory") == "/repo"
        assert route_request(route).url.params.get("workspace") == "ws1"
        stream.response.close()


class TestAsyncEvent:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncOpencode) -> None:
        event_stream = await async_client.event.list()
        await event_stream.response.aclose()

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncOpencode) -> None:
        response = await async_client.event.with_raw_response.list()

        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = await response.parse()
        await stream.close()

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncOpencode) -> None:
        async with async_client.event.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = await response.parse()
            await stream.close()

        assert cast(Any, response.is_closed) is True
