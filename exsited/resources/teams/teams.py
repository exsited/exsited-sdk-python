"""Team endpoints, under ``/api/{api_version}/settings/teams``."""

from __future__ import annotations

from typing import Any, Mapping

from exsited.client.api_response import ApiResponse
from exsited.dto import Dto
from exsited.errors import SdkUsageError
from exsited.resources.teams import teams_urls
from exsited.resources.teams.teams_dto import (
    SettingsTeam,
    SettingsTeamList,
)

__all__ = [
    "get_settings_teams",
    "create_settings_team",
    "get_settings_team",
    "delete_settings_team",
    "update_settings_team",
]

#: The key a listing puts its records under.
RECORD_KEY = "data"

TeamPayload = Mapping[str, Any] | str | Dto


def get_settings_teams(
    client: Any,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[SettingsTeamList]:
    """List teams - ``GET /settings/teams``."""
    return client.send_get_request(
        teams_urls.SETTINGS_TEAMS,
        query_params=query_params,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=SettingsTeamList,
    )


def create_settings_team(
    client: Any,
    payload: TeamPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[SettingsTeam]:
    """Create a team - ``POST /settings/teams``."""
    _require_payload(payload)
    return client.send_post_request(
        teams_urls.SETTINGS_TEAMS,
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=SettingsTeam,
    )


def get_settings_team(
    client: Any,
    team_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[SettingsTeam]:
    """Get one team - ``GET /settings/teams/{team_id}``."""
    return client.send_get_request(
        teams_urls.SETTINGS_TEAM,
        path_params={"team_id": team_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=SettingsTeam,
    )


def delete_settings_team(
    client: Any,
    team_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Delete a team - ``DELETE /settings/teams/{team_id}``; refused while the team has members."""
    return client.send_delete_request(
        teams_urls.SETTINGS_TEAM,
        path_params={"team_id": team_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def update_settings_team(
    client: Any,
    team_id: str,
    payload: TeamPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[SettingsTeam]:
    """Update or enable/disable a team - ``PATCH /settings/teams/{team_id}``; ``status`` takes
    active or inactive."""
    _require_payload(payload)
    return client.send_patch_request(
        teams_urls.SETTINGS_TEAM,
        path_params={"team_id": team_id},
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=SettingsTeam,
    )


def _require_payload(payload: Any) -> None:
    if payload is None:
        raise SdkUsageError(
            "payload is required: this endpoint takes a body, and None would "
            "send the request with no body at all"
        )
