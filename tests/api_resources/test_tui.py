# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from opencode_ai import Opencode, AsyncOpencode
from tests.utils import assert_matches_type
from opencode_ai.types import TuiOpenHelpResponse, TuiAppendPromptResponse

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
