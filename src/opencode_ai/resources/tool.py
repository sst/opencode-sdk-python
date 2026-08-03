# Hand-maintained fork of the Stainless-era opencode SDK. Generated code was replaced by manual maintenance; see CONTRIBUTING.md.

from __future__ import annotations

import httpx

from ..types import tool_list_params, addressing_params
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
from ..types.tool_ids_response import ToolIDsResponse
from ..types.tool_list_response import ToolListResponse

__all__ = ["ToolResource", "AsyncToolResource"]


class ToolResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ToolResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/sst/opencode-sdk-python#accessing-raw-response-data-eg-headers
        """
        return ToolResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ToolResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/sst/opencode-sdk-python#with_streaming_response
        """
        return ToolResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        provider: str,
        model: str,
        directory: str | NotGiven = NOT_GIVEN,
        workspace: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ToolListResponse:
        """
        List the tools available to a given model.

        Args:
          provider: The provider the model belongs to.

          model: The model whose available tools should be listed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/experimental/tool",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "provider": provider,
                        "model": model,
                        "directory": directory,
                        "workspace": workspace,
                    },
                    tool_list_params.ToolListParams,
                ),
            ),
            cast_to=ToolListResponse,
        )

    def ids(
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
    ) -> ToolIDsResponse:
        """List the ids of all available tools"""
        return self._get(
            "/experimental/tool/ids",
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
            cast_to=ToolIDsResponse,
        )


class AsyncToolResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncToolResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/sst/opencode-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncToolResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncToolResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/sst/opencode-sdk-python#with_streaming_response
        """
        return AsyncToolResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        provider: str,
        model: str,
        directory: str | NotGiven = NOT_GIVEN,
        workspace: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ToolListResponse:
        """
        List the tools available to a given model.

        Args:
          provider: The provider the model belongs to.

          model: The model whose available tools should be listed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/experimental/tool",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "provider": provider,
                        "model": model,
                        "directory": directory,
                        "workspace": workspace,
                    },
                    tool_list_params.ToolListParams,
                ),
            ),
            cast_to=ToolListResponse,
        )

    async def ids(
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
    ) -> ToolIDsResponse:
        """List the ids of all available tools"""
        return await self._get(
            "/experimental/tool/ids",
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
            cast_to=ToolIDsResponse,
        )


class ToolResourceWithRawResponse:
    def __init__(self, tool: ToolResource) -> None:
        self._tool = tool

        self.list = to_raw_response_wrapper(
            tool.list,
        )
        self.ids = to_raw_response_wrapper(
            tool.ids,
        )


class AsyncToolResourceWithRawResponse:
    def __init__(self, tool: AsyncToolResource) -> None:
        self._tool = tool

        self.list = async_to_raw_response_wrapper(
            tool.list,
        )
        self.ids = async_to_raw_response_wrapper(
            tool.ids,
        )


class ToolResourceWithStreamingResponse:
    def __init__(self, tool: ToolResource) -> None:
        self._tool = tool

        self.list = to_streamed_response_wrapper(
            tool.list,
        )
        self.ids = to_streamed_response_wrapper(
            tool.ids,
        )


class AsyncToolResourceWithStreamingResponse:
    def __init__(self, tool: AsyncToolResource) -> None:
        self._tool = tool

        self.list = async_to_streamed_response_wrapper(
            tool.list,
        )
        self.ids = async_to_streamed_response_wrapper(
            tool.ids,
        )
