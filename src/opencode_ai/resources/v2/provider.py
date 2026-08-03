# Hand-maintained fork of the Stainless-era opencode SDK. Generated code was replaced by manual maintenance; see CONTRIBUTING.md.

from __future__ import annotations

import httpx

from ...types import v2_location_query_params
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
from ...types.v2_location_query_params import V2Location
from ...types.v2_provider_get_response import V2ProviderGetResponse
from ...types.v2_provider_list_response import V2ProviderListResponse

__all__ = ["V2ProviderResource", "AsyncV2ProviderResource"]


class V2ProviderResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> V2ProviderResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/sst/opencode-sdk-python#accessing-raw-response-data-eg-headers
        """
        return V2ProviderResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> V2ProviderResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/sst/opencode-sdk-python#with_streaming_response
        """
        return V2ProviderResourceWithStreamingResponse(self)

    def get(
        self,
        provider_id: str,
        *,
        location: V2Location | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V2ProviderGetResponse:
        """Get provider"""
        if not provider_id:
            raise ValueError(f"Expected a non-empty value for `provider_id` but received {provider_id!r}")
        return self._get(
            f"/api/provider/{provider_id}",
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
            cast_to=V2ProviderGetResponse,
        )

    def list(
        self,
        *,
        location: V2Location | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V2ProviderListResponse:
        """List providers"""
        return self._get(
            "/api/provider",
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
            cast_to=V2ProviderListResponse,
        )


class AsyncV2ProviderResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncV2ProviderResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/sst/opencode-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncV2ProviderResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncV2ProviderResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/sst/opencode-sdk-python#with_streaming_response
        """
        return AsyncV2ProviderResourceWithStreamingResponse(self)

    async def get(
        self,
        provider_id: str,
        *,
        location: V2Location | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V2ProviderGetResponse:
        """Get provider"""
        if not provider_id:
            raise ValueError(f"Expected a non-empty value for `provider_id` but received {provider_id!r}")
        return await self._get(
            f"/api/provider/{provider_id}",
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
            cast_to=V2ProviderGetResponse,
        )

    async def list(
        self,
        *,
        location: V2Location | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V2ProviderListResponse:
        """List providers"""
        return await self._get(
            "/api/provider",
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
            cast_to=V2ProviderListResponse,
        )


class V2ProviderResourceWithRawResponse:
    def __init__(self, provider: V2ProviderResource) -> None:
        self._provider = provider

        self.get = to_raw_response_wrapper(
            provider.get,
        )
        self.list = to_raw_response_wrapper(
            provider.list,
        )


class AsyncV2ProviderResourceWithRawResponse:
    def __init__(self, provider: AsyncV2ProviderResource) -> None:
        self._provider = provider

        self.get = async_to_raw_response_wrapper(
            provider.get,
        )
        self.list = async_to_raw_response_wrapper(
            provider.list,
        )


class V2ProviderResourceWithStreamingResponse:
    def __init__(self, provider: V2ProviderResource) -> None:
        self._provider = provider

        self.get = to_streamed_response_wrapper(
            provider.get,
        )
        self.list = to_streamed_response_wrapper(
            provider.list,
        )


class AsyncV2ProviderResourceWithStreamingResponse:
    def __init__(self, provider: AsyncV2ProviderResource) -> None:
        self._provider = provider

        self.get = async_to_streamed_response_wrapper(
            provider.get,
        )
        self.list = async_to_streamed_response_wrapper(
            provider.list,
        )
