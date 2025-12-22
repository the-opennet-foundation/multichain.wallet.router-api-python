# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from multichain.wallet.router_api import MultichainWalletRouterAPI, AsyncMultichainWalletRouterAPI

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTerminal:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_chart(self, client: MultichainWalletRouterAPI) -> None:
        terminal = client.solana.terminal.get_chart(
            asset_id="assetId",
            time_from=0,
            time_to=0,
            type="1m",
        )
        assert terminal is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_chart(self, client: MultichainWalletRouterAPI) -> None:
        response = client.solana.terminal.with_raw_response.get_chart(
            asset_id="assetId",
            time_from=0,
            time_to=0,
            type="1m",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        terminal = response.parse()
        assert terminal is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_chart(self, client: MultichainWalletRouterAPI) -> None:
        with client.solana.terminal.with_streaming_response.get_chart(
            asset_id="assetId",
            time_from=0,
            time_to=0,
            type="1m",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            terminal = response.parse()
            assert terminal is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get_chart(self, client: MultichainWalletRouterAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `asset_id` but received ''"):
            client.solana.terminal.with_raw_response.get_chart(
                asset_id="",
                time_from=0,
                time_to=0,
                type="1m",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_description(self, client: MultichainWalletRouterAPI) -> None:
        terminal = client.solana.terminal.get_description(
            "assetId",
        )
        assert terminal is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_description(self, client: MultichainWalletRouterAPI) -> None:
        response = client.solana.terminal.with_raw_response.get_description(
            "assetId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        terminal = response.parse()
        assert terminal is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_description(self, client: MultichainWalletRouterAPI) -> None:
        with client.solana.terminal.with_streaming_response.get_description(
            "assetId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            terminal = response.parse()
            assert terminal is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get_description(self, client: MultichainWalletRouterAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `asset_id` but received ''"):
            client.solana.terminal.with_raw_response.get_description(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_holders(self, client: MultichainWalletRouterAPI) -> None:
        terminal = client.solana.terminal.get_holders(
            "assetId",
        )
        assert terminal is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_holders(self, client: MultichainWalletRouterAPI) -> None:
        response = client.solana.terminal.with_raw_response.get_holders(
            "assetId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        terminal = response.parse()
        assert terminal is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_holders(self, client: MultichainWalletRouterAPI) -> None:
        with client.solana.terminal.with_streaming_response.get_holders(
            "assetId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            terminal = response.parse()
            assert terminal is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get_holders(self, client: MultichainWalletRouterAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `asset_id` but received ''"):
            client.solana.terminal.with_raw_response.get_holders(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_pools(self, client: MultichainWalletRouterAPI) -> None:
        terminal = client.solana.terminal.get_pools(
            asset_ids="assetIds",
        )
        assert terminal is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_pools(self, client: MultichainWalletRouterAPI) -> None:
        response = client.solana.terminal.with_raw_response.get_pools(
            asset_ids="assetIds",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        terminal = response.parse()
        assert terminal is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_pools(self, client: MultichainWalletRouterAPI) -> None:
        with client.solana.terminal.with_streaming_response.get_pools(
            asset_ids="assetIds",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            terminal = response.parse()
            assert terminal is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_recent_trades(self, client: MultichainWalletRouterAPI) -> None:
        terminal = client.solana.terminal.get_recent_trades(
            asset_id="assetId",
        )
        assert terminal is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_recent_trades_with_all_params(self, client: MultichainWalletRouterAPI) -> None:
        terminal = client.solana.terminal.get_recent_trades(
            asset_id="assetId",
            limit=0,
            offset=0,
        )
        assert terminal is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_recent_trades(self, client: MultichainWalletRouterAPI) -> None:
        response = client.solana.terminal.with_raw_response.get_recent_trades(
            asset_id="assetId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        terminal = response.parse()
        assert terminal is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_recent_trades(self, client: MultichainWalletRouterAPI) -> None:
        with client.solana.terminal.with_streaming_response.get_recent_trades(
            asset_id="assetId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            terminal = response.parse()
            assert terminal is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get_recent_trades(self, client: MultichainWalletRouterAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `asset_id` but received ''"):
            client.solana.terminal.with_raw_response.get_recent_trades(
                asset_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_tokens(self, client: MultichainWalletRouterAPI) -> None:
        terminal = client.solana.terminal.get_tokens()
        assert terminal is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_tokens_with_all_params(self, client: MultichainWalletRouterAPI) -> None:
        terminal = client.solana.terminal.get_tokens(
            interval="5m",
        )
        assert terminal is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_tokens(self, client: MultichainWalletRouterAPI) -> None:
        response = client.solana.terminal.with_raw_response.get_tokens()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        terminal = response.parse()
        assert terminal is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_tokens(self, client: MultichainWalletRouterAPI) -> None:
        with client.solana.terminal.with_streaming_response.get_tokens() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            terminal = response.parse()
            assert terminal is None

        assert cast(Any, response.is_closed) is True


class TestAsyncTerminal:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_chart(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        terminal = await async_client.solana.terminal.get_chart(
            asset_id="assetId",
            time_from=0,
            time_to=0,
            type="1m",
        )
        assert terminal is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_chart(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        response = await async_client.solana.terminal.with_raw_response.get_chart(
            asset_id="assetId",
            time_from=0,
            time_to=0,
            type="1m",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        terminal = await response.parse()
        assert terminal is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_chart(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        async with async_client.solana.terminal.with_streaming_response.get_chart(
            asset_id="assetId",
            time_from=0,
            time_to=0,
            type="1m",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            terminal = await response.parse()
            assert terminal is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get_chart(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `asset_id` but received ''"):
            await async_client.solana.terminal.with_raw_response.get_chart(
                asset_id="",
                time_from=0,
                time_to=0,
                type="1m",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_description(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        terminal = await async_client.solana.terminal.get_description(
            "assetId",
        )
        assert terminal is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_description(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        response = await async_client.solana.terminal.with_raw_response.get_description(
            "assetId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        terminal = await response.parse()
        assert terminal is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_description(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        async with async_client.solana.terminal.with_streaming_response.get_description(
            "assetId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            terminal = await response.parse()
            assert terminal is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get_description(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `asset_id` but received ''"):
            await async_client.solana.terminal.with_raw_response.get_description(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_holders(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        terminal = await async_client.solana.terminal.get_holders(
            "assetId",
        )
        assert terminal is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_holders(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        response = await async_client.solana.terminal.with_raw_response.get_holders(
            "assetId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        terminal = await response.parse()
        assert terminal is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_holders(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        async with async_client.solana.terminal.with_streaming_response.get_holders(
            "assetId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            terminal = await response.parse()
            assert terminal is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get_holders(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `asset_id` but received ''"):
            await async_client.solana.terminal.with_raw_response.get_holders(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_pools(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        terminal = await async_client.solana.terminal.get_pools(
            asset_ids="assetIds",
        )
        assert terminal is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_pools(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        response = await async_client.solana.terminal.with_raw_response.get_pools(
            asset_ids="assetIds",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        terminal = await response.parse()
        assert terminal is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_pools(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        async with async_client.solana.terminal.with_streaming_response.get_pools(
            asset_ids="assetIds",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            terminal = await response.parse()
            assert terminal is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_recent_trades(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        terminal = await async_client.solana.terminal.get_recent_trades(
            asset_id="assetId",
        )
        assert terminal is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_recent_trades_with_all_params(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        terminal = await async_client.solana.terminal.get_recent_trades(
            asset_id="assetId",
            limit=0,
            offset=0,
        )
        assert terminal is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_recent_trades(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        response = await async_client.solana.terminal.with_raw_response.get_recent_trades(
            asset_id="assetId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        terminal = await response.parse()
        assert terminal is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_recent_trades(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        async with async_client.solana.terminal.with_streaming_response.get_recent_trades(
            asset_id="assetId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            terminal = await response.parse()
            assert terminal is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get_recent_trades(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `asset_id` but received ''"):
            await async_client.solana.terminal.with_raw_response.get_recent_trades(
                asset_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_tokens(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        terminal = await async_client.solana.terminal.get_tokens()
        assert terminal is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_tokens_with_all_params(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        terminal = await async_client.solana.terminal.get_tokens(
            interval="5m",
        )
        assert terminal is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_tokens(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        response = await async_client.solana.terminal.with_raw_response.get_tokens()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        terminal = await response.parse()
        assert terminal is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_tokens(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        async with async_client.solana.terminal.with_streaming_response.get_tokens() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            terminal = await response.parse()
            assert terminal is None

        assert cast(Any, response.is_closed) is True
