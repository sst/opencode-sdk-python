# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from opencode_ai import Opencode, AsyncOpencode
from tests.utils import assert_matches_type
from opencode_ai.types import Config, ConfigProvidersResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestConfig:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: Opencode) -> None:
        config = client.config.get()
        assert_matches_type(Config, config, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: Opencode) -> None:
        response = client.config.with_raw_response.get()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config = response.parse()
        assert_matches_type(Config, config, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: Opencode) -> None:
        with client.config.with_streaming_response.get() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config = response.parse()
            assert_matches_type(Config, config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_providers(self, client: Opencode) -> None:
        config = client.config.providers()
        assert_matches_type(ConfigProvidersResponse, config, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_providers(self, client: Opencode) -> None:
        response = client.config.with_raw_response.providers()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config = response.parse()
        assert_matches_type(ConfigProvidersResponse, config, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_providers(self, client: Opencode) -> None:
        with client.config.with_streaming_response.providers() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config = response.parse()
            assert_matches_type(ConfigProvidersResponse, config, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncConfig:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncOpencode) -> None:
        config = await async_client.config.get()
        assert_matches_type(Config, config, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncOpencode) -> None:
        response = await async_client.config.with_raw_response.get()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config = await response.parse()
        assert_matches_type(Config, config, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncOpencode) -> None:
        async with async_client.config.with_streaming_response.get() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config = await response.parse()
            assert_matches_type(Config, config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_providers(self, async_client: AsyncOpencode) -> None:
        config = await async_client.config.providers()
        assert_matches_type(ConfigProvidersResponse, config, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_providers(self, async_client: AsyncOpencode) -> None:
        response = await async_client.config.with_raw_response.providers()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config = await response.parse()
        assert_matches_type(ConfigProvidersResponse, config, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_providers(self, async_client: AsyncOpencode) -> None:
        async with async_client.config.with_streaming_response.providers() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config = await response.parse()
            assert_matches_type(ConfigProvidersResponse, config, path=["response"])

        assert cast(Any, response.is_closed) is True
