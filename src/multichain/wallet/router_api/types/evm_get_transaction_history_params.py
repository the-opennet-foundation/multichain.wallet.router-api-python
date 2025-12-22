# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["EvmGetTransactionHistoryParams"]


class EvmGetTransactionHistoryParams(TypedDict, total=False):
    chain_id: Required[
        Annotated[
            Literal[
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
            PropertyInfo(alias="chainId"),
        ]
    ]

    category: str

    from_block: Annotated[str, PropertyInfo(alias="fromBlock")]

    max_count: Annotated[int, PropertyInfo(alias="maxCount")]

    page_key: Annotated[str, PropertyInfo(alias="pageKey")]

    to_block: Annotated[str, PropertyInfo(alias="toBlock")]
