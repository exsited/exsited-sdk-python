"""Item fulfillment endpoints, under ``/api/{api_version}``."""

from __future__ import annotations

from typing import Any, Mapping

from exsited.client.api_response import ApiResponse
from exsited.dto import Dto
from exsited.errors import SdkUsageError
from exsited.resources.item_fulfillments import item_fulfillments_urls
from exsited.resources.item_fulfillments.item_fulfillments_dto import (
    ItemFulfillmentList,
    ItemFulfillmentNoteList,
    ItemFulfillmentNoteRead,
    ItemFulfillmentNotes,
    ItemFulfillmentRead,
    ItemFulfillments,
    ItemFulfillmentUpdated,
)

__all__ = [
    "get_item_fulfillments",
    "create_item_fulfillment",
    "get_item_fulfillment",
    "update_item_fulfillment",
    "create_item_fulfillment_note",
    "delete_item_fulfillment",
    "get_item_fulfillment_notes",
    "get_item_fulfillment_note",
    "delete_item_fulfillment_note",
]

#: The key a listing puts its records under.
RECORD_KEY = "data"

ItemFulfillmentPayload = Mapping[str, Any] | str | Dto


def get_item_fulfillments(
    client: Any,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[ItemFulfillmentList]:
    """List item fulfilments - ``GET /item_fulfillments``."""
    return client.send_get_request(
        item_fulfillments_urls.ITEM_FULFILLMENTS,
        query_params=query_params,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=ItemFulfillmentList,
    )


def create_item_fulfillment(
    client: Any,
    payload: ItemFulfillmentPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[ItemFulfillments]:
    """Create fulfillment - ``POST /item_fulfillments``; answered ``201``."""
    _require_payload(payload)
    return client.send_post_request(
        item_fulfillments_urls.ITEM_FULFILLMENTS,
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=ItemFulfillments,
    )


def get_item_fulfillment(
    client: Any,
    fulfillment_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[ItemFulfillmentRead]:
    """Fulfillment details - ``GET /item_fulfillments/{fulfillment_id}``."""
    return client.send_get_request(
        item_fulfillments_urls.ITEM_FULFILLMENT,
        path_params={"fulfillment_id": fulfillment_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=ItemFulfillmentRead,
    )


def update_item_fulfillment(
    client: Any,
    fulfillment_id: str,
    payload: ItemFulfillmentPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[ItemFulfillmentUpdated]:
    """Update fulfillment - ``PATCH /item_fulfillments/{fulfillment_id}``."""
    _require_payload(payload)
    return client.send_patch_request(
        item_fulfillments_urls.ITEM_FULFILLMENT,
        path_params={"fulfillment_id": fulfillment_id},
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=ItemFulfillmentUpdated,
    )


def create_item_fulfillment_note(
    client: Any,
    fulfillment_id: str,
    note: str,
    files: Any = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[ItemFulfillmentNotes]:
    """Create note - ``POST /item_fulfillments/{fulfillment_id}/notes``;
    multipart, the text as the ``note`` field."""
    _require_note(note)
    return client.send_post_request(
        item_fulfillments_urls.ITEM_FULFILLMENT_NOTES,
        path_params={"fulfillment_id": fulfillment_id},
        form_data={"note": note},
        files=files,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=ItemFulfillmentNotes,
    )


def delete_item_fulfillment(
    client: Any,
    fulfillment_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Delete fulfillment - ``DELETE /item_fulfillments/{fulfillment_id}``, by its ``ifm_`` id;
    refused ``400`` ``stock_committed`` once any of its stock has been sent."""
    return client.send_delete_request(
        item_fulfillments_urls.ITEM_FULFILLMENT,
        path_params={"fulfillment_id": fulfillment_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def get_item_fulfillment_notes(
    client: Any,
    fulfillment_id: str,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[ItemFulfillmentNoteList]:
    """List fulfillment notes - ``GET /item_fulfillments/{fulfillment_id}/notes``; the notes of
    the fulfillment's sale invoice, which is where ``create_item_fulfillment_note`` puts them."""
    return client.send_get_request(
        item_fulfillments_urls.ITEM_FULFILLMENT_NOTES,
        path_params={"fulfillment_id": fulfillment_id},
        query_params=query_params,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=ItemFulfillmentNoteList,
    )


def get_item_fulfillment_note(
    client: Any,
    fulfillment_id: str,
    note_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[ItemFulfillmentNoteRead]:
    """Get one fulfillment note - ``GET /item_fulfillments/{fulfillment_id}/notes/{note_id}``,
    answered under ``item_fulfillment.note``."""
    return client.send_get_request(
        item_fulfillments_urls.ITEM_FULFILLMENT_NOTE,
        path_params={"fulfillment_id": fulfillment_id, "note_id": note_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=ItemFulfillmentNoteRead,
    )


def delete_item_fulfillment_note(
    client: Any,
    fulfillment_id: str,
    note_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Delete fulfillment note - ``DELETE /item_fulfillments/{fulfillment_id}/notes/{note_id}``,
    ``ifm_`` and ``note_`` ids; it looks on the fulfillment, where the create never puts one."""
    return client.send_delete_request(
        item_fulfillments_urls.ITEM_FULFILLMENT_NOTE,
        path_params={"fulfillment_id": fulfillment_id, "note_id": note_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def _require_payload(payload: Any) -> None:
    if payload is None:
        raise SdkUsageError(
            "payload is required: this endpoint takes a body, and None would "
            "send the request with no body at all"
        )


def _require_note(note: Any) -> None:
    # A None note would go out as the text "None" and be stored as the note.
    if note is None:
        raise SdkUsageError(
            "note is required: the note text is the body of this request, and "
            "None would be encoded as the string 'None' and stored as the note"
        )
