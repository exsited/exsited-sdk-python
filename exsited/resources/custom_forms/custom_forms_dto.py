"""Typed views over the custom form bodies."""

from __future__ import annotations

from typing import Any

from exsited.dto import Dto
from exsited.resources.common.pagination_dto import Pagination

__all__ = [
    "SettingsCustomForm",
    "SettingsCustomFormList",
]


class SettingsCustomForm(Dto):
    """The settings custom form body, under ``custom_form``."""

    MEASURED_FROM = (
        "GET /api/{api_version}/settings/custom_forms",
        "GET /api/{api_version}/settings/custom_forms/{custom_form_id}",
        "POST /api/{api_version}/settings/custom_forms",
        "PATCH /api/{api_version}/settings/custom_forms/{custom_form_id}",
    )

    ENVELOPE_KEY = "custom_form"

    # Null in every record measured, so untyped.
    created_by: Any = None
    created_on: str | None = None
    description: str | None = None
    display_name: str | None = None
    for_default_template: bool | None = None
    href: str | None = None
    id: str | None = None
    is_system_template: bool | None = None
    # Null in every record measured, so untyped.
    last_updated_by: Any = None
    last_updated_on: str | None = None
    name: str | None = None
    object: str | None = None
    status: str | None = None


class SettingsCustomFormList(Dto):
    """One page of ``SettingsCustomForm`` records, under ``data``."""

    MEASURED_FROM = ("GET /api/{api_version}/settings/custom_forms",)

    data: list[SettingsCustomForm] | None = None
    object: str | None = None
    pagination: Pagination | None = None
    url: str | None = None
