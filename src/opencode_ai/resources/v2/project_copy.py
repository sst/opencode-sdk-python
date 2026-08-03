# Hand-maintained fork of the Stainless-era opencode SDK. Generated code was replaced by manual maintenance; see CONTRIBUTING.md.

from __future__ import annotations

import httpx

from ...types import v2_location_query_params, v2_project_copy_create_params, v2_project_copy_remove_params
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
from ...types.v2_project_copy_create_response import V2ProjectCopyCreateResponse

__all__ = ["V2ProjectCopyResource", "AsyncV2ProjectCopyResource"]


class V2ProjectCopyResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> V2ProjectCopyResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/sst/opencode-sdk-python#accessing-raw-response-data-eg-headers
        """
        return V2ProjectCopyResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> V2ProjectCopyResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/sst/opencode-sdk-python#with_streaming_response
        """
        return V2ProjectCopyResourceWithStreamingResponse(self)

    def create(
        self,
        project_id: str,
        *,
        strategy: str,
        directory: str,
        name: str | NotGiven = NOT_GIVEN,
        location: V2Location | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V2ProjectCopyCreateResponse:
        """create"""
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        return self._post(
            f"/experimental/project/{project_id}/copy",
            body=maybe_transform(
                {
                    "strategy": strategy,
                    "directory": directory,
                    "name": name,
                },
                v2_project_copy_create_params.V2ProjectCopyCreateParams,
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
            cast_to=V2ProjectCopyCreateResponse,
        )

    def refresh(
        self,
        project_id: str,
        *,
        location: V2Location | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """refresh"""
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        return self._post(
            f"/experimental/project/{project_id}/copy/refresh",
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

    def remove(
        self,
        project_id: str,
        *,
        directory: str,
        force: bool,
        location: V2Location | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """remove"""
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        return self._delete(
            f"/experimental/project/{project_id}/copy",
            body=maybe_transform(
                {
                    "directory": directory,
                    "force": force,
                },
                v2_project_copy_remove_params.V2ProjectCopyRemoveParams,
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
            cast_to=NoneType,
        )


class AsyncV2ProjectCopyResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncV2ProjectCopyResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/sst/opencode-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncV2ProjectCopyResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncV2ProjectCopyResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/sst/opencode-sdk-python#with_streaming_response
        """
        return AsyncV2ProjectCopyResourceWithStreamingResponse(self)

    async def create(
        self,
        project_id: str,
        *,
        strategy: str,
        directory: str,
        name: str | NotGiven = NOT_GIVEN,
        location: V2Location | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V2ProjectCopyCreateResponse:
        """create"""
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        return await self._post(
            f"/experimental/project/{project_id}/copy",
            body=await async_maybe_transform(
                {
                    "strategy": strategy,
                    "directory": directory,
                    "name": name,
                },
                v2_project_copy_create_params.V2ProjectCopyCreateParams,
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
            cast_to=V2ProjectCopyCreateResponse,
        )

    async def refresh(
        self,
        project_id: str,
        *,
        location: V2Location | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """refresh"""
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        return await self._post(
            f"/experimental/project/{project_id}/copy/refresh",
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

    async def remove(
        self,
        project_id: str,
        *,
        directory: str,
        force: bool,
        location: V2Location | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """remove"""
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        return await self._delete(
            f"/experimental/project/{project_id}/copy",
            body=await async_maybe_transform(
                {
                    "directory": directory,
                    "force": force,
                },
                v2_project_copy_remove_params.V2ProjectCopyRemoveParams,
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
            cast_to=NoneType,
        )


class V2ProjectCopyResourceWithRawResponse:
    def __init__(self, project_copy: V2ProjectCopyResource) -> None:
        self._project_copy = project_copy

        self.create = to_raw_response_wrapper(
            project_copy.create,
        )
        self.refresh = to_raw_response_wrapper(
            project_copy.refresh,
        )
        self.remove = to_raw_response_wrapper(
            project_copy.remove,
        )


class AsyncV2ProjectCopyResourceWithRawResponse:
    def __init__(self, project_copy: AsyncV2ProjectCopyResource) -> None:
        self._project_copy = project_copy

        self.create = async_to_raw_response_wrapper(
            project_copy.create,
        )
        self.refresh = async_to_raw_response_wrapper(
            project_copy.refresh,
        )
        self.remove = async_to_raw_response_wrapper(
            project_copy.remove,
        )


class V2ProjectCopyResourceWithStreamingResponse:
    def __init__(self, project_copy: V2ProjectCopyResource) -> None:
        self._project_copy = project_copy

        self.create = to_streamed_response_wrapper(
            project_copy.create,
        )
        self.refresh = to_streamed_response_wrapper(
            project_copy.refresh,
        )
        self.remove = to_streamed_response_wrapper(
            project_copy.remove,
        )


class AsyncV2ProjectCopyResourceWithStreamingResponse:
    def __init__(self, project_copy: AsyncV2ProjectCopyResource) -> None:
        self._project_copy = project_copy

        self.create = async_to_streamed_response_wrapper(
            project_copy.create,
        )
        self.refresh = async_to_streamed_response_wrapper(
            project_copy.refresh,
        )
        self.remove = async_to_streamed_response_wrapper(
            project_copy.remove,
        )
