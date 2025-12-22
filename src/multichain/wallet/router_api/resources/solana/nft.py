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
from ...types.solana import nft_get_editions_params

__all__ = ["NFTResource", "AsyncNFTResource"]


class NFTResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> NFTResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/the-opennet-foundation/multichain.wallet.router-api-python#accessing-raw-response-data-eg-headers
        """
        return NFTResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> NFTResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/the-opennet-foundation/multichain.wallet.router-api-python#with_streaming_response
        """
        return NFTResourceWithStreamingResponse(self)

    def get_editions(
        self,
        mint: str,
        *,
        limit: int | Omit = omit,
        page: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Get NFT edition info

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not mint:
            raise ValueError(f"Expected a non-empty value for `mint` but received {mint!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            f"/solana/nft/{mint}/editions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "page": page,
                    },
                    nft_get_editions_params.NFTGetEditionsParams,
                ),
            ),
            cast_to=NoneType,
        )


class AsyncNFTResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncNFTResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/the-opennet-foundation/multichain.wallet.router-api-python#accessing-raw-response-data-eg-headers
        """
        return AsyncNFTResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncNFTResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/the-opennet-foundation/multichain.wallet.router-api-python#with_streaming_response
        """
        return AsyncNFTResourceWithStreamingResponse(self)

    async def get_editions(
        self,
        mint: str,
        *,
        limit: int | Omit = omit,
        page: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Get NFT edition info

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not mint:
            raise ValueError(f"Expected a non-empty value for `mint` but received {mint!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            f"/solana/nft/{mint}/editions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "page": page,
                    },
                    nft_get_editions_params.NFTGetEditionsParams,
                ),
            ),
            cast_to=NoneType,
        )


class NFTResourceWithRawResponse:
    def __init__(self, nft: NFTResource) -> None:
        self._nft = nft

        self.get_editions = to_raw_response_wrapper(
            nft.get_editions,
        )


class AsyncNFTResourceWithRawResponse:
    def __init__(self, nft: AsyncNFTResource) -> None:
        self._nft = nft

        self.get_editions = async_to_raw_response_wrapper(
            nft.get_editions,
        )


class NFTResourceWithStreamingResponse:
    def __init__(self, nft: NFTResource) -> None:
        self._nft = nft

        self.get_editions = to_streamed_response_wrapper(
            nft.get_editions,
        )


class AsyncNFTResourceWithStreamingResponse:
    def __init__(self, nft: AsyncNFTResource) -> None:
        self._nft = nft

        self.get_editions = async_to_streamed_response_wrapper(
            nft.get_editions,
        )
