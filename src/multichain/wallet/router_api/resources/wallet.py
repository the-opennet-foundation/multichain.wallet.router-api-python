# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from .._types import Body, Query, Headers, NoneType, NotGiven, not_given
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options

__all__ = ["WalletResource", "AsyncWalletResource"]


class WalletResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> WalletResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/multichain.wallet.router-api-python#accessing-raw-response-data-eg-headers
        """
        return WalletResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WalletResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/multichain.wallet.router-api-python#with_streaming_response
        """
        return WalletResourceWithStreamingResponse(self)

    def list_chains(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Get all EVM chain configs for wallet_addEthereumChain"""
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            "/wallet/chains",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def retrieve_chain(
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
        Get single chain config

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
            f"/wallet/add-chain/{chain_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncWalletResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncWalletResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/multichain.wallet.router-api-python#accessing-raw-response-data-eg-headers
        """
        return AsyncWalletResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWalletResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/multichain.wallet.router-api-python#with_streaming_response
        """
        return AsyncWalletResourceWithStreamingResponse(self)

    async def list_chains(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Get all EVM chain configs for wallet_addEthereumChain"""
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            "/wallet/chains",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def retrieve_chain(
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
        Get single chain config

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
            f"/wallet/add-chain/{chain_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class WalletResourceWithRawResponse:
    def __init__(self, wallet: WalletResource) -> None:
        self._wallet = wallet

        self.list_chains = to_raw_response_wrapper(
            wallet.list_chains,
        )
        self.retrieve_chain = to_raw_response_wrapper(
            wallet.retrieve_chain,
        )


class AsyncWalletResourceWithRawResponse:
    def __init__(self, wallet: AsyncWalletResource) -> None:
        self._wallet = wallet

        self.list_chains = async_to_raw_response_wrapper(
            wallet.list_chains,
        )
        self.retrieve_chain = async_to_raw_response_wrapper(
            wallet.retrieve_chain,
        )


class WalletResourceWithStreamingResponse:
    def __init__(self, wallet: WalletResource) -> None:
        self._wallet = wallet

        self.list_chains = to_streamed_response_wrapper(
            wallet.list_chains,
        )
        self.retrieve_chain = to_streamed_response_wrapper(
            wallet.retrieve_chain,
        )


class AsyncWalletResourceWithStreamingResponse:
    def __init__(self, wallet: AsyncWalletResource) -> None:
        self._wallet = wallet

        self.list_chains = async_to_streamed_response_wrapper(
            wallet.list_chains,
        )
        self.retrieve_chain = async_to_streamed_response_wrapper(
            wallet.retrieve_chain,
        )
