# Hand-maintained fork of the Stainless-era opencode SDK. Generated code was replaced by manual maintenance; see CONTRIBUTING.md.

from __future__ import annotations

import httpx

from ...types import v2_location_query_params, v2_credential_update_params
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

__all__ = ["V2CredentialResource", "AsyncV2CredentialResource"]


class V2CredentialResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> V2CredentialResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/sst/opencode-sdk-python#accessing-raw-response-data-eg-headers
        """
        return V2CredentialResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> V2CredentialResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/sst/opencode-sdk-python#with_streaming_response
        """
        return V2CredentialResourceWithStreamingResponse(self)

    def remove(
        self,
        credential_id: str,
        *,
        location: V2Location | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Remove credential"""
        if not credential_id:
            raise ValueError(f"Expected a non-empty value for `credential_id` but received {credential_id!r}")
        return self._delete(
            f"/api/credential/{credential_id}",
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

    def update(
        self,
        credential_id: str,
        *,
        label: str,
        location: V2Location | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Update credential"""
        if not credential_id:
            raise ValueError(f"Expected a non-empty value for `credential_id` but received {credential_id!r}")
        return self._patch(
            f"/api/credential/{credential_id}",
            body=maybe_transform(
                {
                    "label": label,
                },
                v2_credential_update_params.V2CredentialUpdateParams,
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


class AsyncV2CredentialResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncV2CredentialResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/sst/opencode-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncV2CredentialResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncV2CredentialResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/sst/opencode-sdk-python#with_streaming_response
        """
        return AsyncV2CredentialResourceWithStreamingResponse(self)

    async def remove(
        self,
        credential_id: str,
        *,
        location: V2Location | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Remove credential"""
        if not credential_id:
            raise ValueError(f"Expected a non-empty value for `credential_id` but received {credential_id!r}")
        return await self._delete(
            f"/api/credential/{credential_id}",
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

    async def update(
        self,
        credential_id: str,
        *,
        label: str,
        location: V2Location | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Update credential"""
        if not credential_id:
            raise ValueError(f"Expected a non-empty value for `credential_id` but received {credential_id!r}")
        return await self._patch(
            f"/api/credential/{credential_id}",
            body=await async_maybe_transform(
                {
                    "label": label,
                },
                v2_credential_update_params.V2CredentialUpdateParams,
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


class V2CredentialResourceWithRawResponse:
    def __init__(self, credential: V2CredentialResource) -> None:
        self._credential = credential

        self.remove = to_raw_response_wrapper(
            credential.remove,
        )
        self.update = to_raw_response_wrapper(
            credential.update,
        )


class AsyncV2CredentialResourceWithRawResponse:
    def __init__(self, credential: AsyncV2CredentialResource) -> None:
        self._credential = credential

        self.remove = async_to_raw_response_wrapper(
            credential.remove,
        )
        self.update = async_to_raw_response_wrapper(
            credential.update,
        )


class V2CredentialResourceWithStreamingResponse:
    def __init__(self, credential: V2CredentialResource) -> None:
        self._credential = credential

        self.remove = to_streamed_response_wrapper(
            credential.remove,
        )
        self.update = to_streamed_response_wrapper(
            credential.update,
        )


class AsyncV2CredentialResourceWithStreamingResponse:
    def __init__(self, credential: AsyncV2CredentialResource) -> None:
        self._credential = credential

        self.remove = async_to_streamed_response_wrapper(
            credential.remove,
        )
        self.update = async_to_streamed_response_wrapper(
            credential.update,
        )
