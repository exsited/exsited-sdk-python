"""Root organisation endpoints, under ``/api/{api_version}/settings/organisation``."""

from __future__ import annotations

from typing import Any

from exsited.client.api_response import ApiResponse
from exsited.resources.organisation import organisation_urls
from exsited.resources.organisation.organisation_dto import SettingsOrganisation

__all__ = [
    "get_settings_organisation",
]


def get_settings_organisation(
    client: Any,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[SettingsOrganisation]:
    """Get the root organisation - ``GET /settings/organisation``; read only, a PATCH here
    answers 405."""
    return client.send_get_request(
        organisation_urls.SETTINGS_ORGANISATION,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=SettingsOrganisation,
    )
