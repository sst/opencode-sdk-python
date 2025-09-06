# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from opencode_ai import Opencode, AsyncOpencode
from tests.utils import assert_matches_type
from opencode_ai.types import (
    AssistantMessage,
    SessionInitResponse,
    SessionListResponse,
    SessionAbortResponse,
    SessionDeleteResponse,
    SessionPromptResponse,
    SessionCommandResponse,
    SessionMessageResponse,
    SessionChildrenResponse,
    SessionMessagesResponse,
    SessionSummarizeResponse,
)
from opencode_ai.types.session import Session

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSession:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Opencode) -> None:
        session = client.session.create()
        assert_matches_type(Session, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Opencode) -> None:
        session = client.session.create(
            directory="directory",
            parent_id="parentID",
            title="title",
        )
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
    def test_method_update(self, client: Opencode) -> None:
        session = client.session.update(
            id="id",
        )
        assert_matches_type(Session, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Opencode) -> None:
        session = client.session.update(
            id="id",
            directory="directory",
            title="title",
        )
        assert_matches_type(Session, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Opencode) -> None:
        response = client.session.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(Session, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Opencode) -> None:
        with client.session.with_streaming_response.update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(Session, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Opencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.session.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Opencode) -> None:
        session = client.session.list()
        assert_matches_type(SessionListResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Opencode) -> None:
        session = client.session.list(
            directory="directory",
        )
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
            id="id",
        )
        assert_matches_type(SessionDeleteResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete_with_all_params(self, client: Opencode) -> None:
        session = client.session.delete(
            id="id",
            directory="directory",
        )
        assert_matches_type(SessionDeleteResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Opencode) -> None:
        response = client.session.with_raw_response.delete(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(SessionDeleteResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Opencode) -> None:
        with client.session.with_streaming_response.delete(
            id="id",
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
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_abort(self, client: Opencode) -> None:
        session = client.session.abort(
            id="id",
        )
        assert_matches_type(SessionAbortResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_abort_with_all_params(self, client: Opencode) -> None:
        session = client.session.abort(
            id="id",
            directory="directory",
        )
        assert_matches_type(SessionAbortResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_abort(self, client: Opencode) -> None:
        response = client.session.with_raw_response.abort(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(SessionAbortResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_abort(self, client: Opencode) -> None:
        with client.session.with_streaming_response.abort(
            id="id",
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
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_children(self, client: Opencode) -> None:
        session = client.session.children(
            id="id",
        )
        assert_matches_type(SessionChildrenResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_children_with_all_params(self, client: Opencode) -> None:
        session = client.session.children(
            id="id",
            directory="directory",
        )
        assert_matches_type(SessionChildrenResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_children(self, client: Opencode) -> None:
        response = client.session.with_raw_response.children(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(SessionChildrenResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_children(self, client: Opencode) -> None:
        with client.session.with_streaming_response.children(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(SessionChildrenResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_children(self, client: Opencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.session.with_raw_response.children(
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_command(self, client: Opencode) -> None:
        session = client.session.command(
            id="id",
            arguments="arguments",
            command="command",
        )
        assert_matches_type(SessionCommandResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_command_with_all_params(self, client: Opencode) -> None:
        session = client.session.command(
            id="id",
            arguments="arguments",
            command="command",
            directory="directory",
            agent="agent",
            message_id="msg",
            model="model",
        )
        assert_matches_type(SessionCommandResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_command(self, client: Opencode) -> None:
        response = client.session.with_raw_response.command(
            id="id",
            arguments="arguments",
            command="command",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(SessionCommandResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_command(self, client: Opencode) -> None:
        with client.session.with_streaming_response.command(
            id="id",
            arguments="arguments",
            command="command",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(SessionCommandResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_command(self, client: Opencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.session.with_raw_response.command(
                id="",
                arguments="arguments",
                command="command",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get(self, client: Opencode) -> None:
        session = client.session.get(
            id="id",
        )
        assert_matches_type(Session, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_with_all_params(self, client: Opencode) -> None:
        session = client.session.get(
            id="id",
            directory="directory",
        )
        assert_matches_type(Session, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get(self, client: Opencode) -> None:
        response = client.session.with_raw_response.get(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(Session, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get(self, client: Opencode) -> None:
        with client.session.with_streaming_response.get(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(Session, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get(self, client: Opencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.session.with_raw_response.get(
                id="",
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
    def test_method_init_with_all_params(self, client: Opencode) -> None:
        session = client.session.init(
            id="id",
            message_id="messageID",
            model_id="modelID",
            provider_id="providerID",
            directory="directory",
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
    def test_method_message(self, client: Opencode) -> None:
        session = client.session.message(
            message_id="messageID",
            id="id",
        )
        assert_matches_type(SessionMessageResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_message_with_all_params(self, client: Opencode) -> None:
        session = client.session.message(
            message_id="messageID",
            id="id",
            directory="directory",
        )
        assert_matches_type(SessionMessageResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_message(self, client: Opencode) -> None:
        response = client.session.with_raw_response.message(
            message_id="messageID",
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(SessionMessageResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_message(self, client: Opencode) -> None:
        with client.session.with_streaming_response.message(
            message_id="messageID",
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(SessionMessageResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_message(self, client: Opencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.session.with_raw_response.message(
                message_id="messageID",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_id` but received ''"):
            client.session.with_raw_response.message(
                message_id="",
                id="id",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_messages(self, client: Opencode) -> None:
        session = client.session.messages(
            id="id",
        )
        assert_matches_type(SessionMessagesResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_messages_with_all_params(self, client: Opencode) -> None:
        session = client.session.messages(
            id="id",
            directory="directory",
        )
        assert_matches_type(SessionMessagesResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_messages(self, client: Opencode) -> None:
        response = client.session.with_raw_response.messages(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(SessionMessagesResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_messages(self, client: Opencode) -> None:
        with client.session.with_streaming_response.messages(
            id="id",
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
                id="",
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
            directory="directory",
            agent="agent",
            message_id="msg",
            model={
                "model_id": "modelID",
                "provider_id": "providerID",
            },
            system="system",
            tools={"foo": True},
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
            directory="directory",
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
            id="id",
        )
        assert_matches_type(Session, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_share_with_all_params(self, client: Opencode) -> None:
        session = client.session.share(
            id="id",
            directory="directory",
        )
        assert_matches_type(Session, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_share(self, client: Opencode) -> None:
        response = client.session.with_raw_response.share(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(Session, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_share(self, client: Opencode) -> None:
        with client.session.with_streaming_response.share(
            id="id",
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
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_shell(self, client: Opencode) -> None:
        session = client.session.shell(
            id="id",
            agent="agent",
            command="command",
        )
        assert_matches_type(AssistantMessage, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_shell_with_all_params(self, client: Opencode) -> None:
        session = client.session.shell(
            id="id",
            agent="agent",
            command="command",
            directory="directory",
        )
        assert_matches_type(AssistantMessage, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_shell(self, client: Opencode) -> None:
        response = client.session.with_raw_response.shell(
            id="id",
            agent="agent",
            command="command",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(AssistantMessage, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_shell(self, client: Opencode) -> None:
        with client.session.with_streaming_response.shell(
            id="id",
            agent="agent",
            command="command",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(AssistantMessage, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_shell(self, client: Opencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.session.with_raw_response.shell(
                id="",
                agent="agent",
                command="command",
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
    def test_method_summarize_with_all_params(self, client: Opencode) -> None:
        session = client.session.summarize(
            id="id",
            model_id="modelID",
            provider_id="providerID",
            directory="directory",
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
            id="id",
        )
        assert_matches_type(Session, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_unrevert_with_all_params(self, client: Opencode) -> None:
        session = client.session.unrevert(
            id="id",
            directory="directory",
        )
        assert_matches_type(Session, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_unrevert(self, client: Opencode) -> None:
        response = client.session.with_raw_response.unrevert(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(Session, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_unrevert(self, client: Opencode) -> None:
        with client.session.with_streaming_response.unrevert(
            id="id",
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
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_unshare(self, client: Opencode) -> None:
        session = client.session.unshare(
            id="id",
        )
        assert_matches_type(Session, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_unshare_with_all_params(self, client: Opencode) -> None:
        session = client.session.unshare(
            id="id",
            directory="directory",
        )
        assert_matches_type(Session, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_unshare(self, client: Opencode) -> None:
        response = client.session.with_raw_response.unshare(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(Session, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_unshare(self, client: Opencode) -> None:
        with client.session.with_streaming_response.unshare(
            id="id",
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
                id="",
            )


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
    async def test_method_create_with_all_params(self, async_client: AsyncOpencode) -> None:
        session = await async_client.session.create(
            directory="directory",
            parent_id="parentID",
            title="title",
        )
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
    async def test_method_update(self, async_client: AsyncOpencode) -> None:
        session = await async_client.session.update(
            id="id",
        )
        assert_matches_type(Session, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncOpencode) -> None:
        session = await async_client.session.update(
            id="id",
            directory="directory",
            title="title",
        )
        assert_matches_type(Session, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncOpencode) -> None:
        response = await async_client.session.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(Session, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncOpencode) -> None:
        async with async_client.session.with_streaming_response.update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(Session, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncOpencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.session.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncOpencode) -> None:
        session = await async_client.session.list()
        assert_matches_type(SessionListResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncOpencode) -> None:
        session = await async_client.session.list(
            directory="directory",
        )
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
            id="id",
        )
        assert_matches_type(SessionDeleteResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncOpencode) -> None:
        session = await async_client.session.delete(
            id="id",
            directory="directory",
        )
        assert_matches_type(SessionDeleteResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncOpencode) -> None:
        response = await async_client.session.with_raw_response.delete(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(SessionDeleteResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncOpencode) -> None:
        async with async_client.session.with_streaming_response.delete(
            id="id",
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
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_abort(self, async_client: AsyncOpencode) -> None:
        session = await async_client.session.abort(
            id="id",
        )
        assert_matches_type(SessionAbortResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_abort_with_all_params(self, async_client: AsyncOpencode) -> None:
        session = await async_client.session.abort(
            id="id",
            directory="directory",
        )
        assert_matches_type(SessionAbortResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_abort(self, async_client: AsyncOpencode) -> None:
        response = await async_client.session.with_raw_response.abort(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(SessionAbortResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_abort(self, async_client: AsyncOpencode) -> None:
        async with async_client.session.with_streaming_response.abort(
            id="id",
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
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_children(self, async_client: AsyncOpencode) -> None:
        session = await async_client.session.children(
            id="id",
        )
        assert_matches_type(SessionChildrenResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_children_with_all_params(self, async_client: AsyncOpencode) -> None:
        session = await async_client.session.children(
            id="id",
            directory="directory",
        )
        assert_matches_type(SessionChildrenResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_children(self, async_client: AsyncOpencode) -> None:
        response = await async_client.session.with_raw_response.children(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(SessionChildrenResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_children(self, async_client: AsyncOpencode) -> None:
        async with async_client.session.with_streaming_response.children(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(SessionChildrenResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_children(self, async_client: AsyncOpencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.session.with_raw_response.children(
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_command(self, async_client: AsyncOpencode) -> None:
        session = await async_client.session.command(
            id="id",
            arguments="arguments",
            command="command",
        )
        assert_matches_type(SessionCommandResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_command_with_all_params(self, async_client: AsyncOpencode) -> None:
        session = await async_client.session.command(
            id="id",
            arguments="arguments",
            command="command",
            directory="directory",
            agent="agent",
            message_id="msg",
            model="model",
        )
        assert_matches_type(SessionCommandResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_command(self, async_client: AsyncOpencode) -> None:
        response = await async_client.session.with_raw_response.command(
            id="id",
            arguments="arguments",
            command="command",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(SessionCommandResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_command(self, async_client: AsyncOpencode) -> None:
        async with async_client.session.with_streaming_response.command(
            id="id",
            arguments="arguments",
            command="command",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(SessionCommandResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_command(self, async_client: AsyncOpencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.session.with_raw_response.command(
                id="",
                arguments="arguments",
                command="command",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get(self, async_client: AsyncOpencode) -> None:
        session = await async_client.session.get(
            id="id",
        )
        assert_matches_type(Session, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncOpencode) -> None:
        session = await async_client.session.get(
            id="id",
            directory="directory",
        )
        assert_matches_type(Session, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncOpencode) -> None:
        response = await async_client.session.with_raw_response.get(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(Session, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncOpencode) -> None:
        async with async_client.session.with_streaming_response.get(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(Session, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get(self, async_client: AsyncOpencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.session.with_raw_response.get(
                id="",
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
    async def test_method_init_with_all_params(self, async_client: AsyncOpencode) -> None:
        session = await async_client.session.init(
            id="id",
            message_id="messageID",
            model_id="modelID",
            provider_id="providerID",
            directory="directory",
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
    async def test_method_message(self, async_client: AsyncOpencode) -> None:
        session = await async_client.session.message(
            message_id="messageID",
            id="id",
        )
        assert_matches_type(SessionMessageResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_message_with_all_params(self, async_client: AsyncOpencode) -> None:
        session = await async_client.session.message(
            message_id="messageID",
            id="id",
            directory="directory",
        )
        assert_matches_type(SessionMessageResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_message(self, async_client: AsyncOpencode) -> None:
        response = await async_client.session.with_raw_response.message(
            message_id="messageID",
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(SessionMessageResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_message(self, async_client: AsyncOpencode) -> None:
        async with async_client.session.with_streaming_response.message(
            message_id="messageID",
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(SessionMessageResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_message(self, async_client: AsyncOpencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.session.with_raw_response.message(
                message_id="messageID",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_id` but received ''"):
            await async_client.session.with_raw_response.message(
                message_id="",
                id="id",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_messages(self, async_client: AsyncOpencode) -> None:
        session = await async_client.session.messages(
            id="id",
        )
        assert_matches_type(SessionMessagesResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_messages_with_all_params(self, async_client: AsyncOpencode) -> None:
        session = await async_client.session.messages(
            id="id",
            directory="directory",
        )
        assert_matches_type(SessionMessagesResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_messages(self, async_client: AsyncOpencode) -> None:
        response = await async_client.session.with_raw_response.messages(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(SessionMessagesResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_messages(self, async_client: AsyncOpencode) -> None:
        async with async_client.session.with_streaming_response.messages(
            id="id",
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
                id="",
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
            directory="directory",
            agent="agent",
            message_id="msg",
            model={
                "model_id": "modelID",
                "provider_id": "providerID",
            },
            system="system",
            tools={"foo": True},
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
            directory="directory",
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
            id="id",
        )
        assert_matches_type(Session, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_share_with_all_params(self, async_client: AsyncOpencode) -> None:
        session = await async_client.session.share(
            id="id",
            directory="directory",
        )
        assert_matches_type(Session, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_share(self, async_client: AsyncOpencode) -> None:
        response = await async_client.session.with_raw_response.share(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(Session, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_share(self, async_client: AsyncOpencode) -> None:
        async with async_client.session.with_streaming_response.share(
            id="id",
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
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_shell(self, async_client: AsyncOpencode) -> None:
        session = await async_client.session.shell(
            id="id",
            agent="agent",
            command="command",
        )
        assert_matches_type(AssistantMessage, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_shell_with_all_params(self, async_client: AsyncOpencode) -> None:
        session = await async_client.session.shell(
            id="id",
            agent="agent",
            command="command",
            directory="directory",
        )
        assert_matches_type(AssistantMessage, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_shell(self, async_client: AsyncOpencode) -> None:
        response = await async_client.session.with_raw_response.shell(
            id="id",
            agent="agent",
            command="command",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(AssistantMessage, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_shell(self, async_client: AsyncOpencode) -> None:
        async with async_client.session.with_streaming_response.shell(
            id="id",
            agent="agent",
            command="command",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(AssistantMessage, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_shell(self, async_client: AsyncOpencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.session.with_raw_response.shell(
                id="",
                agent="agent",
                command="command",
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
    async def test_method_summarize_with_all_params(self, async_client: AsyncOpencode) -> None:
        session = await async_client.session.summarize(
            id="id",
            model_id="modelID",
            provider_id="providerID",
            directory="directory",
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
            id="id",
        )
        assert_matches_type(Session, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_unrevert_with_all_params(self, async_client: AsyncOpencode) -> None:
        session = await async_client.session.unrevert(
            id="id",
            directory="directory",
        )
        assert_matches_type(Session, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_unrevert(self, async_client: AsyncOpencode) -> None:
        response = await async_client.session.with_raw_response.unrevert(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(Session, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_unrevert(self, async_client: AsyncOpencode) -> None:
        async with async_client.session.with_streaming_response.unrevert(
            id="id",
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
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_unshare(self, async_client: AsyncOpencode) -> None:
        session = await async_client.session.unshare(
            id="id",
        )
        assert_matches_type(Session, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_unshare_with_all_params(self, async_client: AsyncOpencode) -> None:
        session = await async_client.session.unshare(
            id="id",
            directory="directory",
        )
        assert_matches_type(Session, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_unshare(self, async_client: AsyncOpencode) -> None:
        response = await async_client.session.with_raw_response.unshare(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(Session, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_unshare(self, async_client: AsyncOpencode) -> None:
        async with async_client.session.with_streaming_response.unshare(
            id="id",
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
                id="",
            )
