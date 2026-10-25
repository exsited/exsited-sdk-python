"""ABA file endpoints, under ``/api/{api_version}/aba_file/generate``."""

from __future__ import annotations

from typing import Any, Mapping

from exsited.client.api_response import ApiResponse
from exsited.dto import Dto
from exsited.errors import SdkUsageError
from exsited.resources.aba_files import aba_files_urls

__all__ = [
    "generate_aba_file",
]

AbaFilePayload = Mapping[str, Any] | str | Dto


def generate_aba_file(
    client: Any,
    payload: AbaFilePayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Generate an ABA file from transactions - ``POST /aba_file/generate``."""
    _require_payload(payload)
    return client.send_post_request(
        aba_files_urls.ABA_FILE_GENERATE,
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def _require_payload(payload: Any) -> None:
    if payload is None:
        raise SdkUsageError(
            "payload is required: this endpoint takes a body, and None would "
            "send the request with no body at all"
        )
