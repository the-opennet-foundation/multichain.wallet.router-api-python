# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
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
from ...types.solana import fee_get_recent_params, fee_get_priority_params

__all__ = ["FeesResource", "AsyncFeesResource"]


class FeesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> FeesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/multichain.wallet.router-api-python#accessing-raw-response-data-eg-headers
        """
        return FeesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FeesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/multichain.wallet.router-api-python#with_streaming_response
        """
        return FeesResourceWithStreamingResponse(self)

    def get_priority(
        self,
        *,
        account_keys: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Get priority fee estimates (low/med/high/veryHigh)

        Args:
          account_keys: Comma-separated account keys

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            "/solana/fees/priority",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"account_keys": account_keys}, fee_get_priority_params.FeeGetPriorityParams),
            ),
            cast_to=NoneType,
        )

    def get_recent(
        self,
        *,
        addresses: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Get recent prioritization fees

        Args:
          addresses: Comma-separated addresses

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            "/solana/fees/recent",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"addresses": addresses}, fee_get_recent_params.FeeGetRecentParams),
            ),
            cast_to=NoneType,
        )


class AsyncFeesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncFeesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/multichain.wallet.router-api-python#accessing-raw-response-data-eg-headers
        """
        return AsyncFeesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFeesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/multichain.wallet.router-api-python#with_streaming_response
        """
        return AsyncFeesResourceWithStreamingResponse(self)

    async def get_priority(
        self,
        *,
        account_keys: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Get priority fee estimates (low/med/high/veryHigh)

        Args:
          account_keys: Comma-separated account keys

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            "/solana/fees/priority",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"account_keys": account_keys}, fee_get_priority_params.FeeGetPriorityParams
                ),
            ),
            cast_to=NoneType,
        )

    async def get_recent(
        self,
        *,
        addresses: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Get recent prioritization fees

        Args:
          addresses: Comma-separated addresses

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            "/solana/fees/recent",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"addresses": addresses}, fee_get_recent_params.FeeGetRecentParams),
            ),
            cast_to=NoneType,
        )


class FeesResourceWithRawResponse:
    def __init__(self, fees: FeesResource) -> None:
        self._fees = fees

        self.get_priority = to_raw_response_wrapper(
            fees.get_priority,
        )
        self.get_recent = to_raw_response_wrapper(
            fees.get_recent,
        )


class AsyncFeesResourceWithRawResponse:
    def __init__(self, fees: AsyncFeesResource) -> None:
        self._fees = fees

        self.get_priority = async_to_raw_response_wrapper(
            fees.get_priority,
        )
        self.get_recent = async_to_raw_response_wrapper(
            fees.get_recent,
        )


class FeesResourceWithStreamingResponse:
    def __init__(self, fees: FeesResource) -> None:
        self._fees = fees

        self.get_priority = to_streamed_response_wrapper(
            fees.get_priority,
        )
        self.get_recent = to_streamed_response_wrapper(
            fees.get_recent,
        )


class AsyncFeesResourceWithStreamingResponse:
    def __init__(self, fees: AsyncFeesResource) -> None:
        self._fees = fees

        self.get_priority = async_to_streamed_response_wrapper(
            fees.get_priority,
        )
        self.get_recent = async_to_streamed_response_wrapper(
            fees.get_recent,
        )
