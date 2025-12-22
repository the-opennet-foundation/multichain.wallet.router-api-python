# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .tx import (
    TxResource,
    AsyncTxResource,
    TxResourceWithRawResponse,
    AsyncTxResourceWithRawResponse,
    TxResourceWithStreamingResponse,
    AsyncTxResourceWithStreamingResponse,
)
from .fees import (
    FeesResource,
    AsyncFeesResource,
    FeesResourceWithRawResponse,
    AsyncFeesResourceWithRawResponse,
    FeesResourceWithStreamingResponse,
    AsyncFeesResourceWithStreamingResponse,
)
from .block import (
    BlockResource,
    AsyncBlockResource,
    BlockResourceWithRawResponse,
    AsyncBlockResourceWithRawResponse,
    BlockResourceWithStreamingResponse,
    AsyncBlockResourceWithStreamingResponse,
)
from ...types import bitcoin_get_utxo_params, bitcoin_get_hashrate_params
from .mempool import (
    MempoolResource,
    AsyncMempoolResource,
    MempoolResourceWithRawResponse,
    AsyncMempoolResourceWithRawResponse,
    MempoolResourceWithStreamingResponse,
    AsyncMempoolResourceWithStreamingResponse,
)
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
from .address.address import (
    AddressResource,
    AsyncAddressResource,
    AddressResourceWithRawResponse,
    AsyncAddressResourceWithRawResponse,
    AddressResourceWithStreamingResponse,
    AsyncAddressResourceWithStreamingResponse,
)

__all__ = ["BitcoinResource", "AsyncBitcoinResource"]


class BitcoinResource(SyncAPIResource):
    @cached_property
    def address(self) -> AddressResource:
        return AddressResource(self._client)

    @cached_property
    def tx(self) -> TxResource:
        return TxResource(self._client)

    @cached_property
    def block(self) -> BlockResource:
        return BlockResource(self._client)

    @cached_property
    def mempool(self) -> MempoolResource:
        return MempoolResource(self._client)

    @cached_property
    def fees(self) -> FeesResource:
        return FeesResource(self._client)

    @cached_property
    def with_raw_response(self) -> BitcoinResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/the-opennet-foundation/multichain.wallet.router-api-python#accessing-raw-response-data-eg-headers
        """
        return BitcoinResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BitcoinResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/the-opennet-foundation/multichain.wallet.router-api-python#with_streaming_response
        """
        return BitcoinResourceWithStreamingResponse(self)

    def get_difficulty(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Get current mining difficulty"""
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            "/bitcoin/difficulty",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def get_hashrate(
        self,
        *,
        height: int | Omit = omit,
        nblocks: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Get network hashrate

        Args:
          height: Block height (-1 for latest)

          nblocks: Number of blocks to average

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            "/bitcoin/hashrate",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "height": height,
                        "nblocks": nblocks,
                    },
                    bitcoin_get_hashrate_params.BitcoinGetHashrateParams,
                ),
            ),
            cast_to=NoneType,
        )

    def get_info(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Returns chain, blocks, headers, difficulty, etc."""
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            "/bitcoin/info",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def get_price(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Get BTC price (USD, EUR, GBP)"""
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            "/bitcoin/price",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def get_utxo(
        self,
        vout: int,
        *,
        txid: str,
        include_mempool: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Get specific UTXO

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not txid:
            raise ValueError(f"Expected a non-empty value for `txid` but received {txid!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            f"/bitcoin/utxo/{txid}/{vout}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"include_mempool": include_mempool}, bitcoin_get_utxo_params.BitcoinGetUtxoParams
                ),
            ),
            cast_to=NoneType,
        )

    def validate_address(
        self,
        address: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Validate Bitcoin address

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not address:
            raise ValueError(f"Expected a non-empty value for `address` but received {address!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            f"/bitcoin/validate/{address}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncBitcoinResource(AsyncAPIResource):
    @cached_property
    def address(self) -> AsyncAddressResource:
        return AsyncAddressResource(self._client)

    @cached_property
    def tx(self) -> AsyncTxResource:
        return AsyncTxResource(self._client)

    @cached_property
    def block(self) -> AsyncBlockResource:
        return AsyncBlockResource(self._client)

    @cached_property
    def mempool(self) -> AsyncMempoolResource:
        return AsyncMempoolResource(self._client)

    @cached_property
    def fees(self) -> AsyncFeesResource:
        return AsyncFeesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncBitcoinResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/the-opennet-foundation/multichain.wallet.router-api-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBitcoinResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBitcoinResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/the-opennet-foundation/multichain.wallet.router-api-python#with_streaming_response
        """
        return AsyncBitcoinResourceWithStreamingResponse(self)

    async def get_difficulty(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Get current mining difficulty"""
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            "/bitcoin/difficulty",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def get_hashrate(
        self,
        *,
        height: int | Omit = omit,
        nblocks: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Get network hashrate

        Args:
          height: Block height (-1 for latest)

          nblocks: Number of blocks to average

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            "/bitcoin/hashrate",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "height": height,
                        "nblocks": nblocks,
                    },
                    bitcoin_get_hashrate_params.BitcoinGetHashrateParams,
                ),
            ),
            cast_to=NoneType,
        )

    async def get_info(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Returns chain, blocks, headers, difficulty, etc."""
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            "/bitcoin/info",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def get_price(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Get BTC price (USD, EUR, GBP)"""
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            "/bitcoin/price",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def get_utxo(
        self,
        vout: int,
        *,
        txid: str,
        include_mempool: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Get specific UTXO

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not txid:
            raise ValueError(f"Expected a non-empty value for `txid` but received {txid!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            f"/bitcoin/utxo/{txid}/{vout}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"include_mempool": include_mempool}, bitcoin_get_utxo_params.BitcoinGetUtxoParams
                ),
            ),
            cast_to=NoneType,
        )

    async def validate_address(
        self,
        address: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Validate Bitcoin address

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not address:
            raise ValueError(f"Expected a non-empty value for `address` but received {address!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            f"/bitcoin/validate/{address}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class BitcoinResourceWithRawResponse:
    def __init__(self, bitcoin: BitcoinResource) -> None:
        self._bitcoin = bitcoin

        self.get_difficulty = to_raw_response_wrapper(
            bitcoin.get_difficulty,
        )
        self.get_hashrate = to_raw_response_wrapper(
            bitcoin.get_hashrate,
        )
        self.get_info = to_raw_response_wrapper(
            bitcoin.get_info,
        )
        self.get_price = to_raw_response_wrapper(
            bitcoin.get_price,
        )
        self.get_utxo = to_raw_response_wrapper(
            bitcoin.get_utxo,
        )
        self.validate_address = to_raw_response_wrapper(
            bitcoin.validate_address,
        )

    @cached_property
    def address(self) -> AddressResourceWithRawResponse:
        return AddressResourceWithRawResponse(self._bitcoin.address)

    @cached_property
    def tx(self) -> TxResourceWithRawResponse:
        return TxResourceWithRawResponse(self._bitcoin.tx)

    @cached_property
    def block(self) -> BlockResourceWithRawResponse:
        return BlockResourceWithRawResponse(self._bitcoin.block)

    @cached_property
    def mempool(self) -> MempoolResourceWithRawResponse:
        return MempoolResourceWithRawResponse(self._bitcoin.mempool)

    @cached_property
    def fees(self) -> FeesResourceWithRawResponse:
        return FeesResourceWithRawResponse(self._bitcoin.fees)


class AsyncBitcoinResourceWithRawResponse:
    def __init__(self, bitcoin: AsyncBitcoinResource) -> None:
        self._bitcoin = bitcoin

        self.get_difficulty = async_to_raw_response_wrapper(
            bitcoin.get_difficulty,
        )
        self.get_hashrate = async_to_raw_response_wrapper(
            bitcoin.get_hashrate,
        )
        self.get_info = async_to_raw_response_wrapper(
            bitcoin.get_info,
        )
        self.get_price = async_to_raw_response_wrapper(
            bitcoin.get_price,
        )
        self.get_utxo = async_to_raw_response_wrapper(
            bitcoin.get_utxo,
        )
        self.validate_address = async_to_raw_response_wrapper(
            bitcoin.validate_address,
        )

    @cached_property
    def address(self) -> AsyncAddressResourceWithRawResponse:
        return AsyncAddressResourceWithRawResponse(self._bitcoin.address)

    @cached_property
    def tx(self) -> AsyncTxResourceWithRawResponse:
        return AsyncTxResourceWithRawResponse(self._bitcoin.tx)

    @cached_property
    def block(self) -> AsyncBlockResourceWithRawResponse:
        return AsyncBlockResourceWithRawResponse(self._bitcoin.block)

    @cached_property
    def mempool(self) -> AsyncMempoolResourceWithRawResponse:
        return AsyncMempoolResourceWithRawResponse(self._bitcoin.mempool)

    @cached_property
    def fees(self) -> AsyncFeesResourceWithRawResponse:
        return AsyncFeesResourceWithRawResponse(self._bitcoin.fees)


class BitcoinResourceWithStreamingResponse:
    def __init__(self, bitcoin: BitcoinResource) -> None:
        self._bitcoin = bitcoin

        self.get_difficulty = to_streamed_response_wrapper(
            bitcoin.get_difficulty,
        )
        self.get_hashrate = to_streamed_response_wrapper(
            bitcoin.get_hashrate,
        )
        self.get_info = to_streamed_response_wrapper(
            bitcoin.get_info,
        )
        self.get_price = to_streamed_response_wrapper(
            bitcoin.get_price,
        )
        self.get_utxo = to_streamed_response_wrapper(
            bitcoin.get_utxo,
        )
        self.validate_address = to_streamed_response_wrapper(
            bitcoin.validate_address,
        )

    @cached_property
    def address(self) -> AddressResourceWithStreamingResponse:
        return AddressResourceWithStreamingResponse(self._bitcoin.address)

    @cached_property
    def tx(self) -> TxResourceWithStreamingResponse:
        return TxResourceWithStreamingResponse(self._bitcoin.tx)

    @cached_property
    def block(self) -> BlockResourceWithStreamingResponse:
        return BlockResourceWithStreamingResponse(self._bitcoin.block)

    @cached_property
    def mempool(self) -> MempoolResourceWithStreamingResponse:
        return MempoolResourceWithStreamingResponse(self._bitcoin.mempool)

    @cached_property
    def fees(self) -> FeesResourceWithStreamingResponse:
        return FeesResourceWithStreamingResponse(self._bitcoin.fees)


class AsyncBitcoinResourceWithStreamingResponse:
    def __init__(self, bitcoin: AsyncBitcoinResource) -> None:
        self._bitcoin = bitcoin

        self.get_difficulty = async_to_streamed_response_wrapper(
            bitcoin.get_difficulty,
        )
        self.get_hashrate = async_to_streamed_response_wrapper(
            bitcoin.get_hashrate,
        )
        self.get_info = async_to_streamed_response_wrapper(
            bitcoin.get_info,
        )
        self.get_price = async_to_streamed_response_wrapper(
            bitcoin.get_price,
        )
        self.get_utxo = async_to_streamed_response_wrapper(
            bitcoin.get_utxo,
        )
        self.validate_address = async_to_streamed_response_wrapper(
            bitcoin.validate_address,
        )

    @cached_property
    def address(self) -> AsyncAddressResourceWithStreamingResponse:
        return AsyncAddressResourceWithStreamingResponse(self._bitcoin.address)

    @cached_property
    def tx(self) -> AsyncTxResourceWithStreamingResponse:
        return AsyncTxResourceWithStreamingResponse(self._bitcoin.tx)

    @cached_property
    def block(self) -> AsyncBlockResourceWithStreamingResponse:
        return AsyncBlockResourceWithStreamingResponse(self._bitcoin.block)

    @cached_property
    def mempool(self) -> AsyncMempoolResourceWithStreamingResponse:
        return AsyncMempoolResourceWithStreamingResponse(self._bitcoin.mempool)

    @cached_property
    def fees(self) -> AsyncFeesResourceWithStreamingResponse:
        return AsyncFeesResourceWithStreamingResponse(self._bitcoin.fees)
