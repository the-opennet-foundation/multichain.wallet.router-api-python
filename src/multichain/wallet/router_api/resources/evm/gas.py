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
from ...types.evm import gas_estimate_params
from ..._base_client import make_request_options

__all__ = ["GasResource", "AsyncGasResource"]


class GasResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> GasResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/multichain.wallet.router-api-python#accessing-raw-response-data-eg-headers
        """
        return GasResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> GasResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/multichain.wallet.router-api-python#with_streaming_response
        """
        return GasResourceWithStreamingResponse(self)

    def estimate(
        self,
        chain_id: Literal[
            "ethereum",
            "base",
            "optimism",
            "arbitrum",
            "arbitrumNova",
            "polygon",
            "avalanche",
            "bsc",
            "opbnb",
            "unichain",
            "worldchain",
            "abstract",
            "apechain",
            "hyperliquid",
        ],
        *,
        transaction: object | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Estimate gas for transaction

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chain_id:
            raise ValueError(f"Expected a non-empty value for `chain_id` but received {chain_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            f"/evm/{chain_id}/gas/estimate",
            body=maybe_transform({"transaction": transaction}, gas_estimate_params.GasEstimateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def get_price(
        self,
        chain_id: Literal[
            "ethereum",
            "base",
            "optimism",
            "arbitrum",
            "arbitrumNova",
            "polygon",
            "avalanche",
            "bsc",
            "opbnb",
            "unichain",
            "worldchain",
            "abstract",
            "apechain",
            "hyperliquid",
        ],
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Get current gas price

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chain_id:
            raise ValueError(f"Expected a non-empty value for `chain_id` but received {chain_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            f"/evm/{chain_id}/gas/price",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncGasResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncGasResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/multichain.wallet.router-api-python#accessing-raw-response-data-eg-headers
        """
        return AsyncGasResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncGasResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/multichain.wallet.router-api-python#with_streaming_response
        """
        return AsyncGasResourceWithStreamingResponse(self)

    async def estimate(
        self,
        chain_id: Literal[
            "ethereum",
            "base",
            "optimism",
            "arbitrum",
            "arbitrumNova",
            "polygon",
            "avalanche",
            "bsc",
            "opbnb",
            "unichain",
            "worldchain",
            "abstract",
            "apechain",
            "hyperliquid",
        ],
        *,
        transaction: object | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Estimate gas for transaction

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chain_id:
            raise ValueError(f"Expected a non-empty value for `chain_id` but received {chain_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            f"/evm/{chain_id}/gas/estimate",
            body=await async_maybe_transform({"transaction": transaction}, gas_estimate_params.GasEstimateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def get_price(
        self,
        chain_id: Literal[
            "ethereum",
            "base",
            "optimism",
            "arbitrum",
            "arbitrumNova",
            "polygon",
            "avalanche",
            "bsc",
            "opbnb",
            "unichain",
            "worldchain",
            "abstract",
            "apechain",
            "hyperliquid",
        ],
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Get current gas price

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chain_id:
            raise ValueError(f"Expected a non-empty value for `chain_id` but received {chain_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            f"/evm/{chain_id}/gas/price",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class GasResourceWithRawResponse:
    def __init__(self, gas: GasResource) -> None:
        self._gas = gas

        self.estimate = to_raw_response_wrapper(
            gas.estimate,
        )
        self.get_price = to_raw_response_wrapper(
            gas.get_price,
        )


class AsyncGasResourceWithRawResponse:
    def __init__(self, gas: AsyncGasResource) -> None:
        self._gas = gas

        self.estimate = async_to_raw_response_wrapper(
            gas.estimate,
        )
        self.get_price = async_to_raw_response_wrapper(
            gas.get_price,
        )


class GasResourceWithStreamingResponse:
    def __init__(self, gas: GasResource) -> None:
        self._gas = gas

        self.estimate = to_streamed_response_wrapper(
            gas.estimate,
        )
        self.get_price = to_streamed_response_wrapper(
            gas.get_price,
        )


class AsyncGasResourceWithStreamingResponse:
    def __init__(self, gas: AsyncGasResource) -> None:
        self._gas = gas

        self.estimate = async_to_streamed_response_wrapper(
            gas.estimate,
        )
        self.get_price = async_to_streamed_response_wrapper(
            gas.get_price,
        )
