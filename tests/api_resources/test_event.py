# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from opencode_ai import Opencode, AsyncOpencode

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEvent:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Opencode) -> None:
        event_stream = client.event.list()
        event_stream.response.close()

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Opencode) -> None:
        response = client.event.with_raw_response.list()

        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = response.parse()
        stream.close()

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Opencode) -> None:
        with client.event.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = response.parse()
            stream.close()

        assert cast(Any, response.is_closed) is True


class TestAsyncEvent:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncOpencode) -> None:
        event_stream = await async_client.event.list()
        await event_stream.response.aclose()

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncOpencode) -> None:
        response = await async_client.event.with_raw_response.list()

        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = await response.parse()
        await stream.close()

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncOpencode) -> None:
        async with async_client.event.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = await response.parse()
            await stream.close()

        assert cast(Any, response.is_closed) is True
