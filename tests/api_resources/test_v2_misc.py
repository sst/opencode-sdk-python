# Hand-maintained fork of the Stainless-era opencode SDK. Generated code was replaced by manual maintenance; see CONTRIBUTING.md.

from __future__ import annotations

import os

import httpx
import pytest
from respx import MockRouter

from opencode_ai import Opencode, AsyncOpencode
from tests.wire_helpers import route_request, read_json_body
from opencode_ai.resources.v2 import V2Resource, AsyncV2Resource

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestV2MiscWire:
    @pytest.mark.respx(base_url=base_url)
    def test_fs_find(self, client: Opencode, respx_mock: MockRouter) -> None:
        v2 = V2Resource(client)
        route = respx_mock.get("/api/fs/find").mock(
            return_value=httpx.Response(
                200, json={"location": {"directory": "/w", "project": {"id": "p1", "directory": "/w"}}, "data": []}
            )
        )
        result = v2.fs.find(location={"directory": "/d", "workspace": "wrk_1"}, query="x", limit="qv")
        assert route.called
        request = route_request(route)
        assert request.method == "GET"
        assert request.url.params.get("location[directory]") == "/d"
        assert request.url.params.get("query") == "x"
        assert request.url.params.get("limit") == "qv"
        assert result.location.directory == "/w"

    @pytest.mark.respx(base_url=base_url)
    def test_fs_list(self, client: Opencode, respx_mock: MockRouter) -> None:
        v2 = V2Resource(client)
        route = respx_mock.get("/api/fs/list").mock(
            return_value=httpx.Response(
                200, json={"location": {"directory": "/w", "project": {"id": "p1", "directory": "/w"}}, "data": []}
            )
        )
        result = v2.fs.list(location={"directory": "/d", "workspace": "wrk_1"}, path="qv")
        assert route.called
        request = route_request(route)
        assert request.method == "GET"
        assert request.url.params.get("location[directory]") == "/d"
        assert request.url.params.get("path") == "qv"
        assert result.location.directory == "/w"

    @pytest.mark.respx(base_url=base_url)
    def test_fs_read(self, client: Opencode, respx_mock: MockRouter) -> None:
        v2 = V2Resource(client)
        route = respx_mock.get("/api/fs/read/*").mock(
            return_value=httpx.Response(200, content=b"data", headers={"content-type": "application/octet-stream"})
        )
        result = v2.fs.read(location={"directory": "/d", "workspace": "wrk_1"})
        assert route.called
        request = route_request(route)
        assert request.method == "GET"
        assert request.url.params.get("location[directory]") == "/d"
        assert result == "data"

    @pytest.mark.respx(base_url=base_url)
    def test_question_request_list(self, client: Opencode, respx_mock: MockRouter) -> None:
        v2 = V2Resource(client)
        route = respx_mock.get("/api/question/request").mock(
            return_value=httpx.Response(
                200, json={"location": {"directory": "/w", "project": {"id": "p1", "directory": "/w"}}, "data": []}
            )
        )
        result = v2.question.request_list(location={"directory": "/d", "workspace": "wrk_1"})
        assert route.called
        request = route_request(route)
        assert request.method == "GET"
        assert request.url.params.get("location[directory]") == "/d"
        assert result.location.directory == "/w"

    @pytest.mark.respx(base_url=base_url)
    def test_provider_get(self, client: Opencode, respx_mock: MockRouter) -> None:
        v2 = V2Resource(client)
        route = respx_mock.get("/api/provider/provider_id_1").mock(
            return_value=httpx.Response(
                200, json={"location": {"directory": "/w", "project": {"id": "p1", "directory": "/w"}}, "data": {}}
            )
        )
        result = v2.provider.get("provider_id_1", location={"directory": "/d", "workspace": "wrk_1"})
        assert route.called
        request = route_request(route)
        assert request.method == "GET"
        assert request.url.params.get("location[directory]") == "/d"
        assert result.location.directory == "/w"

    @pytest.mark.respx(base_url=base_url)
    def test_provider_list(self, client: Opencode, respx_mock: MockRouter) -> None:
        v2 = V2Resource(client)
        route = respx_mock.get("/api/provider").mock(
            return_value=httpx.Response(
                200, json={"location": {"directory": "/w", "project": {"id": "p1", "directory": "/w"}}, "data": []}
            )
        )
        result = v2.provider.list(location={"directory": "/d", "workspace": "wrk_1"})
        assert route.called
        request = route_request(route)
        assert request.method == "GET"
        assert request.url.params.get("location[directory]") == "/d"
        assert result.location.directory == "/w"

    @pytest.mark.respx(base_url=base_url)
    def test_credential_remove(self, client: Opencode, respx_mock: MockRouter) -> None:
        v2 = V2Resource(client)
        route = respx_mock.delete("/api/credential/credential_id_1").mock(return_value=httpx.Response(200, json=None))
        result = v2.credential.remove("credential_id_1", location={"directory": "/d", "workspace": "wrk_1"})
        assert route.called
        request = route_request(route)
        assert request.method == "DELETE"
        assert request.url.params.get("location[directory]") == "/d"
        assert result is None

    @pytest.mark.respx(base_url=base_url)
    def test_credential_update(self, client: Opencode, respx_mock: MockRouter) -> None:
        v2 = V2Resource(client)
        route = respx_mock.patch("/api/credential/credential_id_1").mock(return_value=httpx.Response(200, json=None))
        result = v2.credential.update("credential_id_1", label="x", location={"directory": "/d", "workspace": "wrk_1"})
        assert route.called
        request = route_request(route)
        assert request.method == "PATCH"
        body = read_json_body(route)
        assert body["label"] == "x"
        assert request.url.params.get("location[directory]") == "/d"
        assert result is None

    @pytest.mark.respx(base_url=base_url)
    def test_health_get(self, client: Opencode, respx_mock: MockRouter) -> None:
        v2 = V2Resource(client)
        route = respx_mock.get("/api/health").mock(return_value=httpx.Response(200, json={"healthy": True}))
        result = v2.health.get()
        assert route.called
        request = route_request(route)
        assert request.method == "GET"
        assert result.healthy is True

    @pytest.mark.respx(base_url=base_url)
    def test_location_get(self, client: Opencode, respx_mock: MockRouter) -> None:
        v2 = V2Resource(client)
        route = respx_mock.get("/api/location").mock(
            return_value=httpx.Response(200, json={"project": {}, "directory": "x"})
        )
        result = v2.location.get(location={"directory": "/d", "workspace": "wrk_1"})
        assert route.called
        request = route_request(route)
        assert request.method == "GET"
        assert request.url.params.get("location[directory]") == "/d"
        assert result is not None

    @pytest.mark.respx(base_url=base_url)
    def test_agent_list(self, client: Opencode, respx_mock: MockRouter) -> None:
        v2 = V2Resource(client)
        route = respx_mock.get("/api/agent").mock(
            return_value=httpx.Response(
                200, json={"location": {"directory": "/w", "project": {"id": "p1", "directory": "/w"}}, "data": []}
            )
        )
        result = v2.agent.list(location={"directory": "/d", "workspace": "wrk_1"})
        assert route.called
        request = route_request(route)
        assert request.method == "GET"
        assert request.url.params.get("location[directory]") == "/d"
        assert result.location.directory == "/w"

    @pytest.mark.respx(base_url=base_url)
    def test_model_list(self, client: Opencode, respx_mock: MockRouter) -> None:
        v2 = V2Resource(client)
        route = respx_mock.get("/api/model").mock(
            return_value=httpx.Response(
                200, json={"location": {"directory": "/w", "project": {"id": "p1", "directory": "/w"}}, "data": []}
            )
        )
        result = v2.model.list(location={"directory": "/d", "workspace": "wrk_1"})
        assert route.called
        request = route_request(route)
        assert request.method == "GET"
        assert request.url.params.get("location[directory]") == "/d"
        assert result.location.directory == "/w"

    @pytest.mark.respx(base_url=base_url)
    def test_command_list(self, client: Opencode, respx_mock: MockRouter) -> None:
        v2 = V2Resource(client)
        route = respx_mock.get("/api/command").mock(
            return_value=httpx.Response(
                200, json={"location": {"directory": "/w", "project": {"id": "p1", "directory": "/w"}}, "data": []}
            )
        )
        result = v2.command.list(location={"directory": "/d", "workspace": "wrk_1"})
        assert route.called
        request = route_request(route)
        assert request.method == "GET"
        assert request.url.params.get("location[directory]") == "/d"
        assert result.location.directory == "/w"

    @pytest.mark.respx(base_url=base_url)
    def test_skill_list(self, client: Opencode, respx_mock: MockRouter) -> None:
        v2 = V2Resource(client)
        route = respx_mock.get("/api/skill").mock(
            return_value=httpx.Response(
                200, json={"location": {"directory": "/w", "project": {"id": "p1", "directory": "/w"}}, "data": []}
            )
        )
        result = v2.skill.list(location={"directory": "/d", "workspace": "wrk_1"})
        assert route.called
        request = route_request(route)
        assert request.method == "GET"
        assert request.url.params.get("location[directory]") == "/d"
        assert result.location.directory == "/w"

    @pytest.mark.respx(base_url=base_url)
    def test_event_subscribe(self, client: Opencode, respx_mock: MockRouter) -> None:
        v2 = V2Resource(client)
        route = respx_mock.get("/api/event").mock(
            return_value=httpx.Response(200, content=b"", headers={"content-type": "text/event-stream"})
        )
        v2.event.subscribe()
        assert route.called
        request = route_request(route)
        assert request.method == "GET"
        assert route.called

    @pytest.mark.respx(base_url=base_url)
    def test_reference_list(self, client: Opencode, respx_mock: MockRouter) -> None:
        v2 = V2Resource(client)
        route = respx_mock.get("/api/reference").mock(
            return_value=httpx.Response(
                200, json={"location": {"directory": "/w", "project": {"id": "p1", "directory": "/w"}}, "data": []}
            )
        )
        result = v2.reference.list(location={"directory": "/d", "workspace": "wrk_1"})
        assert route.called
        request = route_request(route)
        assert request.method == "GET"
        assert request.url.params.get("location[directory]") == "/d"
        assert result.location.directory == "/w"

    @pytest.mark.respx(base_url=base_url)
    def test_project_copy_create(self, client: Opencode, respx_mock: MockRouter) -> None:
        v2 = V2Resource(client)
        route = respx_mock.post("/experimental/project/project_id_1/copy").mock(
            return_value=httpx.Response(200, json={"directory": "x"})
        )
        result = v2.project_copy.create(
            "project_id_1", strategy="x", directory="x", location={"directory": "/d", "workspace": "wrk_1"}
        )
        assert route.called
        request = route_request(route)
        assert request.method == "POST"
        body = read_json_body(route)
        assert body["strategy"] == "x"
        assert body["directory"] == "x"
        assert request.url.params.get("location[directory]") == "/d"
        assert result is not None

    @pytest.mark.respx(base_url=base_url)
    def test_project_copy_refresh(self, client: Opencode, respx_mock: MockRouter) -> None:
        v2 = V2Resource(client)
        route = respx_mock.post("/experimental/project/project_id_1/copy/refresh").mock(
            return_value=httpx.Response(200, json=None)
        )
        result = v2.project_copy.refresh("project_id_1", location={"directory": "/d", "workspace": "wrk_1"})
        assert route.called
        request = route_request(route)
        assert request.method == "POST"
        assert request.url.params.get("location[directory]") == "/d"
        assert result is None

    @pytest.mark.respx(base_url=base_url)
    def test_project_copy_remove(self, client: Opencode, respx_mock: MockRouter) -> None:
        v2 = V2Resource(client)
        route = respx_mock.delete("/experimental/project/project_id_1/copy").mock(
            return_value=httpx.Response(200, json=None)
        )
        result = v2.project_copy.remove(
            "project_id_1", directory="x", force=True, location={"directory": "/d", "workspace": "wrk_1"}
        )
        assert route.called
        request = route_request(route)
        assert request.method == "DELETE"
        body = read_json_body(route)
        assert body["directory"] == "x"
        assert request.url.params.get("location[directory]") == "/d"
        assert result is None


class TestAsyncV2MiscWire:
    @pytest.mark.respx(base_url=base_url)
    async def test_fs_find(self, async_client: AsyncOpencode, respx_mock: MockRouter) -> None:
        v2 = AsyncV2Resource(async_client)
        route = respx_mock.get("/api/fs/find").mock(
            return_value=httpx.Response(
                200, json={"location": {"directory": "/w", "project": {"id": "p1", "directory": "/w"}}, "data": []}
            )
        )
        result = await v2.fs.find(location={"directory": "/d", "workspace": "wrk_1"}, query="x", limit="qv")
        assert route.called
        request = route_request(route)
        assert request.method == "GET"
        assert request.url.params.get("location[directory]") == "/d"
        assert request.url.params.get("query") == "x"
        assert request.url.params.get("limit") == "qv"
        assert result.location.directory == "/w"

    @pytest.mark.respx(base_url=base_url)
    async def test_fs_list(self, async_client: AsyncOpencode, respx_mock: MockRouter) -> None:
        v2 = AsyncV2Resource(async_client)
        route = respx_mock.get("/api/fs/list").mock(
            return_value=httpx.Response(
                200, json={"location": {"directory": "/w", "project": {"id": "p1", "directory": "/w"}}, "data": []}
            )
        )
        result = await v2.fs.list(location={"directory": "/d", "workspace": "wrk_1"}, path="qv")
        assert route.called
        request = route_request(route)
        assert request.method == "GET"
        assert request.url.params.get("location[directory]") == "/d"
        assert request.url.params.get("path") == "qv"
        assert result.location.directory == "/w"

    @pytest.mark.respx(base_url=base_url)
    async def test_fs_read(self, async_client: AsyncOpencode, respx_mock: MockRouter) -> None:
        v2 = AsyncV2Resource(async_client)
        route = respx_mock.get("/api/fs/read/*").mock(
            return_value=httpx.Response(200, content=b"data", headers={"content-type": "application/octet-stream"})
        )
        result = await v2.fs.read(location={"directory": "/d", "workspace": "wrk_1"})
        assert route.called
        request = route_request(route)
        assert request.method == "GET"
        assert request.url.params.get("location[directory]") == "/d"
        assert result == "data"

    @pytest.mark.respx(base_url=base_url)
    async def test_question_request_list(self, async_client: AsyncOpencode, respx_mock: MockRouter) -> None:
        v2 = AsyncV2Resource(async_client)
        route = respx_mock.get("/api/question/request").mock(
            return_value=httpx.Response(
                200, json={"location": {"directory": "/w", "project": {"id": "p1", "directory": "/w"}}, "data": []}
            )
        )
        result = await v2.question.request_list(location={"directory": "/d", "workspace": "wrk_1"})
        assert route.called
        request = route_request(route)
        assert request.method == "GET"
        assert request.url.params.get("location[directory]") == "/d"
        assert result.location.directory == "/w"

    @pytest.mark.respx(base_url=base_url)
    async def test_provider_get(self, async_client: AsyncOpencode, respx_mock: MockRouter) -> None:
        v2 = AsyncV2Resource(async_client)
        route = respx_mock.get("/api/provider/provider_id_1").mock(
            return_value=httpx.Response(
                200, json={"location": {"directory": "/w", "project": {"id": "p1", "directory": "/w"}}, "data": {}}
            )
        )
        result = await v2.provider.get("provider_id_1", location={"directory": "/d", "workspace": "wrk_1"})
        assert route.called
        request = route_request(route)
        assert request.method == "GET"
        assert request.url.params.get("location[directory]") == "/d"
        assert result.location.directory == "/w"

    @pytest.mark.respx(base_url=base_url)
    async def test_provider_list(self, async_client: AsyncOpencode, respx_mock: MockRouter) -> None:
        v2 = AsyncV2Resource(async_client)
        route = respx_mock.get("/api/provider").mock(
            return_value=httpx.Response(
                200, json={"location": {"directory": "/w", "project": {"id": "p1", "directory": "/w"}}, "data": []}
            )
        )
        result = await v2.provider.list(location={"directory": "/d", "workspace": "wrk_1"})
        assert route.called
        request = route_request(route)
        assert request.method == "GET"
        assert request.url.params.get("location[directory]") == "/d"
        assert result.location.directory == "/w"

    @pytest.mark.respx(base_url=base_url)
    async def test_credential_remove(self, async_client: AsyncOpencode, respx_mock: MockRouter) -> None:
        v2 = AsyncV2Resource(async_client)
        route = respx_mock.delete("/api/credential/credential_id_1").mock(return_value=httpx.Response(200, json=None))
        result = await v2.credential.remove("credential_id_1", location={"directory": "/d", "workspace": "wrk_1"})
        assert route.called
        request = route_request(route)
        assert request.method == "DELETE"
        assert request.url.params.get("location[directory]") == "/d"
        assert result is None

    @pytest.mark.respx(base_url=base_url)
    async def test_credential_update(self, async_client: AsyncOpencode, respx_mock: MockRouter) -> None:
        v2 = AsyncV2Resource(async_client)
        route = respx_mock.patch("/api/credential/credential_id_1").mock(return_value=httpx.Response(200, json=None))
        result = await v2.credential.update(
            "credential_id_1", label="x", location={"directory": "/d", "workspace": "wrk_1"}
        )
        assert route.called
        request = route_request(route)
        assert request.method == "PATCH"
        body = read_json_body(route)
        assert body["label"] == "x"
        assert request.url.params.get("location[directory]") == "/d"
        assert result is None

    @pytest.mark.respx(base_url=base_url)
    async def test_health_get(self, async_client: AsyncOpencode, respx_mock: MockRouter) -> None:
        v2 = AsyncV2Resource(async_client)
        route = respx_mock.get("/api/health").mock(return_value=httpx.Response(200, json={"healthy": True}))
        result = await v2.health.get()
        assert route.called
        request = route_request(route)
        assert request.method == "GET"
        assert result.healthy is True

    @pytest.mark.respx(base_url=base_url)
    async def test_location_get(self, async_client: AsyncOpencode, respx_mock: MockRouter) -> None:
        v2 = AsyncV2Resource(async_client)
        route = respx_mock.get("/api/location").mock(
            return_value=httpx.Response(200, json={"project": {}, "directory": "x"})
        )
        result = await v2.location.get(location={"directory": "/d", "workspace": "wrk_1"})
        assert route.called
        request = route_request(route)
        assert request.method == "GET"
        assert request.url.params.get("location[directory]") == "/d"
        assert result is not None

    @pytest.mark.respx(base_url=base_url)
    async def test_agent_list(self, async_client: AsyncOpencode, respx_mock: MockRouter) -> None:
        v2 = AsyncV2Resource(async_client)
        route = respx_mock.get("/api/agent").mock(
            return_value=httpx.Response(
                200, json={"location": {"directory": "/w", "project": {"id": "p1", "directory": "/w"}}, "data": []}
            )
        )
        result = await v2.agent.list(location={"directory": "/d", "workspace": "wrk_1"})
        assert route.called
        request = route_request(route)
        assert request.method == "GET"
        assert request.url.params.get("location[directory]") == "/d"
        assert result.location.directory == "/w"

    @pytest.mark.respx(base_url=base_url)
    async def test_model_list(self, async_client: AsyncOpencode, respx_mock: MockRouter) -> None:
        v2 = AsyncV2Resource(async_client)
        route = respx_mock.get("/api/model").mock(
            return_value=httpx.Response(
                200, json={"location": {"directory": "/w", "project": {"id": "p1", "directory": "/w"}}, "data": []}
            )
        )
        result = await v2.model.list(location={"directory": "/d", "workspace": "wrk_1"})
        assert route.called
        request = route_request(route)
        assert request.method == "GET"
        assert request.url.params.get("location[directory]") == "/d"
        assert result.location.directory == "/w"

    @pytest.mark.respx(base_url=base_url)
    async def test_command_list(self, async_client: AsyncOpencode, respx_mock: MockRouter) -> None:
        v2 = AsyncV2Resource(async_client)
        route = respx_mock.get("/api/command").mock(
            return_value=httpx.Response(
                200, json={"location": {"directory": "/w", "project": {"id": "p1", "directory": "/w"}}, "data": []}
            )
        )
        result = await v2.command.list(location={"directory": "/d", "workspace": "wrk_1"})
        assert route.called
        request = route_request(route)
        assert request.method == "GET"
        assert request.url.params.get("location[directory]") == "/d"
        assert result.location.directory == "/w"

    @pytest.mark.respx(base_url=base_url)
    async def test_skill_list(self, async_client: AsyncOpencode, respx_mock: MockRouter) -> None:
        v2 = AsyncV2Resource(async_client)
        route = respx_mock.get("/api/skill").mock(
            return_value=httpx.Response(
                200, json={"location": {"directory": "/w", "project": {"id": "p1", "directory": "/w"}}, "data": []}
            )
        )
        result = await v2.skill.list(location={"directory": "/d", "workspace": "wrk_1"})
        assert route.called
        request = route_request(route)
        assert request.method == "GET"
        assert request.url.params.get("location[directory]") == "/d"
        assert result.location.directory == "/w"

    @pytest.mark.respx(base_url=base_url)
    async def test_event_subscribe(self, async_client: AsyncOpencode, respx_mock: MockRouter) -> None:
        v2 = AsyncV2Resource(async_client)
        route = respx_mock.get("/api/event").mock(
            return_value=httpx.Response(200, content=b"", headers={"content-type": "text/event-stream"})
        )
        await v2.event.subscribe()
        assert route.called
        request = route_request(route)
        assert request.method == "GET"
        assert route.called

    @pytest.mark.respx(base_url=base_url)
    async def test_reference_list(self, async_client: AsyncOpencode, respx_mock: MockRouter) -> None:
        v2 = AsyncV2Resource(async_client)
        route = respx_mock.get("/api/reference").mock(
            return_value=httpx.Response(
                200, json={"location": {"directory": "/w", "project": {"id": "p1", "directory": "/w"}}, "data": []}
            )
        )
        result = await v2.reference.list(location={"directory": "/d", "workspace": "wrk_1"})
        assert route.called
        request = route_request(route)
        assert request.method == "GET"
        assert request.url.params.get("location[directory]") == "/d"
        assert result.location.directory == "/w"

    @pytest.mark.respx(base_url=base_url)
    async def test_project_copy_create(self, async_client: AsyncOpencode, respx_mock: MockRouter) -> None:
        v2 = AsyncV2Resource(async_client)
        route = respx_mock.post("/experimental/project/project_id_1/copy").mock(
            return_value=httpx.Response(200, json={"directory": "x"})
        )
        result = await v2.project_copy.create(
            "project_id_1", strategy="x", directory="x", location={"directory": "/d", "workspace": "wrk_1"}
        )
        assert route.called
        request = route_request(route)
        assert request.method == "POST"
        body = read_json_body(route)
        assert body["strategy"] == "x"
        assert body["directory"] == "x"
        assert request.url.params.get("location[directory]") == "/d"
        assert result is not None

    @pytest.mark.respx(base_url=base_url)
    async def test_project_copy_refresh(self, async_client: AsyncOpencode, respx_mock: MockRouter) -> None:
        v2 = AsyncV2Resource(async_client)
        route = respx_mock.post("/experimental/project/project_id_1/copy/refresh").mock(
            return_value=httpx.Response(200, json=None)
        )
        result = await v2.project_copy.refresh("project_id_1", location={"directory": "/d", "workspace": "wrk_1"})
        assert route.called
        request = route_request(route)
        assert request.method == "POST"
        assert request.url.params.get("location[directory]") == "/d"
        assert result is None

    @pytest.mark.respx(base_url=base_url)
    async def test_project_copy_remove(self, async_client: AsyncOpencode, respx_mock: MockRouter) -> None:
        v2 = AsyncV2Resource(async_client)
        route = respx_mock.delete("/experimental/project/project_id_1/copy").mock(
            return_value=httpx.Response(200, json=None)
        )
        result = await v2.project_copy.remove(
            "project_id_1", directory="x", force=True, location={"directory": "/d", "workspace": "wrk_1"}
        )
        assert route.called
        request = route_request(route)
        assert request.method == "DELETE"
        body = read_json_body(route)
        assert body["directory"] == "x"
        assert request.url.params.get("location[directory]") == "/d"
        assert result is None
