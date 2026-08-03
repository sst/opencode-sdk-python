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
    Project,
    ProjectListResponse,
    ProjectDirectoriesResponse,
)
from tests.wire_helpers import route_request, read_json_body

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")

PROJECT_SAMPLE: dict[str, object] = {
    "id": "prj_1",
    "worktree": "/repo",
    "time": {"created": 0, "updated": 0},
    "sandboxes": [],
}


class TestProject:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Opencode) -> None:
        project = client.project.list()
        assert_matches_type(ProjectListResponse, project, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Opencode) -> None:
        response = client.project.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = response.parse()
        assert_matches_type(ProjectListResponse, project, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Opencode) -> None:
        with client.project.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = response.parse()
            assert_matches_type(ProjectListResponse, project, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: Opencode) -> None:
        project = client.project.update(
            project_id="projectID",
        )
        assert_matches_type(Project, project, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Opencode) -> None:
        project = client.project.update(
            project_id="projectID",
            commands={"start": "start"},
            icon={
                "color": "color",
                "override": "override",
                "url": "url",
            },
            name="name",
        )
        assert_matches_type(Project, project, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Opencode) -> None:
        response = client.project.with_raw_response.update(
            project_id="projectID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = response.parse()
        assert_matches_type(Project, project, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Opencode) -> None:
        with client.project.with_streaming_response.update(
            project_id="projectID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = response.parse()
            assert_matches_type(Project, project, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Opencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.project.with_raw_response.update(
                project_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_current(self, client: Opencode) -> None:
        project = client.project.current()
        assert_matches_type(Project, project, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_current(self, client: Opencode) -> None:
        response = client.project.with_raw_response.current()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = response.parse()
        assert_matches_type(Project, project, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_current(self, client: Opencode) -> None:
        with client.project.with_streaming_response.current() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = response.parse()
            assert_matches_type(Project, project, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_directories(self, client: Opencode) -> None:
        project = client.project.directories(
            "projectID",
        )
        assert_matches_type(ProjectDirectoriesResponse, project, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_directories(self, client: Opencode) -> None:
        response = client.project.with_raw_response.directories(
            "projectID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = response.parse()
        assert_matches_type(ProjectDirectoriesResponse, project, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_directories(self, client: Opencode) -> None:
        with client.project.with_streaming_response.directories(
            "projectID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = response.parse()
            assert_matches_type(ProjectDirectoriesResponse, project, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_directories(self, client: Opencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.project.with_raw_response.directories(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_init_git(self, client: Opencode) -> None:
        project = client.project.init_git()
        assert_matches_type(Project, project, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_init_git(self, client: Opencode) -> None:
        response = client.project.with_raw_response.init_git()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = response.parse()
        assert_matches_type(Project, project, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_init_git(self, client: Opencode) -> None:
        with client.project.with_streaming_response.init_git() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = response.parse()
            assert_matches_type(Project, project, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestProjectWire:
    @pytest.mark.respx(base_url=base_url)
    def test_list_wire_shape(self, client: Opencode, respx_mock: MockRouter) -> None:
        route = respx_mock.get("/project").mock(return_value=httpx.Response(200, json=[PROJECT_SAMPLE]))
        result = client.project.list()
        assert route.called
        assert route.calls.last.request.method == "GET"
        assert_matches_type(ProjectListResponse, result, path=["response"])

    @pytest.mark.respx(base_url=base_url)
    def test_current_wire_shape(self, client: Opencode, respx_mock: MockRouter) -> None:
        route = respx_mock.get("/project/current").mock(return_value=httpx.Response(200, json=PROJECT_SAMPLE))
        result = client.project.current()
        assert route.called
        assert route.calls.last.request.method == "GET"
        assert_matches_type(Project, result, path=["response"])

    @pytest.mark.respx(base_url=base_url)
    def test_init_git_wire_shape(self, client: Opencode, respx_mock: MockRouter) -> None:
        route = respx_mock.post("/project/git/init").mock(return_value=httpx.Response(200, json=PROJECT_SAMPLE))
        result = client.project.init_git()
        assert route.called
        assert route.calls.last.request.method == "POST"
        assert_matches_type(Project, result, path=["response"])

    @pytest.mark.respx(base_url=base_url)
    def test_directories_wire_shape(self, client: Opencode, respx_mock: MockRouter) -> None:
        route = respx_mock.get("/project/prj_1/directories").mock(
            return_value=httpx.Response(200, json=["/repo", "/repo/sub"])
        )
        result = client.project.directories("prj_1")
        assert route.called
        assert route.calls.last.request.method == "GET"
        assert_matches_type(ProjectDirectoriesResponse, result, path=["response"])

    @pytest.mark.respx(base_url=base_url)
    def test_update_sends_body(self, client: Opencode, respx_mock: MockRouter) -> None:
        route = respx_mock.patch("/project/prj_1").mock(return_value=httpx.Response(200, json=PROJECT_SAMPLE))
        result = client.project.update(
            project_id="prj_1",
            name="new name",
            icon={"color": "red", "override": "override", "url": "https://example.com/icon.png"},
            commands={"start": "npm start"},
        )
        assert route.called
        request = route_request(route)
        assert request.method == "PATCH"
        body = read_json_body(route)
        assert body == {
            "name": "new name",
            "icon": {"color": "red", "override": "override", "url": "https://example.com/icon.png"},
            "commands": {"start": "npm start"},
        }
        assert_matches_type(Project, result, path=["response"])


class TestAsyncProject:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncOpencode) -> None:
        project = await async_client.project.list()
        assert_matches_type(ProjectListResponse, project, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncOpencode) -> None:
        response = await async_client.project.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = await response.parse()
        assert_matches_type(ProjectListResponse, project, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncOpencode) -> None:
        async with async_client.project.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = await response.parse()
            assert_matches_type(ProjectListResponse, project, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncOpencode) -> None:
        project = await async_client.project.update(
            project_id="projectID",
        )
        assert_matches_type(Project, project, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncOpencode) -> None:
        project = await async_client.project.update(
            project_id="projectID",
            commands={"start": "start"},
            icon={
                "color": "color",
                "override": "override",
                "url": "url",
            },
            name="name",
        )
        assert_matches_type(Project, project, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncOpencode) -> None:
        response = await async_client.project.with_raw_response.update(
            project_id="projectID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = await response.parse()
        assert_matches_type(Project, project, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncOpencode) -> None:
        async with async_client.project.with_streaming_response.update(
            project_id="projectID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = await response.parse()
            assert_matches_type(Project, project, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncOpencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.project.with_raw_response.update(
                project_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_current(self, async_client: AsyncOpencode) -> None:
        project = await async_client.project.current()
        assert_matches_type(Project, project, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_current(self, async_client: AsyncOpencode) -> None:
        response = await async_client.project.with_raw_response.current()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = await response.parse()
        assert_matches_type(Project, project, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_current(self, async_client: AsyncOpencode) -> None:
        async with async_client.project.with_streaming_response.current() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = await response.parse()
            assert_matches_type(Project, project, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_directories(self, async_client: AsyncOpencode) -> None:
        project = await async_client.project.directories(
            "projectID",
        )
        assert_matches_type(ProjectDirectoriesResponse, project, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_directories(self, async_client: AsyncOpencode) -> None:
        response = await async_client.project.with_raw_response.directories(
            "projectID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = await response.parse()
        assert_matches_type(ProjectDirectoriesResponse, project, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_directories(self, async_client: AsyncOpencode) -> None:
        async with async_client.project.with_streaming_response.directories(
            "projectID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = await response.parse()
            assert_matches_type(ProjectDirectoriesResponse, project, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_directories(self, async_client: AsyncOpencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.project.with_raw_response.directories(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_init_git(self, async_client: AsyncOpencode) -> None:
        project = await async_client.project.init_git()
        assert_matches_type(Project, project, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_init_git(self, async_client: AsyncOpencode) -> None:
        response = await async_client.project.with_raw_response.init_git()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = await response.parse()
        assert_matches_type(Project, project, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_init_git(self, async_client: AsyncOpencode) -> None:
        async with async_client.project.with_streaming_response.init_git() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = await response.parse()
            assert_matches_type(Project, project, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncProjectWire:
    @pytest.mark.respx(base_url=base_url)
    async def test_list_wire_shape(self, async_client: AsyncOpencode, respx_mock: MockRouter) -> None:
        route = respx_mock.get("/project").mock(return_value=httpx.Response(200, json=[PROJECT_SAMPLE]))
        result = await async_client.project.list()
        assert route.called
        assert route.calls.last.request.method == "GET"
        assert_matches_type(ProjectListResponse, result, path=["response"])

    @pytest.mark.respx(base_url=base_url)
    async def test_update_sends_body(self, async_client: AsyncOpencode, respx_mock: MockRouter) -> None:
        route = respx_mock.patch("/project/prj_1").mock(return_value=httpx.Response(200, json=PROJECT_SAMPLE))
        result = await async_client.project.update(
            project_id="prj_1",
            name="new name",
        )
        assert route.called
        body = read_json_body(route)
        assert body == {"name": "new name"}
        assert_matches_type(Project, result, path=["response"])
