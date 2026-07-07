# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import addressing_params, permission_reply_params
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
from ..types.permission_list_response import PermissionListResponse
from ..types.permission_reply_response import PermissionReplyResponse

__all__ = ["PermissionResource", "AsyncPermissionResource"]


class PermissionResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PermissionResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/sst/opencode-sdk-python#accessing-raw-response-data-eg-headers
        """
        return PermissionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PermissionResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/sst/opencode-sdk-python#with_streaming_response
        """
        return PermissionResourceWithStreamingResponse(self)

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
    ) -> PermissionListResponse:
        """Get a list of all pending permission requests awaiting a response."""
        return self._get(
            "/permission",
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
            cast_to=PermissionListResponse,
        )

    def reply(
        self,
        request_id: str,
        *,
        reply: Literal["once", "always", "reject"],
        message: str | NotGiven = NOT_GIVEN,
        directory: str | NotGiven = NOT_GIVEN,
        workspace: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PermissionReplyResponse:
        """
        Respond to a pending permission request by approving or rejecting it.

        Args:
          reply: How to respond to the permission request

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not request_id:
            raise ValueError(f"Expected a non-empty value for `request_id` but received {request_id!r}")
        return self._post(
            f"/permission/{request_id}/reply",
            body=maybe_transform(
                {
                    "reply": reply,
                    "message": message,
                },
                permission_reply_params.PermissionReplyParams,
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
            cast_to=PermissionReplyResponse,
        )


class AsyncPermissionResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPermissionResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/sst/opencode-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPermissionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPermissionResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/sst/opencode-sdk-python#with_streaming_response
        """
        return AsyncPermissionResourceWithStreamingResponse(self)

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
    ) -> PermissionListResponse:
        """Get a list of all pending permission requests awaiting a response."""
        return await self._get(
            "/permission",
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
            cast_to=PermissionListResponse,
        )

    async def reply(
        self,
        request_id: str,
        *,
        reply: Literal["once", "always", "reject"],
        message: str | NotGiven = NOT_GIVEN,
        directory: str | NotGiven = NOT_GIVEN,
        workspace: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PermissionReplyResponse:
        """
        Respond to a pending permission request by approving or rejecting it.

        Args:
          reply: How to respond to the permission request

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not request_id:
            raise ValueError(f"Expected a non-empty value for `request_id` but received {request_id!r}")
        return await self._post(
            f"/permission/{request_id}/reply",
            body=await async_maybe_transform(
                {
                    "reply": reply,
                    "message": message,
                },
                permission_reply_params.PermissionReplyParams,
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
            cast_to=PermissionReplyResponse,
        )


class PermissionResourceWithRawResponse:
    def __init__(self, permission: PermissionResource) -> None:
        self._permission = permission

        self.list = to_raw_response_wrapper(
            permission.list,
        )
        self.reply = to_raw_response_wrapper(
            permission.reply,
        )


class AsyncPermissionResourceWithRawResponse:
    def __init__(self, permission: AsyncPermissionResource) -> None:
        self._permission = permission

        self.list = async_to_raw_response_wrapper(
            permission.list,
        )
        self.reply = async_to_raw_response_wrapper(
            permission.reply,
        )


class PermissionResourceWithStreamingResponse:
    def __init__(self, permission: PermissionResource) -> None:
        self._permission = permission

        self.list = to_streamed_response_wrapper(
            permission.list,
        )
        self.reply = to_streamed_response_wrapper(
            permission.reply,
        )


class AsyncPermissionResourceWithStreamingResponse:
    def __init__(self, permission: AsyncPermissionResource) -> None:
        self._permission = permission

        self.list = async_to_streamed_response_wrapper(
            permission.list,
        )
        self.reply = async_to_streamed_response_wrapper(
            permission.reply,
        )
