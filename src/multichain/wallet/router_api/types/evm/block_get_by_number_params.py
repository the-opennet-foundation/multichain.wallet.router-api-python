# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["BlockGetByNumberParams"]


class BlockGetByNumberParams(TypedDict, total=False):
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

    full_txs: Annotated[bool, PropertyInfo(alias="fullTxs")]
