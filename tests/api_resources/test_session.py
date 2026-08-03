# Hand-maintained fork of the Stainless-era opencode SDK. Generated code was replaced by manual maintenance; see CONTRIBUTING.md.

from __future__ import annotations

import os
from typing import Any, cast

import httpx
import pytest
from respx import MockRouter

from opencode_ai import Opencode, AsyncOpencode
from tests.utils import assert_matches_type
from opencode_ai.types import (
    Part,
    Session,
    SessionDiffResponse,
    SessionInitResponse,
    SessionListResponse,
    SessionTodoResponse,
    SessionAbortResponse,
    SessionShellResponse,
    SessionDeleteResponse,
    SessionPromptResponse,
    SessionStatusResponse,
    SessionCommandResponse,
    SessionChildrenResponse,
    SessionMessagesResponse,
    SessionSummarizeResponse,
    SessionDeletePartResponse,
    SessionMessagesResponseItem,
    SessionDeleteMessageResponse,
    SessionRespondPermissionResponse,
    session_update_part_params,
)
from tests.wire_helpers import route_request, read_json_body
from opencode_ai._models import construct_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")

MINIMAL_SESSION: dict[str, object] = {
    "id": "ses_1",
    "directory": "/tmp",
    "projectID": "prj_1",
    "slug": "my-session",
    "time": {"created": 0, "updated": 0},
    "title": "Test session",
    "version": "1.0.0",
}

PROMPT_SAMPLE: dict[str, object] = {
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
    def test_prompt_sends_nested_model_and_agent(self, client: Opencode, respx_mock: MockRouter) -> None:
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

    def test_chat_is_removed(self, client: Opencode) -> None:
        assert not hasattr(client.session, "chat")


class TestSessionParamGaps:
    @pytest.mark.respx(base_url=base_url)
    def test_list_sends_new_filters(self, client: Opencode, respx_mock: MockRouter) -> None:
        route = respx_mock.get("/session").mock(return_value=httpx.Response(200, json=[]))
        client.session.list(search="foo", limit=10)
        params = route_request(route).url.params
        assert params.get("search") == "foo"
        assert params.get("limit") == "10"

    @pytest.mark.respx(base_url=base_url)
    def test_summarize_sends_auto(self, client: Opencode, respx_mock: MockRouter) -> None:
        route = respx_mock.post("/session/ses_1/summarize").mock(return_value=httpx.Response(200, json=True))
        client.session.summarize("ses_1", model_id="modelID", provider_id="providerID", auto=True)
        body = route_request(route)
        assert b"auto" in body.content

    @pytest.mark.respx(base_url=base_url)
    def test_messages_sends_pagination(self, client: Opencode, respx_mock: MockRouter) -> None:
        route = respx_mock.get("/session/ses_1/message").mock(return_value=httpx.Response(200, json=[]))
        client.session.messages("ses_1", before="msg_1", limit=5)
        params = route_request(route).url.params
        assert params.get("before") == "msg_1"
        assert params.get("limit") == "5"

    @pytest.mark.respx(base_url=base_url)
    def test_get_sends_directory_and_workspace(self, client: Opencode, respx_mock: MockRouter) -> None:
        route = respx_mock.get("/session/ses_1").mock(return_value=httpx.Response(200, json=MINIMAL_SESSION))
        client.session.get("ses_1", directory="d", workspace="w")
        params = route_request(route).url.params
        assert params.get("directory") == "d"
        assert params.get("workspace") == "w"


class TestSessionNewOperationsWire:
    @pytest.mark.respx(base_url=base_url)
    def test_status(self, client: Opencode, respx_mock: MockRouter) -> None:
        payload = {"ses_1": {"type": "idle"}, "ses_2": {"type": "busy"}}
        route = respx_mock.get("/session/status").mock(return_value=httpx.Response(200, json=payload))
        result = client.session.status()
        assert route_request(route).method == "GET"
        assert_matches_type(SessionStatusResponse, result, path=["response"])
        result = cast(SessionStatusResponse, construct_type(type_=SessionStatusResponse, value=payload))
        assert result["ses_1"].type == "idle"

    @pytest.mark.respx(base_url=base_url)
    def test_get(self, client: Opencode, respx_mock: MockRouter) -> None:
        route = respx_mock.get("/session/ses_1").mock(return_value=httpx.Response(200, json=MINIMAL_SESSION))
        result = client.session.get("ses_1")
        assert route_request(route).method == "GET"
        assert_matches_type(Session, result, path=["response"])

    @pytest.mark.respx(base_url=base_url)
    def test_update_sends_body(self, client: Opencode, respx_mock: MockRouter) -> None:
        route = respx_mock.patch("/session/ses_1").mock(return_value=httpx.Response(200, json=MINIMAL_SESSION))
        result = client.session.update(
            "ses_1",
            title="new title",
            metadata={"foo": "bar"},
            permission=[{"action": "allow", "pattern": "*", "permission": "bash"}],
            time={"archived": 123},
        )
        body = read_json_body(route)
        assert body["title"] == "new title"
        assert body["permission"] == [{"action": "allow", "pattern": "*", "permission": "bash"}]
        assert body["time"] == {"archived": 123}
        assert_matches_type(Session, result, path=["response"])

    @pytest.mark.respx(base_url=base_url)
    def test_children(self, client: Opencode, respx_mock: MockRouter) -> None:
        route = respx_mock.get("/session/ses_1/children").mock(return_value=httpx.Response(200, json=[MINIMAL_SESSION]))
        result = client.session.children("ses_1")
        assert route_request(route).method == "GET"
        assert_matches_type(SessionChildrenResponse, result, path=["response"])

    @pytest.mark.respx(base_url=base_url)
    def test_command_sends_body(self, client: Opencode, respx_mock: MockRouter) -> None:
        payload: dict[str, object] = {"info": PROMPT_SAMPLE["info"], "parts": []}
        route = respx_mock.post("/session/ses_1/command").mock(return_value=httpx.Response(200, json=payload))
        result = client.session.command(
            "ses_1",
            arguments="some args",
            command="mycommand",
            agent="build",
            message_id="msg_1",
            model="claude-opus-4-8",
        )
        body = read_json_body(route)
        assert body["arguments"] == "some args"
        assert body["command"] == "mycommand"
        assert body["messageID"] == "msg_1"
        assert_matches_type(SessionCommandResponse, result, path=["response"])

    @pytest.mark.respx(base_url=base_url)
    def test_diff_sends_message_id_query(self, client: Opencode, respx_mock: MockRouter) -> None:
        payload = [{"additions": 1, "deletions": 0, "file": "a.py", "status": "modified"}]
        route = respx_mock.get("/session/ses_1/diff").mock(return_value=httpx.Response(200, json=payload))
        result = client.session.diff("ses_1", message_id="msg_1")
        params = route_request(route).url.params
        assert params.get("messageID") == "msg_1"
        assert_matches_type(SessionDiffResponse, result, path=["response"])

    @pytest.mark.respx(base_url=base_url)
    def test_fork_sends_message_id_body(self, client: Opencode, respx_mock: MockRouter) -> None:
        route = respx_mock.post("/session/ses_1/fork").mock(return_value=httpx.Response(200, json=MINIMAL_SESSION))
        result = client.session.fork("ses_1", message_id="msg_1")
        body = read_json_body(route)
        assert body["messageID"] == "msg_1"
        assert_matches_type(Session, result, path=["response"])

    @pytest.mark.respx(base_url=base_url)
    def test_delete_message(self, client: Opencode, respx_mock: MockRouter) -> None:
        route = respx_mock.delete("/session/ses_1/message/msg_1").mock(return_value=httpx.Response(200, json=True))
        result = client.session.delete_message("ses_1", message_id="msg_1")
        assert route_request(route).method == "DELETE"
        assert_matches_type(SessionDeleteMessageResponse, result, path=["response"])

    @pytest.mark.respx(base_url=base_url)
    def test_get_message(self, client: Opencode, respx_mock: MockRouter) -> None:
        payload: dict[str, object] = {"info": PROMPT_SAMPLE["info"], "parts": []}
        route = respx_mock.get("/session/ses_1/message/msg_1").mock(return_value=httpx.Response(200, json=payload))
        result = client.session.get_message("ses_1", message_id="msg_1")
        assert route_request(route).method == "GET"
        assert_matches_type(SessionMessagesResponseItem, result, path=["response"])

    @pytest.mark.respx(base_url=base_url)
    def test_delete_part(self, client: Opencode, respx_mock: MockRouter) -> None:
        route = respx_mock.delete("/session/ses_1/message/msg_1/part/prt_1").mock(
            return_value=httpx.Response(200, json=True)
        )
        result = client.session.delete_part("ses_1", message_id="msg_1", part_id="prt_1")
        assert route_request(route).method == "DELETE"
        assert_matches_type(SessionDeletePartResponse, result, path=["response"])

    @pytest.mark.respx(base_url=base_url)
    def test_update_part_sends_full_part_body(self, client: Opencode, respx_mock: MockRouter) -> None:
        wire_payload: dict[str, object] = {
            "id": "prt_1",
            "messageID": "msg_1",
            "sessionID": "ses_1",
            "type": "text",
            "text": "hello",
        }
        part_payload: session_update_part_params.TextPartParam = {
            "id": "prt_1",
            "message_id": "msg_1",
            "session_id": "ses_1",
            "type": "text",
            "text": "hello",
        }
        route = respx_mock.patch("/session/ses_1/message/msg_1/part/prt_1").mock(
            return_value=httpx.Response(200, json=wire_payload)
        )
        result = client.session.update_part(
            "ses_1",
            message_id="msg_1",
            part_id="prt_1",
            part=part_payload,
        )
        body = read_json_body(route)
        assert body["type"] == "text"
        assert body["text"] == "hello"
        part = cast(Part, construct_type(type_=Part, value=result))
        assert part.type == "text"

    @pytest.mark.respx(base_url=base_url)
    def test_respond_permission_sends_body(self, client: Opencode, respx_mock: MockRouter) -> None:
        route = respx_mock.post("/session/ses_1/permissions/per_1").mock(return_value=httpx.Response(200, json=True))
        result = client.session.respond_permission("ses_1", permission_id="per_1", response="once")
        body = read_json_body(route)
        assert body["response"] == "once"
        assert_matches_type(SessionRespondPermissionResponse, result, path=["response"])

    @pytest.mark.respx(base_url=base_url)
    def test_prompt_async_returns_none_on_204(self, client: Opencode, respx_mock: MockRouter) -> None:
        route = respx_mock.post("/session/ses_1/prompt_async").mock(return_value=httpx.Response(204))
        result = client.session.prompt_async(
            "ses_1",
            parts=[{"type": "text", "text": "hi"}],
            no_reply=True,
        )
        body = read_json_body(route)
        assert body["noReply"] is True
        assert result is None

    @pytest.mark.respx(base_url=base_url)
    def test_shell_sends_body(self, client: Opencode, respx_mock: MockRouter) -> None:
        payload: dict[str, object] = {"info": PROMPT_SAMPLE["info"], "parts": []}
        route = respx_mock.post("/session/ses_1/shell").mock(return_value=httpx.Response(200, json=payload))
        result = client.session.shell(
            "ses_1",
            agent="build",
            command="ls -la",
            model={"provider_id": "anthropic", "model_id": "claude-opus-4-8"},
        )
        body = read_json_body(route)
        assert body["agent"] == "build"
        assert body["command"] == "ls -la"
        assert body["model"] == {"providerID": "anthropic", "modelID": "claude-opus-4-8"}
        assert_matches_type(SessionShellResponse, result, path=["response"])

    @pytest.mark.respx(base_url=base_url)
    def test_todo(self, client: Opencode, respx_mock: MockRouter) -> None:
        payload = [{"content": "do the thing", "status": "pending", "priority": "high"}]
        route = respx_mock.get("/session/ses_1/todo").mock(return_value=httpx.Response(200, json=payload))
        result = client.session.todo("ses_1")
        assert route_request(route).method == "GET"
        assert_matches_type(SessionTodoResponse, result, path=["response"])


class TestAsyncSessionNewOperationsWire:
    @pytest.mark.respx(base_url=base_url)
    async def test_status(self, async_client: AsyncOpencode, respx_mock: MockRouter) -> None:
        payload = {"ses_1": {"type": "idle"}}
        respx_mock.get("/session/status").mock(return_value=httpx.Response(200, json=payload))
        result = await async_client.session.status()
        assert_matches_type(SessionStatusResponse, result, path=["response"])

    @pytest.mark.respx(base_url=base_url)
    async def test_get(self, async_client: AsyncOpencode, respx_mock: MockRouter) -> None:
        respx_mock.get("/session/ses_1").mock(return_value=httpx.Response(200, json=MINIMAL_SESSION))
        result = await async_client.session.get("ses_1")
        assert_matches_type(Session, result, path=["response"])

    @pytest.mark.respx(base_url=base_url)
    async def test_update(self, async_client: AsyncOpencode, respx_mock: MockRouter) -> None:
        route = respx_mock.patch("/session/ses_1").mock(return_value=httpx.Response(200, json=MINIMAL_SESSION))
        result = await async_client.session.update("ses_1", title="new title")
        body = read_json_body(route)
        assert body["title"] == "new title"
        assert_matches_type(Session, result, path=["response"])

    @pytest.mark.respx(base_url=base_url)
    async def test_children(self, async_client: AsyncOpencode, respx_mock: MockRouter) -> None:
        respx_mock.get("/session/ses_1/children").mock(return_value=httpx.Response(200, json=[MINIMAL_SESSION]))
        result = await async_client.session.children("ses_1")
        assert_matches_type(SessionChildrenResponse, result, path=["response"])

    @pytest.mark.respx(base_url=base_url)
    async def test_command(self, async_client: AsyncOpencode, respx_mock: MockRouter) -> None:
        payload: dict[str, object] = {"info": PROMPT_SAMPLE["info"], "parts": []}
        respx_mock.post("/session/ses_1/command").mock(return_value=httpx.Response(200, json=payload))
        result = await async_client.session.command("ses_1", arguments="a", command="c")
        assert_matches_type(SessionCommandResponse, result, path=["response"])

    @pytest.mark.respx(base_url=base_url)
    async def test_diff(self, async_client: AsyncOpencode, respx_mock: MockRouter) -> None:
        payload = [{"additions": 1, "deletions": 0}]
        respx_mock.get("/session/ses_1/diff").mock(return_value=httpx.Response(200, json=payload))
        result = await async_client.session.diff("ses_1")
        assert_matches_type(SessionDiffResponse, result, path=["response"])

    @pytest.mark.respx(base_url=base_url)
    async def test_fork(self, async_client: AsyncOpencode, respx_mock: MockRouter) -> None:
        respx_mock.post("/session/ses_1/fork").mock(return_value=httpx.Response(200, json=MINIMAL_SESSION))
        result = await async_client.session.fork("ses_1")
        assert_matches_type(Session, result, path=["response"])

    @pytest.mark.respx(base_url=base_url)
    async def test_delete_message(self, async_client: AsyncOpencode, respx_mock: MockRouter) -> None:
        respx_mock.delete("/session/ses_1/message/msg_1").mock(return_value=httpx.Response(200, json=True))
        result = await async_client.session.delete_message("ses_1", message_id="msg_1")
        assert_matches_type(SessionDeleteMessageResponse, result, path=["response"])

    @pytest.mark.respx(base_url=base_url)
    async def test_get_message(self, async_client: AsyncOpencode, respx_mock: MockRouter) -> None:
        payload: dict[str, object] = {"info": PROMPT_SAMPLE["info"], "parts": []}
        respx_mock.get("/session/ses_1/message/msg_1").mock(return_value=httpx.Response(200, json=payload))
        result = await async_client.session.get_message("ses_1", message_id="msg_1")
        assert_matches_type(SessionMessagesResponseItem, result, path=["response"])

    @pytest.mark.respx(base_url=base_url)
    async def test_delete_part(self, async_client: AsyncOpencode, respx_mock: MockRouter) -> None:
        respx_mock.delete("/session/ses_1/message/msg_1/part/prt_1").mock(return_value=httpx.Response(200, json=True))
        result = await async_client.session.delete_part("ses_1", message_id="msg_1", part_id="prt_1")
        assert_matches_type(SessionDeletePartResponse, result, path=["response"])

    @pytest.mark.respx(base_url=base_url)
    async def test_update_part(self, async_client: AsyncOpencode, respx_mock: MockRouter) -> None:
        wire_payload: dict[str, object] = {
            "id": "prt_1",
            "messageID": "msg_1",
            "sessionID": "ses_1",
            "type": "text",
            "text": "hello",
        }
        part_payload: session_update_part_params.TextPartParam = {
            "id": "prt_1",
            "message_id": "msg_1",
            "session_id": "ses_1",
            "type": "text",
            "text": "hello",
        }
        respx_mock.patch("/session/ses_1/message/msg_1/part/prt_1").mock(
            return_value=httpx.Response(200, json=wire_payload)
        )
        result = await async_client.session.update_part("ses_1", message_id="msg_1", part_id="prt_1", part=part_payload)
        part = cast(Part, construct_type(type_=Part, value=result))
        assert part.type == "text"

    @pytest.mark.respx(base_url=base_url)
    async def test_respond_permission(self, async_client: AsyncOpencode, respx_mock: MockRouter) -> None:
        route = respx_mock.post("/session/ses_1/permissions/per_1").mock(return_value=httpx.Response(200, json=True))
        result = await async_client.session.respond_permission("ses_1", permission_id="per_1", response="always")
        body = read_json_body(route)
        assert body["response"] == "always"
        assert_matches_type(SessionRespondPermissionResponse, result, path=["response"])

    @pytest.mark.respx(base_url=base_url)
    async def test_prompt_async(self, async_client: AsyncOpencode, respx_mock: MockRouter) -> None:
        respx_mock.post("/session/ses_1/prompt_async").mock(return_value=httpx.Response(204))
        result = await async_client.session.prompt_async("ses_1", parts=[{"type": "text", "text": "hi"}])
        assert result is None

    @pytest.mark.respx(base_url=base_url)
    async def test_shell(self, async_client: AsyncOpencode, respx_mock: MockRouter) -> None:
        payload: dict[str, object] = {"info": PROMPT_SAMPLE["info"], "parts": []}
        respx_mock.post("/session/ses_1/shell").mock(return_value=httpx.Response(200, json=payload))
        result = await async_client.session.shell("ses_1", agent="build", command="ls")
        assert_matches_type(SessionShellResponse, result, path=["response"])

    @pytest.mark.respx(base_url=base_url)
    async def test_todo(self, async_client: AsyncOpencode, respx_mock: MockRouter) -> None:
        payload = [{"content": "x", "status": "pending", "priority": "low"}]
        respx_mock.get("/session/ses_1/todo").mock(return_value=httpx.Response(200, json=payload))
        result = await async_client.session.todo("ses_1")
        assert_matches_type(SessionTodoResponse, result, path=["response"])


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
