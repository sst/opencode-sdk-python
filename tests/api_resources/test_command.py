# Hand-maintained fork of the Stainless-era opencode SDK. Generated code was replaced by manual maintenance; see CONTRIBUTING.md.

from __future__ import annotations

import os

import httpx
import pytest
from respx import MockRouter

from opencode_ai import Opencode, AsyncOpencode
from tests.utils import assert_matches_type
from opencode_ai.types import CommandListResponse
from tests.wire_helpers import route_request

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")

COMMAND_SAMPLE: dict[str, object] = {
    "name": "explain",
    "description": "Explain the codebase",
    "agent": "build",
    "model": "anthropic/claude-sonnet-4",
    "source": "command",
    "template": "Explain {{input}}",
    "subtask": False,
    "hints": ["file", "symbol"],
}


class TestCommandWire:
    @pytest.mark.respx(base_url=base_url)
    def test_list_wire_shape(self, client: Opencode, respx_mock: MockRouter) -> None:
        route = respx_mock.get("/command").mock(return_value=httpx.Response(200, json=[COMMAND_SAMPLE]))
        result = client.command.list()
        assert route.called
        request = route_request(route)
        assert request.method == "GET"
        assert_matches_type(CommandListResponse, result, path=["response"])


class TestAsyncCommandWire:
    @pytest.mark.respx(base_url=base_url)
    async def test_list_wire_shape(self, async_client: AsyncOpencode, respx_mock: MockRouter) -> None:
        route = respx_mock.get("/command").mock(return_value=httpx.Response(200, json=[COMMAND_SAMPLE]))
        result = await async_client.command.list()
        assert route.called
        request = route_request(route)
        assert request.method == "GET"
        assert_matches_type(CommandListResponse, result, path=["response"])
