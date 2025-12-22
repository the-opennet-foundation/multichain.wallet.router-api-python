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
from ...types.bitcoin import mempool_get_raw_params

__all__ = ["MempoolResource", "AsyncMempoolResource"]


class MempoolResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MempoolResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/multichain.wallet.router-api-python#accessing-raw-response-data-eg-headers
        """
        return MempoolResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MempoolResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/multichain.wallet.router-api-python#with_streaming_response
        """
        return MempoolResourceWithStreamingResponse(self)

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
        """Returns size, bytes, usage, etc."""
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            "/bitcoin/mempool",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def get_projected_blocks(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Shows estimated next blocks from mempool"""
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            "/bitcoin/mempool/blocks",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def get_raw(
        self,
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
        Get raw mempool

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            "/bitcoin/mempool/raw",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"verbose": verbose}, mempool_get_raw_params.MempoolGetRawParams),
            ),
            cast_to=NoneType,
        )


class AsyncMempoolResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMempoolResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/multichain.wallet.router-api-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMempoolResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMempoolResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/multichain.wallet.router-api-python#with_streaming_response
        """
        return AsyncMempoolResourceWithStreamingResponse(self)

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
        """Returns size, bytes, usage, etc."""
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            "/bitcoin/mempool",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def get_projected_blocks(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Shows estimated next blocks from mempool"""
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            "/bitcoin/mempool/blocks",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def get_raw(
        self,
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
        Get raw mempool

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            "/bitcoin/mempool/raw",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"verbose": verbose}, mempool_get_raw_params.MempoolGetRawParams),
            ),
            cast_to=NoneType,
        )


class MempoolResourceWithRawResponse:
    def __init__(self, mempool: MempoolResource) -> None:
        self._mempool = mempool

        self.get_info = to_raw_response_wrapper(
            mempool.get_info,
        )
        self.get_projected_blocks = to_raw_response_wrapper(
            mempool.get_projected_blocks,
        )
        self.get_raw = to_raw_response_wrapper(
            mempool.get_raw,
        )


class AsyncMempoolResourceWithRawResponse:
    def __init__(self, mempool: AsyncMempoolResource) -> None:
        self._mempool = mempool

        self.get_info = async_to_raw_response_wrapper(
            mempool.get_info,
        )
        self.get_projected_blocks = async_to_raw_response_wrapper(
            mempool.get_projected_blocks,
        )
        self.get_raw = async_to_raw_response_wrapper(
            mempool.get_raw,
        )


class MempoolResourceWithStreamingResponse:
    def __init__(self, mempool: MempoolResource) -> None:
        self._mempool = mempool

        self.get_info = to_streamed_response_wrapper(
            mempool.get_info,
        )
        self.get_projected_blocks = to_streamed_response_wrapper(
            mempool.get_projected_blocks,
        )
        self.get_raw = to_streamed_response_wrapper(
            mempool.get_raw,
        )


class AsyncMempoolResourceWithStreamingResponse:
    def __init__(self, mempool: AsyncMempoolResource) -> None:
        self._mempool = mempool

        self.get_info = async_to_streamed_response_wrapper(
            mempool.get_info,
        )
        self.get_projected_blocks = async_to_streamed_response_wrapper(
            mempool.get_projected_blocks,
        )
        self.get_raw = async_to_streamed_response_wrapper(
            mempool.get_raw,
        )
