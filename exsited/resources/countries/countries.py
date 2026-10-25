"""Country endpoints, under ``/api/{api_version}/settings/countries``."""

from __future__ import annotations

from typing import Any, Mapping

from exsited.client.api_response import ApiResponse
from exsited.dto import Dto
from exsited.errors import SdkUsageError
from exsited.resources.countries import countries_urls
from exsited.resources.countries.countries_dto import (
    SettingsCountry,
    SettingsCountryList,
)

__all__ = [
    "get_settings_countries",
    "get_settings_country",
    "update_settings_country",
]

#: The key a listing puts its records under.
RECORD_KEY = "data"

CountryPayload = Mapping[str, Any] | str | Dto


def get_settings_countries(
    client: Any,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[SettingsCountryList]:
    """List the countries - ``GET /settings/countries``."""
    return client.send_get_request(
        countries_urls.SETTINGS_COUNTRIES,
        query_params=query_params,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=SettingsCountryList,
    )


def get_settings_country(
    client: Any,
    country_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[SettingsCountry]:
    """Read one country by its ``country_`` id - ``GET /settings/countries/{country_id}``."""
    return client.send_get_request(
        countries_urls.SETTINGS_COUNTRY,
        path_params={"country_id": country_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=SettingsCountry,
    )


def update_settings_country(
    client: Any,
    country_id: str,
    payload: CountryPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[SettingsCountry]:
    """Update a country's status, description or ``default_*`` fields; the answer is the country
    as it was before the write - ``PATCH /settings/countries/{country_id}``."""
    _require_payload(payload)
    return client.send_patch_request(
        countries_urls.SETTINGS_COUNTRY,
        path_params={"country_id": country_id},
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=SettingsCountry,
    )


def _require_payload(payload: Any) -> None:
    if payload is None:
        raise SdkUsageError(
            "payload is required: this endpoint takes a body, and None would "
            "send the request with no body at all"
        )
