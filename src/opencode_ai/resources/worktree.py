# Hand-maintained fork of the Stainless-era opencode SDK. Generated code was replaced by manual maintenance; see CONTRIBUTING.md.

from __future__ import annotations

import httpx

from ..types import addressing_params, worktree_reset_params, worktree_create_params, worktree_remove_params
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
from ..types.worktree import Worktree
from ..types.worktree_list_response import WorktreeListResponse
from ..types.worktree_reset_response import WorktreeResetResponse
from ..types.worktree_remove_response import WorktreeRemoveResponse

__all__ = ["WorktreeResource", "AsyncWorktreeResource"]


class WorktreeResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> WorktreeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/sst/opencode-sdk-python#accessing-raw-response-data-eg-headers
        """
        return WorktreeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WorktreeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/sst/opencode-sdk-python#with_streaming_response
        """
        return WorktreeResourceWithStreamingResponse(self)

    def list(
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
    ) -> WorktreeListResponse:
        """List worktrees"""
        return self._get(
            "/experimental/worktree",
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
            cast_to=WorktreeListResponse,
        )

    def create(
        self,
        *,
        name: str | NotGiven = NOT_GIVEN,
        start_command: str | NotGiven = NOT_GIVEN,
        directory: str | NotGiven = NOT_GIVEN,
        workspace: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Worktree:
        """
        Create a worktree.

        Args:
          name: Name of the worktree to create.

          start_command: Command to run inside the worktree when it starts.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/experimental/worktree",
            body=maybe_transform(
                {
                    "name": name,
                    "start_command": start_command,
                },
                worktree_create_params.WorktreeCreateParams,
            ),
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
            cast_to=Worktree,
        )

    def remove(
        self,
        *,
        directory: str,
        query_directory: str | NotGiven = NOT_GIVEN,
        workspace: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WorktreeRemoveResponse:
        """
        Remove a worktree.

        Args:
          directory: Directory of the worktree to remove.

              Note: this is a request body field, distinct from the `directory` query
              parameter that may also be present on this same request.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._delete(
            "/experimental/worktree",
            body=maybe_transform(
                {
                    "directory": directory,
                },
                worktree_remove_params.WorktreeRemoveParams,
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
            cast_to=WorktreeRemoveResponse,
        )

    def reset(
        self,
        *,
        directory: str,
        query_directory: str | NotGiven = NOT_GIVEN,
        workspace: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WorktreeResetResponse:
        """
        Reset a worktree.

        Args:
          directory: Directory of the worktree to reset.

              Note: this is a request body field, distinct from the `directory` query
              parameter that may also be present on this same request.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/experimental/worktree/reset",
            body=maybe_transform(
                {
                    "directory": directory,
                },
                worktree_reset_params.WorktreeResetParams,
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
            cast_to=WorktreeResetResponse,
        )


class AsyncWorktreeResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncWorktreeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/sst/opencode-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncWorktreeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWorktreeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/sst/opencode-sdk-python#with_streaming_response
        """
        return AsyncWorktreeResourceWithStreamingResponse(self)

    async def list(
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
    ) -> WorktreeListResponse:
        """List worktrees"""
        return await self._get(
            "/experimental/worktree",
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
            cast_to=WorktreeListResponse,
        )

    async def create(
        self,
        *,
        name: str | NotGiven = NOT_GIVEN,
        start_command: str | NotGiven = NOT_GIVEN,
        directory: str | NotGiven = NOT_GIVEN,
        workspace: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Worktree:
        """
        Create a worktree.

        Args:
          name: Name of the worktree to create.

          start_command: Command to run inside the worktree when it starts.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/experimental/worktree",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "start_command": start_command,
                },
                worktree_create_params.WorktreeCreateParams,
            ),
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
            cast_to=Worktree,
        )

    async def remove(
        self,
        *,
        directory: str,
        query_directory: str | NotGiven = NOT_GIVEN,
        workspace: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WorktreeRemoveResponse:
        """
        Remove a worktree.

        Args:
          directory: Directory of the worktree to remove.

              Note: this is a request body field, distinct from the `directory` query
              parameter that may also be present on this same request.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._delete(
            "/experimental/worktree",
            body=await async_maybe_transform(
                {
                    "directory": directory,
                },
                worktree_remove_params.WorktreeRemoveParams,
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
            cast_to=WorktreeRemoveResponse,
        )

    async def reset(
        self,
        *,
        directory: str,
        query_directory: str | NotGiven = NOT_GIVEN,
        workspace: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WorktreeResetResponse:
        """
        Reset a worktree.

        Args:
          directory: Directory of the worktree to reset.

              Note: this is a request body field, distinct from the `directory` query
              parameter that may also be present on this same request.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/experimental/worktree/reset",
            body=await async_maybe_transform(
                {
                    "directory": directory,
                },
                worktree_reset_params.WorktreeResetParams,
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
            cast_to=WorktreeResetResponse,
        )


class WorktreeResourceWithRawResponse:
    def __init__(self, worktree: WorktreeResource) -> None:
        self._worktree = worktree

        self.list = to_raw_response_wrapper(
            worktree.list,
        )
        self.create = to_raw_response_wrapper(
            worktree.create,
        )
        self.remove = to_raw_response_wrapper(
            worktree.remove,
        )
        self.reset = to_raw_response_wrapper(
            worktree.reset,
        )


class AsyncWorktreeResourceWithRawResponse:
    def __init__(self, worktree: AsyncWorktreeResource) -> None:
        self._worktree = worktree

        self.list = async_to_raw_response_wrapper(
            worktree.list,
        )
        self.create = async_to_raw_response_wrapper(
            worktree.create,
        )
        self.remove = async_to_raw_response_wrapper(
            worktree.remove,
        )
        self.reset = async_to_raw_response_wrapper(
            worktree.reset,
        )


class WorktreeResourceWithStreamingResponse:
    def __init__(self, worktree: WorktreeResource) -> None:
        self._worktree = worktree

        self.list = to_streamed_response_wrapper(
            worktree.list,
        )
        self.create = to_streamed_response_wrapper(
            worktree.create,
        )
        self.remove = to_streamed_response_wrapper(
            worktree.remove,
        )
        self.reset = to_streamed_response_wrapper(
            worktree.reset,
        )


class AsyncWorktreeResourceWithStreamingResponse:
    def __init__(self, worktree: AsyncWorktreeResource) -> None:
        self._worktree = worktree

        self.list = async_to_streamed_response_wrapper(
            worktree.list,
        )
        self.create = async_to_streamed_response_wrapper(
            worktree.create,
        )
        self.remove = async_to_streamed_response_wrapper(
            worktree.remove,
        )
        self.reset = async_to_streamed_response_wrapper(
            worktree.reset,
        )
