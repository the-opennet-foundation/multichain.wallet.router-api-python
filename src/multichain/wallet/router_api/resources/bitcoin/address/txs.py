# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.bitcoin.address import tx_get_paginated_params

__all__ = ["TxsResource", "AsyncTxsResource"]


class TxsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TxsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/the-opennet-foundation/multichain.wallet.router-api-python#accessing-raw-response-data-eg-headers
        """
        return TxsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TxsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/the-opennet-foundation/multichain.wallet.router-api-python#with_streaming_response
        """
        return TxsResourceWithStreamingResponse(self)

    def get_all(
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
        Get address transactions

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
            f"/bitcoin/address/{address}/txs",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def get_paginated(
        self,
        address: str,
        *,
        last_seen_txid: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Get address transactions (paginated)

        Args:
          last_seen_txid: Last seen txid for pagination

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not address:
            raise ValueError(f"Expected a non-empty value for `address` but received {address!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            f"/bitcoin/address/{address}/txs/chain",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"last_seen_txid": last_seen_txid}, tx_get_paginated_params.TxGetPaginatedParams),
            ),
            cast_to=NoneType,
        )


class AsyncTxsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTxsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/the-opennet-foundation/multichain.wallet.router-api-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTxsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTxsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/the-opennet-foundation/multichain.wallet.router-api-python#with_streaming_response
        """
        return AsyncTxsResourceWithStreamingResponse(self)

    async def get_all(
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
        Get address transactions

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
            f"/bitcoin/address/{address}/txs",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def get_paginated(
        self,
        address: str,
        *,
        last_seen_txid: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Get address transactions (paginated)

        Args:
          last_seen_txid: Last seen txid for pagination

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not address:
            raise ValueError(f"Expected a non-empty value for `address` but received {address!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            f"/bitcoin/address/{address}/txs/chain",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"last_seen_txid": last_seen_txid}, tx_get_paginated_params.TxGetPaginatedParams
                ),
            ),
            cast_to=NoneType,
        )


class TxsResourceWithRawResponse:
    def __init__(self, txs: TxsResource) -> None:
        self._txs = txs

        self.get_all = to_raw_response_wrapper(
            txs.get_all,
        )
        self.get_paginated = to_raw_response_wrapper(
            txs.get_paginated,
        )


class AsyncTxsResourceWithRawResponse:
    def __init__(self, txs: AsyncTxsResource) -> None:
        self._txs = txs

        self.get_all = async_to_raw_response_wrapper(
            txs.get_all,
        )
        self.get_paginated = async_to_raw_response_wrapper(
            txs.get_paginated,
        )


class TxsResourceWithStreamingResponse:
    def __init__(self, txs: TxsResource) -> None:
        self._txs = txs

        self.get_all = to_streamed_response_wrapper(
            txs.get_all,
        )
        self.get_paginated = to_streamed_response_wrapper(
            txs.get_paginated,
        )


class AsyncTxsResourceWithStreamingResponse:
    def __init__(self, txs: AsyncTxsResource) -> None:
        self._txs = txs

        self.get_all = async_to_streamed_response_wrapper(
            txs.get_all,
        )
        self.get_paginated = async_to_streamed_response_wrapper(
            txs.get_paginated,
        )
