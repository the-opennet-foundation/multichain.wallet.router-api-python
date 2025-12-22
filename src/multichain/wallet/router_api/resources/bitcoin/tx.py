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
from ...types.bitcoin import tx_decode_params, tx_get_raw_params, tx_broadcast_params, tx_test_mempool_params

__all__ = ["TxResource", "AsyncTxResource"]


class TxResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TxResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/multichain.wallet.router-api-python#accessing-raw-response-data-eg-headers
        """
        return TxResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TxResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/multichain.wallet.router-api-python#with_streaming_response
        """
        return TxResourceWithStreamingResponse(self)

    def broadcast(
        self,
        *,
        hex: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Broadcast transaction

        Args:
          hex: Signed transaction hex

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/bitcoin/tx/send",
            body=maybe_transform({"hex": hex}, tx_broadcast_params.TxBroadcastParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def decode(
        self,
        *,
        hex: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Decode raw transaction

        Args:
          hex: Raw transaction hex

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/bitcoin/tx/decode",
            body=maybe_transform({"hex": hex}, tx_decode_params.TxDecodeParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def get_info(
        self,
        txid: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Get transaction info

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
            f"/bitcoin/tx/{txid}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def get_raw(
        self,
        txid: str,
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
        Get raw transaction (verbose)

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
            f"/bitcoin/tx/{txid}/raw",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"verbose": verbose}, tx_get_raw_params.TxGetRawParams),
            ),
            cast_to=NoneType,
        )

    def get_raw_hex(
        self,
        txid: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Get raw transaction hex

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
            f"/bitcoin/tx/{txid}/hex",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def get_status(
        self,
        txid: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Get transaction status

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
            f"/bitcoin/tx/{txid}/status",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def test_mempool(
        self,
        *,
        raw_txs: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Test mempool acceptance

        Args:
          raw_txs: Raw transaction hexes

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/bitcoin/tx/test",
            body=maybe_transform({"raw_txs": raw_txs}, tx_test_mempool_params.TxTestMempoolParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncTxResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTxResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/multichain.wallet.router-api-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTxResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTxResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/multichain.wallet.router-api-python#with_streaming_response
        """
        return AsyncTxResourceWithStreamingResponse(self)

    async def broadcast(
        self,
        *,
        hex: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Broadcast transaction

        Args:
          hex: Signed transaction hex

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/bitcoin/tx/send",
            body=await async_maybe_transform({"hex": hex}, tx_broadcast_params.TxBroadcastParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def decode(
        self,
        *,
        hex: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Decode raw transaction

        Args:
          hex: Raw transaction hex

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/bitcoin/tx/decode",
            body=await async_maybe_transform({"hex": hex}, tx_decode_params.TxDecodeParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def get_info(
        self,
        txid: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Get transaction info

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
            f"/bitcoin/tx/{txid}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def get_raw(
        self,
        txid: str,
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
        Get raw transaction (verbose)

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
            f"/bitcoin/tx/{txid}/raw",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"verbose": verbose}, tx_get_raw_params.TxGetRawParams),
            ),
            cast_to=NoneType,
        )

    async def get_raw_hex(
        self,
        txid: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Get raw transaction hex

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
            f"/bitcoin/tx/{txid}/hex",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def get_status(
        self,
        txid: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Get transaction status

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
            f"/bitcoin/tx/{txid}/status",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def test_mempool(
        self,
        *,
        raw_txs: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Test mempool acceptance

        Args:
          raw_txs: Raw transaction hexes

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/bitcoin/tx/test",
            body=await async_maybe_transform({"raw_txs": raw_txs}, tx_test_mempool_params.TxTestMempoolParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class TxResourceWithRawResponse:
    def __init__(self, tx: TxResource) -> None:
        self._tx = tx

        self.broadcast = to_raw_response_wrapper(
            tx.broadcast,
        )
        self.decode = to_raw_response_wrapper(
            tx.decode,
        )
        self.get_info = to_raw_response_wrapper(
            tx.get_info,
        )
        self.get_raw = to_raw_response_wrapper(
            tx.get_raw,
        )
        self.get_raw_hex = to_raw_response_wrapper(
            tx.get_raw_hex,
        )
        self.get_status = to_raw_response_wrapper(
            tx.get_status,
        )
        self.test_mempool = to_raw_response_wrapper(
            tx.test_mempool,
        )


class AsyncTxResourceWithRawResponse:
    def __init__(self, tx: AsyncTxResource) -> None:
        self._tx = tx

        self.broadcast = async_to_raw_response_wrapper(
            tx.broadcast,
        )
        self.decode = async_to_raw_response_wrapper(
            tx.decode,
        )
        self.get_info = async_to_raw_response_wrapper(
            tx.get_info,
        )
        self.get_raw = async_to_raw_response_wrapper(
            tx.get_raw,
        )
        self.get_raw_hex = async_to_raw_response_wrapper(
            tx.get_raw_hex,
        )
        self.get_status = async_to_raw_response_wrapper(
            tx.get_status,
        )
        self.test_mempool = async_to_raw_response_wrapper(
            tx.test_mempool,
        )


class TxResourceWithStreamingResponse:
    def __init__(self, tx: TxResource) -> None:
        self._tx = tx

        self.broadcast = to_streamed_response_wrapper(
            tx.broadcast,
        )
        self.decode = to_streamed_response_wrapper(
            tx.decode,
        )
        self.get_info = to_streamed_response_wrapper(
            tx.get_info,
        )
        self.get_raw = to_streamed_response_wrapper(
            tx.get_raw,
        )
        self.get_raw_hex = to_streamed_response_wrapper(
            tx.get_raw_hex,
        )
        self.get_status = to_streamed_response_wrapper(
            tx.get_status,
        )
        self.test_mempool = to_streamed_response_wrapper(
            tx.test_mempool,
        )


class AsyncTxResourceWithStreamingResponse:
    def __init__(self, tx: AsyncTxResource) -> None:
        self._tx = tx

        self.broadcast = async_to_streamed_response_wrapper(
            tx.broadcast,
        )
        self.decode = async_to_streamed_response_wrapper(
            tx.decode,
        )
        self.get_info = async_to_streamed_response_wrapper(
            tx.get_info,
        )
        self.get_raw = async_to_streamed_response_wrapper(
            tx.get_raw,
        )
        self.get_raw_hex = async_to_streamed_response_wrapper(
            tx.get_raw_hex,
        )
        self.get_status = async_to_streamed_response_wrapper(
            tx.get_status,
        )
        self.test_mempool = async_to_streamed_response_wrapper(
            tx.test_mempool,
        )
