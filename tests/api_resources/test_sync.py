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
    SyncStartResponse,
    SyncStealResponse,
    SyncReplayResponse,
    SyncHistoryListResponse,
)
from tests.wire_helpers import route_request, read_json_body

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")

HISTORY_EVENT_SAMPLE: dict[str, object] = {
    "id": "evt_1",
    "aggregate_id": "agg_1",
    "seq": 1,
    "type": "session.created",
    "data": {},
}


class TestSync:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_history_list(self, client: Opencode) -> None:
        sync = client.sync.history_list()
        assert_matches_type(SyncHistoryListResponse, sync, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_history_list_with_all_params(self, client: Opencode) -> None:
        sync = client.sync.history_list(
            {"agg_1": 0},
        )
        assert_matches_type(SyncHistoryListResponse, sync, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_history_list(self, client: Opencode) -> None:
        response = client.sync.with_raw_response.history_list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sync = response.parse()
        assert_matches_type(SyncHistoryListResponse, sync, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_history_list(self, client: Opencode) -> None:
        with client.sync.with_streaming_response.history_list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sync = response.parse()
            assert_matches_type(SyncHistoryListResponse, sync, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_replay(self, client: Opencode) -> None:
        sync = client.sync.replay(
            directory="directory",
            events=[
                {
                    "id": "id",
                    "aggregate_id": "aggregateID",
                    "data": {},
                    "seq": 0,
                    "type": "type",
                }
            ],
        )
        assert_matches_type(SyncReplayResponse, sync, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_replay(self, client: Opencode) -> None:
        response = client.sync.with_raw_response.replay(
            directory="directory",
            events=[
                {
                    "id": "id",
                    "aggregate_id": "aggregateID",
                    "data": {},
                    "seq": 0,
                    "type": "type",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sync = response.parse()
        assert_matches_type(SyncReplayResponse, sync, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_replay(self, client: Opencode) -> None:
        with client.sync.with_streaming_response.replay(
            directory="directory",
            events=[
                {
                    "id": "id",
                    "aggregate_id": "aggregateID",
                    "data": {},
                    "seq": 0,
                    "type": "type",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sync = response.parse()
            assert_matches_type(SyncReplayResponse, sync, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_start(self, client: Opencode) -> None:
        sync = client.sync.start()
        assert_matches_type(SyncStartResponse, sync, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_start(self, client: Opencode) -> None:
        response = client.sync.with_raw_response.start()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sync = response.parse()
        assert_matches_type(SyncStartResponse, sync, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_start(self, client: Opencode) -> None:
        with client.sync.with_streaming_response.start() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sync = response.parse()
            assert_matches_type(SyncStartResponse, sync, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_steal(self, client: Opencode) -> None:
        sync = client.sync.steal(
            session_id="sessionID",
        )
        assert_matches_type(SyncStealResponse, sync, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_steal(self, client: Opencode) -> None:
        response = client.sync.with_raw_response.steal(
            session_id="sessionID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sync = response.parse()
        assert_matches_type(SyncStealResponse, sync, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_steal(self, client: Opencode) -> None:
        with client.sync.with_streaming_response.steal(
            session_id="sessionID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sync = response.parse()
            assert_matches_type(SyncStealResponse, sync, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestSyncWire:
    @pytest.mark.respx(base_url=base_url)
    def test_history_list_wire_shape(self, client: Opencode, respx_mock: MockRouter) -> None:
        route = respx_mock.post("/sync/history").mock(
            return_value=httpx.Response(200, json=[HISTORY_EVENT_SAMPLE])
        )
        result = client.sync.history_list({"agg_1": 5})
        assert route.called
        request = route_request(route)
        assert request.method == "POST"
        body = read_json_body(route)
        assert body == {"agg_1": 5}
        assert_matches_type(SyncHistoryListResponse, result, path=["response"])
        # Confirm the response's snake_case `aggregate_id` wire field parses correctly
        # (spec's own casing for this operation -- NOT aliased, unlike sync.replay below).
        assert result[0].aggregate_id == "agg_1"

    @pytest.mark.respx(base_url=base_url)
    def test_replay_sends_camelcase_aggregate_id(self, client: Opencode, respx_mock: MockRouter) -> None:
        route = respx_mock.post("/sync/replay").mock(
            return_value=httpx.Response(200, json={"sessionID": "ses_replayed"})
        )
        result = client.sync.replay(
            directory="/repo",
            events=[
                {
                    "id": "evt_1",
                    "aggregate_id": "agg_1",
                    "data": {},
                    "seq": 0,
                    "type": "session.created",
                }
            ],
        )
        assert route.called
        request = route_request(route)
        assert request.method == "POST"
        body = read_json_body(route)
        # The Python-side `aggregate_id` param must serialize to the wire's
        # camelCase `aggregateID` key -- this operation's own schema uses
        # camelCase, unlike sync.history.list's response (snake_case), per the
        # spec's genuine (not normalized) casing inconsistency.
        assert body == {
            "directory": "/repo",
            "events": [
                {
                    "id": "evt_1",
                    "aggregateID": "agg_1",
                    "data": {},
                    "seq": 0,
                    "type": "session.created",
                }
            ],
        }
        assert_matches_type(SyncReplayResponse, result, path=["response"])
        assert result.session_id == "ses_replayed"

    @pytest.mark.respx(base_url=base_url)
    def test_start_wire_shape(self, client: Opencode, respx_mock: MockRouter) -> None:
        route = respx_mock.post("/sync/start").mock(return_value=httpx.Response(200, json=True))
        result = client.sync.start()
        assert route.called
        assert route.calls.last.request.method == "POST"
        assert_matches_type(SyncStartResponse, result, path=["response"])

    @pytest.mark.respx(base_url=base_url)
    def test_steal_sends_camelcase_session_id(self, client: Opencode, respx_mock: MockRouter) -> None:
        route = respx_mock.post("/sync/steal").mock(
            return_value=httpx.Response(200, json={"sessionID": "ses_stolen"})
        )
        result = client.sync.steal(session_id="ses_target")
        assert route.called
        body = read_json_body(route)
        assert body == {"sessionID": "ses_target"}
        assert_matches_type(SyncStealResponse, result, path=["response"])
        assert result.session_id == "ses_stolen"


class TestAsyncSync:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_history_list(self, async_client: AsyncOpencode) -> None:
        sync = await async_client.sync.history_list()
        assert_matches_type(SyncHistoryListResponse, sync, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_history_list(self, async_client: AsyncOpencode) -> None:
        response = await async_client.sync.with_raw_response.history_list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sync = await response.parse()
        assert_matches_type(SyncHistoryListResponse, sync, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_history_list(self, async_client: AsyncOpencode) -> None:
        async with async_client.sync.with_streaming_response.history_list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sync = await response.parse()
            assert_matches_type(SyncHistoryListResponse, sync, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_replay(self, async_client: AsyncOpencode) -> None:
        sync = await async_client.sync.replay(
            directory="directory",
            events=[
                {
                    "id": "id",
                    "aggregate_id": "aggregateID",
                    "data": {},
                    "seq": 0,
                    "type": "type",
                }
            ],
        )
        assert_matches_type(SyncReplayResponse, sync, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_replay(self, async_client: AsyncOpencode) -> None:
        response = await async_client.sync.with_raw_response.replay(
            directory="directory",
            events=[
                {
                    "id": "id",
                    "aggregate_id": "aggregateID",
                    "data": {},
                    "seq": 0,
                    "type": "type",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sync = await response.parse()
        assert_matches_type(SyncReplayResponse, sync, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_replay(self, async_client: AsyncOpencode) -> None:
        async with async_client.sync.with_streaming_response.replay(
            directory="directory",
            events=[
                {
                    "id": "id",
                    "aggregate_id": "aggregateID",
                    "data": {},
                    "seq": 0,
                    "type": "type",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sync = await response.parse()
            assert_matches_type(SyncReplayResponse, sync, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_start(self, async_client: AsyncOpencode) -> None:
        sync = await async_client.sync.start()
        assert_matches_type(SyncStartResponse, sync, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_start(self, async_client: AsyncOpencode) -> None:
        response = await async_client.sync.with_raw_response.start()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sync = await response.parse()
        assert_matches_type(SyncStartResponse, sync, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_start(self, async_client: AsyncOpencode) -> None:
        async with async_client.sync.with_streaming_response.start() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sync = await response.parse()
            assert_matches_type(SyncStartResponse, sync, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_steal(self, async_client: AsyncOpencode) -> None:
        sync = await async_client.sync.steal(
            session_id="sessionID",
        )
        assert_matches_type(SyncStealResponse, sync, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_steal(self, async_client: AsyncOpencode) -> None:
        response = await async_client.sync.with_raw_response.steal(
            session_id="sessionID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sync = await response.parse()
        assert_matches_type(SyncStealResponse, sync, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_steal(self, async_client: AsyncOpencode) -> None:
        async with async_client.sync.with_streaming_response.steal(
            session_id="sessionID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sync = await response.parse()
            assert_matches_type(SyncStealResponse, sync, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSyncWire:
    @pytest.mark.respx(base_url=base_url)
    async def test_history_list_wire_shape(self, async_client: AsyncOpencode, respx_mock: MockRouter) -> None:
        route = respx_mock.post("/sync/history").mock(
            return_value=httpx.Response(200, json=[HISTORY_EVENT_SAMPLE])
        )
        result = await async_client.sync.history_list({"agg_1": 5})
        assert route.called
        assert route.calls.last.request.method == "POST"
        assert_matches_type(SyncHistoryListResponse, result, path=["response"])
        assert result[0].aggregate_id == "agg_1"

    @pytest.mark.respx(base_url=base_url)
    async def test_replay_sends_camelcase_aggregate_id(
        self, async_client: AsyncOpencode, respx_mock: MockRouter
    ) -> None:
        route = respx_mock.post("/sync/replay").mock(
            return_value=httpx.Response(200, json={"sessionID": "ses_replayed"})
        )
        result = await async_client.sync.replay(
            directory="/repo",
            events=[
                {
                    "id": "evt_1",
                    "aggregate_id": "agg_1",
                    "data": {},
                    "seq": 0,
                    "type": "session.created",
                }
            ],
        )
        assert route.called
        body = read_json_body(route)
        assert body["events"] == [
            {
                "id": "evt_1",
                "aggregateID": "agg_1",
                "data": {},
                "seq": 0,
                "type": "session.created",
            }
        ]
        assert_matches_type(SyncReplayResponse, result, path=["response"])
        assert result.session_id == "ses_replayed"

    @pytest.mark.respx(base_url=base_url)
    async def test_steal_sends_camelcase_session_id(
        self, async_client: AsyncOpencode, respx_mock: MockRouter
    ) -> None:
        route = respx_mock.post("/sync/steal").mock(
            return_value=httpx.Response(200, json={"sessionID": "ses_stolen"})
        )
        result = await async_client.sync.steal(session_id="ses_target")
        assert route.called
        body = read_json_body(route)
        assert body == {"sessionID": "ses_target"}
        assert_matches_type(SyncStealResponse, result, path=["response"])
        assert result.session_id == "ses_stolen"
