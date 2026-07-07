# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx
from typing_extensions import Literal

from ..types import addressing_params, vcs_diff_params, vcs_apply_params
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
from ..types.vcs_info import VcsInfo
from ..types.vcs_diff_response import VcsDiffResponse
from ..types.vcs_apply_response import VcsApplyResponse
from ..types.vcs_status_response import VcsStatusResponse

__all__ = ["VcsResource", "AsyncVcsResource"]


class VcsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> VcsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/sst/opencode-sdk-python#accessing-raw-response-data-eg-headers
        """
        return VcsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> VcsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/sst/opencode-sdk-python#with_streaming_response
        """
        return VcsResourceWithStreamingResponse(self)

    def get(
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
    ) -> VcsInfo:
        """Get version control system information for the current directory."""
        return self._get(
            "/vcs",
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
            cast_to=VcsInfo,
        )

    def apply(
        self,
        *,
        patch: str,
        directory: str | NotGiven = NOT_GIVEN,
        workspace: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VcsApplyResponse:
        """
        Apply a patch to the working tree.

        Args:
          patch: The patch to apply, in unified diff format

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/vcs/apply",
            body=maybe_transform({"patch": patch}, vcs_apply_params.VcsApplyParams),
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
            cast_to=VcsApplyResponse,
        )

    def diff(
        self,
        *,
        mode: Literal["git", "branch"],
        context: int | NotGiven = NOT_GIVEN,
        directory: str | NotGiven = NOT_GIVEN,
        workspace: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VcsDiffResponse:
        """
        Get the diff for all changed files.

        Args:
          mode: The diff mode to use

          context: Number of context lines to include around each change

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/vcs/diff",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "mode": mode,
                        "context": context,
                        "directory": directory,
                        "workspace": workspace,
                    },
                    vcs_diff_params.VcsDiffParams,
                ),
            ),
            cast_to=VcsDiffResponse,
        )

    def diff_raw(
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
    ) -> str:
        """Get the raw unified diff for all changed files."""
        return self._get(
            "/vcs/diff/raw",
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
            cast_to=str,
        )

    def status(
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
    ) -> VcsStatusResponse:
        """Get the status of all changed files in the working tree."""
        return self._get(
            "/vcs/status",
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
            cast_to=VcsStatusResponse,
        )


class AsyncVcsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncVcsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/sst/opencode-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncVcsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncVcsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/sst/opencode-sdk-python#with_streaming_response
        """
        return AsyncVcsResourceWithStreamingResponse(self)

    async def get(
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
    ) -> VcsInfo:
        """Get version control system information for the current directory."""
        return await self._get(
            "/vcs",
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
            cast_to=VcsInfo,
        )

    async def apply(
        self,
        *,
        patch: str,
        directory: str | NotGiven = NOT_GIVEN,
        workspace: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VcsApplyResponse:
        """
        Apply a patch to the working tree.

        Args:
          patch: The patch to apply, in unified diff format

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/vcs/apply",
            body=await async_maybe_transform({"patch": patch}, vcs_apply_params.VcsApplyParams),
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
            cast_to=VcsApplyResponse,
        )

    async def diff(
        self,
        *,
        mode: Literal["git", "branch"],
        context: int | NotGiven = NOT_GIVEN,
        directory: str | NotGiven = NOT_GIVEN,
        workspace: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VcsDiffResponse:
        """
        Get the diff for all changed files.

        Args:
          mode: The diff mode to use

          context: Number of context lines to include around each change

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/vcs/diff",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "mode": mode,
                        "context": context,
                        "directory": directory,
                        "workspace": workspace,
                    },
                    vcs_diff_params.VcsDiffParams,
                ),
            ),
            cast_to=VcsDiffResponse,
        )

    async def diff_raw(
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
    ) -> str:
        """Get the raw unified diff for all changed files."""
        return await self._get(
            "/vcs/diff/raw",
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
            cast_to=str,
        )

    async def status(
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
    ) -> VcsStatusResponse:
        """Get the status of all changed files in the working tree."""
        return await self._get(
            "/vcs/status",
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
            cast_to=VcsStatusResponse,
        )


class VcsResourceWithRawResponse:
    def __init__(self, vcs: VcsResource) -> None:
        self._vcs = vcs

        self.get = to_raw_response_wrapper(
            vcs.get,
        )
        self.apply = to_raw_response_wrapper(
            vcs.apply,
        )
        self.diff = to_raw_response_wrapper(
            vcs.diff,
        )
        self.diff_raw = to_raw_response_wrapper(
            vcs.diff_raw,
        )
        self.status = to_raw_response_wrapper(
            vcs.status,
        )


class AsyncVcsResourceWithRawResponse:
    def __init__(self, vcs: AsyncVcsResource) -> None:
        self._vcs = vcs

        self.get = async_to_raw_response_wrapper(
            vcs.get,
        )
        self.apply = async_to_raw_response_wrapper(
            vcs.apply,
        )
        self.diff = async_to_raw_response_wrapper(
            vcs.diff,
        )
        self.diff_raw = async_to_raw_response_wrapper(
            vcs.diff_raw,
        )
        self.status = async_to_raw_response_wrapper(
            vcs.status,
        )


class VcsResourceWithStreamingResponse:
    def __init__(self, vcs: VcsResource) -> None:
        self._vcs = vcs

        self.get = to_streamed_response_wrapper(
            vcs.get,
        )
        self.apply = to_streamed_response_wrapper(
            vcs.apply,
        )
        self.diff = to_streamed_response_wrapper(
            vcs.diff,
        )
        self.diff_raw = to_streamed_response_wrapper(
            vcs.diff_raw,
        )
        self.status = to_streamed_response_wrapper(
            vcs.status,
        )


class AsyncVcsResourceWithStreamingResponse:
    def __init__(self, vcs: AsyncVcsResource) -> None:
        self._vcs = vcs

        self.get = async_to_streamed_response_wrapper(
            vcs.get,
        )
        self.apply = async_to_streamed_response_wrapper(
            vcs.apply,
        )
        self.diff = async_to_streamed_response_wrapper(
            vcs.diff,
        )
        self.diff_raw = async_to_streamed_response_wrapper(
            vcs.diff_raw,
        )
        self.status = async_to_streamed_response_wrapper(
            vcs.status,
        )
