# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from .tx import (
    TxResource,
    AsyncTxResource,
    TxResourceWithRawResponse,
    AsyncTxResourceWithRawResponse,
    TxResourceWithStreamingResponse,
    AsyncTxResourceWithStreamingResponse,
)
from .gas import (
    GasResource,
    AsyncGasResource,
    GasResourceWithRawResponse,
    AsyncGasResourceWithRawResponse,
    GasResourceWithStreamingResponse,
    AsyncGasResourceWithStreamingResponse,
)
from .block import (
    BlockResource,
    AsyncBlockResource,
    BlockResourceWithRawResponse,
    AsyncBlockResourceWithRawResponse,
    BlockResourceWithStreamingResponse,
    AsyncBlockResourceWithStreamingResponse,
)
from .token import (
    TokenResource,
    AsyncTokenResource,
    TokenResourceWithRawResponse,
    AsyncTokenResourceWithRawResponse,
    TokenResourceWithStreamingResponse,
    AsyncTokenResourceWithStreamingResponse,
)
from .chains import (
    ChainsResource,
    AsyncChainsResource,
    ChainsResourceWithRawResponse,
    AsyncChainsResourceWithRawResponse,
    ChainsResourceWithStreamingResponse,
    AsyncChainsResourceWithStreamingResponse,
)
from .prices import (
    PricesResource,
    AsyncPricesResource,
    PricesResourceWithRawResponse,
    AsyncPricesResourceWithRawResponse,
    PricesResourceWithStreamingResponse,
    AsyncPricesResourceWithStreamingResponse,
)
from ...types import (
    evm_get_nfts_params,
    evm_call_contract_params,
    evm_simulate_transaction_params,
    evm_get_transaction_history_params,
)
from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from .contract import (
    ContractResource,
    AsyncContractResource,
    ContractResourceWithRawResponse,
    AsyncContractResourceWithRawResponse,
    ContractResourceWithStreamingResponse,
    AsyncContractResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from .explorer.explorer import (
    ExplorerResource,
    AsyncExplorerResource,
    ExplorerResourceWithRawResponse,
    AsyncExplorerResourceWithRawResponse,
    ExplorerResourceWithStreamingResponse,
    AsyncExplorerResourceWithStreamingResponse,
)

__all__ = ["EvmResource", "AsyncEvmResource"]


class EvmResource(SyncAPIResource):
    @cached_property
    def chains(self) -> ChainsResource:
        return ChainsResource(self._client)

    @cached_property
    def token(self) -> TokenResource:
        return TokenResource(self._client)

    @cached_property
    def contract(self) -> ContractResource:
        return ContractResource(self._client)

    @cached_property
    def tx(self) -> TxResource:
        return TxResource(self._client)

    @cached_property
    def gas(self) -> GasResource:
        return GasResource(self._client)

    @cached_property
    def block(self) -> BlockResource:
        return BlockResource(self._client)

    @cached_property
    def prices(self) -> PricesResource:
        return PricesResource(self._client)

    @cached_property
    def explorer(self) -> ExplorerResource:
        return ExplorerResource(self._client)

    @cached_property
    def with_raw_response(self) -> EvmResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/the-opennet-foundation/multichain.wallet.router-api-python#accessing-raw-response-data-eg-headers
        """
        return EvmResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EvmResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/the-opennet-foundation/multichain.wallet.router-api-python#with_streaming_response
        """
        return EvmResourceWithStreamingResponse(self)

    def call_contract(
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
        block_tag: str | Omit = omit,
        transaction: evm_call_contract_params.Transaction | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Call contract method (read-only)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chain_id:
            raise ValueError(f"Expected a non-empty value for `chain_id` but received {chain_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            f"/evm/{chain_id}/call",
            body=maybe_transform(
                {
                    "block_tag": block_tag,
                    "transaction": transaction,
                },
                evm_call_contract_params.EvmCallContractParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def get_balance(
        self,
        address: str,
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
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Get native token balance (wei)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chain_id:
            raise ValueError(f"Expected a non-empty value for `chain_id` but received {chain_id!r}")
        if not address:
            raise ValueError(f"Expected a non-empty value for `address` but received {address!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            f"/evm/{chain_id}/balance/{address}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def get_contract_code(
        self,
        address: str,
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
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Get contract bytecode

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chain_id:
            raise ValueError(f"Expected a non-empty value for `chain_id` but received {chain_id!r}")
        if not address:
            raise ValueError(f"Expected a non-empty value for `address` but received {address!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            f"/evm/{chain_id}/code/{address}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def get_nft_metadata(
        self,
        token_id: str,
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
        contract_address: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Get NFT metadata

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chain_id:
            raise ValueError(f"Expected a non-empty value for `chain_id` but received {chain_id!r}")
        if not contract_address:
            raise ValueError(f"Expected a non-empty value for `contract_address` but received {contract_address!r}")
        if not token_id:
            raise ValueError(f"Expected a non-empty value for `token_id` but received {token_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            f"/evm/{chain_id}/nft/{contract_address}/{token_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def get_nfts(
        self,
        address: str,
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
        page_key: str | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Get all NFTs owned by address

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chain_id:
            raise ValueError(f"Expected a non-empty value for `chain_id` but received {chain_id!r}")
        if not address:
            raise ValueError(f"Expected a non-empty value for `address` but received {address!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            f"/evm/{chain_id}/nfts/{address}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page_key": page_key,
                        "page_size": page_size,
                    },
                    evm_get_nfts_params.EvmGetNFTsParams,
                ),
            ),
            cast_to=NoneType,
        )

    def get_nonce(
        self,
        address: str,
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
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Get transaction count (nonce)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chain_id:
            raise ValueError(f"Expected a non-empty value for `chain_id` but received {chain_id!r}")
        if not address:
            raise ValueError(f"Expected a non-empty value for `address` but received {address!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            f"/evm/{chain_id}/nonce/{address}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def get_tokens(
        self,
        address: str,
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
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Get all ERC-20 token balances

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chain_id:
            raise ValueError(f"Expected a non-empty value for `chain_id` but received {chain_id!r}")
        if not address:
            raise ValueError(f"Expected a non-empty value for `address` but received {address!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            f"/evm/{chain_id}/tokens/{address}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def get_transaction_history(
        self,
        address: str,
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
        category: str | Omit = omit,
        from_block: str | Omit = omit,
        max_count: int | Omit = omit,
        page_key: str | Omit = omit,
        to_block: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Get asset transfer history

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chain_id:
            raise ValueError(f"Expected a non-empty value for `chain_id` but received {chain_id!r}")
        if not address:
            raise ValueError(f"Expected a non-empty value for `address` but received {address!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            f"/evm/{chain_id}/transactions/{address}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "category": category,
                        "from_block": from_block,
                        "max_count": max_count,
                        "page_key": page_key,
                        "to_block": to_block,
                    },
                    evm_get_transaction_history_params.EvmGetTransactionHistoryParams,
                ),
            ),
            cast_to=NoneType,
        )

    def simulate_transaction(
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
        transaction: object | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Simulate transaction and preview asset changes

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chain_id:
            raise ValueError(f"Expected a non-empty value for `chain_id` but received {chain_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            f"/evm/{chain_id}/simulate",
            body=maybe_transform(
                {"transaction": transaction}, evm_simulate_transaction_params.EvmSimulateTransactionParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncEvmResource(AsyncAPIResource):
    @cached_property
    def chains(self) -> AsyncChainsResource:
        return AsyncChainsResource(self._client)

    @cached_property
    def token(self) -> AsyncTokenResource:
        return AsyncTokenResource(self._client)

    @cached_property
    def contract(self) -> AsyncContractResource:
        return AsyncContractResource(self._client)

    @cached_property
    def tx(self) -> AsyncTxResource:
        return AsyncTxResource(self._client)

    @cached_property
    def gas(self) -> AsyncGasResource:
        return AsyncGasResource(self._client)

    @cached_property
    def block(self) -> AsyncBlockResource:
        return AsyncBlockResource(self._client)

    @cached_property
    def prices(self) -> AsyncPricesResource:
        return AsyncPricesResource(self._client)

    @cached_property
    def explorer(self) -> AsyncExplorerResource:
        return AsyncExplorerResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncEvmResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/the-opennet-foundation/multichain.wallet.router-api-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEvmResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEvmResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/the-opennet-foundation/multichain.wallet.router-api-python#with_streaming_response
        """
        return AsyncEvmResourceWithStreamingResponse(self)

    async def call_contract(
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
        block_tag: str | Omit = omit,
        transaction: evm_call_contract_params.Transaction | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Call contract method (read-only)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chain_id:
            raise ValueError(f"Expected a non-empty value for `chain_id` but received {chain_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            f"/evm/{chain_id}/call",
            body=await async_maybe_transform(
                {
                    "block_tag": block_tag,
                    "transaction": transaction,
                },
                evm_call_contract_params.EvmCallContractParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def get_balance(
        self,
        address: str,
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
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Get native token balance (wei)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chain_id:
            raise ValueError(f"Expected a non-empty value for `chain_id` but received {chain_id!r}")
        if not address:
            raise ValueError(f"Expected a non-empty value for `address` but received {address!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            f"/evm/{chain_id}/balance/{address}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def get_contract_code(
        self,
        address: str,
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
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Get contract bytecode

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chain_id:
            raise ValueError(f"Expected a non-empty value for `chain_id` but received {chain_id!r}")
        if not address:
            raise ValueError(f"Expected a non-empty value for `address` but received {address!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            f"/evm/{chain_id}/code/{address}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def get_nft_metadata(
        self,
        token_id: str,
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
        contract_address: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Get NFT metadata

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chain_id:
            raise ValueError(f"Expected a non-empty value for `chain_id` but received {chain_id!r}")
        if not contract_address:
            raise ValueError(f"Expected a non-empty value for `contract_address` but received {contract_address!r}")
        if not token_id:
            raise ValueError(f"Expected a non-empty value for `token_id` but received {token_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            f"/evm/{chain_id}/nft/{contract_address}/{token_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def get_nfts(
        self,
        address: str,
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
        page_key: str | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Get all NFTs owned by address

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chain_id:
            raise ValueError(f"Expected a non-empty value for `chain_id` but received {chain_id!r}")
        if not address:
            raise ValueError(f"Expected a non-empty value for `address` but received {address!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            f"/evm/{chain_id}/nfts/{address}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "page_key": page_key,
                        "page_size": page_size,
                    },
                    evm_get_nfts_params.EvmGetNFTsParams,
                ),
            ),
            cast_to=NoneType,
        )

    async def get_nonce(
        self,
        address: str,
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
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Get transaction count (nonce)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chain_id:
            raise ValueError(f"Expected a non-empty value for `chain_id` but received {chain_id!r}")
        if not address:
            raise ValueError(f"Expected a non-empty value for `address` but received {address!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            f"/evm/{chain_id}/nonce/{address}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def get_tokens(
        self,
        address: str,
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
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Get all ERC-20 token balances

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chain_id:
            raise ValueError(f"Expected a non-empty value for `chain_id` but received {chain_id!r}")
        if not address:
            raise ValueError(f"Expected a non-empty value for `address` but received {address!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            f"/evm/{chain_id}/tokens/{address}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def get_transaction_history(
        self,
        address: str,
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
        category: str | Omit = omit,
        from_block: str | Omit = omit,
        max_count: int | Omit = omit,
        page_key: str | Omit = omit,
        to_block: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Get asset transfer history

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chain_id:
            raise ValueError(f"Expected a non-empty value for `chain_id` but received {chain_id!r}")
        if not address:
            raise ValueError(f"Expected a non-empty value for `address` but received {address!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            f"/evm/{chain_id}/transactions/{address}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "category": category,
                        "from_block": from_block,
                        "max_count": max_count,
                        "page_key": page_key,
                        "to_block": to_block,
                    },
                    evm_get_transaction_history_params.EvmGetTransactionHistoryParams,
                ),
            ),
            cast_to=NoneType,
        )

    async def simulate_transaction(
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
        transaction: object | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Simulate transaction and preview asset changes

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chain_id:
            raise ValueError(f"Expected a non-empty value for `chain_id` but received {chain_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            f"/evm/{chain_id}/simulate",
            body=await async_maybe_transform(
                {"transaction": transaction}, evm_simulate_transaction_params.EvmSimulateTransactionParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class EvmResourceWithRawResponse:
    def __init__(self, evm: EvmResource) -> None:
        self._evm = evm

        self.call_contract = to_raw_response_wrapper(
            evm.call_contract,
        )
        self.get_balance = to_raw_response_wrapper(
            evm.get_balance,
        )
        self.get_contract_code = to_raw_response_wrapper(
            evm.get_contract_code,
        )
        self.get_nft_metadata = to_raw_response_wrapper(
            evm.get_nft_metadata,
        )
        self.get_nfts = to_raw_response_wrapper(
            evm.get_nfts,
        )
        self.get_nonce = to_raw_response_wrapper(
            evm.get_nonce,
        )
        self.get_tokens = to_raw_response_wrapper(
            evm.get_tokens,
        )
        self.get_transaction_history = to_raw_response_wrapper(
            evm.get_transaction_history,
        )
        self.simulate_transaction = to_raw_response_wrapper(
            evm.simulate_transaction,
        )

    @cached_property
    def chains(self) -> ChainsResourceWithRawResponse:
        return ChainsResourceWithRawResponse(self._evm.chains)

    @cached_property
    def token(self) -> TokenResourceWithRawResponse:
        return TokenResourceWithRawResponse(self._evm.token)

    @cached_property
    def contract(self) -> ContractResourceWithRawResponse:
        return ContractResourceWithRawResponse(self._evm.contract)

    @cached_property
    def tx(self) -> TxResourceWithRawResponse:
        return TxResourceWithRawResponse(self._evm.tx)

    @cached_property
    def gas(self) -> GasResourceWithRawResponse:
        return GasResourceWithRawResponse(self._evm.gas)

    @cached_property
    def block(self) -> BlockResourceWithRawResponse:
        return BlockResourceWithRawResponse(self._evm.block)

    @cached_property
    def prices(self) -> PricesResourceWithRawResponse:
        return PricesResourceWithRawResponse(self._evm.prices)

    @cached_property
    def explorer(self) -> ExplorerResourceWithRawResponse:
        return ExplorerResourceWithRawResponse(self._evm.explorer)


class AsyncEvmResourceWithRawResponse:
    def __init__(self, evm: AsyncEvmResource) -> None:
        self._evm = evm

        self.call_contract = async_to_raw_response_wrapper(
            evm.call_contract,
        )
        self.get_balance = async_to_raw_response_wrapper(
            evm.get_balance,
        )
        self.get_contract_code = async_to_raw_response_wrapper(
            evm.get_contract_code,
        )
        self.get_nft_metadata = async_to_raw_response_wrapper(
            evm.get_nft_metadata,
        )
        self.get_nfts = async_to_raw_response_wrapper(
            evm.get_nfts,
        )
        self.get_nonce = async_to_raw_response_wrapper(
            evm.get_nonce,
        )
        self.get_tokens = async_to_raw_response_wrapper(
            evm.get_tokens,
        )
        self.get_transaction_history = async_to_raw_response_wrapper(
            evm.get_transaction_history,
        )
        self.simulate_transaction = async_to_raw_response_wrapper(
            evm.simulate_transaction,
        )

    @cached_property
    def chains(self) -> AsyncChainsResourceWithRawResponse:
        return AsyncChainsResourceWithRawResponse(self._evm.chains)

    @cached_property
    def token(self) -> AsyncTokenResourceWithRawResponse:
        return AsyncTokenResourceWithRawResponse(self._evm.token)

    @cached_property
    def contract(self) -> AsyncContractResourceWithRawResponse:
        return AsyncContractResourceWithRawResponse(self._evm.contract)

    @cached_property
    def tx(self) -> AsyncTxResourceWithRawResponse:
        return AsyncTxResourceWithRawResponse(self._evm.tx)

    @cached_property
    def gas(self) -> AsyncGasResourceWithRawResponse:
        return AsyncGasResourceWithRawResponse(self._evm.gas)

    @cached_property
    def block(self) -> AsyncBlockResourceWithRawResponse:
        return AsyncBlockResourceWithRawResponse(self._evm.block)

    @cached_property
    def prices(self) -> AsyncPricesResourceWithRawResponse:
        return AsyncPricesResourceWithRawResponse(self._evm.prices)

    @cached_property
    def explorer(self) -> AsyncExplorerResourceWithRawResponse:
        return AsyncExplorerResourceWithRawResponse(self._evm.explorer)


class EvmResourceWithStreamingResponse:
    def __init__(self, evm: EvmResource) -> None:
        self._evm = evm

        self.call_contract = to_streamed_response_wrapper(
            evm.call_contract,
        )
        self.get_balance = to_streamed_response_wrapper(
            evm.get_balance,
        )
        self.get_contract_code = to_streamed_response_wrapper(
            evm.get_contract_code,
        )
        self.get_nft_metadata = to_streamed_response_wrapper(
            evm.get_nft_metadata,
        )
        self.get_nfts = to_streamed_response_wrapper(
            evm.get_nfts,
        )
        self.get_nonce = to_streamed_response_wrapper(
            evm.get_nonce,
        )
        self.get_tokens = to_streamed_response_wrapper(
            evm.get_tokens,
        )
        self.get_transaction_history = to_streamed_response_wrapper(
            evm.get_transaction_history,
        )
        self.simulate_transaction = to_streamed_response_wrapper(
            evm.simulate_transaction,
        )

    @cached_property
    def chains(self) -> ChainsResourceWithStreamingResponse:
        return ChainsResourceWithStreamingResponse(self._evm.chains)

    @cached_property
    def token(self) -> TokenResourceWithStreamingResponse:
        return TokenResourceWithStreamingResponse(self._evm.token)

    @cached_property
    def contract(self) -> ContractResourceWithStreamingResponse:
        return ContractResourceWithStreamingResponse(self._evm.contract)

    @cached_property
    def tx(self) -> TxResourceWithStreamingResponse:
        return TxResourceWithStreamingResponse(self._evm.tx)

    @cached_property
    def gas(self) -> GasResourceWithStreamingResponse:
        return GasResourceWithStreamingResponse(self._evm.gas)

    @cached_property
    def block(self) -> BlockResourceWithStreamingResponse:
        return BlockResourceWithStreamingResponse(self._evm.block)

    @cached_property
    def prices(self) -> PricesResourceWithStreamingResponse:
        return PricesResourceWithStreamingResponse(self._evm.prices)

    @cached_property
    def explorer(self) -> ExplorerResourceWithStreamingResponse:
        return ExplorerResourceWithStreamingResponse(self._evm.explorer)


class AsyncEvmResourceWithStreamingResponse:
    def __init__(self, evm: AsyncEvmResource) -> None:
        self._evm = evm

        self.call_contract = async_to_streamed_response_wrapper(
            evm.call_contract,
        )
        self.get_balance = async_to_streamed_response_wrapper(
            evm.get_balance,
        )
        self.get_contract_code = async_to_streamed_response_wrapper(
            evm.get_contract_code,
        )
        self.get_nft_metadata = async_to_streamed_response_wrapper(
            evm.get_nft_metadata,
        )
        self.get_nfts = async_to_streamed_response_wrapper(
            evm.get_nfts,
        )
        self.get_nonce = async_to_streamed_response_wrapper(
            evm.get_nonce,
        )
        self.get_tokens = async_to_streamed_response_wrapper(
            evm.get_tokens,
        )
        self.get_transaction_history = async_to_streamed_response_wrapper(
            evm.get_transaction_history,
        )
        self.simulate_transaction = async_to_streamed_response_wrapper(
            evm.simulate_transaction,
        )

    @cached_property
    def chains(self) -> AsyncChainsResourceWithStreamingResponse:
        return AsyncChainsResourceWithStreamingResponse(self._evm.chains)

    @cached_property
    def token(self) -> AsyncTokenResourceWithStreamingResponse:
        return AsyncTokenResourceWithStreamingResponse(self._evm.token)

    @cached_property
    def contract(self) -> AsyncContractResourceWithStreamingResponse:
        return AsyncContractResourceWithStreamingResponse(self._evm.contract)

    @cached_property
    def tx(self) -> AsyncTxResourceWithStreamingResponse:
        return AsyncTxResourceWithStreamingResponse(self._evm.tx)

    @cached_property
    def gas(self) -> AsyncGasResourceWithStreamingResponse:
        return AsyncGasResourceWithStreamingResponse(self._evm.gas)

    @cached_property
    def block(self) -> AsyncBlockResourceWithStreamingResponse:
        return AsyncBlockResourceWithStreamingResponse(self._evm.block)

    @cached_property
    def prices(self) -> AsyncPricesResourceWithStreamingResponse:
        return AsyncPricesResourceWithStreamingResponse(self._evm.prices)

    @cached_property
    def explorer(self) -> AsyncExplorerResourceWithStreamingResponse:
        return AsyncExplorerResourceWithStreamingResponse(self._evm.explorer)
