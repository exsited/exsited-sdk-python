"""Typed views over the workflow bodies."""

from __future__ import annotations

from typing import Any

from exsited.dto import Dto
from exsited.resources.common.pagination_dto import Pagination

__all__ = [
    "SettingsWorkflow",
    "SettingsWorkflowList",
]


class SettingsWorkflow(Dto):
    """The settings workflow body, under ``workflow``."""

    MEASURED_FROM = (
        "GET /api/{api_version}/settings/workflows",
        "GET /api/{api_version}/settings/workflows/{workflow_id}",
    )

    ENVELOPE_KEY = "workflow"

    # Null in every record measured, so untyped.
    code: Any = None
    # Null in every record measured, so untyped.
    created_by: Any = None
    created_on: str | None = None
    # Null in every record measured, so untyped.
    description: Any = None
    display_name: str | None = None
    enable_stage: bool | None = None
    entity: str | None = None
    event: str | None = None
    href: str | None = None
    id: str | None = None
    is_pre_built: bool | None = None
    # Null in every record measured, so untyped.
    last_updated_by: Any = None
    last_updated_on: str | None = None
    name: str | None = None
    object: str | None = None
    status: str | None = None


class SettingsWorkflowList(Dto):
    """One page of ``SettingsWorkflow`` records, under ``data``."""

    MEASURED_FROM = ("GET /api/{api_version}/settings/workflows",)

    data: list[SettingsWorkflow] | None = None
    object: str | None = None
    pagination: Pagination | None = None
    url: str | None = None
