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
from .nft import (
    NFTResource,
    AsyncNFTResource,
    NFTResourceWithRawResponse,
    AsyncNFTResourceWithRawResponse,
    NFTResourceWithStreamingResponse,
    AsyncNFTResourceWithStreamingResponse,
)
from .fees import (
    FeesResource,
    AsyncFeesResource,
    FeesResourceWithRawResponse,
    AsyncFeesResourceWithRawResponse,
    FeesResourceWithStreamingResponse,
    AsyncFeesResourceWithStreamingResponse,
)
from .stake import (
    StakeResource,
    AsyncStakeResource,
    StakeResourceWithRawResponse,
    AsyncStakeResourceWithRawResponse,
    StakeResourceWithStreamingResponse,
    AsyncStakeResourceWithStreamingResponse,
)
from .token import (
    TokenResource,
    AsyncTokenResource,
    TokenResourceWithRawResponse,
    AsyncTokenResourceWithRawResponse,
    TokenResourceWithStreamingResponse,
    AsyncTokenResourceWithStreamingResponse,
)
from .assets import (
    AssetsResource,
    AsyncAssetsResource,
    AssetsResourceWithRawResponse,
    AsyncAssetsResourceWithRawResponse,
    AssetsResourceWithStreamingResponse,
    AsyncAssetsResourceWithStreamingResponse,
)
from ...types import solana_list_tokens_params, solana_list_signatures_params, solana_create_multiple_accounts_params
from .jupiter import (
    JupiterResource,
    AsyncJupiterResource,
    JupiterResourceWithRawResponse,
    AsyncJupiterResourceWithRawResponse,
    JupiterResourceWithStreamingResponse,
    AsyncJupiterResourceWithStreamingResponse,
)
from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from .terminal import (
    TerminalResource,
    AsyncTerminalResource,
    TerminalResourceWithRawResponse,
    AsyncTerminalResourceWithRawResponse,
    TerminalResourceWithStreamingResponse,
    AsyncTerminalResourceWithStreamingResponse,
)
from ..._compat import cached_property
from .inflation import (
    InflationResource,
    AsyncInflationResource,
    InflationResourceWithRawResponse,
    AsyncInflationResourceWithRawResponse,
    InflationResourceWithStreamingResponse,
    AsyncInflationResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options

__all__ = ["SolanaResource", "AsyncSolanaResource"]


class SolanaResource(SyncAPIResource):
    @cached_property
    def token(self) -> TokenResource:
        return TokenResource(self._client)

    @cached_property
    def nft(self) -> NFTResource:
        return NFTResource(self._client)

    @cached_property
    def tx(self) -> TxResource:
        return TxResource(self._client)

    @cached_property
    def fees(self) -> FeesResource:
        return FeesResource(self._client)

    @cached_property
    def stake(self) -> StakeResource:
        return StakeResource(self._client)

    @cached_property
    def inflation(self) -> InflationResource:
        return InflationResource(self._client)

    @cached_property
    def jupiter(self) -> JupiterResource:
        return JupiterResource(self._client)

    @cached_property
    def terminal(self) -> TerminalResource:
        return TerminalResource(self._client)

    @cached_property
    def assets(self) -> AssetsResource:
        return AssetsResource(self._client)

    @cached_property
    def with_raw_response(self) -> SolanaResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/multichain.wallet.router-api-python#accessing-raw-response-data-eg-headers
        """
        return SolanaResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SolanaResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/multichain.wallet.router-api-python#with_streaming_response
        """
        return SolanaResourceWithStreamingResponse(self)

    def create_multiple_accounts(
        self,
        *,
        addresses: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Get multiple accounts in one call

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/solana/accounts",
            body=maybe_transform(
                {"addresses": addresses}, solana_create_multiple_accounts_params.SolanaCreateMultipleAccountsParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def list_signatures(
        self,
        address: str,
        *,
        before: str | Omit = omit,
        limit: int | Omit = omit,
        until: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Get transaction signatures for address

        Args:
          before: Get signatures before this one

          until: Get signatures until this one

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not address:
            raise ValueError(f"Expected a non-empty value for `address` but received {address!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            f"/solana/signatures/{address}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "before": before,
                        "limit": limit,
                        "until": until,
                    },
                    solana_list_signatures_params.SolanaListSignaturesParams,
                ),
            ),
            cast_to=NoneType,
        )

    def list_tokens(
        self,
        owner: str,
        *,
        mint: str | Omit = omit,
        program_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Get all SPL token accounts for owner

        Args:
          mint: Filter by specific token mint

          program_id: Token program (default SPL Token)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            f"/solana/tokens/{owner}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "mint": mint,
                        "program_id": program_id,
                    },
                    solana_list_tokens_params.SolanaListTokensParams,
                ),
            ),
            cast_to=NoneType,
        )

    def list_validators(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Get vote accounts (validators)"""
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            "/solana/validators",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def retrieve_account_info(
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
        Get account info with parsed data

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
            f"/solana/account/{address}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def retrieve_balance(
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
        Get SOL balance (lamports and SOL)

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
            f"/solana/balance/{address}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def retrieve_block_by_slot(
        self,
        slot: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Get block by slot

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            f"/solana/block/{slot}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def retrieve_current_slot(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Get current slot number"""
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            "/solana/slot",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def retrieve_info(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Get network info (version, health, epoch)"""
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            "/solana/info",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def retrieve_latest_blockhash(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Get latest blockhash"""
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            "/solana/blockhash",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncSolanaResource(AsyncAPIResource):
    @cached_property
    def token(self) -> AsyncTokenResource:
        return AsyncTokenResource(self._client)

    @cached_property
    def nft(self) -> AsyncNFTResource:
        return AsyncNFTResource(self._client)

    @cached_property
    def tx(self) -> AsyncTxResource:
        return AsyncTxResource(self._client)

    @cached_property
    def fees(self) -> AsyncFeesResource:
        return AsyncFeesResource(self._client)

    @cached_property
    def stake(self) -> AsyncStakeResource:
        return AsyncStakeResource(self._client)

    @cached_property
    def inflation(self) -> AsyncInflationResource:
        return AsyncInflationResource(self._client)

    @cached_property
    def jupiter(self) -> AsyncJupiterResource:
        return AsyncJupiterResource(self._client)

    @cached_property
    def terminal(self) -> AsyncTerminalResource:
        return AsyncTerminalResource(self._client)

    @cached_property
    def assets(self) -> AsyncAssetsResource:
        return AsyncAssetsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncSolanaResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/multichain.wallet.router-api-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSolanaResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSolanaResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/multichain.wallet.router-api-python#with_streaming_response
        """
        return AsyncSolanaResourceWithStreamingResponse(self)

    async def create_multiple_accounts(
        self,
        *,
        addresses: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Get multiple accounts in one call

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/solana/accounts",
            body=await async_maybe_transform(
                {"addresses": addresses}, solana_create_multiple_accounts_params.SolanaCreateMultipleAccountsParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def list_signatures(
        self,
        address: str,
        *,
        before: str | Omit = omit,
        limit: int | Omit = omit,
        until: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Get transaction signatures for address

        Args:
          before: Get signatures before this one

          until: Get signatures until this one

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not address:
            raise ValueError(f"Expected a non-empty value for `address` but received {address!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            f"/solana/signatures/{address}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "before": before,
                        "limit": limit,
                        "until": until,
                    },
                    solana_list_signatures_params.SolanaListSignaturesParams,
                ),
            ),
            cast_to=NoneType,
        )

    async def list_tokens(
        self,
        owner: str,
        *,
        mint: str | Omit = omit,
        program_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Get all SPL token accounts for owner

        Args:
          mint: Filter by specific token mint

          program_id: Token program (default SPL Token)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            f"/solana/tokens/{owner}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "mint": mint,
                        "program_id": program_id,
                    },
                    solana_list_tokens_params.SolanaListTokensParams,
                ),
            ),
            cast_to=NoneType,
        )

    async def list_validators(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Get vote accounts (validators)"""
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            "/solana/validators",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def retrieve_account_info(
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
        Get account info with parsed data

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
            f"/solana/account/{address}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def retrieve_balance(
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
        Get SOL balance (lamports and SOL)

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
            f"/solana/balance/{address}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def retrieve_block_by_slot(
        self,
        slot: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Get block by slot

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            f"/solana/block/{slot}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def retrieve_current_slot(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Get current slot number"""
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            "/solana/slot",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def retrieve_info(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Get network info (version, health, epoch)"""
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            "/solana/info",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def retrieve_latest_blockhash(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Get latest blockhash"""
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            "/solana/blockhash",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class SolanaResourceWithRawResponse:
    def __init__(self, solana: SolanaResource) -> None:
        self._solana = solana

        self.create_multiple_accounts = to_raw_response_wrapper(
            solana.create_multiple_accounts,
        )
        self.list_signatures = to_raw_response_wrapper(
            solana.list_signatures,
        )
        self.list_tokens = to_raw_response_wrapper(
            solana.list_tokens,
        )
        self.list_validators = to_raw_response_wrapper(
            solana.list_validators,
        )
        self.retrieve_account_info = to_raw_response_wrapper(
            solana.retrieve_account_info,
        )
        self.retrieve_balance = to_raw_response_wrapper(
            solana.retrieve_balance,
        )
        self.retrieve_block_by_slot = to_raw_response_wrapper(
            solana.retrieve_block_by_slot,
        )
        self.retrieve_current_slot = to_raw_response_wrapper(
            solana.retrieve_current_slot,
        )
        self.retrieve_info = to_raw_response_wrapper(
            solana.retrieve_info,
        )
        self.retrieve_latest_blockhash = to_raw_response_wrapper(
            solana.retrieve_latest_blockhash,
        )

    @cached_property
    def token(self) -> TokenResourceWithRawResponse:
        return TokenResourceWithRawResponse(self._solana.token)

    @cached_property
    def nft(self) -> NFTResourceWithRawResponse:
        return NFTResourceWithRawResponse(self._solana.nft)

    @cached_property
    def tx(self) -> TxResourceWithRawResponse:
        return TxResourceWithRawResponse(self._solana.tx)

    @cached_property
    def fees(self) -> FeesResourceWithRawResponse:
        return FeesResourceWithRawResponse(self._solana.fees)

    @cached_property
    def stake(self) -> StakeResourceWithRawResponse:
        return StakeResourceWithRawResponse(self._solana.stake)

    @cached_property
    def inflation(self) -> InflationResourceWithRawResponse:
        return InflationResourceWithRawResponse(self._solana.inflation)

    @cached_property
    def jupiter(self) -> JupiterResourceWithRawResponse:
        return JupiterResourceWithRawResponse(self._solana.jupiter)

    @cached_property
    def terminal(self) -> TerminalResourceWithRawResponse:
        return TerminalResourceWithRawResponse(self._solana.terminal)

    @cached_property
    def assets(self) -> AssetsResourceWithRawResponse:
        return AssetsResourceWithRawResponse(self._solana.assets)


class AsyncSolanaResourceWithRawResponse:
    def __init__(self, solana: AsyncSolanaResource) -> None:
        self._solana = solana

        self.create_multiple_accounts = async_to_raw_response_wrapper(
            solana.create_multiple_accounts,
        )
        self.list_signatures = async_to_raw_response_wrapper(
            solana.list_signatures,
        )
        self.list_tokens = async_to_raw_response_wrapper(
            solana.list_tokens,
        )
        self.list_validators = async_to_raw_response_wrapper(
            solana.list_validators,
        )
        self.retrieve_account_info = async_to_raw_response_wrapper(
            solana.retrieve_account_info,
        )
        self.retrieve_balance = async_to_raw_response_wrapper(
            solana.retrieve_balance,
        )
        self.retrieve_block_by_slot = async_to_raw_response_wrapper(
            solana.retrieve_block_by_slot,
        )
        self.retrieve_current_slot = async_to_raw_response_wrapper(
            solana.retrieve_current_slot,
        )
        self.retrieve_info = async_to_raw_response_wrapper(
            solana.retrieve_info,
        )
        self.retrieve_latest_blockhash = async_to_raw_response_wrapper(
            solana.retrieve_latest_blockhash,
        )

    @cached_property
    def token(self) -> AsyncTokenResourceWithRawResponse:
        return AsyncTokenResourceWithRawResponse(self._solana.token)

    @cached_property
    def nft(self) -> AsyncNFTResourceWithRawResponse:
        return AsyncNFTResourceWithRawResponse(self._solana.nft)

    @cached_property
    def tx(self) -> AsyncTxResourceWithRawResponse:
        return AsyncTxResourceWithRawResponse(self._solana.tx)

    @cached_property
    def fees(self) -> AsyncFeesResourceWithRawResponse:
        return AsyncFeesResourceWithRawResponse(self._solana.fees)

    @cached_property
    def stake(self) -> AsyncStakeResourceWithRawResponse:
        return AsyncStakeResourceWithRawResponse(self._solana.stake)

    @cached_property
    def inflation(self) -> AsyncInflationResourceWithRawResponse:
        return AsyncInflationResourceWithRawResponse(self._solana.inflation)

    @cached_property
    def jupiter(self) -> AsyncJupiterResourceWithRawResponse:
        return AsyncJupiterResourceWithRawResponse(self._solana.jupiter)

    @cached_property
    def terminal(self) -> AsyncTerminalResourceWithRawResponse:
        return AsyncTerminalResourceWithRawResponse(self._solana.terminal)

    @cached_property
    def assets(self) -> AsyncAssetsResourceWithRawResponse:
        return AsyncAssetsResourceWithRawResponse(self._solana.assets)


class SolanaResourceWithStreamingResponse:
    def __init__(self, solana: SolanaResource) -> None:
        self._solana = solana

        self.create_multiple_accounts = to_streamed_response_wrapper(
            solana.create_multiple_accounts,
        )
        self.list_signatures = to_streamed_response_wrapper(
            solana.list_signatures,
        )
        self.list_tokens = to_streamed_response_wrapper(
            solana.list_tokens,
        )
        self.list_validators = to_streamed_response_wrapper(
            solana.list_validators,
        )
        self.retrieve_account_info = to_streamed_response_wrapper(
            solana.retrieve_account_info,
        )
        self.retrieve_balance = to_streamed_response_wrapper(
            solana.retrieve_balance,
        )
        self.retrieve_block_by_slot = to_streamed_response_wrapper(
            solana.retrieve_block_by_slot,
        )
        self.retrieve_current_slot = to_streamed_response_wrapper(
            solana.retrieve_current_slot,
        )
        self.retrieve_info = to_streamed_response_wrapper(
            solana.retrieve_info,
        )
        self.retrieve_latest_blockhash = to_streamed_response_wrapper(
            solana.retrieve_latest_blockhash,
        )

    @cached_property
    def token(self) -> TokenResourceWithStreamingResponse:
        return TokenResourceWithStreamingResponse(self._solana.token)

    @cached_property
    def nft(self) -> NFTResourceWithStreamingResponse:
        return NFTResourceWithStreamingResponse(self._solana.nft)

    @cached_property
    def tx(self) -> TxResourceWithStreamingResponse:
        return TxResourceWithStreamingResponse(self._solana.tx)

    @cached_property
    def fees(self) -> FeesResourceWithStreamingResponse:
        return FeesResourceWithStreamingResponse(self._solana.fees)

    @cached_property
    def stake(self) -> StakeResourceWithStreamingResponse:
        return StakeResourceWithStreamingResponse(self._solana.stake)

    @cached_property
    def inflation(self) -> InflationResourceWithStreamingResponse:
        return InflationResourceWithStreamingResponse(self._solana.inflation)

    @cached_property
    def jupiter(self) -> JupiterResourceWithStreamingResponse:
        return JupiterResourceWithStreamingResponse(self._solana.jupiter)

    @cached_property
    def terminal(self) -> TerminalResourceWithStreamingResponse:
        return TerminalResourceWithStreamingResponse(self._solana.terminal)

    @cached_property
    def assets(self) -> AssetsResourceWithStreamingResponse:
        return AssetsResourceWithStreamingResponse(self._solana.assets)


class AsyncSolanaResourceWithStreamingResponse:
    def __init__(self, solana: AsyncSolanaResource) -> None:
        self._solana = solana

        self.create_multiple_accounts = async_to_streamed_response_wrapper(
            solana.create_multiple_accounts,
        )
        self.list_signatures = async_to_streamed_response_wrapper(
            solana.list_signatures,
        )
        self.list_tokens = async_to_streamed_response_wrapper(
            solana.list_tokens,
        )
        self.list_validators = async_to_streamed_response_wrapper(
            solana.list_validators,
        )
        self.retrieve_account_info = async_to_streamed_response_wrapper(
            solana.retrieve_account_info,
        )
        self.retrieve_balance = async_to_streamed_response_wrapper(
            solana.retrieve_balance,
        )
        self.retrieve_block_by_slot = async_to_streamed_response_wrapper(
            solana.retrieve_block_by_slot,
        )
        self.retrieve_current_slot = async_to_streamed_response_wrapper(
            solana.retrieve_current_slot,
        )
        self.retrieve_info = async_to_streamed_response_wrapper(
            solana.retrieve_info,
        )
        self.retrieve_latest_blockhash = async_to_streamed_response_wrapper(
            solana.retrieve_latest_blockhash,
        )

    @cached_property
    def token(self) -> AsyncTokenResourceWithStreamingResponse:
        return AsyncTokenResourceWithStreamingResponse(self._solana.token)

    @cached_property
    def nft(self) -> AsyncNFTResourceWithStreamingResponse:
        return AsyncNFTResourceWithStreamingResponse(self._solana.nft)

    @cached_property
    def tx(self) -> AsyncTxResourceWithStreamingResponse:
        return AsyncTxResourceWithStreamingResponse(self._solana.tx)

    @cached_property
    def fees(self) -> AsyncFeesResourceWithStreamingResponse:
        return AsyncFeesResourceWithStreamingResponse(self._solana.fees)

    @cached_property
    def stake(self) -> AsyncStakeResourceWithStreamingResponse:
        return AsyncStakeResourceWithStreamingResponse(self._solana.stake)

    @cached_property
    def inflation(self) -> AsyncInflationResourceWithStreamingResponse:
        return AsyncInflationResourceWithStreamingResponse(self._solana.inflation)

    @cached_property
    def jupiter(self) -> AsyncJupiterResourceWithStreamingResponse:
        return AsyncJupiterResourceWithStreamingResponse(self._solana.jupiter)

    @cached_property
    def terminal(self) -> AsyncTerminalResourceWithStreamingResponse:
        return AsyncTerminalResourceWithStreamingResponse(self._solana.terminal)

    @cached_property
    def assets(self) -> AsyncAssetsResourceWithStreamingResponse:
        return AsyncAssetsResourceWithStreamingResponse(self._solana.assets)
