# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["JupiterGetQuoteParams"]


class JupiterGetQuoteParams(TypedDict, total=False):
    amount: Required[int]
    """Input amount in base units"""

    input_mint: Required[Annotated[str, PropertyInfo(alias="inputMint")]]
    """Input token mint"""

    output_mint: Required[Annotated[str, PropertyInfo(alias="outputMint")]]
    """Output token mint"""

    slippage_bps: Annotated[int, PropertyInfo(alias="slippageBps")]
    """Slippage in basis points (100 = 1%)"""
