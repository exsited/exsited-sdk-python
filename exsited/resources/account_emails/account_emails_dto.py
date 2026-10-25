"""Typed views over the account email bodies."""

from __future__ import annotations

from typing import Any

from exsited.dto import Dto
from exsited.resources.common.pagination_dto import Pagination

__all__ = [
    "AccountCommunicationsEmail",
    "AccountCommunicationsEmailList",
    "AccountCommunicationsEmailAttachment",
]


class AccountCommunicationsEmail(Dto):
    """The account communications email body, under ``email``."""

    MEASURED_FROM = (
        "GET /api/{api_version}/accounts/{account_id}/communications/emails",
        "GET /api/{api_version}/accounts/{account_id}/communications/emails/{email_uuid}",
        "GET /api/{api_version}/accounts/{account_id}/communications/emails/{email_id}",
    )

    ENVELOPE_KEY = "email"

    # Null in every record measured, so untyped.
    additional_template: Any = None
    attachments: list[AccountCommunicationsEmailAttachment] | None = None
    bcc: list[Any] | None = None
    # Null in every record measured, so untyped.
    body: Any = None
    cc: list[Any] | None = None
    # Null in every record measured, so untyped.
    created_by: Any = None
    created_on: str | None = None
    # Null in every record measured, so untyped.
    # ``from`` is a keyword, so it is declared through the annotations.
    __annotations__["from"] = "Any"
    id: str | None = None
    # Null in every record measured, so untyped.
    last_updated_by: Any = None
    # Null in every record measured, so untyped.
    last_updated_on: Any = None
    mail_type: str | None = None
    message_type: str | None = None
    object: str | None = None
    status: str | None = None
    # Null in every record measured, so untyped.
    subject: Any = None
    to: str | None = None
    uuid: str | None = None


class AccountCommunicationsEmailList(Dto):
    """One page of ``AccountCommunicationsEmail`` records, under ``data``."""

    MEASURED_FROM = ("GET /api/{api_version}/accounts/{account_id}/communications/emails",)

    data: list[AccountCommunicationsEmail] | None = None
    object: str | None = None
    pagination: Pagination | None = None
    url: str | None = None


class AccountCommunicationsEmailAttachment(Dto):
    """One entry of a :class:`AccountCommunicationsEmail`'s ``attachments``."""

    file_path: str | None = None
    name: str | None = None
    path: str | None = None
    size: int | None = None
    type: str | None = None
