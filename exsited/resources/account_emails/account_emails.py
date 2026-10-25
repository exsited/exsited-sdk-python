"""Account email endpoints, under ``/api/{api_version}/accounts``."""

from __future__ import annotations

from typing import Any

from exsited.client.api_response import ApiResponse
from exsited.resources.account_emails import account_emails_urls

__all__ = [
    "delete_account_communications_email",
]

#: The key a listing puts its records under.
RECORD_KEY = "data"


def delete_account_communications_email(
    client: Any,
    account_id: str,
    email_uuid: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Delete email - ``DELETE /accounts/{account_id}/communications/emails/{email_uuid}``."""
    return client.send_delete_request(
        account_emails_urls.ACCOUNT_COMMUNICATIONS_EMAIL,
        path_params={"account_id": account_id, "email_uuid": email_uuid},
        raise_on_error=raise_on_error,
        response_format=response_format,
    )
