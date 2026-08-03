# Hand-maintained fork of the Stainless-era opencode SDK. Generated code was replaced by manual maintenance; see CONTRIBUTING.md.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ...types import v2_fs_find_params, v2_fs_list_params, v2_location_query_params
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
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
from ...types.v2_fs_find_response import V2FsFindResponse
from ...types.v2_fs_list_response import V2FsListResponse
from ...types.v2_location_query_params import V2Location

__all__ = ["V2FsResource", "AsyncV2FsResource"]


class V2FsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> V2FsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/sst/opencode-sdk-python#accessing-raw-response-data-eg-headers
        """
        return V2FsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> V2FsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/sst/opencode-sdk-python#with_streaming_response
        """
        return V2FsResourceWithStreamingResponse(self)

    def find(
        self,
        *,
        location: V2Location | NotGiven = NOT_GIVEN,
        query: str,
        type: Literal["file", "directory"] | NotGiven = NOT_GIVEN,
        limit: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V2FsFindResponse:
        """Find files"""
        return self._get(
            "/api/fs/find",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "location": location,
                        "query": query,
                        "type": type,
                        "limit": limit,
                    },
                    v2_fs_find_params.V2FsFindParams,
                ),
            ),
            cast_to=V2FsFindResponse,
        )

    def list(
        self,
        *,
        location: V2Location | NotGiven = NOT_GIVEN,
        path: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V2FsListResponse:
        """List directory"""
        return self._get(
            "/api/fs/list",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "location": location,
                        "path": path,
                    },
                    v2_fs_list_params.V2FsListParams,
                ),
            ),
            cast_to=V2FsListResponse,
        )

    def read(
        self,
        *,
        location: V2Location | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """Read file"""
        return self._get(
            "/api/fs/read/*",
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
            cast_to=str,
        )


class AsyncV2FsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncV2FsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/sst/opencode-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncV2FsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncV2FsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/sst/opencode-sdk-python#with_streaming_response
        """
        return AsyncV2FsResourceWithStreamingResponse(self)

    async def find(
        self,
        *,
        location: V2Location | NotGiven = NOT_GIVEN,
        query: str,
        type: Literal["file", "directory"] | NotGiven = NOT_GIVEN,
        limit: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V2FsFindResponse:
        """Find files"""
        return await self._get(
            "/api/fs/find",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "location": location,
                        "query": query,
                        "type": type,
                        "limit": limit,
                    },
                    v2_fs_find_params.V2FsFindParams,
                ),
            ),
            cast_to=V2FsFindResponse,
        )

    async def list(
        self,
        *,
        location: V2Location | NotGiven = NOT_GIVEN,
        path: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V2FsListResponse:
        """List directory"""
        return await self._get(
            "/api/fs/list",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "location": location,
                        "path": path,
                    },
                    v2_fs_list_params.V2FsListParams,
                ),
            ),
            cast_to=V2FsListResponse,
        )

    async def read(
        self,
        *,
        location: V2Location | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """Read file"""
        return await self._get(
            "/api/fs/read/*",
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
            cast_to=str,
        )


class V2FsResourceWithRawResponse:
    def __init__(self, fs: V2FsResource) -> None:
        self._fs = fs

        self.find = to_raw_response_wrapper(
            fs.find,
        )
        self.list = to_raw_response_wrapper(
            fs.list,
        )
        self.read = to_raw_response_wrapper(
            fs.read,
        )


class AsyncV2FsResourceWithRawResponse:
    def __init__(self, fs: AsyncV2FsResource) -> None:
        self._fs = fs

        self.find = async_to_raw_response_wrapper(
            fs.find,
        )
        self.list = async_to_raw_response_wrapper(
            fs.list,
        )
        self.read = async_to_raw_response_wrapper(
            fs.read,
        )


class V2FsResourceWithStreamingResponse:
    def __init__(self, fs: V2FsResource) -> None:
        self._fs = fs

        self.find = to_streamed_response_wrapper(
            fs.find,
        )
        self.list = to_streamed_response_wrapper(
            fs.list,
        )
        self.read = to_streamed_response_wrapper(
            fs.read,
        )


class AsyncV2FsResourceWithStreamingResponse:
    def __init__(self, fs: AsyncV2FsResource) -> None:
        self._fs = fs

        self.find = async_to_streamed_response_wrapper(
            fs.find,
        )
        self.list = async_to_streamed_response_wrapper(
            fs.list,
        )
        self.read = async_to_streamed_response_wrapper(
            fs.read,
        )
