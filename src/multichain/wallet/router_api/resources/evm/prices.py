# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

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
from ...types.evm import price_get_by_symbol_params, price_get_by_address_params
from ..._base_client import make_request_options

__all__ = ["PricesResource", "AsyncPricesResource"]


class PricesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PricesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/multichain.wallet.router-api-python#accessing-raw-response-data-eg-headers
        """
        return PricesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PricesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/multichain.wallet.router-api-python#with_streaming_response
        """
        return PricesResourceWithStreamingResponse(self)

    def get_by_address(
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
        addresses: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Get token prices by address

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
            f"/evm/{chain_id}/prices/by-address",
            body=maybe_transform({"addresses": addresses}, price_get_by_address_params.PriceGetByAddressParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def get_by_symbol(
        self,
        *,
        symbols: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Get token prices by symbol

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/evm/prices/by-symbol",
            body=maybe_transform({"symbols": symbols}, price_get_by_symbol_params.PriceGetBySymbolParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncPricesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPricesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/multichain.wallet.router-api-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPricesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPricesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/multichain.wallet.router-api-python#with_streaming_response
        """
        return AsyncPricesResourceWithStreamingResponse(self)

    async def get_by_address(
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
        addresses: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Get token prices by address

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
            f"/evm/{chain_id}/prices/by-address",
            body=await async_maybe_transform(
                {"addresses": addresses}, price_get_by_address_params.PriceGetByAddressParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def get_by_symbol(
        self,
        *,
        symbols: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Get token prices by symbol

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/evm/prices/by-symbol",
            body=await async_maybe_transform({"symbols": symbols}, price_get_by_symbol_params.PriceGetBySymbolParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class PricesResourceWithRawResponse:
    def __init__(self, prices: PricesResource) -> None:
        self._prices = prices

        self.get_by_address = to_raw_response_wrapper(
            prices.get_by_address,
        )
        self.get_by_symbol = to_raw_response_wrapper(
            prices.get_by_symbol,
        )


class AsyncPricesResourceWithRawResponse:
    def __init__(self, prices: AsyncPricesResource) -> None:
        self._prices = prices

        self.get_by_address = async_to_raw_response_wrapper(
            prices.get_by_address,
        )
        self.get_by_symbol = async_to_raw_response_wrapper(
            prices.get_by_symbol,
        )


class PricesResourceWithStreamingResponse:
    def __init__(self, prices: PricesResource) -> None:
        self._prices = prices

        self.get_by_address = to_streamed_response_wrapper(
            prices.get_by_address,
        )
        self.get_by_symbol = to_streamed_response_wrapper(
            prices.get_by_symbol,
        )


class AsyncPricesResourceWithStreamingResponse:
    def __init__(self, prices: AsyncPricesResource) -> None:
        self._prices = prices

        self.get_by_address = async_to_streamed_response_wrapper(
            prices.get_by_address,
        )
        self.get_by_symbol = async_to_streamed_response_wrapper(
            prices.get_by_symbol,
        )
