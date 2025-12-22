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
from ...types.solana import jupiter_swap_params, jupiter_get_price_params, jupiter_get_quote_params

__all__ = ["JupiterResource", "AsyncJupiterResource"]


class JupiterResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> JupiterResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/multichain.wallet.router-api-python#accessing-raw-response-data-eg-headers
        """
        return JupiterResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> JupiterResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/multichain.wallet.router-api-python#with_streaming_response
        """
        return JupiterResourceWithStreamingResponse(self)

    def get_price(
        self,
        *,
        ids: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Get token prices (USD)

        Args:
          ids: Comma-separated mint addresses

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            "/solana/jupiter/price",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"ids": ids}, jupiter_get_price_params.JupiterGetPriceParams),
            ),
            cast_to=NoneType,
        )

    def get_quote(
        self,
        *,
        amount: int,
        input_mint: str,
        output_mint: str,
        slippage_bps: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Returns best route, output amount, price impact

        Args:
          amount: Input amount in base units

          input_mint: Input token mint

          output_mint: Output token mint

          slippage_bps: Slippage in basis points (100 = 1%)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            "/solana/jupiter/quote",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "amount": amount,
                        "input_mint": input_mint,
                        "output_mint": output_mint,
                        "slippage_bps": slippage_bps,
                    },
                    jupiter_get_quote_params.JupiterGetQuoteParams,
                ),
            ),
            cast_to=NoneType,
        )

    def get_tokens(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Get all tradeable tokens"""
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            "/solana/jupiter/tokens",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def swap(
        self,
        *,
        quote_response: object,
        user_public_key: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Build swap transaction from quote

        Args:
          quote_response: Quote response from /jupiter/quote

          user_public_key: User wallet public key

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/solana/jupiter/swap",
            body=maybe_transform(
                {
                    "quote_response": quote_response,
                    "user_public_key": user_public_key,
                },
                jupiter_swap_params.JupiterSwapParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncJupiterResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncJupiterResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/multichain.wallet.router-api-python#accessing-raw-response-data-eg-headers
        """
        return AsyncJupiterResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncJupiterResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/multichain.wallet.router-api-python#with_streaming_response
        """
        return AsyncJupiterResourceWithStreamingResponse(self)

    async def get_price(
        self,
        *,
        ids: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Get token prices (USD)

        Args:
          ids: Comma-separated mint addresses

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            "/solana/jupiter/price",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"ids": ids}, jupiter_get_price_params.JupiterGetPriceParams),
            ),
            cast_to=NoneType,
        )

    async def get_quote(
        self,
        *,
        amount: int,
        input_mint: str,
        output_mint: str,
        slippage_bps: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Returns best route, output amount, price impact

        Args:
          amount: Input amount in base units

          input_mint: Input token mint

          output_mint: Output token mint

          slippage_bps: Slippage in basis points (100 = 1%)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            "/solana/jupiter/quote",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "amount": amount,
                        "input_mint": input_mint,
                        "output_mint": output_mint,
                        "slippage_bps": slippage_bps,
                    },
                    jupiter_get_quote_params.JupiterGetQuoteParams,
                ),
            ),
            cast_to=NoneType,
        )

    async def get_tokens(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Get all tradeable tokens"""
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            "/solana/jupiter/tokens",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def swap(
        self,
        *,
        quote_response: object,
        user_public_key: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Build swap transaction from quote

        Args:
          quote_response: Quote response from /jupiter/quote

          user_public_key: User wallet public key

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/solana/jupiter/swap",
            body=await async_maybe_transform(
                {
                    "quote_response": quote_response,
                    "user_public_key": user_public_key,
                },
                jupiter_swap_params.JupiterSwapParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class JupiterResourceWithRawResponse:
    def __init__(self, jupiter: JupiterResource) -> None:
        self._jupiter = jupiter

        self.get_price = to_raw_response_wrapper(
            jupiter.get_price,
        )
        self.get_quote = to_raw_response_wrapper(
            jupiter.get_quote,
        )
        self.get_tokens = to_raw_response_wrapper(
            jupiter.get_tokens,
        )
        self.swap = to_raw_response_wrapper(
            jupiter.swap,
        )


class AsyncJupiterResourceWithRawResponse:
    def __init__(self, jupiter: AsyncJupiterResource) -> None:
        self._jupiter = jupiter

        self.get_price = async_to_raw_response_wrapper(
            jupiter.get_price,
        )
        self.get_quote = async_to_raw_response_wrapper(
            jupiter.get_quote,
        )
        self.get_tokens = async_to_raw_response_wrapper(
            jupiter.get_tokens,
        )
        self.swap = async_to_raw_response_wrapper(
            jupiter.swap,
        )


class JupiterResourceWithStreamingResponse:
    def __init__(self, jupiter: JupiterResource) -> None:
        self._jupiter = jupiter

        self.get_price = to_streamed_response_wrapper(
            jupiter.get_price,
        )
        self.get_quote = to_streamed_response_wrapper(
            jupiter.get_quote,
        )
        self.get_tokens = to_streamed_response_wrapper(
            jupiter.get_tokens,
        )
        self.swap = to_streamed_response_wrapper(
            jupiter.swap,
        )


class AsyncJupiterResourceWithStreamingResponse:
    def __init__(self, jupiter: AsyncJupiterResource) -> None:
        self._jupiter = jupiter

        self.get_price = async_to_streamed_response_wrapper(
            jupiter.get_price,
        )
        self.get_quote = async_to_streamed_response_wrapper(
            jupiter.get_quote,
        )
        self.get_tokens = async_to_streamed_response_wrapper(
            jupiter.get_tokens,
        )
        self.swap = async_to_streamed_response_wrapper(
            jupiter.swap,
        )
