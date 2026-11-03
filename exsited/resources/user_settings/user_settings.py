"""User settings endpoints, under ``/api/{api_version}/user_settings``."""

from __future__ import annotations

from typing import Any

from exsited.client.api_response import ApiResponse
from exsited.resources.user_settings import user_settings_urls
from exsited.resources.user_settings.user_settings_dto import (
    UserSettings,
    UserSettingsProfileImage,
)

__all__ = [
    "get_user_settings",
    "get_user_settings_profile_image",
]


def get_user_settings(
    client: Any,
    user_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[UserSettings]:
    """Read one user's settings - ``GET /user_settings/{user_id}``, under ``user_settings``;
    ``user_id`` is the ``usr_`` id, which carries the same hex as the user's ``op_`` id."""
    return client.send_get_request(
        user_settings_urls.USER_SETTINGS,
        path_params={"user_id": user_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=UserSettings,
    )


def get_user_settings_profile_image(
    client: Any,
    user_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[UserSettingsProfileImage]:
    """Read a user's profile image - ``GET /user_settings/{user_id}/profile_image``; ``base64``
    is the image without a data URI prefix, and empty when the read has none to serve."""
    return client.send_get_request(
        user_settings_urls.USER_SETTINGS_PROFILE_IMAGE,
        path_params={"user_id": user_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=UserSettingsProfileImage,
    )
