# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from opencode_ai import Opencode, AsyncOpencode
from tests.utils import assert_matches_type
from opencode_ai.types import (
    TuiOpenHelpResponse,
    TuiShowToastResponse,
    TuiOpenModelsResponse,
    TuiOpenThemesResponse,
    TuiClearPromptResponse,
    TuiAppendPromptResponse,
    TuiOpenSessionsResponse,
    TuiSubmitPromptResponse,
    TuiExecuteCommandResponse,
)

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
    def test_method_append_prompt_with_all_params(self, client: Opencode) -> None:
        tui = client.tui.append_prompt(
            text="text",
            directory="directory",
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
    def test_method_clear_prompt(self, client: Opencode) -> None:
        tui = client.tui.clear_prompt()
        assert_matches_type(TuiClearPromptResponse, tui, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_clear_prompt_with_all_params(self, client: Opencode) -> None:
        tui = client.tui.clear_prompt(
            directory="directory",
        )
        assert_matches_type(TuiClearPromptResponse, tui, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_clear_prompt(self, client: Opencode) -> None:
        response = client.tui.with_raw_response.clear_prompt()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tui = response.parse()
        assert_matches_type(TuiClearPromptResponse, tui, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_clear_prompt(self, client: Opencode) -> None:
        with client.tui.with_streaming_response.clear_prompt() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tui = response.parse()
            assert_matches_type(TuiClearPromptResponse, tui, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_execute_command(self, client: Opencode) -> None:
        tui = client.tui.execute_command(
            command="command",
        )
        assert_matches_type(TuiExecuteCommandResponse, tui, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_execute_command_with_all_params(self, client: Opencode) -> None:
        tui = client.tui.execute_command(
            command="command",
            directory="directory",
        )
        assert_matches_type(TuiExecuteCommandResponse, tui, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_execute_command(self, client: Opencode) -> None:
        response = client.tui.with_raw_response.execute_command(
            command="command",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tui = response.parse()
        assert_matches_type(TuiExecuteCommandResponse, tui, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_execute_command(self, client: Opencode) -> None:
        with client.tui.with_streaming_response.execute_command(
            command="command",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tui = response.parse()
            assert_matches_type(TuiExecuteCommandResponse, tui, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_open_help(self, client: Opencode) -> None:
        tui = client.tui.open_help()
        assert_matches_type(TuiOpenHelpResponse, tui, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_open_help_with_all_params(self, client: Opencode) -> None:
        tui = client.tui.open_help(
            directory="directory",
        )
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

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_open_models(self, client: Opencode) -> None:
        tui = client.tui.open_models()
        assert_matches_type(TuiOpenModelsResponse, tui, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_open_models_with_all_params(self, client: Opencode) -> None:
        tui = client.tui.open_models(
            directory="directory",
        )
        assert_matches_type(TuiOpenModelsResponse, tui, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_open_models(self, client: Opencode) -> None:
        response = client.tui.with_raw_response.open_models()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tui = response.parse()
        assert_matches_type(TuiOpenModelsResponse, tui, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_open_models(self, client: Opencode) -> None:
        with client.tui.with_streaming_response.open_models() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tui = response.parse()
            assert_matches_type(TuiOpenModelsResponse, tui, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_open_sessions(self, client: Opencode) -> None:
        tui = client.tui.open_sessions()
        assert_matches_type(TuiOpenSessionsResponse, tui, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_open_sessions_with_all_params(self, client: Opencode) -> None:
        tui = client.tui.open_sessions(
            directory="directory",
        )
        assert_matches_type(TuiOpenSessionsResponse, tui, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_open_sessions(self, client: Opencode) -> None:
        response = client.tui.with_raw_response.open_sessions()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tui = response.parse()
        assert_matches_type(TuiOpenSessionsResponse, tui, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_open_sessions(self, client: Opencode) -> None:
        with client.tui.with_streaming_response.open_sessions() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tui = response.parse()
            assert_matches_type(TuiOpenSessionsResponse, tui, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_open_themes(self, client: Opencode) -> None:
        tui = client.tui.open_themes()
        assert_matches_type(TuiOpenThemesResponse, tui, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_open_themes_with_all_params(self, client: Opencode) -> None:
        tui = client.tui.open_themes(
            directory="directory",
        )
        assert_matches_type(TuiOpenThemesResponse, tui, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_open_themes(self, client: Opencode) -> None:
        response = client.tui.with_raw_response.open_themes()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tui = response.parse()
        assert_matches_type(TuiOpenThemesResponse, tui, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_open_themes(self, client: Opencode) -> None:
        with client.tui.with_streaming_response.open_themes() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tui = response.parse()
            assert_matches_type(TuiOpenThemesResponse, tui, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_show_toast(self, client: Opencode) -> None:
        tui = client.tui.show_toast(
            message="message",
            variant="info",
        )
        assert_matches_type(TuiShowToastResponse, tui, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_show_toast_with_all_params(self, client: Opencode) -> None:
        tui = client.tui.show_toast(
            message="message",
            variant="info",
            directory="directory",
            title="title",
        )
        assert_matches_type(TuiShowToastResponse, tui, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_show_toast(self, client: Opencode) -> None:
        response = client.tui.with_raw_response.show_toast(
            message="message",
            variant="info",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tui = response.parse()
        assert_matches_type(TuiShowToastResponse, tui, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_show_toast(self, client: Opencode) -> None:
        with client.tui.with_streaming_response.show_toast(
            message="message",
            variant="info",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tui = response.parse()
            assert_matches_type(TuiShowToastResponse, tui, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_submit_prompt(self, client: Opencode) -> None:
        tui = client.tui.submit_prompt()
        assert_matches_type(TuiSubmitPromptResponse, tui, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_submit_prompt_with_all_params(self, client: Opencode) -> None:
        tui = client.tui.submit_prompt(
            directory="directory",
        )
        assert_matches_type(TuiSubmitPromptResponse, tui, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_submit_prompt(self, client: Opencode) -> None:
        response = client.tui.with_raw_response.submit_prompt()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tui = response.parse()
        assert_matches_type(TuiSubmitPromptResponse, tui, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_submit_prompt(self, client: Opencode) -> None:
        with client.tui.with_streaming_response.submit_prompt() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tui = response.parse()
            assert_matches_type(TuiSubmitPromptResponse, tui, path=["response"])

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
    async def test_method_append_prompt_with_all_params(self, async_client: AsyncOpencode) -> None:
        tui = await async_client.tui.append_prompt(
            text="text",
            directory="directory",
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
    async def test_method_clear_prompt(self, async_client: AsyncOpencode) -> None:
        tui = await async_client.tui.clear_prompt()
        assert_matches_type(TuiClearPromptResponse, tui, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_clear_prompt_with_all_params(self, async_client: AsyncOpencode) -> None:
        tui = await async_client.tui.clear_prompt(
            directory="directory",
        )
        assert_matches_type(TuiClearPromptResponse, tui, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_clear_prompt(self, async_client: AsyncOpencode) -> None:
        response = await async_client.tui.with_raw_response.clear_prompt()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tui = await response.parse()
        assert_matches_type(TuiClearPromptResponse, tui, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_clear_prompt(self, async_client: AsyncOpencode) -> None:
        async with async_client.tui.with_streaming_response.clear_prompt() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tui = await response.parse()
            assert_matches_type(TuiClearPromptResponse, tui, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_execute_command(self, async_client: AsyncOpencode) -> None:
        tui = await async_client.tui.execute_command(
            command="command",
        )
        assert_matches_type(TuiExecuteCommandResponse, tui, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_execute_command_with_all_params(self, async_client: AsyncOpencode) -> None:
        tui = await async_client.tui.execute_command(
            command="command",
            directory="directory",
        )
        assert_matches_type(TuiExecuteCommandResponse, tui, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_execute_command(self, async_client: AsyncOpencode) -> None:
        response = await async_client.tui.with_raw_response.execute_command(
            command="command",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tui = await response.parse()
        assert_matches_type(TuiExecuteCommandResponse, tui, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_execute_command(self, async_client: AsyncOpencode) -> None:
        async with async_client.tui.with_streaming_response.execute_command(
            command="command",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tui = await response.parse()
            assert_matches_type(TuiExecuteCommandResponse, tui, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_open_help(self, async_client: AsyncOpencode) -> None:
        tui = await async_client.tui.open_help()
        assert_matches_type(TuiOpenHelpResponse, tui, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_open_help_with_all_params(self, async_client: AsyncOpencode) -> None:
        tui = await async_client.tui.open_help(
            directory="directory",
        )
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

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_open_models(self, async_client: AsyncOpencode) -> None:
        tui = await async_client.tui.open_models()
        assert_matches_type(TuiOpenModelsResponse, tui, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_open_models_with_all_params(self, async_client: AsyncOpencode) -> None:
        tui = await async_client.tui.open_models(
            directory="directory",
        )
        assert_matches_type(TuiOpenModelsResponse, tui, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_open_models(self, async_client: AsyncOpencode) -> None:
        response = await async_client.tui.with_raw_response.open_models()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tui = await response.parse()
        assert_matches_type(TuiOpenModelsResponse, tui, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_open_models(self, async_client: AsyncOpencode) -> None:
        async with async_client.tui.with_streaming_response.open_models() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tui = await response.parse()
            assert_matches_type(TuiOpenModelsResponse, tui, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_open_sessions(self, async_client: AsyncOpencode) -> None:
        tui = await async_client.tui.open_sessions()
        assert_matches_type(TuiOpenSessionsResponse, tui, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_open_sessions_with_all_params(self, async_client: AsyncOpencode) -> None:
        tui = await async_client.tui.open_sessions(
            directory="directory",
        )
        assert_matches_type(TuiOpenSessionsResponse, tui, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_open_sessions(self, async_client: AsyncOpencode) -> None:
        response = await async_client.tui.with_raw_response.open_sessions()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tui = await response.parse()
        assert_matches_type(TuiOpenSessionsResponse, tui, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_open_sessions(self, async_client: AsyncOpencode) -> None:
        async with async_client.tui.with_streaming_response.open_sessions() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tui = await response.parse()
            assert_matches_type(TuiOpenSessionsResponse, tui, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_open_themes(self, async_client: AsyncOpencode) -> None:
        tui = await async_client.tui.open_themes()
        assert_matches_type(TuiOpenThemesResponse, tui, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_open_themes_with_all_params(self, async_client: AsyncOpencode) -> None:
        tui = await async_client.tui.open_themes(
            directory="directory",
        )
        assert_matches_type(TuiOpenThemesResponse, tui, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_open_themes(self, async_client: AsyncOpencode) -> None:
        response = await async_client.tui.with_raw_response.open_themes()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tui = await response.parse()
        assert_matches_type(TuiOpenThemesResponse, tui, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_open_themes(self, async_client: AsyncOpencode) -> None:
        async with async_client.tui.with_streaming_response.open_themes() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tui = await response.parse()
            assert_matches_type(TuiOpenThemesResponse, tui, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_show_toast(self, async_client: AsyncOpencode) -> None:
        tui = await async_client.tui.show_toast(
            message="message",
            variant="info",
        )
        assert_matches_type(TuiShowToastResponse, tui, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_show_toast_with_all_params(self, async_client: AsyncOpencode) -> None:
        tui = await async_client.tui.show_toast(
            message="message",
            variant="info",
            directory="directory",
            title="title",
        )
        assert_matches_type(TuiShowToastResponse, tui, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_show_toast(self, async_client: AsyncOpencode) -> None:
        response = await async_client.tui.with_raw_response.show_toast(
            message="message",
            variant="info",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tui = await response.parse()
        assert_matches_type(TuiShowToastResponse, tui, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_show_toast(self, async_client: AsyncOpencode) -> None:
        async with async_client.tui.with_streaming_response.show_toast(
            message="message",
            variant="info",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tui = await response.parse()
            assert_matches_type(TuiShowToastResponse, tui, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_submit_prompt(self, async_client: AsyncOpencode) -> None:
        tui = await async_client.tui.submit_prompt()
        assert_matches_type(TuiSubmitPromptResponse, tui, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_submit_prompt_with_all_params(self, async_client: AsyncOpencode) -> None:
        tui = await async_client.tui.submit_prompt(
            directory="directory",
        )
        assert_matches_type(TuiSubmitPromptResponse, tui, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_submit_prompt(self, async_client: AsyncOpencode) -> None:
        response = await async_client.tui.with_raw_response.submit_prompt()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tui = await response.parse()
        assert_matches_type(TuiSubmitPromptResponse, tui, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_submit_prompt(self, async_client: AsyncOpencode) -> None:
        async with async_client.tui.with_streaming_response.submit_prompt() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tui = await response.parse()
            assert_matches_type(TuiSubmitPromptResponse, tui, path=["response"])

        assert cast(Any, response.is_closed) is True
