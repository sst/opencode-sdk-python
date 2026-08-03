# Contract tests for the experimental resource (16 operations, sync + async).
# The resource is constructed directly because client.experimental wiring is task-7's.
from __future__ import annotations

import httpx
import pytest
from respx import MockRouter

from opencode_ai import Opencode, AsyncOpencode
from tests.wire_helpers import route_request, read_json_body
from opencode_ai.resources.experimental import ExperimentalResource, AsyncExperimentalResource

base_url = "http://127.0.0.1:4010"

WORKSPACE_PAYLOAD = {
    "id": "wrk_x",
    "type": "local",
    "name": "my workspace",
    "projectID": "prj_x",
    "timeUsed": 1.0,
}


@pytest.fixture
def experimental(client: Opencode) -> ExperimentalResource:
    return ExperimentalResource(client)


@pytest.fixture
def async_experimental(async_client: AsyncOpencode) -> AsyncExperimentalResource:
    return AsyncExperimentalResource(async_client)


class TestExperimentalWire:
    @pytest.mark.respx(base_url=base_url)
    def test_capabilities_get(self, experimental: ExperimentalResource, respx_mock: MockRouter) -> None:
        route = respx_mock.get("/experimental/capabilities").mock(
            return_value=httpx.Response(200, json={"backgroundSubagents": True})
        )
        result = experimental.capabilities_get(directory="/tmp/proj", workspace="wrk_ws")
        assert route.called
        request = route_request(route)
        assert request.method == "GET"
        assert request.url.path == "/experimental/capabilities"
        assert request.url.params["directory"] == "/tmp/proj"
        assert request.url.params["workspace"] == "wrk_ws"
        assert result.background_subagents is True

    @pytest.mark.respx(base_url=base_url)
    def test_console_get(self, experimental: ExperimentalResource, respx_mock: MockRouter) -> None:
        route = respx_mock.get("/experimental/console").mock(
            return_value=httpx.Response(
                200,
                json={"consoleManagedProviders": ["acct_x"], "activeOrgName": "org_x", "switchableOrgCount": 2},
            )
        )
        result = experimental.console_get(directory="/tmp/proj", workspace="wrk_ws")
        assert route.called
        request = route_request(route)
        assert request.method == "GET"
        assert request.url.path == "/experimental/console"
        assert request.url.params["directory"] == "/tmp/proj"
        assert request.url.params["workspace"] == "wrk_ws"
        assert result.console_managed_providers == ["acct_x"]
        assert result.active_org_name == "org_x"
        assert result.switchable_org_count == 2

    @pytest.mark.respx(base_url=base_url)
    def test_console_list_orgs(self, experimental: ExperimentalResource, respx_mock: MockRouter) -> None:
        route = respx_mock.get("/experimental/console/orgs").mock(
            return_value=httpx.Response(
                200,
                json={
                    "orgs": [
                        {
                            "accountID": "acct_x",
                            "accountEmail": "a@x.dev",
                            "accountUrl": "https://x.dev",
                            "orgID": "org_x",
                            "orgName": "Org X",
                            "active": True,
                        }
                    ]
                },
            )
        )
        result = experimental.console_list_orgs(directory="/tmp/proj", workspace="wrk_ws")
        assert route.called
        request = route_request(route)
        assert request.method == "GET"
        assert request.url.path == "/experimental/console/orgs"
        assert request.url.params["directory"] == "/tmp/proj"
        assert request.url.params["workspace"] == "wrk_ws"
        assert result.orgs[0].org_id == "org_x"
        assert result.orgs[0].org_name == "Org X"
        assert result.orgs[0].active is True

    @pytest.mark.respx(base_url=base_url)
    def test_console_switch_org(self, experimental: ExperimentalResource, respx_mock: MockRouter) -> None:
        route = respx_mock.post("/experimental/console/switch").mock(return_value=httpx.Response(200, json=True))
        result = experimental.console_switch_org(
            account_id="acct_x", org_id="org_x", directory="/tmp/proj", workspace="wrk_ws"
        )
        assert route.called
        request = route_request(route)
        assert request.method == "POST"
        assert request.url.path == "/experimental/console/switch"
        assert request.url.params["directory"] == "/tmp/proj"
        assert request.url.params["workspace"] == "wrk_ws"
        body = read_json_body(route)
        assert body["accountID"] == "acct_x"
        assert body["orgID"] == "org_x"
        assert result is True

    @pytest.mark.respx(base_url=base_url)
    def test_session_list(self, experimental: ExperimentalResource, respx_mock: MockRouter) -> None:
        route = respx_mock.get("/experimental/session").mock(
            return_value=httpx.Response(
                200,
                json=[
                    {
                        "id": "ses_x",
                        "slug": "s1",
                        "projectID": "prj_x",
                        "directory": "/tmp/proj",
                        "title": "T",
                        "version": "1",
                        "time": {"created": 1, "updated": 2},
                        "project": {"id": "prj_x", "worktree": "wt_x"},
                    }
                ],
            )
        )
        result = experimental.session_list(
            roots=True,
            start=0,
            cursor=5,
            search="foo",
            limit=10,
            archived=False,
            directory="/tmp/proj",
            workspace="wrk_ws",
        )
        assert route.called
        request = route_request(route)
        assert request.method == "GET"
        assert request.url.path == "/experimental/session"
        assert request.url.params["roots"] == "true"
        assert request.url.params["start"] == "0"
        assert request.url.params["cursor"] == "5"
        assert request.url.params["search"] == "foo"
        assert request.url.params["limit"] == "10"
        assert request.url.params["archived"] == "false"
        assert request.url.params["directory"] == "/tmp/proj"
        assert request.url.params["workspace"] == "wrk_ws"
        assert result[0].id == "ses_x"
        assert result[0].project_id == "prj_x"

    @pytest.mark.respx(base_url=base_url)
    def test_session_background(self, experimental: ExperimentalResource, respx_mock: MockRouter) -> None:
        route = respx_mock.post("/experimental/session/ses_x/background").mock(
            return_value=httpx.Response(200, json=True)
        )
        result = experimental.session_background("ses_x", directory="/tmp/proj", workspace="wrk_ws")
        assert route.called
        request = route_request(route)
        assert request.method == "POST"
        assert request.url.path == "/experimental/session/ses_x/background"
        assert request.url.params["directory"] == "/tmp/proj"
        assert request.url.params["workspace"] == "wrk_ws"
        assert result is True

    @pytest.mark.respx(base_url=base_url)
    def test_resource_list(self, experimental: ExperimentalResource, respx_mock: MockRouter) -> None:
        route = respx_mock.get("/experimental/resource").mock(
            return_value=httpx.Response(
                200,
                json={"res://x": {"name": "n", "uri": "res://x", "client": "c", "mimeType": "text/plain"}},
            )
        )
        result = experimental.resource_list(directory="/tmp/proj", workspace="wrk_ws")
        assert route.called
        request = route_request(route)
        assert request.method == "GET"
        assert request.url.path == "/experimental/resource"
        assert request.url.params["directory"] == "/tmp/proj"
        assert request.url.params["workspace"] == "wrk_ws"
        assert result["res://x"].name == "n"
        assert result["res://x"].mime_type == "text/plain"

    @pytest.mark.respx(base_url=base_url)
    def test_control_plane_move_session(self, experimental: ExperimentalResource, respx_mock: MockRouter) -> None:
        route = respx_mock.post("/experimental/control-plane/move-session").mock(return_value=httpx.Response(204))
        result = experimental.control_plane_move_session(
            session_id="ses_x", destination={"directory": "/tmp/proj"}, move_changes=True
        )
        assert route.called
        request = route_request(route)
        assert request.method == "POST"
        assert request.url.path == "/experimental/control-plane/move-session"
        assert "directory" not in request.url.params
        assert "workspace" not in request.url.params
        body = read_json_body(route)
        assert body["sessionID"] == "ses_x"
        assert body["destination"]["directory"] == "/tmp/proj"
        assert body["moveChanges"] is True
        assert result is None

    @pytest.mark.respx(base_url=base_url)
    def test_project_copy_generate_name(self, experimental: ExperimentalResource, respx_mock: MockRouter) -> None:
        route = respx_mock.post("/experimental/project/prj_x/copy/generate-name").mock(
            return_value=httpx.Response(200, json={"name": "proj-copy"})
        )
        result = experimental.project_copy_generate_name("prj_x", context="ctx", directory="/tmp/proj", workspace="wrk_ws")
        assert route.called
        request = route_request(route)
        assert request.method == "POST"
        assert request.url.path == "/experimental/project/prj_x/copy/generate-name"
        assert request.url.params["directory"] == "/tmp/proj"
        assert request.url.params["workspace"] == "wrk_ws"
        body = read_json_body(route)
        assert body["context"] == "ctx"
        assert result.name == "proj-copy"

    @pytest.mark.respx(base_url=base_url)
    def test_workspace_list(self, experimental: ExperimentalResource, respx_mock: MockRouter) -> None:
        route = respx_mock.get("/experimental/workspace").mock(
            return_value=httpx.Response(200, json=[WORKSPACE_PAYLOAD])
        )
        result = experimental.workspace_list(directory="/tmp/proj", workspace="wrk_ws")
        assert route.called
        request = route_request(route)
        assert request.method == "GET"
        assert request.url.path == "/experimental/workspace"
        assert request.url.params["directory"] == "/tmp/proj"
        assert request.url.params["workspace"] == "wrk_ws"
        assert result[0].id == "wrk_x"
        assert result[0].project_id == "prj_x"
        assert result[0].time_used == 1.0

    @pytest.mark.respx(base_url=base_url)
    def test_workspace_create(self, experimental: ExperimentalResource, respx_mock: MockRouter) -> None:
        route = respx_mock.post("/experimental/workspace").mock(
            return_value=httpx.Response(200, json=WORKSPACE_PAYLOAD)
        )
        result = experimental.workspace_create(
            type="local", id="wrk_x", branch="main", extra={"k": "v"}, directory="/tmp/proj", workspace="wrk_ws"
        )
        assert route.called
        request = route_request(route)
        assert request.method == "POST"
        assert request.url.path == "/experimental/workspace"
        assert request.url.params["directory"] == "/tmp/proj"
        assert request.url.params["workspace"] == "wrk_ws"
        body = read_json_body(route)
        assert body["type"] == "local"
        assert body["id"] == "wrk_x"
        assert body["branch"] == "main"
        assert body["extra"] == {"k": "v"}
        assert result.id == "wrk_x"

    @pytest.mark.respx(base_url=base_url)
    def test_workspace_sync_list(self, experimental: ExperimentalResource, respx_mock: MockRouter) -> None:
        route = respx_mock.post("/experimental/workspace/sync-list").mock(return_value=httpx.Response(204))
        result = experimental.workspace_sync_list(directory="/tmp/proj", workspace="wrk_ws")
        assert route.called
        request = route_request(route)
        assert request.method == "POST"
        assert request.url.path == "/experimental/workspace/sync-list"
        assert request.url.params["directory"] == "/tmp/proj"
        assert request.url.params["workspace"] == "wrk_ws"
        assert result is None

    @pytest.mark.respx(base_url=base_url)
    def test_workspace_status(self, experimental: ExperimentalResource, respx_mock: MockRouter) -> None:
        route = respx_mock.get("/experimental/workspace/status").mock(
            return_value=httpx.Response(200, json=[{"workspaceID": "wrk_x", "status": "connected"}])
        )
        result = experimental.workspace_status(directory="/tmp/proj", workspace="wrk_ws")
        assert route.called
        request = route_request(route)
        assert request.method == "GET"
        assert request.url.path == "/experimental/workspace/status"
        assert request.url.params["directory"] == "/tmp/proj"
        assert request.url.params["workspace"] == "wrk_ws"
        assert result[0].workspace_id == "wrk_x"
        assert result[0].status == "connected"

    @pytest.mark.respx(base_url=base_url)
    def test_workspace_remove(self, experimental: ExperimentalResource, respx_mock: MockRouter) -> None:
        route = respx_mock.delete("/experimental/workspace/wrk_x").mock(
            return_value=httpx.Response(200, json=WORKSPACE_PAYLOAD)
        )
        result = experimental.workspace_remove("wrk_x", directory="/tmp/proj", workspace="wrk_ws")
        assert route.called
        request = route_request(route)
        assert request.method == "DELETE"
        assert request.url.path == "/experimental/workspace/wrk_x"
        assert request.url.params["directory"] == "/tmp/proj"
        assert request.url.params["workspace"] == "wrk_ws"
        assert result.id == "wrk_x"

    @pytest.mark.respx(base_url=base_url)
    def test_workspace_warp(self, experimental: ExperimentalResource, respx_mock: MockRouter) -> None:
        route = respx_mock.post("/experimental/workspace/warp").mock(return_value=httpx.Response(204))
        result = experimental.workspace_warp(
            id="wrk_x", session_id="ses_x", copy_changes=False, directory="/tmp/proj", workspace="wrk_ws"
        )
        assert route.called
        request = route_request(route)
        assert request.method == "POST"
        assert request.url.path == "/experimental/workspace/warp"
        assert request.url.params["directory"] == "/tmp/proj"
        assert request.url.params["workspace"] == "wrk_ws"
        body = read_json_body(route)
        assert body["id"] == "wrk_x"
        assert body["sessionID"] == "ses_x"
        assert body["copyChanges"] is False
        assert result is None

    @pytest.mark.respx(base_url=base_url)
    def test_workspace_adapter_list(self, experimental: ExperimentalResource, respx_mock: MockRouter) -> None:
        route = respx_mock.get("/experimental/workspace/adapter").mock(
            return_value=httpx.Response(200, json=[{"type": "local", "name": "n", "description": "d"}])
        )
        result = experimental.workspace_adapter_list(directory="/tmp/proj", workspace="wrk_ws")
        assert route.called
        request = route_request(route)
        assert request.method == "GET"
        assert request.url.path == "/experimental/workspace/adapter"
        assert request.url.params["directory"] == "/tmp/proj"
        assert request.url.params["workspace"] == "wrk_ws"
        assert result[0].type == "local"
        assert result[0].name == "n"
        assert result[0].description == "d"


class TestAsyncExperimentalWire:
    @pytest.mark.respx(base_url=base_url)
    async def test_capabilities_get(self, async_experimental: AsyncExperimentalResource, respx_mock: MockRouter) -> None:
        route = respx_mock.get("/experimental/capabilities").mock(
            return_value=httpx.Response(200, json={"backgroundSubagents": False})
        )
        result = await async_experimental.capabilities_get(directory="/tmp/proj", workspace="wrk_ws")
        assert route.called
        request = route_request(route)
        assert request.method == "GET"
        assert request.url.path == "/experimental/capabilities"
        assert request.url.params["directory"] == "/tmp/proj"
        assert request.url.params["workspace"] == "wrk_ws"
        assert result.background_subagents is False

    @pytest.mark.respx(base_url=base_url)
    async def test_console_get(self, async_experimental: AsyncExperimentalResource, respx_mock: MockRouter) -> None:
        route = respx_mock.get("/experimental/console").mock(
            return_value=httpx.Response(
                200,
                json={"consoleManagedProviders": ["acct_x"], "activeOrgName": "org_x", "switchableOrgCount": 2},
            )
        )
        result = await async_experimental.console_get(directory="/tmp/proj", workspace="wrk_ws")
        assert route.called
        request = route_request(route)
        assert request.method == "GET"
        assert request.url.path == "/experimental/console"
        assert request.url.params["directory"] == "/tmp/proj"
        assert request.url.params["workspace"] == "wrk_ws"
        assert result.switchable_org_count == 2

    @pytest.mark.respx(base_url=base_url)
    async def test_console_list_orgs(self, async_experimental: AsyncExperimentalResource, respx_mock: MockRouter) -> None:
        route = respx_mock.get("/experimental/console/orgs").mock(
            return_value=httpx.Response(
                200,
                json={
                    "orgs": [
                        {
                            "accountID": "acct_x",
                            "accountEmail": "a@x.dev",
                            "accountUrl": "https://x.dev",
                            "orgID": "org_x",
                            "orgName": "Org X",
                            "active": True,
                        }
                    ]
                },
            )
        )
        result = await async_experimental.console_list_orgs(directory="/tmp/proj", workspace="wrk_ws")
        assert route.called
        request = route_request(route)
        assert request.method == "GET"
        assert request.url.path == "/experimental/console/orgs"
        assert request.url.params["directory"] == "/tmp/proj"
        assert request.url.params["workspace"] == "wrk_ws"
        assert result.orgs[0].org_id == "org_x"

    @pytest.mark.respx(base_url=base_url)
    async def test_console_switch_org(self, async_experimental: AsyncExperimentalResource, respx_mock: MockRouter) -> None:
        route = respx_mock.post("/experimental/console/switch").mock(return_value=httpx.Response(200, json=True))
        result = await async_experimental.console_switch_org(
            account_id="acct_x", org_id="org_x", directory="/tmp/proj", workspace="wrk_ws"
        )
        assert route.called
        request = route_request(route)
        assert request.method == "POST"
        assert request.url.path == "/experimental/console/switch"
        body = read_json_body(route)
        assert body["accountID"] == "acct_x"
        assert body["orgID"] == "org_x"
        assert result is True

    @pytest.mark.respx(base_url=base_url)
    async def test_session_list(self, async_experimental: AsyncExperimentalResource, respx_mock: MockRouter) -> None:
        route = respx_mock.get("/experimental/session").mock(
            return_value=httpx.Response(
                200,
                json=[
                    {
                        "id": "ses_x",
                        "slug": "s1",
                        "projectID": "prj_x",
                        "directory": "/tmp/proj",
                        "title": "T",
                        "version": "1",
                        "time": {"created": 1, "updated": 2},
                        "project": {"id": "prj_x", "worktree": "wt_x"},
                    }
                ],
            )
        )
        result = await async_experimental.session_list(
            roots=True, start=0, cursor=5, search="foo", limit=10, archived=False,
            directory="/tmp/proj", workspace="wrk_ws",
        )
        assert route.called
        request = route_request(route)
        assert request.method == "GET"
        assert request.url.path == "/experimental/session"
        assert request.url.params["roots"] == "true"
        assert request.url.params["limit"] == "10"
        assert request.url.params["archived"] == "false"
        assert result[0].id == "ses_x"

    @pytest.mark.respx(base_url=base_url)
    async def test_session_background(self, async_experimental: AsyncExperimentalResource, respx_mock: MockRouter) -> None:
        route = respx_mock.post("/experimental/session/ses_x/background").mock(
            return_value=httpx.Response(200, json=True)
        )
        result = await async_experimental.session_background("ses_x", directory="/tmp/proj", workspace="wrk_ws")
        assert route.called
        request = route_request(route)
        assert request.method == "POST"
        assert request.url.path == "/experimental/session/ses_x/background"
        assert result is True

    @pytest.mark.respx(base_url=base_url)
    async def test_resource_list(self, async_experimental: AsyncExperimentalResource, respx_mock: MockRouter) -> None:
        route = respx_mock.get("/experimental/resource").mock(
            return_value=httpx.Response(200, json={"res://x": {"name": "n", "uri": "res://x", "client": "c"}})
        )
        result = await async_experimental.resource_list(directory="/tmp/proj", workspace="wrk_ws")
        assert route.called
        request = route_request(route)
        assert request.method == "GET"
        assert request.url.path == "/experimental/resource"
        assert request.url.params["directory"] == "/tmp/proj"
        assert request.url.params["workspace"] == "wrk_ws"
        assert result["res://x"].client == "c"

    @pytest.mark.respx(base_url=base_url)
    async def test_control_plane_move_session(
        self, async_experimental: AsyncExperimentalResource, respx_mock: MockRouter
    ) -> None:
        route = respx_mock.post("/experimental/control-plane/move-session").mock(return_value=httpx.Response(204))
        result = await async_experimental.control_plane_move_session(
            session_id="ses_x", destination={"directory": "/tmp/proj"}, move_changes=True
        )
        assert route.called
        request = route_request(route)
        assert request.method == "POST"
        assert request.url.path == "/experimental/control-plane/move-session"
        assert "directory" not in request.url.params
        assert "workspace" not in request.url.params
        body = read_json_body(route)
        assert body["sessionID"] == "ses_x"
        assert body["destination"]["directory"] == "/tmp/proj"
        assert result is None

    @pytest.mark.respx(base_url=base_url)
    async def test_project_copy_generate_name(
        self, async_experimental: AsyncExperimentalResource, respx_mock: MockRouter
    ) -> None:
        route = respx_mock.post("/experimental/project/prj_x/copy/generate-name").mock(
            return_value=httpx.Response(200, json={"name": "proj-copy"})
        )
        result = await async_experimental.project_copy_generate_name(
            "prj_x", context="ctx", directory="/tmp/proj", workspace="wrk_ws"
        )
        assert route.called
        request = route_request(route)
        assert request.method == "POST"
        assert request.url.path == "/experimental/project/prj_x/copy/generate-name"
        body = read_json_body(route)
        assert body["context"] == "ctx"
        assert result.name == "proj-copy"

    @pytest.mark.respx(base_url=base_url)
    async def test_workspace_list(self, async_experimental: AsyncExperimentalResource, respx_mock: MockRouter) -> None:
        route = respx_mock.get("/experimental/workspace").mock(
            return_value=httpx.Response(200, json=[WORKSPACE_PAYLOAD])
        )
        result = await async_experimental.workspace_list(directory="/tmp/proj", workspace="wrk_ws")
        assert route.called
        request = route_request(route)
        assert request.method == "GET"
        assert request.url.path == "/experimental/workspace"
        assert result[0].id == "wrk_x"

    @pytest.mark.respx(base_url=base_url)
    async def test_workspace_create(self, async_experimental: AsyncExperimentalResource, respx_mock: MockRouter) -> None:
        route = respx_mock.post("/experimental/workspace").mock(
            return_value=httpx.Response(200, json=WORKSPACE_PAYLOAD)
        )
        result = await async_experimental.workspace_create(
            type="local", id="wrk_x", branch="main", extra={"k": "v"}, directory="/tmp/proj", workspace="wrk_ws"
        )
        assert route.called
        request = route_request(route)
        assert request.method == "POST"
        assert request.url.path == "/experimental/workspace"
        body = read_json_body(route)
        assert body["type"] == "local"
        assert body["extra"] == {"k": "v"}
        assert result.id == "wrk_x"

    @pytest.mark.respx(base_url=base_url)
    async def test_workspace_sync_list(self, async_experimental: AsyncExperimentalResource, respx_mock: MockRouter) -> None:
        route = respx_mock.post("/experimental/workspace/sync-list").mock(return_value=httpx.Response(204))
        result = await async_experimental.workspace_sync_list(directory="/tmp/proj", workspace="wrk_ws")
        assert route.called
        request = route_request(route)
        assert request.method == "POST"
        assert request.url.path == "/experimental/workspace/sync-list"
        assert result is None

    @pytest.mark.respx(base_url=base_url)
    async def test_workspace_status(self, async_experimental: AsyncExperimentalResource, respx_mock: MockRouter) -> None:
        route = respx_mock.get("/experimental/workspace/status").mock(
            return_value=httpx.Response(200, json=[{"workspaceID": "wrk_x", "status": "connected"}])
        )
        result = await async_experimental.workspace_status(directory="/tmp/proj", workspace="wrk_ws")
        assert route.called
        request = route_request(route)
        assert request.method == "GET"
        assert request.url.path == "/experimental/workspace/status"
        assert result[0].status == "connected"

    @pytest.mark.respx(base_url=base_url)
    async def test_workspace_remove(self, async_experimental: AsyncExperimentalResource, respx_mock: MockRouter) -> None:
        route = respx_mock.delete("/experimental/workspace/wrk_x").mock(
            return_value=httpx.Response(200, json=WORKSPACE_PAYLOAD)
        )
        result = await async_experimental.workspace_remove("wrk_x", directory="/tmp/proj", workspace="wrk_ws")
        assert route.called
        request = route_request(route)
        assert request.method == "DELETE"
        assert request.url.path == "/experimental/workspace/wrk_x"
        assert result.id == "wrk_x"

    @pytest.mark.respx(base_url=base_url)
    async def test_workspace_warp(self, async_experimental: AsyncExperimentalResource, respx_mock: MockRouter) -> None:
        route = respx_mock.post("/experimental/workspace/warp").mock(return_value=httpx.Response(204))
        result = await async_experimental.workspace_warp(
            id="wrk_x", session_id="ses_x", copy_changes=False, directory="/tmp/proj", workspace="wrk_ws"
        )
        assert route.called
        request = route_request(route)
        assert request.method == "POST"
        assert request.url.path == "/experimental/workspace/warp"
        body = read_json_body(route)
        assert body["sessionID"] == "ses_x"
        assert body["copyChanges"] is False
        assert result is None

    @pytest.mark.respx(base_url=base_url)
    async def test_workspace_adapter_list(
        self, async_experimental: AsyncExperimentalResource, respx_mock: MockRouter
    ) -> None:
        route = respx_mock.get("/experimental/workspace/adapter").mock(
            return_value=httpx.Response(200, json=[{"type": "local", "name": "n", "description": "d"}])
        )
        result = await async_experimental.workspace_adapter_list(directory="/tmp/proj", workspace="wrk_ws")
        assert route.called
        request = route_request(route)
        assert request.method == "GET"
        assert request.url.path == "/experimental/workspace/adapter"
        assert result[0].name == "n"
