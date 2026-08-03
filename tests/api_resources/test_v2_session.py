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


class TestV2SessionWire:
    @pytest.mark.respx(base_url=base_url)
    def test_session_active(self, client: Opencode, respx_mock: MockRouter) -> None:
        v2 = V2Resource(client)
        route = respx_mock.get("/api/session/active").mock(return_value=httpx.Response(200, json={"data": {}}))
        result = v2.session.active()
        assert route.called
        request = route_request(route)
        assert request.method == "GET"
        assert result is not None

    @pytest.mark.respx(base_url=base_url)
    def test_session_compact(self, client: Opencode, respx_mock: MockRouter) -> None:
        v2 = V2Resource(client)
        route = respx_mock.post("/api/session/session_id_1/compact").mock(return_value=httpx.Response(200, json=None))
        result = v2.session.compact("session_id_1")
        assert route.called
        request = route_request(route)
        assert request.method == "POST"
        assert result is None

    @pytest.mark.respx(base_url=base_url)
    def test_session_context(self, client: Opencode, respx_mock: MockRouter) -> None:
        v2 = V2Resource(client)
        route = respx_mock.get("/api/session/session_id_1/context").mock(
            return_value=httpx.Response(200, json={"data": []})
        )
        result = v2.session.context("session_id_1")
        assert route.called
        request = route_request(route)
        assert request.method == "GET"
        assert result is not None

    @pytest.mark.respx(base_url=base_url)
    def test_session_create(self, client: Opencode, respx_mock: MockRouter) -> None:
        v2 = V2Resource(client)
        route = respx_mock.post("/api/session").mock(return_value=httpx.Response(200, json={"data": {}}))
        result = v2.session.create()
        assert route.called
        request = route_request(route)
        assert request.method == "POST"
        assert result is not None

    @pytest.mark.respx(base_url=base_url)
    def test_session_events(self, client: Opencode, respx_mock: MockRouter) -> None:
        v2 = V2Resource(client)
        route = respx_mock.get("/api/session/session_id_1/event").mock(
            return_value=httpx.Response(200, content=b"", headers={"content-type": "text/event-stream"})
        )
        v2.session.events("session_id_1", after="qv")
        assert route.called
        request = route_request(route)
        assert request.method == "GET"
        assert request.url.params.get("after") == "qv"
        assert route.called

    @pytest.mark.respx(base_url=base_url)
    def test_session_get(self, client: Opencode, respx_mock: MockRouter) -> None:
        v2 = V2Resource(client)
        route = respx_mock.get("/api/session/session_id_1").mock(return_value=httpx.Response(200, json={"data": {}}))
        result = v2.session.get("session_id_1")
        assert route.called
        request = route_request(route)
        assert request.method == "GET"
        assert result is not None

    @pytest.mark.respx(base_url=base_url)
    def test_session_history(self, client: Opencode, respx_mock: MockRouter) -> None:
        v2 = V2Resource(client)
        route = respx_mock.get("/api/session/session_id_1/history").mock(
            return_value=httpx.Response(200, json={"data": [], "hasMore": True})
        )
        result = v2.session.history("session_id_1", limit="qv", after="qv")
        assert route.called
        request = route_request(route)
        assert request.method == "GET"
        assert request.url.params.get("limit") == "qv"
        assert request.url.params.get("after") == "qv"
        assert result is not None

    @pytest.mark.respx(base_url=base_url)
    def test_session_interrupt(self, client: Opencode, respx_mock: MockRouter) -> None:
        v2 = V2Resource(client)
        route = respx_mock.post("/api/session/session_id_1/interrupt").mock(return_value=httpx.Response(200, json=None))
        result = v2.session.interrupt("session_id_1")
        assert route.called
        request = route_request(route)
        assert request.method == "POST"
        assert result is None

    @pytest.mark.respx(base_url=base_url)
    def test_session_list(self, client: Opencode, respx_mock: MockRouter) -> None:
        v2 = V2Resource(client)
        route = respx_mock.get("/api/session").mock(return_value=httpx.Response(200, json={"data": [], "cursor": {}}))
        result = v2.session.list(workspace="qv", search="qv", directory="qv", project="qv", subpath="qv", cursor="qv")
        assert route.called
        request = route_request(route)
        assert request.method == "GET"
        assert request.url.params.get("workspace") == "qv"
        assert request.url.params.get("search") == "qv"
        assert request.url.params.get("directory") == "qv"
        assert request.url.params.get("project") == "qv"
        assert request.url.params.get("subpath") == "qv"
        assert request.url.params.get("cursor") == "qv"
        assert result is not None

    @pytest.mark.respx(base_url=base_url)
    def test_session_message(self, client: Opencode, respx_mock: MockRouter) -> None:
        v2 = V2Resource(client)
        route = respx_mock.get("/api/session/session_id_1/message/message_id_1").mock(
            return_value=httpx.Response(200, json={"data": {}})
        )
        result = v2.session.message("session_id_1", "message_id_1")
        assert route.called
        request = route_request(route)
        assert request.method == "GET"
        assert result is not None

    @pytest.mark.respx(base_url=base_url)
    def test_session_messages(self, client: Opencode, respx_mock: MockRouter) -> None:
        v2 = V2Resource(client)
        route = respx_mock.get("/api/session/session_id_1/message").mock(
            return_value=httpx.Response(200, json={"data": [], "cursor": {}})
        )
        result = v2.session.messages("session_id_1", cursor="qv")
        assert route.called
        request = route_request(route)
        assert request.method == "GET"
        assert request.url.params.get("cursor") == "qv"
        assert result is not None

    @pytest.mark.respx(base_url=base_url)
    def test_session_permission_create(self, client: Opencode, respx_mock: MockRouter) -> None:
        v2 = V2Resource(client)
        route = respx_mock.post("/api/session/session_id_1/permission").mock(
            return_value=httpx.Response(200, json={"data": {}})
        )
        result = v2.session.permission_create("session_id_1", action="x", resources=["x"])
        assert route.called
        request = route_request(route)
        assert request.method == "POST"
        body = read_json_body(route)
        assert body["action"] == "x"
        assert result is not None

    @pytest.mark.respx(base_url=base_url)
    def test_session_permission_get(self, client: Opencode, respx_mock: MockRouter) -> None:
        v2 = V2Resource(client)
        route = respx_mock.get("/api/session/session_id_1/permission/request_id_1").mock(
            return_value=httpx.Response(200, json={"data": {}})
        )
        result = v2.session.permission_get("session_id_1", "request_id_1")
        assert route.called
        request = route_request(route)
        assert request.method == "GET"
        assert result is not None

    @pytest.mark.respx(base_url=base_url)
    def test_session_permission_list(self, client: Opencode, respx_mock: MockRouter) -> None:
        v2 = V2Resource(client)
        route = respx_mock.get("/api/session/session_id_1/permission").mock(
            return_value=httpx.Response(200, json={"data": []})
        )
        result = v2.session.permission_list("session_id_1")
        assert route.called
        request = route_request(route)
        assert request.method == "GET"
        assert result is not None

    @pytest.mark.respx(base_url=base_url)
    def test_session_permission_reply(self, client: Opencode, respx_mock: MockRouter) -> None:
        v2 = V2Resource(client)
        route = respx_mock.post("/api/session/session_id_1/permission/request_id_1/reply").mock(
            return_value=httpx.Response(200, json=None)
        )
        result = v2.session.permission_reply("session_id_1", "request_id_1", reply="once")
        assert route.called
        request = route_request(route)
        assert request.method == "POST"
        assert result is None

    @pytest.mark.respx(base_url=base_url)
    def test_session_prompt(self, client: Opencode, respx_mock: MockRouter) -> None:
        v2 = V2Resource(client)
        route = respx_mock.post("/api/session/session_id_1/prompt").mock(
            return_value=httpx.Response(200, json={"data": {}})
        )
        result = v2.session.prompt("session_id_1", prompt={})
        assert route.called
        request = route_request(route)
        assert request.method == "POST"
        assert result is not None

    @pytest.mark.respx(base_url=base_url)
    def test_session_question_list(self, client: Opencode, respx_mock: MockRouter) -> None:
        v2 = V2Resource(client)
        route = respx_mock.get("/api/session/session_id_1/question").mock(
            return_value=httpx.Response(200, json={"data": []})
        )
        result = v2.session.question_list("session_id_1")
        assert route.called
        request = route_request(route)
        assert request.method == "GET"
        assert result is not None

    @pytest.mark.respx(base_url=base_url)
    def test_session_question_reject(self, client: Opencode, respx_mock: MockRouter) -> None:
        v2 = V2Resource(client)
        route = respx_mock.post("/api/session/session_id_1/question/request_id_1/reject").mock(
            return_value=httpx.Response(200, json=None)
        )
        result = v2.session.question_reject("session_id_1", "request_id_1")
        assert route.called
        request = route_request(route)
        assert request.method == "POST"
        assert result is None

    @pytest.mark.respx(base_url=base_url)
    def test_session_question_reply(self, client: Opencode, respx_mock: MockRouter) -> None:
        v2 = V2Resource(client)
        route = respx_mock.post("/api/session/session_id_1/question/request_id_1/reply").mock(
            return_value=httpx.Response(200, json=None)
        )
        result = v2.session.question_reply("session_id_1", "request_id_1", answers=[{}])
        assert route.called
        request = route_request(route)
        assert request.method == "POST"
        assert result is None

    @pytest.mark.respx(base_url=base_url)
    def test_session_revert_clear(self, client: Opencode, respx_mock: MockRouter) -> None:
        v2 = V2Resource(client)
        route = respx_mock.post("/api/session/session_id_1/revert/clear").mock(
            return_value=httpx.Response(200, json=None)
        )
        result = v2.session.revert_clear("session_id_1")
        assert route.called
        request = route_request(route)
        assert request.method == "POST"
        assert result is None

    @pytest.mark.respx(base_url=base_url)
    def test_session_revert_commit(self, client: Opencode, respx_mock: MockRouter) -> None:
        v2 = V2Resource(client)
        route = respx_mock.post("/api/session/session_id_1/revert/commit").mock(
            return_value=httpx.Response(200, json=None)
        )
        result = v2.session.revert_commit("session_id_1")
        assert route.called
        request = route_request(route)
        assert request.method == "POST"
        assert result is None

    @pytest.mark.respx(base_url=base_url)
    def test_session_revert_stage(self, client: Opencode, respx_mock: MockRouter) -> None:
        v2 = V2Resource(client)
        route = respx_mock.post("/api/session/session_id_1/revert/stage").mock(
            return_value=httpx.Response(200, json={"data": {}})
        )
        result = v2.session.revert_stage("session_id_1", message_id="x")
        assert route.called
        request = route_request(route)
        assert request.method == "POST"
        body = read_json_body(route)
        assert body["messageID"] == "x"
        assert result is not None

    @pytest.mark.respx(base_url=base_url)
    def test_session_switch_agent(self, client: Opencode, respx_mock: MockRouter) -> None:
        v2 = V2Resource(client)
        route = respx_mock.post("/api/session/session_id_1/agent").mock(return_value=httpx.Response(200, json=None))
        result = v2.session.switch_agent("session_id_1", agent="x")
        assert route.called
        request = route_request(route)
        assert request.method == "POST"
        body = read_json_body(route)
        assert body["agent"] == "x"
        assert result is None

    @pytest.mark.respx(base_url=base_url)
    def test_session_switch_model(self, client: Opencode, respx_mock: MockRouter) -> None:
        v2 = V2Resource(client)
        route = respx_mock.post("/api/session/session_id_1/model").mock(return_value=httpx.Response(200, json=None))
        result = v2.session.switch_model("session_id_1", model={})
        assert route.called
        request = route_request(route)
        assert request.method == "POST"
        assert result is None

    @pytest.mark.respx(base_url=base_url)
    def test_session_wait(self, client: Opencode, respx_mock: MockRouter) -> None:
        v2 = V2Resource(client)
        route = respx_mock.post("/api/session/session_id_1/wait").mock(return_value=httpx.Response(200, json=None))
        result = v2.session.wait("session_id_1")
        assert route.called
        request = route_request(route)
        assert request.method == "POST"
        assert result is None


class TestAsyncV2SessionWire:
    @pytest.mark.respx(base_url=base_url)
    async def test_session_active(self, async_client: AsyncOpencode, respx_mock: MockRouter) -> None:
        v2 = AsyncV2Resource(async_client)
        route = respx_mock.get("/api/session/active").mock(return_value=httpx.Response(200, json={"data": {}}))
        result = await v2.session.active()
        assert route.called
        request = route_request(route)
        assert request.method == "GET"
        assert result is not None

    @pytest.mark.respx(base_url=base_url)
    async def test_session_compact(self, async_client: AsyncOpencode, respx_mock: MockRouter) -> None:
        v2 = AsyncV2Resource(async_client)
        route = respx_mock.post("/api/session/session_id_1/compact").mock(return_value=httpx.Response(200, json=None))
        result = await v2.session.compact("session_id_1")
        assert route.called
        request = route_request(route)
        assert request.method == "POST"
        assert result is None

    @pytest.mark.respx(base_url=base_url)
    async def test_session_context(self, async_client: AsyncOpencode, respx_mock: MockRouter) -> None:
        v2 = AsyncV2Resource(async_client)
        route = respx_mock.get("/api/session/session_id_1/context").mock(
            return_value=httpx.Response(200, json={"data": []})
        )
        result = await v2.session.context("session_id_1")
        assert route.called
        request = route_request(route)
        assert request.method == "GET"
        assert result is not None

    @pytest.mark.respx(base_url=base_url)
    async def test_session_create(self, async_client: AsyncOpencode, respx_mock: MockRouter) -> None:
        v2 = AsyncV2Resource(async_client)
        route = respx_mock.post("/api/session").mock(return_value=httpx.Response(200, json={"data": {}}))
        result = await v2.session.create()
        assert route.called
        request = route_request(route)
        assert request.method == "POST"
        assert result is not None

    @pytest.mark.respx(base_url=base_url)
    async def test_session_events(self, async_client: AsyncOpencode, respx_mock: MockRouter) -> None:
        v2 = AsyncV2Resource(async_client)
        route = respx_mock.get("/api/session/session_id_1/event").mock(
            return_value=httpx.Response(200, content=b"", headers={"content-type": "text/event-stream"})
        )
        await v2.session.events("session_id_1", after="qv")
        assert route.called
        request = route_request(route)
        assert request.method == "GET"
        assert request.url.params.get("after") == "qv"
        assert route.called

    @pytest.mark.respx(base_url=base_url)
    async def test_session_get(self, async_client: AsyncOpencode, respx_mock: MockRouter) -> None:
        v2 = AsyncV2Resource(async_client)
        route = respx_mock.get("/api/session/session_id_1").mock(return_value=httpx.Response(200, json={"data": {}}))
        result = await v2.session.get("session_id_1")
        assert route.called
        request = route_request(route)
        assert request.method == "GET"
        assert result is not None

    @pytest.mark.respx(base_url=base_url)
    async def test_session_history(self, async_client: AsyncOpencode, respx_mock: MockRouter) -> None:
        v2 = AsyncV2Resource(async_client)
        route = respx_mock.get("/api/session/session_id_1/history").mock(
            return_value=httpx.Response(200, json={"data": [], "hasMore": True})
        )
        result = await v2.session.history("session_id_1", limit="qv", after="qv")
        assert route.called
        request = route_request(route)
        assert request.method == "GET"
        assert request.url.params.get("limit") == "qv"
        assert request.url.params.get("after") == "qv"
        assert result is not None

    @pytest.mark.respx(base_url=base_url)
    async def test_session_interrupt(self, async_client: AsyncOpencode, respx_mock: MockRouter) -> None:
        v2 = AsyncV2Resource(async_client)
        route = respx_mock.post("/api/session/session_id_1/interrupt").mock(return_value=httpx.Response(200, json=None))
        result = await v2.session.interrupt("session_id_1")
        assert route.called
        request = route_request(route)
        assert request.method == "POST"
        assert result is None

    @pytest.mark.respx(base_url=base_url)
    async def test_session_list(self, async_client: AsyncOpencode, respx_mock: MockRouter) -> None:
        v2 = AsyncV2Resource(async_client)
        route = respx_mock.get("/api/session").mock(return_value=httpx.Response(200, json={"data": [], "cursor": {}}))
        result = await v2.session.list(
            workspace="qv", search="qv", directory="qv", project="qv", subpath="qv", cursor="qv"
        )
        assert route.called
        request = route_request(route)
        assert request.method == "GET"
        assert request.url.params.get("workspace") == "qv"
        assert request.url.params.get("search") == "qv"
        assert request.url.params.get("directory") == "qv"
        assert request.url.params.get("project") == "qv"
        assert request.url.params.get("subpath") == "qv"
        assert request.url.params.get("cursor") == "qv"
        assert result is not None

    @pytest.mark.respx(base_url=base_url)
    async def test_session_message(self, async_client: AsyncOpencode, respx_mock: MockRouter) -> None:
        v2 = AsyncV2Resource(async_client)
        route = respx_mock.get("/api/session/session_id_1/message/message_id_1").mock(
            return_value=httpx.Response(200, json={"data": {}})
        )
        result = await v2.session.message("session_id_1", "message_id_1")
        assert route.called
        request = route_request(route)
        assert request.method == "GET"
        assert result is not None

    @pytest.mark.respx(base_url=base_url)
    async def test_session_messages(self, async_client: AsyncOpencode, respx_mock: MockRouter) -> None:
        v2 = AsyncV2Resource(async_client)
        route = respx_mock.get("/api/session/session_id_1/message").mock(
            return_value=httpx.Response(200, json={"data": [], "cursor": {}})
        )
        result = await v2.session.messages("session_id_1", cursor="qv")
        assert route.called
        request = route_request(route)
        assert request.method == "GET"
        assert request.url.params.get("cursor") == "qv"
        assert result is not None

    @pytest.mark.respx(base_url=base_url)
    async def test_session_permission_create(self, async_client: AsyncOpencode, respx_mock: MockRouter) -> None:
        v2 = AsyncV2Resource(async_client)
        route = respx_mock.post("/api/session/session_id_1/permission").mock(
            return_value=httpx.Response(200, json={"data": {}})
        )
        result = await v2.session.permission_create("session_id_1", action="x", resources=["x"])
        assert route.called
        request = route_request(route)
        assert request.method == "POST"
        body = read_json_body(route)
        assert body["action"] == "x"
        assert result is not None

    @pytest.mark.respx(base_url=base_url)
    async def test_session_permission_get(self, async_client: AsyncOpencode, respx_mock: MockRouter) -> None:
        v2 = AsyncV2Resource(async_client)
        route = respx_mock.get("/api/session/session_id_1/permission/request_id_1").mock(
            return_value=httpx.Response(200, json={"data": {}})
        )
        result = await v2.session.permission_get("session_id_1", "request_id_1")
        assert route.called
        request = route_request(route)
        assert request.method == "GET"
        assert result is not None

    @pytest.mark.respx(base_url=base_url)
    async def test_session_permission_list(self, async_client: AsyncOpencode, respx_mock: MockRouter) -> None:
        v2 = AsyncV2Resource(async_client)
        route = respx_mock.get("/api/session/session_id_1/permission").mock(
            return_value=httpx.Response(200, json={"data": []})
        )
        result = await v2.session.permission_list("session_id_1")
        assert route.called
        request = route_request(route)
        assert request.method == "GET"
        assert result is not None

    @pytest.mark.respx(base_url=base_url)
    async def test_session_permission_reply(self, async_client: AsyncOpencode, respx_mock: MockRouter) -> None:
        v2 = AsyncV2Resource(async_client)
        route = respx_mock.post("/api/session/session_id_1/permission/request_id_1/reply").mock(
            return_value=httpx.Response(200, json=None)
        )
        result = await v2.session.permission_reply("session_id_1", "request_id_1", reply="once")
        assert route.called
        request = route_request(route)
        assert request.method == "POST"
        assert result is None

    @pytest.mark.respx(base_url=base_url)
    async def test_session_prompt(self, async_client: AsyncOpencode, respx_mock: MockRouter) -> None:
        v2 = AsyncV2Resource(async_client)
        route = respx_mock.post("/api/session/session_id_1/prompt").mock(
            return_value=httpx.Response(200, json={"data": {}})
        )
        result = await v2.session.prompt("session_id_1", prompt={})
        assert route.called
        request = route_request(route)
        assert request.method == "POST"
        assert result is not None

    @pytest.mark.respx(base_url=base_url)
    async def test_session_question_list(self, async_client: AsyncOpencode, respx_mock: MockRouter) -> None:
        v2 = AsyncV2Resource(async_client)
        route = respx_mock.get("/api/session/session_id_1/question").mock(
            return_value=httpx.Response(200, json={"data": []})
        )
        result = await v2.session.question_list("session_id_1")
        assert route.called
        request = route_request(route)
        assert request.method == "GET"
        assert result is not None

    @pytest.mark.respx(base_url=base_url)
    async def test_session_question_reject(self, async_client: AsyncOpencode, respx_mock: MockRouter) -> None:
        v2 = AsyncV2Resource(async_client)
        route = respx_mock.post("/api/session/session_id_1/question/request_id_1/reject").mock(
            return_value=httpx.Response(200, json=None)
        )
        result = await v2.session.question_reject("session_id_1", "request_id_1")
        assert route.called
        request = route_request(route)
        assert request.method == "POST"
        assert result is None

    @pytest.mark.respx(base_url=base_url)
    async def test_session_question_reply(self, async_client: AsyncOpencode, respx_mock: MockRouter) -> None:
        v2 = AsyncV2Resource(async_client)
        route = respx_mock.post("/api/session/session_id_1/question/request_id_1/reply").mock(
            return_value=httpx.Response(200, json=None)
        )
        result = await v2.session.question_reply("session_id_1", "request_id_1", answers=[{}])
        assert route.called
        request = route_request(route)
        assert request.method == "POST"
        assert result is None

    @pytest.mark.respx(base_url=base_url)
    async def test_session_revert_clear(self, async_client: AsyncOpencode, respx_mock: MockRouter) -> None:
        v2 = AsyncV2Resource(async_client)
        route = respx_mock.post("/api/session/session_id_1/revert/clear").mock(
            return_value=httpx.Response(200, json=None)
        )
        result = await v2.session.revert_clear("session_id_1")
        assert route.called
        request = route_request(route)
        assert request.method == "POST"
        assert result is None

    @pytest.mark.respx(base_url=base_url)
    async def test_session_revert_commit(self, async_client: AsyncOpencode, respx_mock: MockRouter) -> None:
        v2 = AsyncV2Resource(async_client)
        route = respx_mock.post("/api/session/session_id_1/revert/commit").mock(
            return_value=httpx.Response(200, json=None)
        )
        result = await v2.session.revert_commit("session_id_1")
        assert route.called
        request = route_request(route)
        assert request.method == "POST"
        assert result is None

    @pytest.mark.respx(base_url=base_url)
    async def test_session_revert_stage(self, async_client: AsyncOpencode, respx_mock: MockRouter) -> None:
        v2 = AsyncV2Resource(async_client)
        route = respx_mock.post("/api/session/session_id_1/revert/stage").mock(
            return_value=httpx.Response(200, json={"data": {}})
        )
        result = await v2.session.revert_stage("session_id_1", message_id="x")
        assert route.called
        request = route_request(route)
        assert request.method == "POST"
        body = read_json_body(route)
        assert body["messageID"] == "x"
        assert result is not None

    @pytest.mark.respx(base_url=base_url)
    async def test_session_switch_agent(self, async_client: AsyncOpencode, respx_mock: MockRouter) -> None:
        v2 = AsyncV2Resource(async_client)
        route = respx_mock.post("/api/session/session_id_1/agent").mock(return_value=httpx.Response(200, json=None))
        result = await v2.session.switch_agent("session_id_1", agent="x")
        assert route.called
        request = route_request(route)
        assert request.method == "POST"
        body = read_json_body(route)
        assert body["agent"] == "x"
        assert result is None

    @pytest.mark.respx(base_url=base_url)
    async def test_session_switch_model(self, async_client: AsyncOpencode, respx_mock: MockRouter) -> None:
        v2 = AsyncV2Resource(async_client)
        route = respx_mock.post("/api/session/session_id_1/model").mock(return_value=httpx.Response(200, json=None))
        result = await v2.session.switch_model("session_id_1", model={})
        assert route.called
        request = route_request(route)
        assert request.method == "POST"
        assert result is None

    @pytest.mark.respx(base_url=base_url)
    async def test_session_wait(self, async_client: AsyncOpencode, respx_mock: MockRouter) -> None:
        v2 = AsyncV2Resource(async_client)
        route = respx_mock.post("/api/session/session_id_1/wait").mock(return_value=httpx.Response(200, json=None))
        result = await v2.session.wait("session_id_1")
        assert route.called
        request = route_request(route)
        assert request.method == "POST"
        assert result is None
