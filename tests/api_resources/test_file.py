# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from opencode import Opencode, AsyncOpencode
from tests.utils import assert_matches_type
from opencode.types import FileSearchResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFile:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_search(self, client: Opencode) -> None:
        file = client.file.search(
            query="query",
        )
        assert_matches_type(FileSearchResponse, file, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_search(self, client: Opencode) -> None:
        response = client.file.with_raw_response.search(
            query="query",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(FileSearchResponse, file, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_search(self, client: Opencode) -> None:
        with client.file.with_streaming_response.search(
            query="query",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(FileSearchResponse, file, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncFile:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip()
    @parametrize
    async def test_method_search(self, async_client: AsyncOpencode) -> None:
        file = await async_client.file.search(
            query="query",
        )
        assert_matches_type(FileSearchResponse, file, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_search(self, async_client: AsyncOpencode) -> None:
        response = await async_client.file.with_raw_response.search(
            query="query",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert_matches_type(FileSearchResponse, file, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_search(self, async_client: AsyncOpencode) -> None:
        async with async_client.file.with_streaming_response.search(
            query="query",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(FileSearchResponse, file, path=["response"])

        assert cast(Any, response.is_closed) is True
