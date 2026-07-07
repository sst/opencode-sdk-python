# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import httpx
import pytest
from respx import MockRouter

from opencode_ai import Opencode, AsyncOpencode
from tests.utils import assert_matches_type
from opencode_ai.types import FileListResponse, FileStatusResponse, FileContentResponse
from tests.wire_helpers import route_request
from opencode_ai.types.file_list_response import FileNode

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFile:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Opencode) -> None:
        file = client.file.list(
            path="path",
        )
        assert_matches_type(FileListResponse, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Opencode) -> None:
        response = client.file.with_raw_response.list(
            path="path",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(FileListResponse, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Opencode) -> None:
        with client.file.with_streaming_response.list(
            path="path",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(FileListResponse, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_content(self, client: Opencode) -> None:
        file = client.file.content(
            path="path",
        )
        assert_matches_type(FileContentResponse, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_content(self, client: Opencode) -> None:
        response = client.file.with_raw_response.content(
            path="path",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(FileContentResponse, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_content(self, client: Opencode) -> None:
        with client.file.with_streaming_response.content(
            path="path",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(FileContentResponse, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_status(self, client: Opencode) -> None:
        file = client.file.status()
        assert_matches_type(FileStatusResponse, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_status(self, client: Opencode) -> None:
        response = client.file.with_raw_response.status()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(FileStatusResponse, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_status(self, client: Opencode) -> None:
        with client.file.with_streaming_response.status() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(FileStatusResponse, file, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncFile:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncOpencode) -> None:
        file = await async_client.file.list(
            path="path",
        )
        assert_matches_type(FileListResponse, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncOpencode) -> None:
        response = await async_client.file.with_raw_response.list(
            path="path",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert_matches_type(FileListResponse, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncOpencode) -> None:
        async with async_client.file.with_streaming_response.list(
            path="path",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(FileListResponse, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_content(self, async_client: AsyncOpencode) -> None:
        file = await async_client.file.content(
            path="path",
        )
        assert_matches_type(FileContentResponse, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_content(self, async_client: AsyncOpencode) -> None:
        response = await async_client.file.with_raw_response.content(
            path="path",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert_matches_type(FileContentResponse, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_content(self, async_client: AsyncOpencode) -> None:
        async with async_client.file.with_streaming_response.content(
            path="path",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(FileContentResponse, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_status(self, async_client: AsyncOpencode) -> None:
        file = await async_client.file.status()
        assert_matches_type(FileStatusResponse, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_status(self, async_client: AsyncOpencode) -> None:
        response = await async_client.file.with_raw_response.status()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert_matches_type(FileStatusResponse, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_status(self, async_client: AsyncOpencode) -> None:
        async with async_client.file.with_streaming_response.status() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(FileStatusResponse, file, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestFileWire:
    @pytest.mark.respx(base_url=base_url)
    def test_list_hits_file_path_and_returns_array(self, client: Opencode, respx_mock: MockRouter) -> None:
        route = respx_mock.get("/file").mock(
            return_value=httpx.Response(
                200,
                json=[
                    {
                        "name": "a.py",
                        "path": "a.py",
                        "absolute": "/repo/a.py",
                        "type": "file",
                        "ignored": False,
                    }
                ],
            )
        )
        result = client.file.list(path="src")
        assert route_request(route).url.params.get("path") == "src"
        assert_matches_type(FileListResponse, result, path=["response"])
        assert isinstance(result[0], FileNode)

    @pytest.mark.respx(base_url=base_url)
    def test_content_hits_file_content_path(self, client: Opencode, respx_mock: MockRouter) -> None:
        route = respx_mock.get("/file/content").mock(
            return_value=httpx.Response(200, json={"content": "x", "type": "text"})
        )
        result = client.file.content(path="a.py")
        assert route_request(route).url.path == "/file/content"
        assert route_request(route).url.params.get("path") == "a.py"
        assert_matches_type(FileContentResponse, result, path=["response"])

    @pytest.mark.respx(base_url=base_url)
    def test_status_sends_directory_and_workspace_query(self, client: Opencode, respx_mock: MockRouter) -> None:
        route = respx_mock.get("/file/status").mock(return_value=httpx.Response(200, json=[]))
        client.file.status(directory="/repo", workspace="ws1")
        assert route_request(route).url.params.get("directory") == "/repo"
        assert route_request(route).url.params.get("workspace") == "ws1"

    def test_read_is_removed(self, client: Opencode) -> None:
        assert not hasattr(client.file, "read")
