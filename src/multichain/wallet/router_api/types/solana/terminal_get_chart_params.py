# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["TerminalGetChartParams"]


class TerminalGetChartParams(TypedDict, total=False):
    time_from: Required[int]
    """Start timestamp (Unix)"""

    time_to: Required[int]
    """End timestamp (Unix)"""

    type: Required[Literal["1m", "5m", "15m", "1h", "4h", "1d"]]
    """Chart resolution"""
