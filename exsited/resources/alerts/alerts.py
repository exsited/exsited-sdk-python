"""Alert endpoints, under ``/api/{api_version}/alerts``."""

from __future__ import annotations

from typing import Any, Mapping

from exsited.client.api_response import ApiResponse
from exsited.resources.alerts import alerts_urls
from exsited.resources.alerts.alerts_dto import Alerts

__all__ = [
    "get_alerts",
    "get_alert",
    "get_alerts_account_by_id",
    "get_alerts_employee_by_id",
    "get_alerts_labour_by_id",
]


def get_alerts(
    client: Any,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[Alerts]:
    """List all - ``GET /alerts``."""
    return client.send_get_request(
        alerts_urls.ALERTS,
        query_params=query_params,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=Alerts,
    )


def get_alert(
    client: Any,
    alert_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Get single - ``GET /alerts/{alert_id}``."""
    return client.send_get_request(
        alerts_urls.ALERT,
        path_params={"alert_id": alert_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def get_alerts_account_by_id(
    client: Any,
    account_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[Alerts]:
    """Alerts by account - ``GET /alerts/account/{account_id}``."""
    return client.send_get_request(
        alerts_urls.ALERTS_ACCOUNT_BY_ID,
        path_params={"account_id": account_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=Alerts,
    )


def get_alerts_employee_by_id(
    client: Any,
    employee_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[Alerts]:
    """Alerts by employee - ``GET /alerts/employee/{employee_id}``."""
    return client.send_get_request(
        alerts_urls.ALERTS_EMPLOYEE_BY_ID,
        path_params={"employee_id": employee_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=Alerts,
    )


def get_alerts_labour_by_id(
    client: Any,
    labour_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[Alerts]:
    """Alerts by labour - ``GET /alerts/labour/{labour_id}``."""
    return client.send_get_request(
        alerts_urls.ALERTS_LABOUR_BY_ID,
        path_params={"labour_id": labour_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=Alerts,
    )
