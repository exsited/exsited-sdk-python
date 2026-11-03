"""Typed views over the user settings bodies."""

from __future__ import annotations

from typing import Any

from exsited.dto import Dto

__all__ = [
    "UserSettings",
    "UserSettingsDashboard",
    "UserSettingsDisplaySettings",
    "UserSettingsProfile",
    "UserSettingsProfileImage",
]


class UserSettingsProfile(Dto):
    """A :class:`UserSettings`' ``profile``. ``time_zone`` is untyped."""

    display_name: str | None = None
    email: str | None = None
    image_link: str | None = None
    name: str | None = None
    time_zone: Any = None


class UserSettingsDashboard(Dto):
    """A :class:`UserSettings`' ``dashboard``. ``enabled_dashboards`` and
    ``default_dashboard`` are not typed further."""

    default_dashboard: Any = None
    enabled_dashboards: dict[str, Any] | None = None
    use_default: bool | None = None


class UserSettingsDisplaySettings(Dto):
    """A :class:`UserSettings`' ``display_settings``. ``modules`` is untyped."""

    modules: list[Any] | None = None
    use_default: bool | None = None


class UserSettings(Dto):
    """One user's settings, under ``user_settings``. ``created_by`` and ``last_updated_by``
    are untyped."""


    ENVELOPE_KEY = "user_settings"

    created_by: Any = None
    created_on: str | None = None
    dashboard: UserSettingsDashboard | None = None
    display_settings: UserSettingsDisplaySettings | None = None
    href: str | None = None
    id: str | None = None
    last_updated_by: Any = None
    last_updated_on: str | None = None
    object: str | None = None
    profile: UserSettingsProfile | None = None


class UserSettingsProfileImage(Dto):
    """A user's profile image, under ``user_settings``."""


    ENVELOPE_KEY = "user_settings"

    base64: str | None = None
