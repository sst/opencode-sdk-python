# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import httpx
import pytest

from opencode_ai import Opencode, AsyncOpencode
from tests.utils import assert_matches_type
from opencode_ai.types import (
    Session,
    SessionInitResponse,
    SessionListResponse,
    SessionAbortResponse,
    SessionDeleteResponse,
    SessionPromptResponse,
    SessionMessagesResponse,
    SessionSummarizeResponse,
)
from tests.wire_helpers import route_request, read_json_body

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")

PROMPT_SAMPLE = {
    "info": {
        "id": "msg_1",
        "agent": "build",
        "cost": 0,
        "mode": "build",
        "modelID": "claude-opus-4-8",
        "parentID": "ses_1",
        "path": {"cwd": "/", "root": "/"},
        "providerID": "anthropic",
        "role": "assistant",
        "sessionID": "ses_1",
        "time": {"created": 0},
        "tokens": {
            "cache": {"read": 0, "write": 0},
            "input": 0,
            "output": 0,
            "reasoning": 0,
        },
    },
    "parts": [],
}


class TestSession:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Opencode) -> None:
        session = client.session.create()
        assert_matches_type(Session, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Opencode) -> None:
        response = client.session.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(Session, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Opencode) -> None:
        with client.session.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(Session, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Opencode) -> None:
        session = client.session.list()
        assert_matches_type(SessionListResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Opencode) -> None:
        response = client.session.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(SessionListResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Opencode) -> None:
        with client.session.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(SessionListResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: Opencode) -> None:
        session = client.session.delete(
            "id",
        )
        assert_matches_type(SessionDeleteResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Opencode) -> None:
        response = client.session.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(SessionDeleteResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Opencode) -> None:
        with client.session.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(SessionDeleteResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Opencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.session.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_abort(self, client: Opencode) -> None:
        session = client.session.abort(
            "id",
        )
        assert_matches_type(SessionAbortResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_abort(self, client: Opencode) -> None:
        response = client.session.with_raw_response.abort(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(SessionAbortResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_abort(self, client: Opencode) -> None:
        with client.session.with_streaming_response.abort(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(SessionAbortResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_abort(self, client: Opencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.session.with_raw_response.abort(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_prompt(self, client: Opencode) -> None:
        session = client.session.prompt(
            id="id",
            parts=[
                {
                    "text": "text",
                    "type": "text",
                }
            ],
        )
        assert_matches_type(SessionPromptResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_prompt_with_all_params(self, client: Opencode) -> None:
        session = client.session.prompt(
            id="id",
            parts=[
                {
                    "text": "text",
                    "type": "text",
                    "id": "id",
                    "synthetic": True,
                    "time": {
                        "start": 0,
                        "end": 0,
                    },
                }
            ],
            model={
                "provider_id": "providerID",
                "model_id": "modelID",
            },
            agent="agent",
            message_id="msg",
            no_reply=True,
            tools={"foo": True},
            system="system",
            variant="variant",
        )
        assert_matches_type(SessionPromptResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_prompt(self, client: Opencode) -> None:
        response = client.session.with_raw_response.prompt(
            id="id",
            parts=[
                {
                    "text": "text",
                    "type": "text",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(SessionPromptResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_prompt(self, client: Opencode) -> None:
        with client.session.with_streaming_response.prompt(
            id="id",
            parts=[
                {
                    "text": "text",
                    "type": "text",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(SessionPromptResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_prompt(self, client: Opencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.session.with_raw_response.prompt(
                id="",
                parts=[
                    {
                        "text": "text",
                        "type": "text",
                    }
                ],
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_init(self, client: Opencode) -> None:
        session = client.session.init(
            id="id",
            message_id="messageID",
            model_id="modelID",
            provider_id="providerID",
        )
        assert_matches_type(SessionInitResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_init(self, client: Opencode) -> None:
        response = client.session.with_raw_response.init(
            id="id",
            message_id="messageID",
            model_id="modelID",
            provider_id="providerID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(SessionInitResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_init(self, client: Opencode) -> None:
        with client.session.with_streaming_response.init(
            id="id",
            message_id="messageID",
            model_id="modelID",
            provider_id="providerID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(SessionInitResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_init(self, client: Opencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.session.with_raw_response.init(
                id="",
                message_id="messageID",
                model_id="modelID",
                provider_id="providerID",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_messages(self, client: Opencode) -> None:
        session = client.session.messages(
            "id",
        )
        assert_matches_type(SessionMessagesResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_messages(self, client: Opencode) -> None:
        response = client.session.with_raw_response.messages(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(SessionMessagesResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_messages(self, client: Opencode) -> None:
        with client.session.with_streaming_response.messages(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(SessionMessagesResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_messages(self, client: Opencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.session.with_raw_response.messages(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_revert(self, client: Opencode) -> None:
        session = client.session.revert(
            id="id",
            message_id="msg",
        )
        assert_matches_type(Session, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_revert_with_all_params(self, client: Opencode) -> None:
        session = client.session.revert(
            id="id",
            message_id="msg",
            part_id="prt",
        )
        assert_matches_type(Session, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_revert(self, client: Opencode) -> None:
        response = client.session.with_raw_response.revert(
            id="id",
            message_id="msg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(Session, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_revert(self, client: Opencode) -> None:
        with client.session.with_streaming_response.revert(
            id="id",
            message_id="msg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(Session, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_revert(self, client: Opencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.session.with_raw_response.revert(
                id="",
                message_id="msg",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_share(self, client: Opencode) -> None:
        session = client.session.share(
            "id",
        )
        assert_matches_type(Session, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_share(self, client: Opencode) -> None:
        response = client.session.with_raw_response.share(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(Session, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_share(self, client: Opencode) -> None:
        with client.session.with_streaming_response.share(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(Session, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_share(self, client: Opencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.session.with_raw_response.share(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_summarize(self, client: Opencode) -> None:
        session = client.session.summarize(
            id="id",
            model_id="modelID",
            provider_id="providerID",
        )
        assert_matches_type(SessionSummarizeResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_summarize(self, client: Opencode) -> None:
        response = client.session.with_raw_response.summarize(
            id="id",
            model_id="modelID",
            provider_id="providerID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(SessionSummarizeResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_summarize(self, client: Opencode) -> None:
        with client.session.with_streaming_response.summarize(
            id="id",
            model_id="modelID",
            provider_id="providerID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(SessionSummarizeResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_summarize(self, client: Opencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.session.with_raw_response.summarize(
                id="",
                model_id="modelID",
                provider_id="providerID",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_unrevert(self, client: Opencode) -> None:
        session = client.session.unrevert(
            "id",
        )
        assert_matches_type(Session, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_unrevert(self, client: Opencode) -> None:
        response = client.session.with_raw_response.unrevert(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(Session, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_unrevert(self, client: Opencode) -> None:
        with client.session.with_streaming_response.unrevert(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(Session, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_unrevert(self, client: Opencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.session.with_raw_response.unrevert(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_unshare(self, client: Opencode) -> None:
        session = client.session.unshare(
            "id",
        )
        assert_matches_type(Session, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_unshare(self, client: Opencode) -> None:
        response = client.session.with_raw_response.unshare(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(Session, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_unshare(self, client: Opencode) -> None:
        with client.session.with_streaming_response.unshare(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(Session, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_unshare(self, client: Opencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.session.with_raw_response.unshare(
                "",
            )


class TestSessionPromptWire:
    @pytest.mark.respx(base_url=base_url)
    def test_prompt_sends_nested_model_and_agent(self, client, respx_mock) -> None:
        route = respx_mock.post("/session/ses_1/message").mock(return_value=httpx.Response(200, json=PROMPT_SAMPLE))
        result = client.session.prompt(
            "ses_1",
            parts=[{"type": "text", "text": "hi"}],
            model={"provider_id": "anthropic", "model_id": "claude-opus-4-8"},
            agent="build",
        )
        body = read_json_body(route)
        assert body["model"] == {"providerID": "anthropic", "modelID": "claude-opus-4-8"}
        assert body["agent"] == "build"
        assert "mode" not in body
        assert "modelID" not in body
        assert_matches_type(SessionPromptResponse, result, path=["response"])

    def test_chat_is_removed(self, client) -> None:
        assert not hasattr(client.session, "chat")


class TestSessionParamGaps:
    @pytest.mark.respx(base_url=base_url)
    def test_list_sends_new_filters(self, client, respx_mock) -> None:
        route = respx_mock.get("/session").mock(return_value=httpx.Response(200, json=[]))
        client.session.list(search="foo", limit=10)
        params = route_request(route).url.params
        assert params.get("search") == "foo"
        assert params.get("limit") == "10"

    @pytest.mark.respx(base_url=base_url)
    def test_summarize_sends_auto(self, client, respx_mock) -> None:
        route = respx_mock.post("/session/ses_1/summarize").mock(return_value=httpx.Response(200, json=True))
        client.session.summarize("ses_1", model_id="modelID", provider_id="providerID", auto=True)
        body = route_request(route)
        assert b"auto" in body.content

    @pytest.mark.respx(base_url=base_url)
    def test_messages_sends_pagination(self, client, respx_mock) -> None:
        route = respx_mock.get("/session/ses_1/message").mock(return_value=httpx.Response(200, json=[]))
        client.session.messages("ses_1", before="msg_1", limit=5)
        params = route_request(route).url.params
        assert params.get("before") == "msg_1"
        assert params.get("limit") == "5"


class TestAsyncSession:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncOpencode) -> None:
        session = await async_client.session.create()
        assert_matches_type(Session, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncOpencode) -> None:
        response = await async_client.session.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(Session, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncOpencode) -> None:
        async with async_client.session.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(Session, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncOpencode) -> None:
        session = await async_client.session.list()
        assert_matches_type(SessionListResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncOpencode) -> None:
        response = await async_client.session.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(SessionListResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncOpencode) -> None:
        async with async_client.session.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(SessionListResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncOpencode) -> None:
        session = await async_client.session.delete(
            "id",
        )
        assert_matches_type(SessionDeleteResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncOpencode) -> None:
        response = await async_client.session.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(SessionDeleteResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncOpencode) -> None:
        async with async_client.session.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(SessionDeleteResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncOpencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.session.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_abort(self, async_client: AsyncOpencode) -> None:
        session = await async_client.session.abort(
            "id",
        )
        assert_matches_type(SessionAbortResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_abort(self, async_client: AsyncOpencode) -> None:
        response = await async_client.session.with_raw_response.abort(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(SessionAbortResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_abort(self, async_client: AsyncOpencode) -> None:
        async with async_client.session.with_streaming_response.abort(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(SessionAbortResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_abort(self, async_client: AsyncOpencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.session.with_raw_response.abort(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_prompt(self, async_client: AsyncOpencode) -> None:
        session = await async_client.session.prompt(
            id="id",
            parts=[
                {
                    "text": "text",
                    "type": "text",
                }
            ],
        )
        assert_matches_type(SessionPromptResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_prompt_with_all_params(self, async_client: AsyncOpencode) -> None:
        session = await async_client.session.prompt(
            id="id",
            parts=[
                {
                    "text": "text",
                    "type": "text",
                    "id": "id",
                    "synthetic": True,
                    "time": {
                        "start": 0,
                        "end": 0,
                    },
                }
            ],
            model={
                "provider_id": "providerID",
                "model_id": "modelID",
            },
            agent="agent",
            message_id="msg",
            no_reply=True,
            tools={"foo": True},
            system="system",
            variant="variant",
        )
        assert_matches_type(SessionPromptResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_prompt(self, async_client: AsyncOpencode) -> None:
        response = await async_client.session.with_raw_response.prompt(
            id="id",
            parts=[
                {
                    "text": "text",
                    "type": "text",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(SessionPromptResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_prompt(self, async_client: AsyncOpencode) -> None:
        async with async_client.session.with_streaming_response.prompt(
            id="id",
            parts=[
                {
                    "text": "text",
                    "type": "text",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(SessionPromptResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_prompt(self, async_client: AsyncOpencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.session.with_raw_response.prompt(
                id="",
                parts=[
                    {
                        "text": "text",
                        "type": "text",
                    }
                ],
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_init(self, async_client: AsyncOpencode) -> None:
        session = await async_client.session.init(
            id="id",
            message_id="messageID",
            model_id="modelID",
            provider_id="providerID",
        )
        assert_matches_type(SessionInitResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_init(self, async_client: AsyncOpencode) -> None:
        response = await async_client.session.with_raw_response.init(
            id="id",
            message_id="messageID",
            model_id="modelID",
            provider_id="providerID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(SessionInitResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_init(self, async_client: AsyncOpencode) -> None:
        async with async_client.session.with_streaming_response.init(
            id="id",
            message_id="messageID",
            model_id="modelID",
            provider_id="providerID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(SessionInitResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_init(self, async_client: AsyncOpencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.session.with_raw_response.init(
                id="",
                message_id="messageID",
                model_id="modelID",
                provider_id="providerID",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_messages(self, async_client: AsyncOpencode) -> None:
        session = await async_client.session.messages(
            "id",
        )
        assert_matches_type(SessionMessagesResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_messages(self, async_client: AsyncOpencode) -> None:
        response = await async_client.session.with_raw_response.messages(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(SessionMessagesResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_messages(self, async_client: AsyncOpencode) -> None:
        async with async_client.session.with_streaming_response.messages(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(SessionMessagesResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_messages(self, async_client: AsyncOpencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.session.with_raw_response.messages(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_revert(self, async_client: AsyncOpencode) -> None:
        session = await async_client.session.revert(
            id="id",
            message_id="msg",
        )
        assert_matches_type(Session, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_revert_with_all_params(self, async_client: AsyncOpencode) -> None:
        session = await async_client.session.revert(
            id="id",
            message_id="msg",
            part_id="prt",
        )
        assert_matches_type(Session, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_revert(self, async_client: AsyncOpencode) -> None:
        response = await async_client.session.with_raw_response.revert(
            id="id",
            message_id="msg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(Session, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_revert(self, async_client: AsyncOpencode) -> None:
        async with async_client.session.with_streaming_response.revert(
            id="id",
            message_id="msg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(Session, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_revert(self, async_client: AsyncOpencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.session.with_raw_response.revert(
                id="",
                message_id="msg",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_share(self, async_client: AsyncOpencode) -> None:
        session = await async_client.session.share(
            "id",
        )
        assert_matches_type(Session, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_share(self, async_client: AsyncOpencode) -> None:
        response = await async_client.session.with_raw_response.share(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(Session, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_share(self, async_client: AsyncOpencode) -> None:
        async with async_client.session.with_streaming_response.share(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(Session, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_share(self, async_client: AsyncOpencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.session.with_raw_response.share(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_summarize(self, async_client: AsyncOpencode) -> None:
        session = await async_client.session.summarize(
            id="id",
            model_id="modelID",
            provider_id="providerID",
        )
        assert_matches_type(SessionSummarizeResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_summarize(self, async_client: AsyncOpencode) -> None:
        response = await async_client.session.with_raw_response.summarize(
            id="id",
            model_id="modelID",
            provider_id="providerID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(SessionSummarizeResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_summarize(self, async_client: AsyncOpencode) -> None:
        async with async_client.session.with_streaming_response.summarize(
            id="id",
            model_id="modelID",
            provider_id="providerID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(SessionSummarizeResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_summarize(self, async_client: AsyncOpencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.session.with_raw_response.summarize(
                id="",
                model_id="modelID",
                provider_id="providerID",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_unrevert(self, async_client: AsyncOpencode) -> None:
        session = await async_client.session.unrevert(
            "id",
        )
        assert_matches_type(Session, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_unrevert(self, async_client: AsyncOpencode) -> None:
        response = await async_client.session.with_raw_response.unrevert(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(Session, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_unrevert(self, async_client: AsyncOpencode) -> None:
        async with async_client.session.with_streaming_response.unrevert(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(Session, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_unrevert(self, async_client: AsyncOpencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.session.with_raw_response.unrevert(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_unshare(self, async_client: AsyncOpencode) -> None:
        session = await async_client.session.unshare(
            "id",
        )
        assert_matches_type(Session, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_unshare(self, async_client: AsyncOpencode) -> None:
        response = await async_client.session.with_raw_response.unshare(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(Session, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_unshare(self, async_client: AsyncOpencode) -> None:
        async with async_client.session.with_streaming_response.unshare(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(Session, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_unshare(self, async_client: AsyncOpencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.session.with_raw_response.unshare(
                "",
            )
