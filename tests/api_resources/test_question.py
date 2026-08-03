# Hand-maintained fork of the Stainless-era opencode SDK. Generated code was replaced by manual maintenance; see CONTRIBUTING.md.

from __future__ import annotations

import os

import httpx
import pytest
from respx import MockRouter

from opencode_ai import Opencode, AsyncOpencode
from tests.utils import assert_matches_type
from opencode_ai.types import (
    QuestionListResponse,
    QuestionReplyResponse,
    QuestionRejectResponse,
)
from tests.wire_helpers import route_request, read_json_body

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")

QUESTION_SAMPLE: dict[str, object] = {
    "id": "que_123",
    "sessionID": "ses_123",
    "questions": [
        {
            "question": "Which approach should I take?",
            "header": "Approach",
            "options": [
                {"label": "Option A", "description": "Do it the first way"},
                {"label": "Option B", "description": "Do it the second way"},
            ],
            "multiple": False,
            "custom": True,
        }
    ],
    "tool": {"messageID": "msg_123", "callID": "call_123"},
}


class TestQuestionWire:
    @pytest.mark.respx(base_url=base_url)
    def test_list_wire_shape(self, client: Opencode, respx_mock: MockRouter) -> None:
        route = respx_mock.get("/question").mock(return_value=httpx.Response(200, json=[QUESTION_SAMPLE]))
        result = client.question.list()
        assert route.called
        request = route_request(route)
        assert request.method == "GET"
        assert_matches_type(QuestionListResponse, result, path=["response"])

    @pytest.mark.respx(base_url=base_url)
    def test_reject_wire_shape(self, client: Opencode, respx_mock: MockRouter) -> None:
        route = respx_mock.post("/question/que_123/reject").mock(return_value=httpx.Response(200, json=True))
        result = client.question.reject("que_123")
        assert route.called
        request = route_request(route)
        assert request.method == "POST"
        assert_matches_type(QuestionRejectResponse, result, path=["response"])

    @pytest.mark.respx(base_url=base_url)
    def test_reply_sends_body(self, client: Opencode, respx_mock: MockRouter) -> None:
        route = respx_mock.post("/question/que_123/reply").mock(return_value=httpx.Response(200, json=True))
        result = client.question.reply(
            "que_123",
            answers=[["Option A"]],
        )
        assert route.called
        request = route_request(route)
        assert request.method == "POST"
        body = read_json_body(route)
        assert body == {"answers": [["Option A"]]}
        assert_matches_type(QuestionReplyResponse, result, path=["response"])

    def test_path_params_reject(self, client: Opencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `request_id` but received ''"):
            client.question.with_raw_response.reject("")

    def test_path_params_reply(self, client: Opencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `request_id` but received ''"):
            client.question.with_raw_response.reply(
                "",
                answers=[["Option A"]],
            )


class TestAsyncQuestionWire:
    @pytest.mark.respx(base_url=base_url)
    async def test_list_wire_shape(self, async_client: AsyncOpencode, respx_mock: MockRouter) -> None:
        route = respx_mock.get("/question").mock(return_value=httpx.Response(200, json=[QUESTION_SAMPLE]))
        result = await async_client.question.list()
        assert route.called
        request = route_request(route)
        assert request.method == "GET"
        assert_matches_type(QuestionListResponse, result, path=["response"])

    @pytest.mark.respx(base_url=base_url)
    async def test_reject_wire_shape(self, async_client: AsyncOpencode, respx_mock: MockRouter) -> None:
        route = respx_mock.post("/question/que_123/reject").mock(return_value=httpx.Response(200, json=True))
        result = await async_client.question.reject("que_123")
        assert route.called
        request = route_request(route)
        assert request.method == "POST"
        assert_matches_type(QuestionRejectResponse, result, path=["response"])

    @pytest.mark.respx(base_url=base_url)
    async def test_reply_sends_body(self, async_client: AsyncOpencode, respx_mock: MockRouter) -> None:
        route = respx_mock.post("/question/que_123/reply").mock(return_value=httpx.Response(200, json=True))
        result = await async_client.question.reply(
            "que_123",
            answers=[["Option A"]],
        )
        assert route.called
        request = route_request(route)
        assert request.method == "POST"
        body = read_json_body(route)
        assert body == {"answers": [["Option A"]]}
        assert_matches_type(QuestionReplyResponse, result, path=["response"])

    async def test_path_params_reject(self, async_client: AsyncOpencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `request_id` but received ''"):
            await async_client.question.with_raw_response.reject("")

    async def test_path_params_reply(self, async_client: AsyncOpencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `request_id` but received ''"):
            await async_client.question.with_raw_response.reply(
                "",
                answers=[["Option A"]],
            )
