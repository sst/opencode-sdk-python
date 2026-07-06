# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
import json
from typing import Any, cast

import httpx
import pytest

from respx import MockRouter

from opencode_ai import Opencode, AsyncOpencode
from tests.utils import assert_matches_type
from opencode_ai.types import Config

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestConfig:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get(self, client: Opencode) -> None:
        config = client.config.get()
        assert_matches_type(Config, config, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get(self, client: Opencode) -> None:
        response = client.config.with_raw_response.get()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config = response.parse()
        assert_matches_type(Config, config, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get(self, client: Opencode) -> None:
        with client.config.with_streaming_response.get() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config = response.parse()
            assert_matches_type(Config, config, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestConfigWire:
    @pytest.mark.respx(base_url=base_url)
    def test_get_wire_shape(self, client: Opencode, respx_mock: MockRouter) -> None:
        route = respx_mock.get("/config").mock(return_value=httpx.Response(200, json={}))
        client.config.get()
        assert route.called
        assert route.calls.last.request.method == "GET"

    @pytest.mark.respx(base_url=base_url)
    def test_update_wire_shape(self, client: Opencode, respx_mock: MockRouter) -> None:
        route = respx_mock.patch("/config").mock(return_value=httpx.Response(200, json={"theme": "dark"}))
        config = client.config.update(
            theme="dark",
            model="anthropic/claude-2",
            share="manual",
            disabled_providers=["openai"],
            keybinds={
                "app_exit": "ctrl+c",
                "app_help": "?",
                "editor_open": "e",
                "file_close": "esc",
                "file_diff_toggle": "d",
                "file_list": "f",
                "file_search": "/",
                "input_clear": "ctrl+u",
                "input_newline": "shift+enter",
                "input_paste": "ctrl+v",
                "input_submit": "enter",
                "leader": "ctrl+x",
                "messages_copy": "c",
                "messages_first": "g",
                "messages_half_page_down": "ctrl+d",
                "messages_half_page_up": "ctrl+u",
                "messages_last": "G",
                "messages_layout_toggle": "l",
                "messages_next": "j",
                "messages_page_down": "ctrl+f",
                "messages_page_up": "ctrl+b",
                "messages_previous": "k",
                "messages_redo": "ctrl+r",
                "messages_revert": "u",
                "messages_undo": "u",
                "model_list": "m",
                "project_init": "i",
                "session_compact": "c",
                "session_export": "x",
                "session_interrupt": "ctrl+c",
                "session_list": "l",
                "session_new": "n",
                "session_share": "s",
                "session_unshare": "S",
                "switch_mode": "tab",
                "switch_mode_reverse": "shift+tab",
                "theme_list": "t",
                "tool_details": "T",
            },
            mcp={
                "local-server": {
                    "type": "local",
                    "command": ["node", "server.js"],
                    "enabled": True,
                },
                "remote-server": {
                    "type": "remote",
                    "url": "https://example.com/mcp",
                    "oauth": False,
                },
            },
        )
        assert route.called
        request = route.calls.last.request
        assert request.method == "PATCH"
        body = json.loads(request.content)
        assert body["theme"] == "dark"
        assert body["model"] == "anthropic/claude-2"
        assert body["share"] == "manual"
        assert body["disabled_providers"] == ["openai"]
        assert body["keybinds"]["model_list"] == "m"
        assert body["mcp"]["local-server"]["command"] == ["node", "server.js"]
        assert body["mcp"]["remote-server"]["oauth"] is False
        assert_matches_type(Config, config, path=["response"])


class TestAsyncConfig:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get(self, async_client: AsyncOpencode) -> None:
        config = await async_client.config.get()
        assert_matches_type(Config, config, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncOpencode) -> None:
        response = await async_client.config.with_raw_response.get()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config = await response.parse()
        assert_matches_type(Config, config, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncOpencode) -> None:
        async with async_client.config.with_streaming_response.get() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config = await response.parse()
            assert_matches_type(Config, config, path=["response"])

        assert cast(Any, response.is_closed) is True
