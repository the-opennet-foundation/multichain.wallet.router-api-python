# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Query, Headers, NoneType, NotGiven, not_given
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
from ...types.solana import tx_send_params, tx_simulate_params

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

    def retrieve(
        self,
        signature: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Get transaction by signature

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not signature:
            raise ValueError(f"Expected a non-empty value for `signature` but received {signature!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            f"/solana/tx/{signature}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def send(
        self,
        *,
        signed_transaction: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Send signed transaction

        Args:
          signed_transaction: Base64-encoded signed transaction

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/solana/tx/send",
            body=maybe_transform({"signed_transaction": signed_transaction}, tx_send_params.TxSendParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def simulate(
        self,
        *,
        transaction: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Simulate transaction

        Args:
          transaction: Base64-encoded transaction

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/solana/tx/simulate",
            body=maybe_transform({"transaction": transaction}, tx_simulate_params.TxSimulateParams),
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

    async def retrieve(
        self,
        signature: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Get transaction by signature

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not signature:
            raise ValueError(f"Expected a non-empty value for `signature` but received {signature!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            f"/solana/tx/{signature}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def send(
        self,
        *,
        signed_transaction: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Send signed transaction

        Args:
          signed_transaction: Base64-encoded signed transaction

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/solana/tx/send",
            body=await async_maybe_transform({"signed_transaction": signed_transaction}, tx_send_params.TxSendParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def simulate(
        self,
        *,
        transaction: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Simulate transaction

        Args:
          transaction: Base64-encoded transaction

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/solana/tx/simulate",
            body=await async_maybe_transform({"transaction": transaction}, tx_simulate_params.TxSimulateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class TxResourceWithRawResponse:
    def __init__(self, tx: TxResource) -> None:
        self._tx = tx

        self.retrieve = to_raw_response_wrapper(
            tx.retrieve,
        )
        self.send = to_raw_response_wrapper(
            tx.send,
        )
        self.simulate = to_raw_response_wrapper(
            tx.simulate,
        )


class AsyncTxResourceWithRawResponse:
    def __init__(self, tx: AsyncTxResource) -> None:
        self._tx = tx

        self.retrieve = async_to_raw_response_wrapper(
            tx.retrieve,
        )
        self.send = async_to_raw_response_wrapper(
            tx.send,
        )
        self.simulate = async_to_raw_response_wrapper(
            tx.simulate,
        )


class TxResourceWithStreamingResponse:
    def __init__(self, tx: TxResource) -> None:
        self._tx = tx

        self.retrieve = to_streamed_response_wrapper(
            tx.retrieve,
        )
        self.send = to_streamed_response_wrapper(
            tx.send,
        )
        self.simulate = to_streamed_response_wrapper(
            tx.simulate,
        )


class AsyncTxResourceWithStreamingResponse:
    def __init__(self, tx: AsyncTxResource) -> None:
        self._tx = tx

        self.retrieve = async_to_streamed_response_wrapper(
            tx.retrieve,
        )
        self.send = async_to_streamed_response_wrapper(
            tx.send,
        )
        self.simulate = async_to_streamed_response_wrapper(
            tx.simulate,
        )
