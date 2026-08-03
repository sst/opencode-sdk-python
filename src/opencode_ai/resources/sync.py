# Hand-maintained fork of the Stainless-era opencode SDK. Generated code was replaced by manual maintenance; see CONTRIBUTING.md.

from __future__ import annotations

from typing import Dict, Iterable

import httpx

from ..types import addressing_params, sync_steal_params, sync_replay_params, sync_history_list_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.sync_start_response import SyncStartResponse
from ..types.sync_steal_response import SyncStealResponse
from ..types.sync_replay_response import SyncReplayResponse
from ..types.sync_history_list_response import SyncHistoryListResponse

__all__ = ["SyncResource", "AsyncSyncResource"]


class SyncResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SyncResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/sst/opencode-sdk-python#accessing-raw-response-data-eg-headers
        """
        return SyncResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SyncResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/sst/opencode-sdk-python#with_streaming_response
        """
        return SyncResourceWithStreamingResponse(self)

    def history_list(
        self,
        body: Dict[str, int] | NotGiven = NOT_GIVEN,
        *,
        directory: str | NotGiven = NOT_GIVEN,
        workspace: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncHistoryListResponse:
        """
        List sync events for all aggregates. Keys are aggregate IDs the client
        already knows about, values are the last known sequence ID. Events with
        seq > value are returned for those aggregates. Aggregates not listed in the
        input get their full history.

        Args:
          body: Map of aggregate ID to the last known sequence number the client has seen.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/sync/history",
            body=maybe_transform(body, sync_history_list_params.SyncHistoryListParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "directory": directory,
                        "workspace": workspace,
                    },
                    addressing_params.AddressingParams,
                ),
            ),
            cast_to=SyncHistoryListResponse,
        )

    def replay(
        self,
        *,
        directory: str,
        events: Iterable[sync_replay_params.Event],
        query_directory: str | NotGiven = NOT_GIVEN,
        workspace: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncReplayResponse:
        """
        Validate and replay a complete sync event history.

        Args:
          directory: Directory whose sync events should be replayed.

              Note: this is a request body field, distinct from the `directory` query
              parameter that may also be present on this same request.

          events: Full sync event history to replay, in order.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/sync/replay",
            body=maybe_transform(
                {
                    "directory": directory,
                    "events": events,
                },
                sync_replay_params.SyncReplayParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "directory": query_directory,
                        "workspace": workspace,
                    },
                    addressing_params.AddressingParams,
                ),
            ),
            cast_to=SyncReplayResponse,
        )

    def start(
        self,
        *,
        directory: str | NotGiven = NOT_GIVEN,
        workspace: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncStartResponse:
        """
        Start sync loops for workspaces in the current project that have active
        sessions.
        """
        return self._post(
            "/sync/start",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "directory": directory,
                        "workspace": workspace,
                    },
                    addressing_params.AddressingParams,
                ),
            ),
            cast_to=SyncStartResponse,
        )

    def steal(
        self,
        *,
        session_id: str,
        directory: str | NotGiven = NOT_GIVEN,
        workspace: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncStealResponse:
        """
        Update a session to belong to the current workspace through the sync event
        system.

        Args:
          session_id: Session ID to steal into the current workspace.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/sync/steal",
            body=maybe_transform({"session_id": session_id}, sync_steal_params.SyncStealParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "directory": directory,
                        "workspace": workspace,
                    },
                    addressing_params.AddressingParams,
                ),
            ),
            cast_to=SyncStealResponse,
        )


class AsyncSyncResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSyncResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/sst/opencode-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSyncResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSyncResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/sst/opencode-sdk-python#with_streaming_response
        """
        return AsyncSyncResourceWithStreamingResponse(self)

    async def history_list(
        self,
        body: Dict[str, int] | NotGiven = NOT_GIVEN,
        *,
        directory: str | NotGiven = NOT_GIVEN,
        workspace: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncHistoryListResponse:
        """
        List sync events for all aggregates. Keys are aggregate IDs the client
        already knows about, values are the last known sequence ID. Events with
        seq > value are returned for those aggregates. Aggregates not listed in the
        input get their full history.

        Args:
          body: Map of aggregate ID to the last known sequence number the client has seen.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/sync/history",
            body=await async_maybe_transform(body, sync_history_list_params.SyncHistoryListParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "directory": directory,
                        "workspace": workspace,
                    },
                    addressing_params.AddressingParams,
                ),
            ),
            cast_to=SyncHistoryListResponse,
        )

    async def replay(
        self,
        *,
        directory: str,
        events: Iterable[sync_replay_params.Event],
        query_directory: str | NotGiven = NOT_GIVEN,
        workspace: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncReplayResponse:
        """
        Validate and replay a complete sync event history.

        Args:
          directory: Directory whose sync events should be replayed.

              Note: this is a request body field, distinct from the `directory` query
              parameter that may also be present on this same request.

          events: Full sync event history to replay, in order.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/sync/replay",
            body=await async_maybe_transform(
                {
                    "directory": directory,
                    "events": events,
                },
                sync_replay_params.SyncReplayParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "directory": query_directory,
                        "workspace": workspace,
                    },
                    addressing_params.AddressingParams,
                ),
            ),
            cast_to=SyncReplayResponse,
        )

    async def start(
        self,
        *,
        directory: str | NotGiven = NOT_GIVEN,
        workspace: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncStartResponse:
        """
        Start sync loops for workspaces in the current project that have active
        sessions.
        """
        return await self._post(
            "/sync/start",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "directory": directory,
                        "workspace": workspace,
                    },
                    addressing_params.AddressingParams,
                ),
            ),
            cast_to=SyncStartResponse,
        )

    async def steal(
        self,
        *,
        session_id: str,
        directory: str | NotGiven = NOT_GIVEN,
        workspace: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncStealResponse:
        """
        Update a session to belong to the current workspace through the sync event
        system.

        Args:
          session_id: Session ID to steal into the current workspace.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/sync/steal",
            body=await async_maybe_transform({"session_id": session_id}, sync_steal_params.SyncStealParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "directory": directory,
                        "workspace": workspace,
                    },
                    addressing_params.AddressingParams,
                ),
            ),
            cast_to=SyncStealResponse,
        )


class SyncResourceWithRawResponse:
    def __init__(self, sync: SyncResource) -> None:
        self._sync = sync

        self.history_list = to_raw_response_wrapper(
            sync.history_list,
        )
        self.replay = to_raw_response_wrapper(
            sync.replay,
        )
        self.start = to_raw_response_wrapper(
            sync.start,
        )
        self.steal = to_raw_response_wrapper(
            sync.steal,
        )


class AsyncSyncResourceWithRawResponse:
    def __init__(self, sync: AsyncSyncResource) -> None:
        self._sync = sync

        self.history_list = async_to_raw_response_wrapper(
            sync.history_list,
        )
        self.replay = async_to_raw_response_wrapper(
            sync.replay,
        )
        self.start = async_to_raw_response_wrapper(
            sync.start,
        )
        self.steal = async_to_raw_response_wrapper(
            sync.steal,
        )


class SyncResourceWithStreamingResponse:
    def __init__(self, sync: SyncResource) -> None:
        self._sync = sync

        self.history_list = to_streamed_response_wrapper(
            sync.history_list,
        )
        self.replay = to_streamed_response_wrapper(
            sync.replay,
        )
        self.start = to_streamed_response_wrapper(
            sync.start,
        )
        self.steal = to_streamed_response_wrapper(
            sync.steal,
        )


class AsyncSyncResourceWithStreamingResponse:
    def __init__(self, sync: AsyncSyncResource) -> None:
        self._sync = sync

        self.history_list = async_to_streamed_response_wrapper(
            sync.history_list,
        )
        self.replay = async_to_streamed_response_wrapper(
            sync.replay,
        )
        self.start = async_to_streamed_response_wrapper(
            sync.start,
        )
        self.steal = async_to_streamed_response_wrapper(
            sync.steal,
        )
