# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List

import httpx

from ..types import pty_create_params, pty_update_params, pty_connect_params
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
from ..types.pty import Pty
from ..types.pty_list_response import PtyListResponse
from ..types.pty_delete_response import PtyDeleteResponse
from ..types.pty_shells_response import PtyShellsResponse
from ..types.pty_connect_response import PtyConnectResponse
from ..types.pty_connect_token_response import PtyConnectTokenResponse

__all__ = ["PtyResource", "AsyncPtyResource"]


class PtyResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PtyResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/sst/opencode-sdk-python#accessing-raw-response-data-eg-headers
        """
        return PtyResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PtyResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/sst/opencode-sdk-python#with_streaming_response
        """
        return PtyResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PtyListResponse:
        """Get a list of all active pseudo-terminal (PTY) sessions managed by OpenCode."""
        return self._get(
            "/pty",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PtyListResponse,
        )

    def create(
        self,
        *,
        args: List[str] | NotGiven = NOT_GIVEN,
        command: str | NotGiven = NOT_GIVEN,
        cwd: str | NotGiven = NOT_GIVEN,
        env: Dict[str, str] | NotGiven = NOT_GIVEN,
        title: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Pty:
        """
        Create a new pseudo-terminal (PTY) session for running shell commands and
        processes.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/pty",
            body=maybe_transform(
                {
                    "args": args,
                    "command": command,
                    "cwd": cwd,
                    "env": env,
                    "title": title,
                },
                pty_create_params.PtyCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Pty,
        )

    def retrieve(
        self,
        pty_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Pty:
        """
        Retrieve detailed information about a specific pseudo-terminal (PTY) session.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not pty_id:
            raise ValueError(f"Expected a non-empty value for `pty_id` but received {pty_id!r}")
        return self._get(
            f"/pty/{pty_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Pty,
        )

    def update(
        self,
        pty_id: str,
        *,
        size: pty_update_params.Size | NotGiven = NOT_GIVEN,
        title: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Pty:
        """
        Update properties of an existing pseudo-terminal (PTY) session.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not pty_id:
            raise ValueError(f"Expected a non-empty value for `pty_id` but received {pty_id!r}")
        return self._put(
            f"/pty/{pty_id}",
            body=maybe_transform(
                {
                    "size": size,
                    "title": title,
                },
                pty_update_params.PtyUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Pty,
        )

    def delete(
        self,
        pty_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PtyDeleteResponse:
        """
        Remove and terminate a specific pseudo-terminal (PTY) session.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not pty_id:
            raise ValueError(f"Expected a non-empty value for `pty_id` but received {pty_id!r}")
        return self._delete(
            f"/pty/{pty_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PtyDeleteResponse,
        )

    def connect(
        self,
        pty_id: str,
        *,
        cursor: str | NotGiven = NOT_GIVEN,
        ticket: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PtyConnectResponse:
        """
        Establish a WebSocket connection to interact with a pseudo-terminal (PTY)
        session in real-time.

        Note: despite the declared `GET .../connect` shape and the `bool` response
        schema below, this endpoint is actually a WebSocket upgrade in the real
        server. This method only reflects the schema as declared in the OpenAPI
        spec (a plain HTTP GET returning a boolean) and does not implement a
        WebSocket client. Do not rely on it to establish a real-time PTY session.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not pty_id:
            raise ValueError(f"Expected a non-empty value for `pty_id` but received {pty_id!r}")
        return self._get(
            f"/pty/{pty_id}/connect",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "ticket": ticket,
                    },
                    pty_connect_params.PtyConnectParams,
                ),
            ),
            cast_to=PtyConnectResponse,
        )

    def connect_token(
        self,
        pty_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PtyConnectTokenResponse:
        """
        Create a short-lived ticket for opening a PTY WebSocket connection.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not pty_id:
            raise ValueError(f"Expected a non-empty value for `pty_id` but received {pty_id!r}")
        return self._post(
            f"/pty/{pty_id}/connect-token",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PtyConnectTokenResponse,
        )

    def shells(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PtyShellsResponse:
        """Get a list of available shells on the system."""
        return self._get(
            "/pty/shells",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PtyShellsResponse,
        )


class AsyncPtyResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPtyResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/sst/opencode-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPtyResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPtyResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/sst/opencode-sdk-python#with_streaming_response
        """
        return AsyncPtyResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PtyListResponse:
        """Get a list of all active pseudo-terminal (PTY) sessions managed by OpenCode."""
        return await self._get(
            "/pty",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PtyListResponse,
        )

    async def create(
        self,
        *,
        args: List[str] | NotGiven = NOT_GIVEN,
        command: str | NotGiven = NOT_GIVEN,
        cwd: str | NotGiven = NOT_GIVEN,
        env: Dict[str, str] | NotGiven = NOT_GIVEN,
        title: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Pty:
        """
        Create a new pseudo-terminal (PTY) session for running shell commands and
        processes.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/pty",
            body=await async_maybe_transform(
                {
                    "args": args,
                    "command": command,
                    "cwd": cwd,
                    "env": env,
                    "title": title,
                },
                pty_create_params.PtyCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Pty,
        )

    async def retrieve(
        self,
        pty_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Pty:
        """
        Retrieve detailed information about a specific pseudo-terminal (PTY) session.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not pty_id:
            raise ValueError(f"Expected a non-empty value for `pty_id` but received {pty_id!r}")
        return await self._get(
            f"/pty/{pty_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Pty,
        )

    async def update(
        self,
        pty_id: str,
        *,
        size: pty_update_params.Size | NotGiven = NOT_GIVEN,
        title: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Pty:
        """
        Update properties of an existing pseudo-terminal (PTY) session.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not pty_id:
            raise ValueError(f"Expected a non-empty value for `pty_id` but received {pty_id!r}")
        return await self._put(
            f"/pty/{pty_id}",
            body=await async_maybe_transform(
                {
                    "size": size,
                    "title": title,
                },
                pty_update_params.PtyUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Pty,
        )

    async def delete(
        self,
        pty_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PtyDeleteResponse:
        """
        Remove and terminate a specific pseudo-terminal (PTY) session.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not pty_id:
            raise ValueError(f"Expected a non-empty value for `pty_id` but received {pty_id!r}")
        return await self._delete(
            f"/pty/{pty_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PtyDeleteResponse,
        )

    async def connect(
        self,
        pty_id: str,
        *,
        cursor: str | NotGiven = NOT_GIVEN,
        ticket: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PtyConnectResponse:
        """
        Establish a WebSocket connection to interact with a pseudo-terminal (PTY)
        session in real-time.

        Note: despite the declared `GET .../connect` shape and the `bool` response
        schema below, this endpoint is actually a WebSocket upgrade in the real
        server. This method only reflects the schema as declared in the OpenAPI
        spec (a plain HTTP GET returning a boolean) and does not implement a
        WebSocket client. Do not rely on it to establish a real-time PTY session.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not pty_id:
            raise ValueError(f"Expected a non-empty value for `pty_id` but received {pty_id!r}")
        return await self._get(
            f"/pty/{pty_id}/connect",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "cursor": cursor,
                        "ticket": ticket,
                    },
                    pty_connect_params.PtyConnectParams,
                ),
            ),
            cast_to=PtyConnectResponse,
        )

    async def connect_token(
        self,
        pty_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PtyConnectTokenResponse:
        """
        Create a short-lived ticket for opening a PTY WebSocket connection.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not pty_id:
            raise ValueError(f"Expected a non-empty value for `pty_id` but received {pty_id!r}")
        return await self._post(
            f"/pty/{pty_id}/connect-token",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PtyConnectTokenResponse,
        )

    async def shells(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PtyShellsResponse:
        """Get a list of available shells on the system."""
        return await self._get(
            "/pty/shells",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PtyShellsResponse,
        )


class PtyResourceWithRawResponse:
    def __init__(self, pty: PtyResource) -> None:
        self._pty = pty

        self.list = to_raw_response_wrapper(
            pty.list,
        )
        self.create = to_raw_response_wrapper(
            pty.create,
        )
        self.retrieve = to_raw_response_wrapper(
            pty.retrieve,
        )
        self.update = to_raw_response_wrapper(
            pty.update,
        )
        self.delete = to_raw_response_wrapper(
            pty.delete,
        )
        self.connect = to_raw_response_wrapper(
            pty.connect,
        )
        self.connect_token = to_raw_response_wrapper(
            pty.connect_token,
        )
        self.shells = to_raw_response_wrapper(
            pty.shells,
        )


class AsyncPtyResourceWithRawResponse:
    def __init__(self, pty: AsyncPtyResource) -> None:
        self._pty = pty

        self.list = async_to_raw_response_wrapper(
            pty.list,
        )
        self.create = async_to_raw_response_wrapper(
            pty.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            pty.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            pty.update,
        )
        self.delete = async_to_raw_response_wrapper(
            pty.delete,
        )
        self.connect = async_to_raw_response_wrapper(
            pty.connect,
        )
        self.connect_token = async_to_raw_response_wrapper(
            pty.connect_token,
        )
        self.shells = async_to_raw_response_wrapper(
            pty.shells,
        )


class PtyResourceWithStreamingResponse:
    def __init__(self, pty: PtyResource) -> None:
        self._pty = pty

        self.list = to_streamed_response_wrapper(
            pty.list,
        )
        self.create = to_streamed_response_wrapper(
            pty.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            pty.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            pty.update,
        )
        self.delete = to_streamed_response_wrapper(
            pty.delete,
        )
        self.connect = to_streamed_response_wrapper(
            pty.connect,
        )
        self.connect_token = to_streamed_response_wrapper(
            pty.connect_token,
        )
        self.shells = to_streamed_response_wrapper(
            pty.shells,
        )


class AsyncPtyResourceWithStreamingResponse:
    def __init__(self, pty: AsyncPtyResource) -> None:
        self._pty = pty

        self.list = async_to_streamed_response_wrapper(
            pty.list,
        )
        self.create = async_to_streamed_response_wrapper(
            pty.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            pty.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            pty.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            pty.delete,
        )
        self.connect = async_to_streamed_response_wrapper(
            pty.connect,
        )
        self.connect_token = async_to_streamed_response_wrapper(
            pty.connect_token,
        )
        self.shells = async_to_streamed_response_wrapper(
            pty.shells,
        )
