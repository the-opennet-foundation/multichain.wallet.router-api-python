# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["BitcoinGetHashrateParams"]


class BitcoinGetHashrateParams(TypedDict, total=False):
    height: int
    """Block height (-1 for latest)"""

    nblocks: int
    """Number of blocks to average"""
