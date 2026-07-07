# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os

import httpx
import pytest
from respx import MockRouter

from opencode_ai import Opencode, AsyncOpencode
from tests.utils import assert_matches_type
from opencode_ai.types import (
    VcsInfo,
    VcsDiffResponse,
    VcsApplyResponse,
    VcsStatusResponse,
)
from tests.wire_helpers import route_request, read_json_body

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")

VCS_INFO_SAMPLE: dict[str, object] = {"branch": "main", "default_branch": "main"}

VCS_FILE_STATUS_SAMPLE: dict[str, object] = {
    "file": "src/index.ts",
    "additions": 3,
    "deletions": 1,
    "status": "modified",
}

VCS_FILE_DIFF_SAMPLE: dict[str, object] = {
    "file": "src/index.ts",
    "patch": "@@ -1 +1 @@\n-old\n+new\n",
    "additions": 3,
    "deletions": 1,
    "status": "modified",
}

RAW_DIFF_TEXT = "diff --git a/src/index.ts b/src/index.ts\n@@ -1 +1 @@\n-old\n+new\n"


class TestVcsWire:
    @pytest.mark.respx(base_url=base_url)
    def test_get_wire_shape(self, client: Opencode, respx_mock: MockRouter) -> None:
        route = respx_mock.get("/vcs").mock(return_value=httpx.Response(200, json=VCS_INFO_SAMPLE))
        result = client.vcs.get()
        assert route.called
        request = route_request(route)
        assert request.method == "GET"
        assert_matches_type(VcsInfo, result, path=["response"])

    @pytest.mark.respx(base_url=base_url)
    def test_get_sends_directory_and_workspace_query_params(
        self, client: Opencode, respx_mock: MockRouter
    ) -> None:
        route = respx_mock.get("/vcs").mock(return_value=httpx.Response(200, json=VCS_INFO_SAMPLE))
        result = client.vcs.get(directory="/tmp/project", workspace="my-workspace")
        assert route.called
        request = route_request(route)
        assert dict(request.url.params) == {
            "directory": "/tmp/project",
            "workspace": "my-workspace",
        }
        assert_matches_type(VcsInfo, result, path=["response"])

    @pytest.mark.respx(base_url=base_url)
    def test_status_wire_shape(self, client: Opencode, respx_mock: MockRouter) -> None:
        route = respx_mock.get("/vcs/status").mock(return_value=httpx.Response(200, json=[VCS_FILE_STATUS_SAMPLE]))
        result = client.vcs.status()
        assert route.called
        request = route_request(route)
        assert request.method == "GET"
        assert_matches_type(VcsStatusResponse, result, path=["response"])

    @pytest.mark.respx(base_url=base_url)
    def test_diff_sends_query_params(self, client: Opencode, respx_mock: MockRouter) -> None:
        route = respx_mock.get("/vcs/diff").mock(return_value=httpx.Response(200, json=[VCS_FILE_DIFF_SAMPLE]))
        result = client.vcs.diff(mode="git", context=3)
        assert route.called
        request = route_request(route)
        assert dict(request.url.params) == {
            "mode": "git",
            "context": "3",
        }
        assert_matches_type(VcsDiffResponse, result, path=["response"])

    @pytest.mark.respx(base_url=base_url)
    def test_diff_raw_wire_shape(self, client: Opencode, respx_mock: MockRouter) -> None:
        route = respx_mock.get("/vcs/diff/raw").mock(
            return_value=httpx.Response(
                200,
                content=RAW_DIFF_TEXT.encode("utf-8"),
                headers={"content-type": "text/x-diff; charset=utf-8"},
            )
        )
        result = client.vcs.diff_raw()
        assert route.called
        request = route_request(route)
        assert request.method == "GET"
        assert isinstance(result, str)
        assert result == RAW_DIFF_TEXT

    @pytest.mark.respx(base_url=base_url)
    def test_apply_sends_body(self, client: Opencode, respx_mock: MockRouter) -> None:
        route = respx_mock.post("/vcs/apply").mock(return_value=httpx.Response(200, json={"applied": True}))
        result = client.vcs.apply(
            patch="@@ -1 +1 @@\n-old\n+new\n",
        )
        assert route.called
        request = route_request(route)
        assert request.method == "POST"
        body = read_json_body(route)
        assert body == {"patch": "@@ -1 +1 @@\n-old\n+new\n"}
        assert_matches_type(VcsApplyResponse, result, path=["response"])


class TestAsyncVcsWire:
    @pytest.mark.respx(base_url=base_url)
    async def test_get_wire_shape(self, async_client: AsyncOpencode, respx_mock: MockRouter) -> None:
        route = respx_mock.get("/vcs").mock(return_value=httpx.Response(200, json=VCS_INFO_SAMPLE))
        result = await async_client.vcs.get()
        assert route.called
        request = route_request(route)
        assert request.method == "GET"
        assert_matches_type(VcsInfo, result, path=["response"])

    @pytest.mark.respx(base_url=base_url)
    async def test_get_sends_directory_and_workspace_query_params(
        self, async_client: AsyncOpencode, respx_mock: MockRouter
    ) -> None:
        route = respx_mock.get("/vcs").mock(return_value=httpx.Response(200, json=VCS_INFO_SAMPLE))
        result = await async_client.vcs.get(directory="/tmp/project", workspace="my-workspace")
        assert route.called
        request = route_request(route)
        assert dict(request.url.params) == {
            "directory": "/tmp/project",
            "workspace": "my-workspace",
        }
        assert_matches_type(VcsInfo, result, path=["response"])

    @pytest.mark.respx(base_url=base_url)
    async def test_status_wire_shape(self, async_client: AsyncOpencode, respx_mock: MockRouter) -> None:
        route = respx_mock.get("/vcs/status").mock(return_value=httpx.Response(200, json=[VCS_FILE_STATUS_SAMPLE]))
        result = await async_client.vcs.status()
        assert route.called
        request = route_request(route)
        assert request.method == "GET"
        assert_matches_type(VcsStatusResponse, result, path=["response"])

    @pytest.mark.respx(base_url=base_url)
    async def test_diff_sends_query_params(self, async_client: AsyncOpencode, respx_mock: MockRouter) -> None:
        route = respx_mock.get("/vcs/diff").mock(return_value=httpx.Response(200, json=[VCS_FILE_DIFF_SAMPLE]))
        result = await async_client.vcs.diff(mode="git", context=3)
        assert route.called
        request = route_request(route)
        assert dict(request.url.params) == {
            "mode": "git",
            "context": "3",
        }
        assert_matches_type(VcsDiffResponse, result, path=["response"])

    @pytest.mark.respx(base_url=base_url)
    async def test_diff_raw_wire_shape(self, async_client: AsyncOpencode, respx_mock: MockRouter) -> None:
        route = respx_mock.get("/vcs/diff/raw").mock(
            return_value=httpx.Response(
                200,
                content=RAW_DIFF_TEXT.encode("utf-8"),
                headers={"content-type": "text/x-diff; charset=utf-8"},
            )
        )
        result = await async_client.vcs.diff_raw()
        assert route.called
        request = route_request(route)
        assert request.method == "GET"
        assert isinstance(result, str)
        assert result == RAW_DIFF_TEXT

    @pytest.mark.respx(base_url=base_url)
    async def test_apply_sends_body(self, async_client: AsyncOpencode, respx_mock: MockRouter) -> None:
        route = respx_mock.post("/vcs/apply").mock(return_value=httpx.Response(200, json={"applied": True}))
        result = await async_client.vcs.apply(
            patch="@@ -1 +1 @@\n-old\n+new\n",
        )
        assert route.called
        request = route_request(route)
        assert request.method == "POST"
        body = read_json_body(route)
        assert body == {"patch": "@@ -1 +1 @@\n-old\n+new\n"}
        assert_matches_type(VcsApplyResponse, result, path=["response"])
