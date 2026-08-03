# Hand-maintained fork of the Stainless-era opencode SDK. Generated code was replaced by manual maintenance; see CONTRIBUTING.md.

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
from opencode_ai._models import construct_type

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
    def test_get_sends_directory_and_workspace_query(self, client: Opencode, respx_mock: MockRouter) -> None:
        route = respx_mock.get("/config").mock(return_value=httpx.Response(200, json={}))
        client.config.get(directory="/repo", workspace="ws1")
        params = route.calls.last.request.url.params
        assert params.get("directory") == "/repo"
        assert params.get("workspace") == "ws1"

    @pytest.mark.respx(base_url=base_url)
    def test_update_wire_shape(self, client: Opencode, respx_mock: MockRouter) -> None:
        route = respx_mock.patch("/config").mock(return_value=httpx.Response(200, json={"username": "sam"}))
        config = client.config.update(
            username="sam",
            model="anthropic/claude-2",
            share="manual",
            disabled_providers=["openai"],
            shell="/bin/bash",
            log_level="INFO",
            server={
                "port": 4096,
                "hostname": "127.0.0.1",
            },
            permission="ask",
            agent={
                "general": {
                    "description": "General purpose agent",
                    "model": "anthropic/claude-2",
                    "permission": {
                        "bash": "allow",
                        "edit": "ask",
                    },
                },
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
                "disabled-server": {
                    "enabled": False,
                },
            },
        )
        assert route.called
        request = route.calls.last.request
        assert request.method == "PATCH"
        body = json.loads(request.content)
        assert body["username"] == "sam"
        assert body["model"] == "anthropic/claude-2"
        assert body["share"] == "manual"
        assert body["disabled_providers"] == ["openai"]
        assert body["shell"] == "/bin/bash"
        assert body["logLevel"] == "INFO"
        assert body["server"]["port"] == 4096
        assert body["permission"] == "ask"
        assert body["agent"]["general"]["permission"]["bash"] == "allow"
        assert body["mcp"]["local-server"]["command"] == ["node", "server.js"]
        assert body["mcp"]["remote-server"]["oauth"] is False
        assert body["mcp"]["disabled-server"]["enabled"] is False
        assert_matches_type(Config, config, path=["response"])


def test_config_subagent_depth() -> None:
    config = cast(Config, construct_type(type_=Config, value={"subagent_depth": 4}))
    assert config.subagent_depth == 4

    config_missing = cast(Config, construct_type(type_=Config, value={}))
    assert config_missing.subagent_depth is None


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
