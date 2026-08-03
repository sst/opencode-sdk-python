# Hand-maintained fork of the Stainless-era opencode SDK. Generated code was replaced by manual maintenance; see CONTRIBUTING.md.

from __future__ import annotations

import httpx

from ..types import addressing_params
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
from ..types.instance_dispose_response import InstanceDisposeResponse

__all__ = ["InstanceResource", "AsyncInstanceResource"]


class InstanceResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> InstanceResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/sst/opencode-sdk-python#accessing-raw-response-data-eg-headers
        """
        return InstanceResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> InstanceResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/sst/opencode-sdk-python#with_streaming_response
        """
        return InstanceResourceWithStreamingResponse(self)

    def dispose(
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
    ) -> InstanceDisposeResponse:
        """Dispose of the current instance and free its resources."""
        return self._post(
            "/instance/dispose",
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
            cast_to=InstanceDisposeResponse,
        )


class AsyncInstanceResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncInstanceResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/sst/opencode-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncInstanceResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncInstanceResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/sst/opencode-sdk-python#with_streaming_response
        """
        return AsyncInstanceResourceWithStreamingResponse(self)

    async def dispose(
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
    ) -> InstanceDisposeResponse:
        """Dispose of the current instance and free its resources."""
        return await self._post(
            "/instance/dispose",
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
            cast_to=InstanceDisposeResponse,
        )


class InstanceResourceWithRawResponse:
    def __init__(self, instance: InstanceResource) -> None:
        self._instance = instance

        self.dispose = to_raw_response_wrapper(
            instance.dispose,
        )


class AsyncInstanceResourceWithRawResponse:
    def __init__(self, instance: AsyncInstanceResource) -> None:
        self._instance = instance

        self.dispose = async_to_raw_response_wrapper(
            instance.dispose,
        )


class InstanceResourceWithStreamingResponse:
    def __init__(self, instance: InstanceResource) -> None:
        self._instance = instance

        self.dispose = to_streamed_response_wrapper(
            instance.dispose,
        )


class AsyncInstanceResourceWithStreamingResponse:
    def __init__(self, instance: AsyncInstanceResource) -> None:
        self._instance = instance

        self.dispose = async_to_streamed_response_wrapper(
            instance.dispose,
        )
