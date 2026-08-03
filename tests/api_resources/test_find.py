# Hand-maintained fork of the Stainless-era opencode SDK. Generated code was replaced by manual maintenance; see CONTRIBUTING.md.

from __future__ import annotations

import os
from typing import Any, cast

import httpx
import pytest
from respx import MockRouter

from opencode_ai import Opencode, AsyncOpencode
from tests.utils import assert_matches_type
from opencode_ai.types import (
    FindTextResponse,
    FindFilesResponse,
    FindSymbolsResponse,
)
from tests.wire_helpers import route_request

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFind:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_files(self, client: Opencode) -> None:
        find = client.find.files(
            query="query",
        )
        assert_matches_type(FindFilesResponse, find, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_files(self, client: Opencode) -> None:
        response = client.find.with_raw_response.files(
            query="query",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        find = response.parse()
        assert_matches_type(FindFilesResponse, find, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_files(self, client: Opencode) -> None:
        with client.find.with_streaming_response.files(
            query="query",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            find = response.parse()
            assert_matches_type(FindFilesResponse, find, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_symbols(self, client: Opencode) -> None:
        find = client.find.symbols(
            query="query",
        )
        assert_matches_type(FindSymbolsResponse, find, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_symbols(self, client: Opencode) -> None:
        response = client.find.with_raw_response.symbols(
            query="query",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        find = response.parse()
        assert_matches_type(FindSymbolsResponse, find, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_symbols(self, client: Opencode) -> None:
        with client.find.with_streaming_response.symbols(
            query="query",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            find = response.parse()
            assert_matches_type(FindSymbolsResponse, find, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_text(self, client: Opencode) -> None:
        find = client.find.text(
            pattern="pattern",
        )
        assert_matches_type(FindTextResponse, find, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_text(self, client: Opencode) -> None:
        response = client.find.with_raw_response.text(
            pattern="pattern",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        find = response.parse()
        assert_matches_type(FindTextResponse, find, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_text(self, client: Opencode) -> None:
        with client.find.with_streaming_response.text(
            pattern="pattern",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            find = response.parse()
            assert_matches_type(FindTextResponse, find, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestFindWire:
    @pytest.mark.respx(base_url=base_url)
    def test_files_sends_directory_and_workspace_query(self, client: Opencode, respx_mock: MockRouter) -> None:
        route = respx_mock.get("/find/file").mock(return_value=httpx.Response(200, json=[]))
        client.find.files(query="foo", directory="/repo", workspace="ws1")
        assert route_request(route).url.params.get("query") == "foo"
        assert route_request(route).url.params.get("directory") == "/repo"
        assert route_request(route).url.params.get("workspace") == "ws1"


class TestAsyncFind:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_files(self, async_client: AsyncOpencode) -> None:
        find = await async_client.find.files(
            query="query",
        )
        assert_matches_type(FindFilesResponse, find, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_files(self, async_client: AsyncOpencode) -> None:
        response = await async_client.find.with_raw_response.files(
            query="query",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        find = await response.parse()
        assert_matches_type(FindFilesResponse, find, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_files(self, async_client: AsyncOpencode) -> None:
        async with async_client.find.with_streaming_response.files(
            query="query",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            find = await response.parse()
            assert_matches_type(FindFilesResponse, find, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_symbols(self, async_client: AsyncOpencode) -> None:
        find = await async_client.find.symbols(
            query="query",
        )
        assert_matches_type(FindSymbolsResponse, find, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_symbols(self, async_client: AsyncOpencode) -> None:
        response = await async_client.find.with_raw_response.symbols(
            query="query",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        find = await response.parse()
        assert_matches_type(FindSymbolsResponse, find, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_symbols(self, async_client: AsyncOpencode) -> None:
        async with async_client.find.with_streaming_response.symbols(
            query="query",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            find = await response.parse()
            assert_matches_type(FindSymbolsResponse, find, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_text(self, async_client: AsyncOpencode) -> None:
        find = await async_client.find.text(
            pattern="pattern",
        )
        assert_matches_type(FindTextResponse, find, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_text(self, async_client: AsyncOpencode) -> None:
        response = await async_client.find.with_raw_response.text(
            pattern="pattern",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        find = await response.parse()
        assert_matches_type(FindTextResponse, find, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_text(self, async_client: AsyncOpencode) -> None:
        async with async_client.find.with_streaming_response.text(
            pattern="pattern",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            find = await response.parse()
            assert_matches_type(FindTextResponse, find, path=["response"])

        assert cast(Any, response.is_closed) is True
