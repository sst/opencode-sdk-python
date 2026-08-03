# Hand-maintained fork of the Stainless-era opencode SDK. Generated code was replaced by manual maintenance; see CONTRIBUTING.md.

from __future__ import annotations

import os
from typing import Any, cast

import httpx
import pytest
from respx import MockRouter

from opencode_ai import Opencode, AsyncOpencode
from tests.utils import assert_matches_type
from opencode_ai.types import AppLogResponse, AppAgentsResponse, AppSkillsResponse, AppProvidersResponse
from tests.wire_helpers import route_request

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestApp:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_log(self, client: Opencode) -> None:
        app = client.app.log(
            level="debug",
            message="message",
            service="service",
        )
        assert_matches_type(AppLogResponse, app, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_log_with_all_params(self, client: Opencode) -> None:
        app = client.app.log(
            level="debug",
            message="message",
            service="service",
            extra={"foo": "bar"},
        )
        assert_matches_type(AppLogResponse, app, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_log(self, client: Opencode) -> None:
        response = client.app.with_raw_response.log(
            level="debug",
            message="message",
            service="service",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app = response.parse()
        assert_matches_type(AppLogResponse, app, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_log(self, client: Opencode) -> None:
        with client.app.with_streaming_response.log(
            level="debug",
            message="message",
            service="service",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app = response.parse()
            assert_matches_type(AppLogResponse, app, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_providers(self, client: Opencode) -> None:
        app = client.app.providers()
        assert_matches_type(AppProvidersResponse, app, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_providers(self, client: Opencode) -> None:
        response = client.app.with_raw_response.providers()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app = response.parse()
        assert_matches_type(AppProvidersResponse, app, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_providers(self, client: Opencode) -> None:
        with client.app.with_streaming_response.providers() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app = response.parse()
            assert_matches_type(AppProvidersResponse, app, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncApp:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_log(self, async_client: AsyncOpencode) -> None:
        app = await async_client.app.log(
            level="debug",
            message="message",
            service="service",
        )
        assert_matches_type(AppLogResponse, app, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_log_with_all_params(self, async_client: AsyncOpencode) -> None:
        app = await async_client.app.log(
            level="debug",
            message="message",
            service="service",
            extra={"foo": "bar"},
        )
        assert_matches_type(AppLogResponse, app, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_log(self, async_client: AsyncOpencode) -> None:
        response = await async_client.app.with_raw_response.log(
            level="debug",
            message="message",
            service="service",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app = await response.parse()
        assert_matches_type(AppLogResponse, app, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_log(self, async_client: AsyncOpencode) -> None:
        async with async_client.app.with_streaming_response.log(
            level="debug",
            message="message",
            service="service",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app = await response.parse()
            assert_matches_type(AppLogResponse, app, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_providers(self, async_client: AsyncOpencode) -> None:
        app = await async_client.app.providers()
        assert_matches_type(AppProvidersResponse, app, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_providers(self, async_client: AsyncOpencode) -> None:
        response = await async_client.app.with_raw_response.providers()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app = await response.parse()
        assert_matches_type(AppProvidersResponse, app, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_providers(self, async_client: AsyncOpencode) -> None:
        async with async_client.app.with_streaming_response.providers() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app = await response.parse()
            assert_matches_type(AppProvidersResponse, app, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAppWire:
    @pytest.mark.respx(base_url=base_url)
    def test_agents_hits_agent_path(self, client: Opencode, respx_mock: MockRouter) -> None:
        route = respx_mock.get("/agent").mock(return_value=httpx.Response(200, json=[]))
        result = client.app.agents()
        assert route_request(route).url.path == "/agent"
        assert_matches_type(AppAgentsResponse, result, path=["response"])

    @pytest.mark.respx(base_url=base_url)
    def test_agents_sends_directory_and_workspace_query(self, client: Opencode, respx_mock: MockRouter) -> None:
        route = respx_mock.get("/agent").mock(return_value=httpx.Response(200, json=[]))
        client.app.agents(directory="/repo", workspace="ws1")
        assert route_request(route).url.params.get("directory") == "/repo"
        assert route_request(route).url.params.get("workspace") == "ws1"

    @pytest.mark.respx(base_url=base_url)
    def test_skills_hits_skill_path(self, client: Opencode, respx_mock: MockRouter) -> None:
        route = respx_mock.get("/skill").mock(return_value=httpx.Response(200, json=[]))
        result = client.app.skills()
        assert route_request(route).url.path == "/skill"
        assert_matches_type(AppSkillsResponse, result, path=["response"])

    def test_removed_methods(self, client: Opencode) -> None:
        assert not hasattr(client.app, "get")
        assert not hasattr(client.app, "init")
        assert not hasattr(client.app, "modes")
