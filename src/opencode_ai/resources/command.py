# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import command_list_params
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
from ..types.command_list_response import CommandListResponse

__all__ = ["CommandResource", "AsyncCommandResource"]


class CommandResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CommandResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/sst/opencode-sdk-python#accessing-raw-response-data-eg-headers
        """
        return CommandResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CommandResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/sst/opencode-sdk-python#with_streaming_response
        """
        return CommandResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        directory: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CommandListResponse:
        """
        List all commands

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/command",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"directory": directory}, command_list_params.CommandListParams),
            ),
            cast_to=CommandListResponse,
        )


class AsyncCommandResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCommandResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/sst/opencode-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCommandResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCommandResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/sst/opencode-sdk-python#with_streaming_response
        """
        return AsyncCommandResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        directory: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CommandListResponse:
        """
        List all commands

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/command",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"directory": directory}, command_list_params.CommandListParams),
            ),
            cast_to=CommandListResponse,
        )


class CommandResourceWithRawResponse:
    def __init__(self, command: CommandResource) -> None:
        self._command = command

        self.list = to_raw_response_wrapper(
            command.list,
        )


class AsyncCommandResourceWithRawResponse:
    def __init__(self, command: AsyncCommandResource) -> None:
        self._command = command

        self.list = async_to_raw_response_wrapper(
            command.list,
        )


class CommandResourceWithStreamingResponse:
    def __init__(self, command: CommandResource) -> None:
        self._command = command

        self.list = to_streamed_response_wrapper(
            command.list,
        )


class AsyncCommandResourceWithStreamingResponse:
    def __init__(self, command: AsyncCommandResource) -> None:
        self._command = command

        self.list = async_to_streamed_response_wrapper(
            command.list,
        )
