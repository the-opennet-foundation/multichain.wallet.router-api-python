# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .txs import (
    TxsResource,
    AsyncTxsResource,
    TxsResourceWithRawResponse,
    AsyncTxsResourceWithRawResponse,
    TxsResourceWithStreamingResponse,
    AsyncTxsResourceWithStreamingResponse,
)
from ...._types import Body, Query, Headers, NoneType, NotGiven, not_given
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options

__all__ = ["AddressResource", "AsyncAddressResource"]


class AddressResource(SyncAPIResource):
    @cached_property
    def txs(self) -> TxsResource:
        return TxsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AddressResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/multichain.wallet.router-api-python#accessing-raw-response-data-eg-headers
        """
        return AddressResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AddressResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/multichain.wallet.router-api-python#with_streaming_response
        """
        return AddressResourceWithStreamingResponse(self)

    def get_info(
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
        Returns balance, tx count, funded/spent sums

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
            f"/bitcoin/address/{address}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def get_utxos(
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
        Returns unspent transaction outputs

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
            f"/bitcoin/address/{address}/utxo",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncAddressResource(AsyncAPIResource):
    @cached_property
    def txs(self) -> AsyncTxsResource:
        return AsyncTxsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAddressResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/multichain.wallet.router-api-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAddressResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAddressResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/multichain.wallet.router-api-python#with_streaming_response
        """
        return AsyncAddressResourceWithStreamingResponse(self)

    async def get_info(
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
        Returns balance, tx count, funded/spent sums

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
            f"/bitcoin/address/{address}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def get_utxos(
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
        Returns unspent transaction outputs

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
            f"/bitcoin/address/{address}/utxo",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AddressResourceWithRawResponse:
    def __init__(self, address: AddressResource) -> None:
        self._address = address

        self.get_info = to_raw_response_wrapper(
            address.get_info,
        )
        self.get_utxos = to_raw_response_wrapper(
            address.get_utxos,
        )

    @cached_property
    def txs(self) -> TxsResourceWithRawResponse:
        return TxsResourceWithRawResponse(self._address.txs)


class AsyncAddressResourceWithRawResponse:
    def __init__(self, address: AsyncAddressResource) -> None:
        self._address = address

        self.get_info = async_to_raw_response_wrapper(
            address.get_info,
        )
        self.get_utxos = async_to_raw_response_wrapper(
            address.get_utxos,
        )

    @cached_property
    def txs(self) -> AsyncTxsResourceWithRawResponse:
        return AsyncTxsResourceWithRawResponse(self._address.txs)


class AddressResourceWithStreamingResponse:
    def __init__(self, address: AddressResource) -> None:
        self._address = address

        self.get_info = to_streamed_response_wrapper(
            address.get_info,
        )
        self.get_utxos = to_streamed_response_wrapper(
            address.get_utxos,
        )

    @cached_property
    def txs(self) -> TxsResourceWithStreamingResponse:
        return TxsResourceWithStreamingResponse(self._address.txs)


class AsyncAddressResourceWithStreamingResponse:
    def __init__(self, address: AsyncAddressResource) -> None:
        self._address = address

        self.get_info = async_to_streamed_response_wrapper(
            address.get_info,
        )
        self.get_utxos = async_to_streamed_response_wrapper(
            address.get_utxos,
        )

    @cached_property
    def txs(self) -> AsyncTxsResourceWithStreamingResponse:
        return AsyncTxsResourceWithStreamingResponse(self._address.txs)
