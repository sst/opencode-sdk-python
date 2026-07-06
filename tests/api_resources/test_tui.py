# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import httpx
import pytest
from respx import MockRouter

from opencode_ai import Opencode, AsyncOpencode
from tests.utils import assert_matches_type
from opencode_ai.types import (
    TuiPublishResponse,
    TuiOpenHelpResponse,
    TuiShowToastResponse,
    TuiOpenModelsResponse,
    TuiOpenThemesResponse,
    TuiClearPromptResponse,
    TuiControlNextResponse,
    TuiAppendPromptResponse,
    TuiOpenSessionsResponse,
    TuiSubmitPromptResponse,
    TuiSelectSessionResponse,
    TuiExecuteCommandResponse,
    TuiControlResponseResponse,
)
from tests.wire_helpers import route_request, read_json_body
from opencode_ai._models import construct_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTui:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_append_prompt(self, client: Opencode) -> None:
        tui = client.tui.append_prompt(
            text="text",
        )
        assert_matches_type(TuiAppendPromptResponse, tui, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_append_prompt(self, client: Opencode) -> None:
        response = client.tui.with_raw_response.append_prompt(
            text="text",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tui = response.parse()
        assert_matches_type(TuiAppendPromptResponse, tui, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_append_prompt(self, client: Opencode) -> None:
        with client.tui.with_streaming_response.append_prompt(
            text="text",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tui = response.parse()
            assert_matches_type(TuiAppendPromptResponse, tui, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_open_help(self, client: Opencode) -> None:
        tui = client.tui.open_help()
        assert_matches_type(TuiOpenHelpResponse, tui, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_open_help(self, client: Opencode) -> None:
        response = client.tui.with_raw_response.open_help()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tui = response.parse()
        assert_matches_type(TuiOpenHelpResponse, tui, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_open_help(self, client: Opencode) -> None:
        with client.tui.with_streaming_response.open_help() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tui = response.parse()
            assert_matches_type(TuiOpenHelpResponse, tui, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestTuiWire:
    @pytest.mark.respx(base_url=base_url)
    def test_open_sessions_wire_shape(self, client: Opencode, respx_mock: MockRouter) -> None:
        route = respx_mock.post("/tui/open-sessions").mock(return_value=httpx.Response(200, json=True))
        result = client.tui.open_sessions()
        assert route.called
        assert route.calls.last.request.method == "POST"
        assert_matches_type(TuiOpenSessionsResponse, result, path=["response"])

    @pytest.mark.respx(base_url=base_url)
    def test_open_themes_wire_shape(self, client: Opencode, respx_mock: MockRouter) -> None:
        route = respx_mock.post("/tui/open-themes").mock(return_value=httpx.Response(200, json=True))
        result = client.tui.open_themes()
        assert route.called
        assert_matches_type(TuiOpenThemesResponse, result, path=["response"])

    @pytest.mark.respx(base_url=base_url)
    def test_open_models_wire_shape(self, client: Opencode, respx_mock: MockRouter) -> None:
        route = respx_mock.post("/tui/open-models").mock(return_value=httpx.Response(200, json=True))
        result = client.tui.open_models()
        assert route.called
        assert_matches_type(TuiOpenModelsResponse, result, path=["response"])

    @pytest.mark.respx(base_url=base_url)
    def test_submit_prompt_wire_shape(self, client: Opencode, respx_mock: MockRouter) -> None:
        route = respx_mock.post("/tui/submit-prompt").mock(return_value=httpx.Response(200, json=True))
        result = client.tui.submit_prompt()
        assert route.called
        assert_matches_type(TuiSubmitPromptResponse, result, path=["response"])

    @pytest.mark.respx(base_url=base_url)
    def test_clear_prompt_wire_shape(self, client: Opencode, respx_mock: MockRouter) -> None:
        route = respx_mock.post("/tui/clear-prompt").mock(return_value=httpx.Response(200, json=True))
        result = client.tui.clear_prompt()
        assert route.called
        assert_matches_type(TuiClearPromptResponse, result, path=["response"])

    @pytest.mark.respx(base_url=base_url)
    def test_execute_command_sends_command(self, client: Opencode, respx_mock: MockRouter) -> None:
        route = respx_mock.post("/tui/execute-command").mock(return_value=httpx.Response(200, json=True))
        result = client.tui.execute_command(command="session.new")
        assert route.called
        body = read_json_body(route)
        assert body == {"command": "session.new"}
        assert_matches_type(TuiExecuteCommandResponse, result, path=["response"])

    @pytest.mark.respx(base_url=base_url)
    def test_show_toast_sends_all_fields(self, client: Opencode, respx_mock: MockRouter) -> None:
        route = respx_mock.post("/tui/show-toast").mock(return_value=httpx.Response(200, json=True))
        result = client.tui.show_toast(
            message="hello",
            variant="info",
            title="Notice",
            duration=1500,
        )
        assert route.called
        body = read_json_body(route)
        assert body == {
            "message": "hello",
            "variant": "info",
            "title": "Notice",
            "duration": 1500,
        }
        assert_matches_type(TuiShowToastResponse, result, path=["response"])

    @pytest.mark.respx(base_url=base_url)
    def test_publish_sends_camelcase_session_id(self, client: Opencode, respx_mock: MockRouter) -> None:
        route = respx_mock.post("/tui/publish").mock(return_value=httpx.Response(200, json=True))
        result = client.tui.publish(
            {
                "type": "tui.session.select",
                "properties": {"session_id": "ses_abc"},
            }
        )
        assert route.called
        body = read_json_body(route)
        # The Python-side `session_id` param must serialize to the wire's
        # camelCase `sessionID` key per the `EventTuiSessionSelect` schema.
        assert body == {
            "type": "tui.session.select",
            "properties": {"sessionID": "ses_abc"},
        }
        assert_matches_type(TuiPublishResponse, result, path=["response"])

    @pytest.mark.respx(base_url=base_url)
    def test_select_session_sends_camelcase_session_id(self, client: Opencode, respx_mock: MockRouter) -> None:
        route = respx_mock.post("/tui/select-session").mock(return_value=httpx.Response(200, json=True))
        result = client.tui.select_session(session_id="ses_abc")
        assert route.called
        body = read_json_body(route)
        assert body == {"sessionID": "ses_abc"}
        assert_matches_type(TuiSelectSessionResponse, result, path=["response"])

    @pytest.mark.respx(base_url=base_url)
    def test_control_next_wire_shape(self, client: Opencode, respx_mock: MockRouter) -> None:
        route = respx_mock.get("/tui/control/next").mock(
            return_value=httpx.Response(200, json={"path": "/tui/show-toast", "body": {"message": "hi"}})
        )
        result = client.tui.control_next()
        assert route.called
        assert route_request(route).method == "GET"
        assert_matches_type(TuiControlNextResponse, result, path=["response"])
        assert result.path == "/tui/show-toast"
        assert result.body == {"message": "hi"}

    @pytest.mark.respx(base_url=base_url)
    def test_control_response_passes_arbitrary_body_through(self, client: Opencode, respx_mock: MockRouter) -> None:
        route = respx_mock.post("/tui/control/response").mock(return_value=httpx.Response(200, json=True))
        result = client.tui.control_response({"ok": True, "nested": {"count": 1}})
        assert route.called
        body = read_json_body(route)
        assert body == {"ok": True, "nested": {"count": 1}}
        assert_matches_type(TuiControlResponseResponse, result, path=["response"])

    def test_control_next_response_accepts_arbitrary_body_shapes(self) -> None:
        for sample_body in ({"a": 1}, [1, 2, 3], "a string", None):
            result = cast(
                TuiControlNextResponse,
                construct_type(type_=TuiControlNextResponse, value={"path": "/x", "body": sample_body}),
            )
            assert result.path == "/x"
            assert result.body == sample_body


class TestAsyncTui:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_append_prompt(self, async_client: AsyncOpencode) -> None:
        tui = await async_client.tui.append_prompt(
            text="text",
        )
        assert_matches_type(TuiAppendPromptResponse, tui, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_append_prompt(self, async_client: AsyncOpencode) -> None:
        response = await async_client.tui.with_raw_response.append_prompt(
            text="text",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tui = await response.parse()
        assert_matches_type(TuiAppendPromptResponse, tui, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_append_prompt(self, async_client: AsyncOpencode) -> None:
        async with async_client.tui.with_streaming_response.append_prompt(
            text="text",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tui = await response.parse()
            assert_matches_type(TuiAppendPromptResponse, tui, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_open_help(self, async_client: AsyncOpencode) -> None:
        tui = await async_client.tui.open_help()
        assert_matches_type(TuiOpenHelpResponse, tui, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_open_help(self, async_client: AsyncOpencode) -> None:
        response = await async_client.tui.with_raw_response.open_help()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tui = await response.parse()
        assert_matches_type(TuiOpenHelpResponse, tui, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_open_help(self, async_client: AsyncOpencode) -> None:
        async with async_client.tui.with_streaming_response.open_help() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tui = await response.parse()
            assert_matches_type(TuiOpenHelpResponse, tui, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncTuiWire:
    @pytest.mark.respx(base_url=base_url)
    async def test_open_sessions_wire_shape(self, async_client: AsyncOpencode, respx_mock: MockRouter) -> None:
        route = respx_mock.post("/tui/open-sessions").mock(return_value=httpx.Response(200, json=True))
        result = await async_client.tui.open_sessions()
        assert route.called
        assert_matches_type(TuiOpenSessionsResponse, result, path=["response"])

    @pytest.mark.respx(base_url=base_url)
    async def test_open_themes_wire_shape(self, async_client: AsyncOpencode, respx_mock: MockRouter) -> None:
        route = respx_mock.post("/tui/open-themes").mock(return_value=httpx.Response(200, json=True))
        result = await async_client.tui.open_themes()
        assert route.called
        assert_matches_type(TuiOpenThemesResponse, result, path=["response"])

    @pytest.mark.respx(base_url=base_url)
    async def test_open_models_wire_shape(self, async_client: AsyncOpencode, respx_mock: MockRouter) -> None:
        route = respx_mock.post("/tui/open-models").mock(return_value=httpx.Response(200, json=True))
        result = await async_client.tui.open_models()
        assert route.called
        assert_matches_type(TuiOpenModelsResponse, result, path=["response"])

    @pytest.mark.respx(base_url=base_url)
    async def test_submit_prompt_wire_shape(self, async_client: AsyncOpencode, respx_mock: MockRouter) -> None:
        route = respx_mock.post("/tui/submit-prompt").mock(return_value=httpx.Response(200, json=True))
        result = await async_client.tui.submit_prompt()
        assert route.called
        assert_matches_type(TuiSubmitPromptResponse, result, path=["response"])

    @pytest.mark.respx(base_url=base_url)
    async def test_clear_prompt_wire_shape(self, async_client: AsyncOpencode, respx_mock: MockRouter) -> None:
        route = respx_mock.post("/tui/clear-prompt").mock(return_value=httpx.Response(200, json=True))
        result = await async_client.tui.clear_prompt()
        assert route.called
        assert_matches_type(TuiClearPromptResponse, result, path=["response"])

    @pytest.mark.respx(base_url=base_url)
    async def test_execute_command_sends_command(self, async_client: AsyncOpencode, respx_mock: MockRouter) -> None:
        route = respx_mock.post("/tui/execute-command").mock(return_value=httpx.Response(200, json=True))
        result = await async_client.tui.execute_command(command="session.new")
        assert route.called
        body = read_json_body(route)
        assert body == {"command": "session.new"}
        assert_matches_type(TuiExecuteCommandResponse, result, path=["response"])

    @pytest.mark.respx(base_url=base_url)
    async def test_show_toast_sends_all_fields(self, async_client: AsyncOpencode, respx_mock: MockRouter) -> None:
        route = respx_mock.post("/tui/show-toast").mock(return_value=httpx.Response(200, json=True))
        result = await async_client.tui.show_toast(
            message="hello",
            variant="info",
            title="Notice",
            duration=1500,
        )
        assert route.called
        body = read_json_body(route)
        assert body == {
            "message": "hello",
            "variant": "info",
            "title": "Notice",
            "duration": 1500,
        }
        assert_matches_type(TuiShowToastResponse, result, path=["response"])

    @pytest.mark.respx(base_url=base_url)
    async def test_publish_sends_camelcase_session_id(
        self, async_client: AsyncOpencode, respx_mock: MockRouter
    ) -> None:
        route = respx_mock.post("/tui/publish").mock(return_value=httpx.Response(200, json=True))
        result = await async_client.tui.publish(
            {
                "type": "tui.session.select",
                "properties": {"session_id": "ses_abc"},
            }
        )
        assert route.called
        body = read_json_body(route)
        assert body == {
            "type": "tui.session.select",
            "properties": {"sessionID": "ses_abc"},
        }
        assert_matches_type(TuiPublishResponse, result, path=["response"])

    @pytest.mark.respx(base_url=base_url)
    async def test_select_session_sends_camelcase_session_id(
        self, async_client: AsyncOpencode, respx_mock: MockRouter
    ) -> None:
        route = respx_mock.post("/tui/select-session").mock(return_value=httpx.Response(200, json=True))
        result = await async_client.tui.select_session(session_id="ses_abc")
        assert route.called
        body = read_json_body(route)
        assert body == {"sessionID": "ses_abc"}
        assert_matches_type(TuiSelectSessionResponse, result, path=["response"])

    @pytest.mark.respx(base_url=base_url)
    async def test_control_next_wire_shape(self, async_client: AsyncOpencode, respx_mock: MockRouter) -> None:
        route = respx_mock.get("/tui/control/next").mock(
            return_value=httpx.Response(200, json={"path": "/tui/show-toast", "body": {"message": "hi"}})
        )
        result = await async_client.tui.control_next()
        assert route.called
        assert route_request(route).method == "GET"
        assert_matches_type(TuiControlNextResponse, result, path=["response"])
        assert result.path == "/tui/show-toast"
        assert result.body == {"message": "hi"}

    @pytest.mark.respx(base_url=base_url)
    async def test_control_response_passes_arbitrary_body_through(
        self, async_client: AsyncOpencode, respx_mock: MockRouter
    ) -> None:
        route = respx_mock.post("/tui/control/response").mock(return_value=httpx.Response(200, json=True))
        result = await async_client.tui.control_response({"ok": True, "nested": {"count": 1}})
        assert route.called
        body = read_json_body(route)
        assert body == {"ok": True, "nested": {"count": 1}}
        assert_matches_type(TuiControlResponseResponse, result, path=["response"])
