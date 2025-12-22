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
from ..._base_client import make_request_options
from ...types.solana import (
    terminal_get_chart_params,
    terminal_get_pools_params,
    terminal_get_tokens_params,
    terminal_get_recent_trades_params,
)

__all__ = ["TerminalResource", "AsyncTerminalResource"]


class TerminalResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TerminalResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/multichain.wallet.router-api-python#accessing-raw-response-data-eg-headers
        """
        return TerminalResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TerminalResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/multichain.wallet.router-api-python#with_streaming_response
        """
        return TerminalResourceWithStreamingResponse(self)

    def get_chart(
        self,
        asset_id: str,
        *,
        time_from: int,
        time_to: int,
        type: Literal["1m", "5m", "15m", "1h", "4h", "1d"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Get OHLCV price chart

        Args:
          time_from: Start timestamp (Unix)

          time_to: End timestamp (Unix)

          type: Chart resolution

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not asset_id:
            raise ValueError(f"Expected a non-empty value for `asset_id` but received {asset_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            f"/solana/terminal/chart/{asset_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "time_from": time_from,
                        "time_to": time_to,
                        "type": type,
                    },
                    terminal_get_chart_params.TerminalGetChartParams,
                ),
            ),
            cast_to=NoneType,
        )

    def get_description(
        self,
        asset_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Get token description/info

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not asset_id:
            raise ValueError(f"Expected a non-empty value for `asset_id` but received {asset_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            f"/solana/terminal/description/{asset_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def get_holders(
        self,
        asset_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Get top token holders

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not asset_id:
            raise ValueError(f"Expected a non-empty value for `asset_id` but received {asset_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            f"/solana/terminal/holders/{asset_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def get_pools(
        self,
        *,
        asset_ids: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Get liquidity pool info

        Args:
          asset_ids: Comma-separated mint addresses

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            "/solana/terminal/pools",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"asset_ids": asset_ids}, terminal_get_pools_params.TerminalGetPoolsParams),
            ),
            cast_to=NoneType,
        )

    def get_recent_trades(
        self,
        asset_id: str,
        *,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Get recent token trades

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not asset_id:
            raise ValueError(f"Expected a non-empty value for `asset_id` but received {asset_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            f"/solana/terminal/txs/{asset_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                    },
                    terminal_get_recent_trades_params.TerminalGetRecentTradesParams,
                ),
            ),
            cast_to=NoneType,
        )

    def get_tokens(
        self,
        *,
        interval: Literal["5m", "1h", "6h", "24h"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Get trending/new/top volume tokens

        Args:
          interval: Time interval for metrics

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            "/solana/terminal/tokens",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"interval": interval}, terminal_get_tokens_params.TerminalGetTokensParams),
            ),
            cast_to=NoneType,
        )


class AsyncTerminalResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTerminalResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/multichain.wallet.router-api-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTerminalResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTerminalResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/multichain.wallet.router-api-python#with_streaming_response
        """
        return AsyncTerminalResourceWithStreamingResponse(self)

    async def get_chart(
        self,
        asset_id: str,
        *,
        time_from: int,
        time_to: int,
        type: Literal["1m", "5m", "15m", "1h", "4h", "1d"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Get OHLCV price chart

        Args:
          time_from: Start timestamp (Unix)

          time_to: End timestamp (Unix)

          type: Chart resolution

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not asset_id:
            raise ValueError(f"Expected a non-empty value for `asset_id` but received {asset_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            f"/solana/terminal/chart/{asset_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "time_from": time_from,
                        "time_to": time_to,
                        "type": type,
                    },
                    terminal_get_chart_params.TerminalGetChartParams,
                ),
            ),
            cast_to=NoneType,
        )

    async def get_description(
        self,
        asset_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Get token description/info

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not asset_id:
            raise ValueError(f"Expected a non-empty value for `asset_id` but received {asset_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            f"/solana/terminal/description/{asset_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def get_holders(
        self,
        asset_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Get top token holders

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not asset_id:
            raise ValueError(f"Expected a non-empty value for `asset_id` but received {asset_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            f"/solana/terminal/holders/{asset_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def get_pools(
        self,
        *,
        asset_ids: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Get liquidity pool info

        Args:
          asset_ids: Comma-separated mint addresses

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            "/solana/terminal/pools",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"asset_ids": asset_ids}, terminal_get_pools_params.TerminalGetPoolsParams
                ),
            ),
            cast_to=NoneType,
        )

    async def get_recent_trades(
        self,
        asset_id: str,
        *,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Get recent token trades

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not asset_id:
            raise ValueError(f"Expected a non-empty value for `asset_id` but received {asset_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            f"/solana/terminal/txs/{asset_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                    },
                    terminal_get_recent_trades_params.TerminalGetRecentTradesParams,
                ),
            ),
            cast_to=NoneType,
        )

    async def get_tokens(
        self,
        *,
        interval: Literal["5m", "1h", "6h", "24h"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Get trending/new/top volume tokens

        Args:
          interval: Time interval for metrics

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            "/solana/terminal/tokens",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"interval": interval}, terminal_get_tokens_params.TerminalGetTokensParams
                ),
            ),
            cast_to=NoneType,
        )


class TerminalResourceWithRawResponse:
    def __init__(self, terminal: TerminalResource) -> None:
        self._terminal = terminal

        self.get_chart = to_raw_response_wrapper(
            terminal.get_chart,
        )
        self.get_description = to_raw_response_wrapper(
            terminal.get_description,
        )
        self.get_holders = to_raw_response_wrapper(
            terminal.get_holders,
        )
        self.get_pools = to_raw_response_wrapper(
            terminal.get_pools,
        )
        self.get_recent_trades = to_raw_response_wrapper(
            terminal.get_recent_trades,
        )
        self.get_tokens = to_raw_response_wrapper(
            terminal.get_tokens,
        )


class AsyncTerminalResourceWithRawResponse:
    def __init__(self, terminal: AsyncTerminalResource) -> None:
        self._terminal = terminal

        self.get_chart = async_to_raw_response_wrapper(
            terminal.get_chart,
        )
        self.get_description = async_to_raw_response_wrapper(
            terminal.get_description,
        )
        self.get_holders = async_to_raw_response_wrapper(
            terminal.get_holders,
        )
        self.get_pools = async_to_raw_response_wrapper(
            terminal.get_pools,
        )
        self.get_recent_trades = async_to_raw_response_wrapper(
            terminal.get_recent_trades,
        )
        self.get_tokens = async_to_raw_response_wrapper(
            terminal.get_tokens,
        )


class TerminalResourceWithStreamingResponse:
    def __init__(self, terminal: TerminalResource) -> None:
        self._terminal = terminal

        self.get_chart = to_streamed_response_wrapper(
            terminal.get_chart,
        )
        self.get_description = to_streamed_response_wrapper(
            terminal.get_description,
        )
        self.get_holders = to_streamed_response_wrapper(
            terminal.get_holders,
        )
        self.get_pools = to_streamed_response_wrapper(
            terminal.get_pools,
        )
        self.get_recent_trades = to_streamed_response_wrapper(
            terminal.get_recent_trades,
        )
        self.get_tokens = to_streamed_response_wrapper(
            terminal.get_tokens,
        )


class AsyncTerminalResourceWithStreamingResponse:
    def __init__(self, terminal: AsyncTerminalResource) -> None:
        self._terminal = terminal

        self.get_chart = async_to_streamed_response_wrapper(
            terminal.get_chart,
        )
        self.get_description = async_to_streamed_response_wrapper(
            terminal.get_description,
        )
        self.get_holders = async_to_streamed_response_wrapper(
            terminal.get_holders,
        )
        self.get_pools = async_to_streamed_response_wrapper(
            terminal.get_pools,
        )
        self.get_recent_trades = async_to_streamed_response_wrapper(
            terminal.get_recent_trades,
        )
        self.get_tokens = async_to_streamed_response_wrapper(
            terminal.get_tokens,
        )
