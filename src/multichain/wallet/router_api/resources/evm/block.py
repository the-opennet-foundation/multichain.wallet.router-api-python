# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

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
from ...types.evm import block_get_by_number_params
from ..._base_client import make_request_options

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

    def get_by_number(
        self,
        block_number: str,
        *,
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
        full_txs: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Get block by number

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chain_id:
            raise ValueError(f"Expected a non-empty value for `chain_id` but received {chain_id!r}")
        if not block_number:
            raise ValueError(f"Expected a non-empty value for `block_number` but received {block_number!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            f"/evm/{chain_id}/block/{block_number}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"full_txs": full_txs}, block_get_by_number_params.BlockGetByNumberParams),
            ),
            cast_to=NoneType,
        )

    def get_current_number(
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
        Get current block number

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
            f"/evm/{chain_id}/block/number",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
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

    async def get_by_number(
        self,
        block_number: str,
        *,
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
        full_txs: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Get block by number

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chain_id:
            raise ValueError(f"Expected a non-empty value for `chain_id` but received {chain_id!r}")
        if not block_number:
            raise ValueError(f"Expected a non-empty value for `block_number` but received {block_number!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            f"/evm/{chain_id}/block/{block_number}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"full_txs": full_txs}, block_get_by_number_params.BlockGetByNumberParams
                ),
            ),
            cast_to=NoneType,
        )

    async def get_current_number(
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
        Get current block number

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
            f"/evm/{chain_id}/block/number",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class BlockResourceWithRawResponse:
    def __init__(self, block: BlockResource) -> None:
        self._block = block

        self.get_by_number = to_raw_response_wrapper(
            block.get_by_number,
        )
        self.get_current_number = to_raw_response_wrapper(
            block.get_current_number,
        )


class AsyncBlockResourceWithRawResponse:
    def __init__(self, block: AsyncBlockResource) -> None:
        self._block = block

        self.get_by_number = async_to_raw_response_wrapper(
            block.get_by_number,
        )
        self.get_current_number = async_to_raw_response_wrapper(
            block.get_current_number,
        )


class BlockResourceWithStreamingResponse:
    def __init__(self, block: BlockResource) -> None:
        self._block = block

        self.get_by_number = to_streamed_response_wrapper(
            block.get_by_number,
        )
        self.get_current_number = to_streamed_response_wrapper(
            block.get_current_number,
        )


class AsyncBlockResourceWithStreamingResponse:
    def __init__(self, block: AsyncBlockResource) -> None:
        self._block = block

        self.get_by_number = async_to_streamed_response_wrapper(
            block.get_by_number,
        )
        self.get_current_number = async_to_streamed_response_wrapper(
            block.get_current_number,
        )
