# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["SolanaListSignaturesParams"]


class SolanaListSignaturesParams(TypedDict, total=False):
    before: str
    """Get signatures before this one"""

    limit: int

    until: str
    """Get signatures until this one"""
