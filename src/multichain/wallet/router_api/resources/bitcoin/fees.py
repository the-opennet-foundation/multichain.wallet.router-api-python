# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

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
from ...types.bitcoin import fee_estimate_params

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

    def estimate(
        self,
        *,
        conf_target: int | Omit = omit,
        mode: Literal["ECONOMICAL", "CONSERVATIVE"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Estimate fee for confirmation target

        Args:
          conf_target: Target blocks for confirmation

          mode: Estimate mode

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            "/bitcoin/fees/estimate",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "conf_target": conf_target,
                        "mode": mode,
                    },
                    fee_estimate_params.FeeEstimateParams,
                ),
            ),
            cast_to=NoneType,
        )

    def get_recommended(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Returns fastestFee, halfHourFee, hourFee, economyFee, minimumFee"""
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            "/bitcoin/fees",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
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

    async def estimate(
        self,
        *,
        conf_target: int | Omit = omit,
        mode: Literal["ECONOMICAL", "CONSERVATIVE"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Estimate fee for confirmation target

        Args:
          conf_target: Target blocks for confirmation

          mode: Estimate mode

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            "/bitcoin/fees/estimate",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "conf_target": conf_target,
                        "mode": mode,
                    },
                    fee_estimate_params.FeeEstimateParams,
                ),
            ),
            cast_to=NoneType,
        )

    async def get_recommended(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Returns fastestFee, halfHourFee, hourFee, economyFee, minimumFee"""
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            "/bitcoin/fees",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class FeesResourceWithRawResponse:
    def __init__(self, fees: FeesResource) -> None:
        self._fees = fees

        self.estimate = to_raw_response_wrapper(
            fees.estimate,
        )
        self.get_recommended = to_raw_response_wrapper(
            fees.get_recommended,
        )


class AsyncFeesResourceWithRawResponse:
    def __init__(self, fees: AsyncFeesResource) -> None:
        self._fees = fees

        self.estimate = async_to_raw_response_wrapper(
            fees.estimate,
        )
        self.get_recommended = async_to_raw_response_wrapper(
            fees.get_recommended,
        )


class FeesResourceWithStreamingResponse:
    def __init__(self, fees: FeesResource) -> None:
        self._fees = fees

        self.estimate = to_streamed_response_wrapper(
            fees.estimate,
        )
        self.get_recommended = to_streamed_response_wrapper(
            fees.get_recommended,
        )


class AsyncFeesResourceWithStreamingResponse:
    def __init__(self, fees: AsyncFeesResource) -> None:
        self._fees = fees

        self.estimate = async_to_streamed_response_wrapper(
            fees.estimate,
        )
        self.get_recommended = async_to_streamed_response_wrapper(
            fees.get_recommended,
        )
