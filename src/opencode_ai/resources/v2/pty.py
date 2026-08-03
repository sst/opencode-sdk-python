# Hand-maintained fork of the Stainless-era opencode SDK. Generated code was replaced by manual maintenance; see CONTRIBUTING.md.

from __future__ import annotations

from typing import Dict, List

import httpx

from ...types import v2_pty_create_params, v2_pty_update_params, v2_pty_connect_params, v2_location_query_params
from ..._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.v2_pty_get_response import V2PtyGetResponse
from ...types.v2_pty_list_response import V2PtyListResponse
from ...types.v2_pty_create_response import V2PtyCreateResponse
from ...types.v2_pty_update_response import V2PtyUpdateResponse
from ...types.v2_location_query_params import V2Location
from ...types.v2_pty_connect_token_response import V2PtyConnectTokenResponse

__all__ = ["V2PtyResource", "AsyncV2PtyResource"]


class V2PtyResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> V2PtyResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/sst/opencode-sdk-python#accessing-raw-response-data-eg-headers
        """
        return V2PtyResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> V2PtyResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/sst/opencode-sdk-python#with_streaming_response
        """
        return V2PtyResourceWithStreamingResponse(self)

    def connect(
        self,
        pty_id: str,
        *,
        directory: str | NotGiven = NOT_GIVEN,
        workspace: str | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        ticket: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> bool:
        """Connect to PTY session"""
        if not pty_id:
            raise ValueError(f"Expected a non-empty value for `pty_id` but received {pty_id!r}")
        return self._get(
            f"/api/pty/{pty_id}/connect",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "directory": directory,
                        "workspace": workspace,
                        "cursor": cursor,
                        "ticket": ticket,
                    },
                    v2_pty_connect_params.V2PtyConnectParams,
                ),
            ),
            cast_to=bool,
        )

    def connect_token(
        self,
        pty_id: str,
        *,
        location: V2Location | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V2PtyConnectTokenResponse:
        """Create PTY WebSocket token"""
        if not pty_id:
            raise ValueError(f"Expected a non-empty value for `pty_id` but received {pty_id!r}")
        return self._post(
            f"/api/pty/{pty_id}/connect-token",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"location": location},
                    v2_location_query_params.V2LocationQueryParams,
                ),
            ),
            cast_to=V2PtyConnectTokenResponse,
        )

    def create(
        self,
        *,
        command: str | NotGiven = NOT_GIVEN,
        args: List[str] | NotGiven = NOT_GIVEN,
        cwd: str | NotGiven = NOT_GIVEN,
        title: str | NotGiven = NOT_GIVEN,
        env: Dict[str, object] | NotGiven = NOT_GIVEN,
        location: V2Location | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V2PtyCreateResponse:
        """Create PTY session"""
        return self._post(
            "/api/pty",
            body=maybe_transform(
                {
                    "command": command,
                    "args": args,
                    "cwd": cwd,
                    "title": title,
                    "env": env,
                },
                v2_pty_create_params.V2PtyCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"location": location},
                    v2_location_query_params.V2LocationQueryParams,
                ),
            ),
            cast_to=V2PtyCreateResponse,
        )

    def get(
        self,
        pty_id: str,
        *,
        location: V2Location | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V2PtyGetResponse:
        """Get PTY session"""
        if not pty_id:
            raise ValueError(f"Expected a non-empty value for `pty_id` but received {pty_id!r}")
        return self._get(
            f"/api/pty/{pty_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"location": location},
                    v2_location_query_params.V2LocationQueryParams,
                ),
            ),
            cast_to=V2PtyGetResponse,
        )

    def list(
        self,
        *,
        location: V2Location | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V2PtyListResponse:
        """List PTY sessions"""
        return self._get(
            "/api/pty",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"location": location},
                    v2_location_query_params.V2LocationQueryParams,
                ),
            ),
            cast_to=V2PtyListResponse,
        )

    def remove(
        self,
        pty_id: str,
        *,
        location: V2Location | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Remove PTY session"""
        if not pty_id:
            raise ValueError(f"Expected a non-empty value for `pty_id` but received {pty_id!r}")
        return self._delete(
            f"/api/pty/{pty_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"location": location},
                    v2_location_query_params.V2LocationQueryParams,
                ),
            ),
            cast_to=NoneType,
        )

    def update(
        self,
        pty_id: str,
        *,
        title: str | NotGiven = NOT_GIVEN,
        size: object | NotGiven = NOT_GIVEN,
        location: V2Location | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V2PtyUpdateResponse:
        """Update PTY session"""
        if not pty_id:
            raise ValueError(f"Expected a non-empty value for `pty_id` but received {pty_id!r}")
        return self._put(
            f"/api/pty/{pty_id}",
            body=maybe_transform(
                {
                    "title": title,
                    "size": size,
                },
                v2_pty_update_params.V2PtyUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"location": location},
                    v2_location_query_params.V2LocationQueryParams,
                ),
            ),
            cast_to=V2PtyUpdateResponse,
        )


class AsyncV2PtyResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncV2PtyResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/sst/opencode-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncV2PtyResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncV2PtyResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/sst/opencode-sdk-python#with_streaming_response
        """
        return AsyncV2PtyResourceWithStreamingResponse(self)

    async def connect(
        self,
        pty_id: str,
        *,
        directory: str | NotGiven = NOT_GIVEN,
        workspace: str | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        ticket: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> bool:
        """Connect to PTY session"""
        if not pty_id:
            raise ValueError(f"Expected a non-empty value for `pty_id` but received {pty_id!r}")
        return await self._get(
            f"/api/pty/{pty_id}/connect",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "directory": directory,
                        "workspace": workspace,
                        "cursor": cursor,
                        "ticket": ticket,
                    },
                    v2_pty_connect_params.V2PtyConnectParams,
                ),
            ),
            cast_to=bool,
        )

    async def connect_token(
        self,
        pty_id: str,
        *,
        location: V2Location | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V2PtyConnectTokenResponse:
        """Create PTY WebSocket token"""
        if not pty_id:
            raise ValueError(f"Expected a non-empty value for `pty_id` but received {pty_id!r}")
        return await self._post(
            f"/api/pty/{pty_id}/connect-token",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"location": location},
                    v2_location_query_params.V2LocationQueryParams,
                ),
            ),
            cast_to=V2PtyConnectTokenResponse,
        )

    async def create(
        self,
        *,
        command: str | NotGiven = NOT_GIVEN,
        args: List[str] | NotGiven = NOT_GIVEN,
        cwd: str | NotGiven = NOT_GIVEN,
        title: str | NotGiven = NOT_GIVEN,
        env: Dict[str, object] | NotGiven = NOT_GIVEN,
        location: V2Location | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V2PtyCreateResponse:
        """Create PTY session"""
        return await self._post(
            "/api/pty",
            body=await async_maybe_transform(
                {
                    "command": command,
                    "args": args,
                    "cwd": cwd,
                    "title": title,
                    "env": env,
                },
                v2_pty_create_params.V2PtyCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"location": location},
                    v2_location_query_params.V2LocationQueryParams,
                ),
            ),
            cast_to=V2PtyCreateResponse,
        )

    async def get(
        self,
        pty_id: str,
        *,
        location: V2Location | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V2PtyGetResponse:
        """Get PTY session"""
        if not pty_id:
            raise ValueError(f"Expected a non-empty value for `pty_id` but received {pty_id!r}")
        return await self._get(
            f"/api/pty/{pty_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"location": location},
                    v2_location_query_params.V2LocationQueryParams,
                ),
            ),
            cast_to=V2PtyGetResponse,
        )

    async def list(
        self,
        *,
        location: V2Location | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V2PtyListResponse:
        """List PTY sessions"""
        return await self._get(
            "/api/pty",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"location": location},
                    v2_location_query_params.V2LocationQueryParams,
                ),
            ),
            cast_to=V2PtyListResponse,
        )

    async def remove(
        self,
        pty_id: str,
        *,
        location: V2Location | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Remove PTY session"""
        if not pty_id:
            raise ValueError(f"Expected a non-empty value for `pty_id` but received {pty_id!r}")
        return await self._delete(
            f"/api/pty/{pty_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"location": location},
                    v2_location_query_params.V2LocationQueryParams,
                ),
            ),
            cast_to=NoneType,
        )

    async def update(
        self,
        pty_id: str,
        *,
        title: str | NotGiven = NOT_GIVEN,
        size: object | NotGiven = NOT_GIVEN,
        location: V2Location | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V2PtyUpdateResponse:
        """Update PTY session"""
        if not pty_id:
            raise ValueError(f"Expected a non-empty value for `pty_id` but received {pty_id!r}")
        return await self._put(
            f"/api/pty/{pty_id}",
            body=await async_maybe_transform(
                {
                    "title": title,
                    "size": size,
                },
                v2_pty_update_params.V2PtyUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"location": location},
                    v2_location_query_params.V2LocationQueryParams,
                ),
            ),
            cast_to=V2PtyUpdateResponse,
        )


class V2PtyResourceWithRawResponse:
    def __init__(self, pty: V2PtyResource) -> None:
        self._pty = pty

        self.connect = to_raw_response_wrapper(
            pty.connect,
        )
        self.connect_token = to_raw_response_wrapper(
            pty.connect_token,
        )
        self.create = to_raw_response_wrapper(
            pty.create,
        )
        self.get = to_raw_response_wrapper(
            pty.get,
        )
        self.list = to_raw_response_wrapper(
            pty.list,
        )
        self.remove = to_raw_response_wrapper(
            pty.remove,
        )
        self.update = to_raw_response_wrapper(
            pty.update,
        )


class AsyncV2PtyResourceWithRawResponse:
    def __init__(self, pty: AsyncV2PtyResource) -> None:
        self._pty = pty

        self.connect = async_to_raw_response_wrapper(
            pty.connect,
        )
        self.connect_token = async_to_raw_response_wrapper(
            pty.connect_token,
        )
        self.create = async_to_raw_response_wrapper(
            pty.create,
        )
        self.get = async_to_raw_response_wrapper(
            pty.get,
        )
        self.list = async_to_raw_response_wrapper(
            pty.list,
        )
        self.remove = async_to_raw_response_wrapper(
            pty.remove,
        )
        self.update = async_to_raw_response_wrapper(
            pty.update,
        )


class V2PtyResourceWithStreamingResponse:
    def __init__(self, pty: V2PtyResource) -> None:
        self._pty = pty

        self.connect = to_streamed_response_wrapper(
            pty.connect,
        )
        self.connect_token = to_streamed_response_wrapper(
            pty.connect_token,
        )
        self.create = to_streamed_response_wrapper(
            pty.create,
        )
        self.get = to_streamed_response_wrapper(
            pty.get,
        )
        self.list = to_streamed_response_wrapper(
            pty.list,
        )
        self.remove = to_streamed_response_wrapper(
            pty.remove,
        )
        self.update = to_streamed_response_wrapper(
            pty.update,
        )


class AsyncV2PtyResourceWithStreamingResponse:
    def __init__(self, pty: AsyncV2PtyResource) -> None:
        self._pty = pty

        self.connect = async_to_streamed_response_wrapper(
            pty.connect,
        )
        self.connect_token = async_to_streamed_response_wrapper(
            pty.connect_token,
        )
        self.create = async_to_streamed_response_wrapper(
            pty.create,
        )
        self.get = async_to_streamed_response_wrapper(
            pty.get,
        )
        self.list = async_to_streamed_response_wrapper(
            pty.list,
        )
        self.remove = async_to_streamed_response_wrapper(
            pty.remove,
        )
        self.update = async_to_streamed_response_wrapper(
            pty.update,
        )
