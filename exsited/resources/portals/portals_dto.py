"""Typed views over the portal bodies."""

from __future__ import annotations

from exsited.dto import Dto

__all__ = [
    "PortalLogin",
    "PortalChangePassword",
    "PortalResetLink",
    "PortalLoginUser",
    "PortalLoginUserRow",
]


class PortalLogin(Dto):
    """The portal login body, under ``portal``."""

    MEASURED_FROM = ("POST /api/{api_version}/portal/login",)

    ENVELOPE_KEY = "portal"

    user: PortalLoginUser | None = None


class PortalChangePassword(Dto):
    """What ``create_portal_change_password`` answers, under ``portal``."""

    MEASURED_FROM = ("POST /api/{api_version}/portal/change_password",)

    ENVELOPE_KEY = "portal"

    message: str | None = None


class PortalResetLink(Dto):
    """What ``create_portal_reset_link`` answers."""

    MEASURED_FROM = ("POST /api/{api_version}/portal/reset_link",)

    message: str | None = None
    object: str | None = None


class PortalLoginUser(Dto):
    """A :class:`PortalLogin`'s ``user``."""

    email_address: str | None = None
    grant_access_portal: bool | None = None
    image_uri: str | None = None
    name: str | None = None
    portals: list[PortalLoginUserRow] | None = None
    type: str | None = None


class PortalLoginUserRow(Dto):
    """One entry of a :class:`PortalLoginUser`'s ``portals``."""

    account: str | None = None
    display_name: str | None = None
    uuid: str | None = None
