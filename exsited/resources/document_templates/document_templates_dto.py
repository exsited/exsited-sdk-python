"""Typed views over the document template bodies."""

from __future__ import annotations

from typing import Any

from exsited.dto import Dto
from exsited.resources.common.pagination_dto import Pagination

__all__ = [
    "SettingsDocumentTemplate",
    "SettingsDocumentTemplateList",
]


class SettingsDocumentTemplate(Dto):
    """The settings document template body, under ``document_template``."""


    ENVELOPE_KEY = "document_template"

    created_by: Any = None
    created_on: str | None = None
    description: str | None = None
    display_name: str | None = None
    href: str | None = None
    id: str | None = None
    is_custom_template: bool | None = None
    is_default: bool | None = None
    is_edited: bool | None = None
    is_system_template: bool | None = None
    last_updated_by: Any = None
    last_updated_on: str | None = None
    name: str | None = None
    object: str | None = None
    status: str | None = None
    type: str | None = None
    version: int | None = None


class SettingsDocumentTemplateList(Dto):
    """One page of ``SettingsDocumentTemplate`` records, under ``data``."""


    data: list[SettingsDocumentTemplate] | None = None
    object: str | None = None
    pagination: Pagination | None = None
    url: str | None = None
