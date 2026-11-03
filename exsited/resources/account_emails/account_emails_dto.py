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


    ENVELOPE_KEY = "email"

    additional_template: Any = None
    attachments: list[AccountCommunicationsEmailAttachment] | None = None
    bcc: list[Any] | None = None
    body: Any = None
    cc: list[Any] | None = None
    created_by: Any = None
    created_on: str | None = None
    __annotations__["from"] = "Any"
    id: str | None = None
    last_updated_by: Any = None
    last_updated_on: Any = None
    mail_type: str | None = None
    message_type: str | None = None
    object: str | None = None
    status: str | None = None
    subject: Any = None
    to: str | None = None
    uuid: str | None = None


class AccountCommunicationsEmailList(Dto):
    """One page of ``AccountCommunicationsEmail`` records, under ``data``."""


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
