# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from opencode_ai import Opencode, AsyncOpencode
from tests.utils import assert_matches_type
from opencode_ai.types import (
    Session,
    AssistantMessage,
    SessionInitResponse,
    SessionListResponse,
    SessionAbortResponse,
    SessionDeleteResponse,
    SessionMessagesResponse,
    SessionSummarizeResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSession:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: Opencode) -> None:
        session = client.session.create()
        assert_matches_type(Session, session, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: Opencode) -> None:
        response = client.session.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(Session, session, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: Opencode) -> None:
        with client.session.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(Session, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Opencode) -> None:
        session = client.session.list()
        assert_matches_type(SessionListResponse, session, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Opencode) -> None:
        response = client.session.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(SessionListResponse, session, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Opencode) -> None:
        with client.session.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(SessionListResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Opencode) -> None:
        session = client.session.delete(
            "id",
        )
        assert_matches_type(SessionDeleteResponse, session, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Opencode) -> None:
        response = client.session.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(SessionDeleteResponse, session, path=["response"])

    @pytest.mark.skip()
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

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete(self, client: Opencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.session.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_abort(self, client: Opencode) -> None:
        session = client.session.abort(
            "id",
        )
        assert_matches_type(SessionAbortResponse, session, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_abort(self, client: Opencode) -> None:
        response = client.session.with_raw_response.abort(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(SessionAbortResponse, session, path=["response"])

    @pytest.mark.skip()
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

    @pytest.mark.skip()
    @parametrize
    def test_path_params_abort(self, client: Opencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.session.with_raw_response.abort(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_chat(self, client: Opencode) -> None:
        session = client.session.chat(
            id="id",
            model_id="modelID",
            parts=[
                {
                    "text": "text",
                    "type": "text",
                }
            ],
            provider_id="providerID",
        )
        assert_matches_type(AssistantMessage, session, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_chat(self, client: Opencode) -> None:
        response = client.session.with_raw_response.chat(
            id="id",
            model_id="modelID",
            parts=[
                {
                    "text": "text",
                    "type": "text",
                }
            ],
            provider_id="providerID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(AssistantMessage, session, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_chat(self, client: Opencode) -> None:
        with client.session.with_streaming_response.chat(
            id="id",
            model_id="modelID",
            parts=[
                {
                    "text": "text",
                    "type": "text",
                }
            ],
            provider_id="providerID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(AssistantMessage, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_chat(self, client: Opencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.session.with_raw_response.chat(
                id="",
                model_id="modelID",
                parts=[
                    {
                        "text": "text",
                        "type": "text",
                    }
                ],
                provider_id="providerID",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_init(self, client: Opencode) -> None:
        session = client.session.init(
            id="id",
            model_id="modelID",
            provider_id="providerID",
        )
        assert_matches_type(SessionInitResponse, session, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_init(self, client: Opencode) -> None:
        response = client.session.with_raw_response.init(
            id="id",
            model_id="modelID",
            provider_id="providerID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(SessionInitResponse, session, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_init(self, client: Opencode) -> None:
        with client.session.with_streaming_response.init(
            id="id",
            model_id="modelID",
            provider_id="providerID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(SessionInitResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_init(self, client: Opencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.session.with_raw_response.init(
                id="",
                model_id="modelID",
                provider_id="providerID",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_messages(self, client: Opencode) -> None:
        session = client.session.messages(
            "id",
        )
        assert_matches_type(SessionMessagesResponse, session, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_messages(self, client: Opencode) -> None:
        response = client.session.with_raw_response.messages(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(SessionMessagesResponse, session, path=["response"])

    @pytest.mark.skip()
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

    @pytest.mark.skip()
    @parametrize
    def test_path_params_messages(self, client: Opencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.session.with_raw_response.messages(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_share(self, client: Opencode) -> None:
        session = client.session.share(
            "id",
        )
        assert_matches_type(Session, session, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_share(self, client: Opencode) -> None:
        response = client.session.with_raw_response.share(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(Session, session, path=["response"])

    @pytest.mark.skip()
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

    @pytest.mark.skip()
    @parametrize
    def test_path_params_share(self, client: Opencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.session.with_raw_response.share(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_summarize(self, client: Opencode) -> None:
        session = client.session.summarize(
            id="id",
            model_id="modelID",
            provider_id="providerID",
        )
        assert_matches_type(SessionSummarizeResponse, session, path=["response"])

    @pytest.mark.skip()
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

    @pytest.mark.skip()
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

    @pytest.mark.skip()
    @parametrize
    def test_path_params_summarize(self, client: Opencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.session.with_raw_response.summarize(
                id="",
                model_id="modelID",
                provider_id="providerID",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_unshare(self, client: Opencode) -> None:
        session = client.session.unshare(
            "id",
        )
        assert_matches_type(Session, session, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_unshare(self, client: Opencode) -> None:
        response = client.session.with_raw_response.unshare(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(Session, session, path=["response"])

    @pytest.mark.skip()
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

    @pytest.mark.skip()
    @parametrize
    def test_path_params_unshare(self, client: Opencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.session.with_raw_response.unshare(
                "",
            )


class TestAsyncSession:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncOpencode) -> None:
        session = await async_client.session.create()
        assert_matches_type(Session, session, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncOpencode) -> None:
        response = await async_client.session.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(Session, session, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncOpencode) -> None:
        async with async_client.session.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(Session, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncOpencode) -> None:
        session = await async_client.session.list()
        assert_matches_type(SessionListResponse, session, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncOpencode) -> None:
        response = await async_client.session.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(SessionListResponse, session, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncOpencode) -> None:
        async with async_client.session.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(SessionListResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncOpencode) -> None:
        session = await async_client.session.delete(
            "id",
        )
        assert_matches_type(SessionDeleteResponse, session, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncOpencode) -> None:
        response = await async_client.session.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(SessionDeleteResponse, session, path=["response"])

    @pytest.mark.skip()
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

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncOpencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.session.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_abort(self, async_client: AsyncOpencode) -> None:
        session = await async_client.session.abort(
            "id",
        )
        assert_matches_type(SessionAbortResponse, session, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_abort(self, async_client: AsyncOpencode) -> None:
        response = await async_client.session.with_raw_response.abort(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(SessionAbortResponse, session, path=["response"])

    @pytest.mark.skip()
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

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_abort(self, async_client: AsyncOpencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.session.with_raw_response.abort(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_chat(self, async_client: AsyncOpencode) -> None:
        session = await async_client.session.chat(
            id="id",
            model_id="modelID",
            parts=[
                {
                    "text": "text",
                    "type": "text",
                }
            ],
            provider_id="providerID",
        )
        assert_matches_type(AssistantMessage, session, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_chat(self, async_client: AsyncOpencode) -> None:
        response = await async_client.session.with_raw_response.chat(
            id="id",
            model_id="modelID",
            parts=[
                {
                    "text": "text",
                    "type": "text",
                }
            ],
            provider_id="providerID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(AssistantMessage, session, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_chat(self, async_client: AsyncOpencode) -> None:
        async with async_client.session.with_streaming_response.chat(
            id="id",
            model_id="modelID",
            parts=[
                {
                    "text": "text",
                    "type": "text",
                }
            ],
            provider_id="providerID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(AssistantMessage, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_chat(self, async_client: AsyncOpencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.session.with_raw_response.chat(
                id="",
                model_id="modelID",
                parts=[
                    {
                        "text": "text",
                        "type": "text",
                    }
                ],
                provider_id="providerID",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_init(self, async_client: AsyncOpencode) -> None:
        session = await async_client.session.init(
            id="id",
            model_id="modelID",
            provider_id="providerID",
        )
        assert_matches_type(SessionInitResponse, session, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_init(self, async_client: AsyncOpencode) -> None:
        response = await async_client.session.with_raw_response.init(
            id="id",
            model_id="modelID",
            provider_id="providerID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(SessionInitResponse, session, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_init(self, async_client: AsyncOpencode) -> None:
        async with async_client.session.with_streaming_response.init(
            id="id",
            model_id="modelID",
            provider_id="providerID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(SessionInitResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_init(self, async_client: AsyncOpencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.session.with_raw_response.init(
                id="",
                model_id="modelID",
                provider_id="providerID",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_messages(self, async_client: AsyncOpencode) -> None:
        session = await async_client.session.messages(
            "id",
        )
        assert_matches_type(SessionMessagesResponse, session, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_messages(self, async_client: AsyncOpencode) -> None:
        response = await async_client.session.with_raw_response.messages(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(SessionMessagesResponse, session, path=["response"])

    @pytest.mark.skip()
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

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_messages(self, async_client: AsyncOpencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.session.with_raw_response.messages(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_share(self, async_client: AsyncOpencode) -> None:
        session = await async_client.session.share(
            "id",
        )
        assert_matches_type(Session, session, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_share(self, async_client: AsyncOpencode) -> None:
        response = await async_client.session.with_raw_response.share(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(Session, session, path=["response"])

    @pytest.mark.skip()
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

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_share(self, async_client: AsyncOpencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.session.with_raw_response.share(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_summarize(self, async_client: AsyncOpencode) -> None:
        session = await async_client.session.summarize(
            id="id",
            model_id="modelID",
            provider_id="providerID",
        )
        assert_matches_type(SessionSummarizeResponse, session, path=["response"])

    @pytest.mark.skip()
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

    @pytest.mark.skip()
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

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_summarize(self, async_client: AsyncOpencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.session.with_raw_response.summarize(
                id="",
                model_id="modelID",
                provider_id="providerID",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_unshare(self, async_client: AsyncOpencode) -> None:
        session = await async_client.session.unshare(
            "id",
        )
        assert_matches_type(Session, session, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_unshare(self, async_client: AsyncOpencode) -> None:
        response = await async_client.session.with_raw_response.unshare(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(Session, session, path=["response"])

    @pytest.mark.skip()
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

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_unshare(self, async_client: AsyncOpencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.session.with_raw_response.unshare(
                "",
            )
