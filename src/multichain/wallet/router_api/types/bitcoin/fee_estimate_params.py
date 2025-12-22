# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["FeeEstimateParams"]


class FeeEstimateParams(TypedDict, total=False):
    conf_target: Annotated[int, PropertyInfo(alias="confTarget")]
    """Target blocks for confirmation"""

    mode: Literal["ECONOMICAL", "CONSERVATIVE"]
    """Estimate mode"""
