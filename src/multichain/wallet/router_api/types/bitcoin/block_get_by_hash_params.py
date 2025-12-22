# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["BlockGetByHashParams"]


class BlockGetByHashParams(TypedDict, total=False):
    verbosity: int
    """0=hex, 1=json, 2=json+txs"""
