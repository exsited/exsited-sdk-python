"""Department endpoints, under ``/api/{api_version}/settings/departments``."""

from __future__ import annotations

from typing import Any, Mapping

from exsited.client.api_response import ApiResponse
from exsited.resources.departments import departments_urls
from exsited.resources.departments.departments_dto import (
    SettingsDepartment,
    SettingsDepartmentList,
)

__all__ = [
    "get_settings_departments",
    "get_settings_department",
]

#: The key a listing puts its records under.
RECORD_KEY = "data"


def get_settings_departments(
    client: Any,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[SettingsDepartmentList]:
    """List the departments; some carry no ``id`` and cannot be read singly -
    ``GET /settings/departments``."""
    return client.send_get_request(
        departments_urls.SETTINGS_DEPARTMENTS,
        query_params=query_params,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=SettingsDepartmentList,
    )


def get_settings_department(
    client: Any,
    department_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[SettingsDepartment]:
    """Read one department by its ``dept_`` id - ``GET /settings/departments/{department_id}``."""
    return client.send_get_request(
        departments_urls.SETTINGS_DEPARTMENT,
        path_params={"department_id": department_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=SettingsDepartment,
    )
