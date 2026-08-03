# Hand-maintained fork of the Stainless-era opencode SDK. Generated code was replaced by manual maintenance; see CONTRIBUTING.md.

from __future__ import annotations

import httpx

from ...types import v2_location_query_params, v2_permission_saved_list_params
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
from ...types.v2_location_query_params import V2Location
from ...types.v2_permission_saved_list_response import V2PermissionSavedListResponse
from ...types.v2_permission_request_list_response import V2PermissionRequestListResponse

__all__ = ["V2PermissionResource", "AsyncV2PermissionResource"]


class V2PermissionResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> V2PermissionResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/sst/opencode-sdk-python#accessing-raw-response-data-eg-headers
        """
        return V2PermissionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> V2PermissionResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/sst/opencode-sdk-python#with_streaming_response
        """
        return V2PermissionResourceWithStreamingResponse(self)

    def request_list(
        self,
        *,
        location: V2Location | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V2PermissionRequestListResponse:
        """List pending permission requests"""
        return self._get(
            "/api/permission/request",
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
            cast_to=V2PermissionRequestListResponse,
        )

    def saved_list(
        self,
        *,
        project_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V2PermissionSavedListResponse:
        """List saved permissions"""
        return self._get(
            "/api/permission/saved",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "project_id": project_id,
                    },
                    v2_permission_saved_list_params.V2PermissionSavedListParams,
                ),
            ),
            cast_to=V2PermissionSavedListResponse,
        )

    def saved_remove(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Remove saved permission"""
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            f"/api/permission/saved/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=NoneType,
        )


class AsyncV2PermissionResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncV2PermissionResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/sst/opencode-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncV2PermissionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncV2PermissionResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/sst/opencode-sdk-python#with_streaming_response
        """
        return AsyncV2PermissionResourceWithStreamingResponse(self)

    async def request_list(
        self,
        *,
        location: V2Location | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V2PermissionRequestListResponse:
        """List pending permission requests"""
        return await self._get(
            "/api/permission/request",
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
            cast_to=V2PermissionRequestListResponse,
        )

    async def saved_list(
        self,
        *,
        project_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V2PermissionSavedListResponse:
        """List saved permissions"""
        return await self._get(
            "/api/permission/saved",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "project_id": project_id,
                    },
                    v2_permission_saved_list_params.V2PermissionSavedListParams,
                ),
            ),
            cast_to=V2PermissionSavedListResponse,
        )

    async def saved_remove(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Remove saved permission"""
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            f"/api/permission/saved/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=NoneType,
        )


class V2PermissionResourceWithRawResponse:
    def __init__(self, permission: V2PermissionResource) -> None:
        self._permission = permission

        self.request_list = to_raw_response_wrapper(
            permission.request_list,
        )
        self.saved_list = to_raw_response_wrapper(
            permission.saved_list,
        )
        self.saved_remove = to_raw_response_wrapper(
            permission.saved_remove,
        )


class AsyncV2PermissionResourceWithRawResponse:
    def __init__(self, permission: AsyncV2PermissionResource) -> None:
        self._permission = permission

        self.request_list = async_to_raw_response_wrapper(
            permission.request_list,
        )
        self.saved_list = async_to_raw_response_wrapper(
            permission.saved_list,
        )
        self.saved_remove = async_to_raw_response_wrapper(
            permission.saved_remove,
        )


class V2PermissionResourceWithStreamingResponse:
    def __init__(self, permission: V2PermissionResource) -> None:
        self._permission = permission

        self.request_list = to_streamed_response_wrapper(
            permission.request_list,
        )
        self.saved_list = to_streamed_response_wrapper(
            permission.saved_list,
        )
        self.saved_remove = to_streamed_response_wrapper(
            permission.saved_remove,
        )


class AsyncV2PermissionResourceWithStreamingResponse:
    def __init__(self, permission: AsyncV2PermissionResource) -> None:
        self._permission = permission

        self.request_list = async_to_streamed_response_wrapper(
            permission.request_list,
        )
        self.saved_list = async_to_streamed_response_wrapper(
            permission.saved_list,
        )
        self.saved_remove = async_to_streamed_response_wrapper(
            permission.saved_remove,
        )
