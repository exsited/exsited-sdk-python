"""Typed views over the email template bodies."""

from __future__ import annotations

from typing import Any

from exsited.dto import Dto
from exsited.resources.common.pagination_dto import Pagination

__all__ = [
    "SettingsEmailTemplate",
    "SettingsEmailTemplateList",
]


class SettingsEmailTemplate(Dto):
    """The settings email template body, under ``email_template``."""

    MEASURED_FROM = (
        "GET /api/{api_version}/settings/email_templates",
        "GET /api/{api_version}/settings/email_templates/{email_template_id}",
        "POST /api/{api_version}/settings/email_templates",
        "PATCH /api/{api_version}/settings/email_templates/{email_template_id}",
    )

    ENVELOPE_KEY = "email_template"

    # Null in every record measured, so untyped.
    created_by: Any = None
    created_on: str | None = None
    description: str | None = None
    display_name: str | None = None
    # Null in every record measured, so untyped.
    entity: Any = None
    href: str | None = None
    id: str | None = None
    is_edited: bool | None = None
    is_system_template: bool | None = None
    # Null in every record measured, so untyped.
    last_updated_by: Any = None
    last_updated_on: str | None = None
    name: str | None = None
    object: str | None = None
    # Null in every record measured, so untyped.
    reply_address: Any = None
    rich_editor: bool | None = None
    # Null in every record measured, so untyped.
    sender_address: Any = None
    # Null in every record measured, so untyped.
    sender_name: Any = None
    status: str | None = None
    subject: str | None = None
    track_email_open: bool | None = None
    track_link_click: bool | None = None


class SettingsEmailTemplateList(Dto):
    """One page of ``SettingsEmailTemplate`` records, under ``data``."""

    MEASURED_FROM = ("GET /api/{api_version}/settings/email_templates",)

    data: list[SettingsEmailTemplate] | None = None
    object: str | None = None
    pagination: Pagination | None = None
    url: str | None = None
