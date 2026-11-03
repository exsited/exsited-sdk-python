"""Typed views over the milestone bodies."""

from __future__ import annotations

from typing import Any

from exsited.dto import Dto
from exsited.resources.common.pagination_dto import Pagination

__all__ = [
    "Milestones",
]


class Milestones(Dto):
    """The milestones body."""


    data: list[Any] | None = None
    object: str | None = None
    pagination: Pagination | None = None
    url: str | None = None
