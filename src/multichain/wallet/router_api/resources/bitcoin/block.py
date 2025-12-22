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
from ...types.bitcoin import block_get_header_params, block_get_by_hash_params, block_get_transactions_params

__all__ = ["BlockResource", "AsyncBlockResource"]


class BlockResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BlockResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/multichain.wallet.router-api-python#accessing-raw-response-data-eg-headers
        """
        return BlockResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BlockResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/multichain.wallet.router-api-python#with_streaming_response
        """
        return BlockResourceWithStreamingResponse(self)

    def get_best(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Get best block hash"""
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            "/bitcoin/block/best",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def get_by_hash(
        self,
        hash: str,
        *,
        verbosity: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Get block by hash

        Args:
          verbosity: 0=hex, 1=json, 2=json+txs

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not hash:
            raise ValueError(f"Expected a non-empty value for `hash` but received {hash!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            f"/bitcoin/block/hash/{hash}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"verbosity": verbosity}, block_get_by_hash_params.BlockGetByHashParams),
            ),
            cast_to=NoneType,
        )

    def get_by_height(
        self,
        height: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Get block by height

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            f"/bitcoin/block/height/{height}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def get_header(
        self,
        hash: str,
        *,
        verbose: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Get block header

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not hash:
            raise ValueError(f"Expected a non-empty value for `hash` but received {hash!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            f"/bitcoin/block/{hash}/header",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"verbose": verbose}, block_get_header_params.BlockGetHeaderParams),
            ),
            cast_to=NoneType,
        )

    def get_stats(
        self,
        hash: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Get block stats

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not hash:
            raise ValueError(f"Expected a non-empty value for `hash` but received {hash!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            f"/bitcoin/block/{hash}/stats",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def get_tip(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Get current block height"""
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            "/bitcoin/block/tip",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def get_transaction_ids(
        self,
        hash: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Get block transaction IDs

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not hash:
            raise ValueError(f"Expected a non-empty value for `hash` but received {hash!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            f"/bitcoin/block/{hash}/txids",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def get_transactions(
        self,
        hash: str,
        *,
        start_index: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Get block transactions

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not hash:
            raise ValueError(f"Expected a non-empty value for `hash` but received {hash!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            f"/bitcoin/block/{hash}/txs",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"start_index": start_index}, block_get_transactions_params.BlockGetTransactionsParams
                ),
            ),
            cast_to=NoneType,
        )


class AsyncBlockResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBlockResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/multichain.wallet.router-api-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBlockResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBlockResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/multichain.wallet.router-api-python#with_streaming_response
        """
        return AsyncBlockResourceWithStreamingResponse(self)

    async def get_best(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Get best block hash"""
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            "/bitcoin/block/best",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def get_by_hash(
        self,
        hash: str,
        *,
        verbosity: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Get block by hash

        Args:
          verbosity: 0=hex, 1=json, 2=json+txs

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not hash:
            raise ValueError(f"Expected a non-empty value for `hash` but received {hash!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            f"/bitcoin/block/hash/{hash}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"verbosity": verbosity}, block_get_by_hash_params.BlockGetByHashParams
                ),
            ),
            cast_to=NoneType,
        )

    async def get_by_height(
        self,
        height: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Get block by height

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            f"/bitcoin/block/height/{height}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def get_header(
        self,
        hash: str,
        *,
        verbose: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Get block header

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not hash:
            raise ValueError(f"Expected a non-empty value for `hash` but received {hash!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            f"/bitcoin/block/{hash}/header",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"verbose": verbose}, block_get_header_params.BlockGetHeaderParams),
            ),
            cast_to=NoneType,
        )

    async def get_stats(
        self,
        hash: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Get block stats

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not hash:
            raise ValueError(f"Expected a non-empty value for `hash` but received {hash!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            f"/bitcoin/block/{hash}/stats",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def get_tip(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Get current block height"""
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            "/bitcoin/block/tip",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def get_transaction_ids(
        self,
        hash: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Get block transaction IDs

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not hash:
            raise ValueError(f"Expected a non-empty value for `hash` but received {hash!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            f"/bitcoin/block/{hash}/txids",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def get_transactions(
        self,
        hash: str,
        *,
        start_index: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Get block transactions

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not hash:
            raise ValueError(f"Expected a non-empty value for `hash` but received {hash!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            f"/bitcoin/block/{hash}/txs",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"start_index": start_index}, block_get_transactions_params.BlockGetTransactionsParams
                ),
            ),
            cast_to=NoneType,
        )


class BlockResourceWithRawResponse:
    def __init__(self, block: BlockResource) -> None:
        self._block = block

        self.get_best = to_raw_response_wrapper(
            block.get_best,
        )
        self.get_by_hash = to_raw_response_wrapper(
            block.get_by_hash,
        )
        self.get_by_height = to_raw_response_wrapper(
            block.get_by_height,
        )
        self.get_header = to_raw_response_wrapper(
            block.get_header,
        )
        self.get_stats = to_raw_response_wrapper(
            block.get_stats,
        )
        self.get_tip = to_raw_response_wrapper(
            block.get_tip,
        )
        self.get_transaction_ids = to_raw_response_wrapper(
            block.get_transaction_ids,
        )
        self.get_transactions = to_raw_response_wrapper(
            block.get_transactions,
        )


class AsyncBlockResourceWithRawResponse:
    def __init__(self, block: AsyncBlockResource) -> None:
        self._block = block

        self.get_best = async_to_raw_response_wrapper(
            block.get_best,
        )
        self.get_by_hash = async_to_raw_response_wrapper(
            block.get_by_hash,
        )
        self.get_by_height = async_to_raw_response_wrapper(
            block.get_by_height,
        )
        self.get_header = async_to_raw_response_wrapper(
            block.get_header,
        )
        self.get_stats = async_to_raw_response_wrapper(
            block.get_stats,
        )
        self.get_tip = async_to_raw_response_wrapper(
            block.get_tip,
        )
        self.get_transaction_ids = async_to_raw_response_wrapper(
            block.get_transaction_ids,
        )
        self.get_transactions = async_to_raw_response_wrapper(
            block.get_transactions,
        )


class BlockResourceWithStreamingResponse:
    def __init__(self, block: BlockResource) -> None:
        self._block = block

        self.get_best = to_streamed_response_wrapper(
            block.get_best,
        )
        self.get_by_hash = to_streamed_response_wrapper(
            block.get_by_hash,
        )
        self.get_by_height = to_streamed_response_wrapper(
            block.get_by_height,
        )
        self.get_header = to_streamed_response_wrapper(
            block.get_header,
        )
        self.get_stats = to_streamed_response_wrapper(
            block.get_stats,
        )
        self.get_tip = to_streamed_response_wrapper(
            block.get_tip,
        )
        self.get_transaction_ids = to_streamed_response_wrapper(
            block.get_transaction_ids,
        )
        self.get_transactions = to_streamed_response_wrapper(
            block.get_transactions,
        )


class AsyncBlockResourceWithStreamingResponse:
    def __init__(self, block: AsyncBlockResource) -> None:
        self._block = block

        self.get_best = async_to_streamed_response_wrapper(
            block.get_best,
        )
        self.get_by_hash = async_to_streamed_response_wrapper(
            block.get_by_hash,
        )
        self.get_by_height = async_to_streamed_response_wrapper(
            block.get_by_height,
        )
        self.get_header = async_to_streamed_response_wrapper(
            block.get_header,
        )
        self.get_stats = async_to_streamed_response_wrapper(
            block.get_stats,
        )
        self.get_tip = async_to_streamed_response_wrapper(
            block.get_tip,
        )
        self.get_transaction_ids = async_to_streamed_response_wrapper(
            block.get_transaction_ids,
        )
        self.get_transactions = async_to_streamed_response_wrapper(
            block.get_transactions,
        )
