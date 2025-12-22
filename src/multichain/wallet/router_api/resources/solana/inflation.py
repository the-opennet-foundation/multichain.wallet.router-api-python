# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
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
from ...types.solana import inflation_get_rewards_params

__all__ = ["InflationResource", "AsyncInflationResource"]


class InflationResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> InflationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/multichain.wallet.router-api-python#accessing-raw-response-data-eg-headers
        """
        return InflationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> InflationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/multichain.wallet.router-api-python#with_streaming_response
        """
        return InflationResourceWithStreamingResponse(self)

    def get_rate(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Get inflation rate"""
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            "/solana/inflation/rate",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def get_rewards(
        self,
        *,
        addresses: SequenceNotStr[str],
        epoch: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Get inflation rewards for addresses

        Args:
          epoch: Epoch (default current)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/solana/inflation/rewards",
            body=maybe_transform(
                {
                    "addresses": addresses,
                    "epoch": epoch,
                },
                inflation_get_rewards_params.InflationGetRewardsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncInflationResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncInflationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/multichain.wallet.router-api-python#accessing-raw-response-data-eg-headers
        """
        return AsyncInflationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncInflationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/multichain.wallet.router-api-python#with_streaming_response
        """
        return AsyncInflationResourceWithStreamingResponse(self)

    async def get_rate(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Get inflation rate"""
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            "/solana/inflation/rate",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def get_rewards(
        self,
        *,
        addresses: SequenceNotStr[str],
        epoch: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Get inflation rewards for addresses

        Args:
          epoch: Epoch (default current)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/solana/inflation/rewards",
            body=await async_maybe_transform(
                {
                    "addresses": addresses,
                    "epoch": epoch,
                },
                inflation_get_rewards_params.InflationGetRewardsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class InflationResourceWithRawResponse:
    def __init__(self, inflation: InflationResource) -> None:
        self._inflation = inflation

        self.get_rate = to_raw_response_wrapper(
            inflation.get_rate,
        )
        self.get_rewards = to_raw_response_wrapper(
            inflation.get_rewards,
        )


class AsyncInflationResourceWithRawResponse:
    def __init__(self, inflation: AsyncInflationResource) -> None:
        self._inflation = inflation

        self.get_rate = async_to_raw_response_wrapper(
            inflation.get_rate,
        )
        self.get_rewards = async_to_raw_response_wrapper(
            inflation.get_rewards,
        )


class InflationResourceWithStreamingResponse:
    def __init__(self, inflation: InflationResource) -> None:
        self._inflation = inflation

        self.get_rate = to_streamed_response_wrapper(
            inflation.get_rate,
        )
        self.get_rewards = to_streamed_response_wrapper(
            inflation.get_rewards,
        )


class AsyncInflationResourceWithStreamingResponse:
    def __init__(self, inflation: AsyncInflationResource) -> None:
        self._inflation = inflation

        self.get_rate = async_to_streamed_response_wrapper(
            inflation.get_rate,
        )
        self.get_rewards = async_to_streamed_response_wrapper(
            inflation.get_rewards,
        )
