# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["SolanaListTokensParams"]


class SolanaListTokensParams(TypedDict, total=False):
    mint: str
    """Filter by specific token mint"""

    program_id: Annotated[str, PropertyInfo(alias="programId")]
    """Token program (default SPL Token)"""
