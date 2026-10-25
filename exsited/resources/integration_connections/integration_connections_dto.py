"""Typed views over the integration connection bodies."""

from __future__ import annotations

from typing import Any

from exsited.dto import Dto
from exsited.resources.common.pagination_dto import Pagination

__all__ = [
    "IntegrationConnections",
]


class IntegrationConnections(Dto):
    """The integration connections body."""

    MEASURED_FROM = ("GET /api/{api_version}/integration_connections",)

    data: list[Any] | None = None
    object: str | None = None
    pagination: Pagination | None = None
    url: str | None = None
