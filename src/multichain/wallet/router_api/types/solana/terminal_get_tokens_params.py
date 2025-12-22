# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["TerminalGetTokensParams"]


class TerminalGetTokensParams(TypedDict, total=False):
    interval: Literal["5m", "1h", "6h", "24h"]
    """Time interval for metrics"""
