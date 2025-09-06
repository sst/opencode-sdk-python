# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import project_list_params, project_current_params
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
from ..types.project import Project
from ..types.project_list_response import ProjectListResponse

__all__ = ["ProjectResource", "AsyncProjectResource"]


class ProjectResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ProjectResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/sst/opencode-sdk-python#accessing-raw-response-data-eg-headers
        """
        return ProjectResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ProjectResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/sst/opencode-sdk-python#with_streaming_response
        """
        return ProjectResourceWithStreamingResponse(self)

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
    ) -> ProjectListResponse:
        """
        List all projects

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/project",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"directory": directory}, project_list_params.ProjectListParams),
            ),
            cast_to=ProjectListResponse,
        )

    def current(
        self,
        *,
        directory: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Project:
        """
        Get the current project

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/project/current",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"directory": directory}, project_current_params.ProjectCurrentParams),
            ),
            cast_to=Project,
        )


class AsyncProjectResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncProjectResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/sst/opencode-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncProjectResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncProjectResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/sst/opencode-sdk-python#with_streaming_response
        """
        return AsyncProjectResourceWithStreamingResponse(self)

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
    ) -> ProjectListResponse:
        """
        List all projects

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/project",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"directory": directory}, project_list_params.ProjectListParams),
            ),
            cast_to=ProjectListResponse,
        )

    async def current(
        self,
        *,
        directory: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Project:
        """
        Get the current project

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/project/current",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"directory": directory}, project_current_params.ProjectCurrentParams
                ),
            ),
            cast_to=Project,
        )


class ProjectResourceWithRawResponse:
    def __init__(self, project: ProjectResource) -> None:
        self._project = project

        self.list = to_raw_response_wrapper(
            project.list,
        )
        self.current = to_raw_response_wrapper(
            project.current,
        )


class AsyncProjectResourceWithRawResponse:
    def __init__(self, project: AsyncProjectResource) -> None:
        self._project = project

        self.list = async_to_raw_response_wrapper(
            project.list,
        )
        self.current = async_to_raw_response_wrapper(
            project.current,
        )


class ProjectResourceWithStreamingResponse:
    def __init__(self, project: ProjectResource) -> None:
        self._project = project

        self.list = to_streamed_response_wrapper(
            project.list,
        )
        self.current = to_streamed_response_wrapper(
            project.current,
        )


class AsyncProjectResourceWithStreamingResponse:
    def __init__(self, project: AsyncProjectResource) -> None:
        self._project = project

        self.list = async_to_streamed_response_wrapper(
            project.list,
        )
        self.current = async_to_streamed_response_wrapper(
            project.current,
        )
