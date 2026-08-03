# Hand-maintained fork of the Stainless-era opencode SDK. Generated code was replaced by manual maintenance; see CONTRIBUTING.md.

from __future__ import annotations

import os

import httpx
import pytest
from respx import MockRouter

from opencode_ai import Opencode, AsyncOpencode
from tests.utils import assert_matches_type
from opencode_ai.types import (
    PermissionListResponse,
    PermissionReplyResponse,
)
from tests.wire_helpers import route_request, read_json_body

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")

PERMISSION_SAMPLE: dict[str, object] = {
    "id": "per_123",
    "sessionID": "ses_123",
    "permission": "bash",
    "patterns": ["git *"],
    "metadata": {"foo": "bar"},
    "always": ["git status"],
    "tool": {"messageID": "msg_123", "callID": "call_123"},
}


class TestPermissionWire:
    @pytest.mark.respx(base_url=base_url)
    def test_list_wire_shape(self, client: Opencode, respx_mock: MockRouter) -> None:
        route = respx_mock.get("/permission").mock(return_value=httpx.Response(200, json=[PERMISSION_SAMPLE]))
        result = client.permission.list()
        assert route.called
        request = route_request(route)
        assert request.method == "GET"
        assert_matches_type(PermissionListResponse, result, path=["response"])

    @pytest.mark.respx(base_url=base_url)
    def test_reply_sends_body(self, client: Opencode, respx_mock: MockRouter) -> None:
        route = respx_mock.post("/permission/per_123/reply").mock(return_value=httpx.Response(200, json=True))
        result = client.permission.reply(
            "per_123",
            reply="once",
            message="approved",
        )
        assert route.called
        request = route_request(route)
        assert request.method == "POST"
        body = read_json_body(route)
        assert body == {"reply": "once", "message": "approved"}
        assert_matches_type(PermissionReplyResponse, result, path=["response"])

    @pytest.mark.respx(base_url=base_url)
    def test_reply_without_optional_params(self, client: Opencode, respx_mock: MockRouter) -> None:
        route = respx_mock.post("/permission/per_123/reply").mock(return_value=httpx.Response(200, json=True))
        result = client.permission.reply(
            "per_123",
            reply="reject",
        )
        assert route.called
        body = read_json_body(route)
        assert body == {"reply": "reject"}
        assert_matches_type(PermissionReplyResponse, result, path=["response"])

    def test_path_params_reply(self, client: Opencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `request_id` but received ''"):
            client.permission.with_raw_response.reply(
                "",
                reply="once",
            )


class TestAsyncPermissionWire:
    @pytest.mark.respx(base_url=base_url)
    async def test_list_wire_shape(self, async_client: AsyncOpencode, respx_mock: MockRouter) -> None:
        route = respx_mock.get("/permission").mock(return_value=httpx.Response(200, json=[PERMISSION_SAMPLE]))
        result = await async_client.permission.list()
        assert route.called
        request = route_request(route)
        assert request.method == "GET"
        assert_matches_type(PermissionListResponse, result, path=["response"])

    @pytest.mark.respx(base_url=base_url)
    async def test_reply_sends_body(self, async_client: AsyncOpencode, respx_mock: MockRouter) -> None:
        route = respx_mock.post("/permission/per_123/reply").mock(return_value=httpx.Response(200, json=True))
        result = await async_client.permission.reply(
            "per_123",
            reply="once",
            message="approved",
        )
        assert route.called
        request = route_request(route)
        assert request.method == "POST"
        body = read_json_body(route)
        assert body == {"reply": "once", "message": "approved"}
        assert_matches_type(PermissionReplyResponse, result, path=["response"])

    @pytest.mark.respx(base_url=base_url)
    async def test_reply_without_optional_params(
        self, async_client: AsyncOpencode, respx_mock: MockRouter
    ) -> None:
        route = respx_mock.post("/permission/per_123/reply").mock(return_value=httpx.Response(200, json=True))
        result = await async_client.permission.reply(
            "per_123",
            reply="reject",
        )
        assert route.called
        body = read_json_body(route)
        assert body == {"reply": "reject"}
        assert_matches_type(PermissionReplyResponse, result, path=["response"])

    async def test_path_params_reply(self, async_client: AsyncOpencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `request_id` but received ''"):
            await async_client.permission.with_raw_response.reply(
                "",
                reply="once",
            )
