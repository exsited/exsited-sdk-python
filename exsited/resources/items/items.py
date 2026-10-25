"""Item endpoints, under ``/api/{api_version}/items``."""

from __future__ import annotations

from typing import Any, Mapping

from exsited.client.api_response import ApiResponse
from exsited.dto import Dto
from exsited.errors import SdkUsageError
from exsited.http.query_params import SortDirection, filter_param, sort_param
from exsited.resources.items import items_urls
from exsited.resources.items.items_dto import (
    InventoryAdjustmentList,
    Item,
    ItemInventoriesView,
    ItemList,
    ItemNoteFile,
    ItemPurchaseView,
    ItemSaleView,
    NoteFileList,
    NoteList,
    NoteView,
)

__all__ = [
    "get_items",
    "get_item",
    "get_item_information",
    "create_item",
    "update_item_information",
    "deactivate_item",
    "reactivate_item",
    "delete_item",
    "upload_item_image",
    "get_item_sale",
    "create_item_sale",
    "update_item_sale",
    "get_item_purchase",
    "create_item_purchase",
    "update_item_purchase",
    "get_item_inventories",
    "update_item_inventories",
    "add_item_inventory",
    "get_item_inventory_adjustments",
    "get_item_warehouse_inventories",
    "update_item_bundle_details",
    "update_item_variations",
    "get_item_family_details",
    "create_item_family_details",
    "get_item_package_details",
    "get_item_package_detail",
    "create_item_package_details",
    "delete_item_package_detail",
    "get_item_notes",
    "get_item_note",
    "create_item_note",
    "update_item_note",
    "delete_item_note",
    "get_item_note_files",
    "get_item_note_file",
    "create_item_inventories",
    "create_item_inventory",
    "add_item_inventories",
    "update_item_package_detail",
    "delete_item_note_file",
    "get_item_kpis",
]

#: A body as the API's own mapping, as JSON text, or as an ``items_dto`` type.
ItemPayload = Mapping[str, Any] | str | Dto


def item_filter_param(field: str, operator: str = "eq") -> str:
    """Build a ``filter_*`` name for the item listing, as ``exsited.http.query_params.filter_param``
    does. The API checks the name and the value's type, but a well-typed value the field cannot take
    answers ``200`` with an empty ``data``."""
    return filter_param(field, operator)


def sort_params(field: str, descending: bool = False) -> dict[str, str]:
    """The item listing's sort parameter as a one-key mapping, ``{"sort": "-created_on"}``;
    ``order_by`` and ``direction`` are accepted and ignored."""
    if not isinstance(field, str) or not field.strip():
        raise SdkUsageError(f"sort field: expected a name like 'created_on', got {field!r}")
    return {
        "sort": sort_param(field.strip(), SortDirection.DESC if descending else SortDirection.ASC)
    }


def get_items(
    client: Any,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[ItemList]:
    """List items - ``GET /items``. ``ITEMS_QUERY_PARAMS`` shape the listing; every other name is a
    ``filter_<field>`` over the ``items_urls`` filter sets. Never send a ``filter`` expression: it
    is ``400``."""
    return client.send_get_request(
        items_urls.ITEMS,
        query_params=query_params,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=ItemList,
    )


def get_item(
    client: Any,
    item_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[Item]:
    """Retrieve one item - ``GET /items/{item_id}``. Pass the ``id`` (``"ITEM-0001"``), not the
    ``uuid`` or the integer id the sale, purchase and inventories reads carry."""
    return client.send_get_request(
        items_urls.ITEM,
        path_params={"item_id": item_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=Item,
    )


def get_item_information(
    client: Any,
    item_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[Item]:
    """Retrieve an item's core information - ``GET /items/{item_id}/information``."""
    return client.send_get_request(
        items_urls.ITEM_INFORMATION,
        path_params={"item_id": item_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=Item,
    )


def create_item(
    client: Any,
    payload: ItemPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[Item]:
    """Create an item - ``POST /items``, wrapped in ``item``; ``type`` and ``name`` are the minimum,
    and an unknown ``group`` is ``400 Invalid group``."""
    _require_payload(payload)
    return client.send_post_request(
        items_urls.ITEMS,
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=Item,
    )


def update_item_information(
    client: Any,
    item_id: str,
    payload: ItemPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[Item]:
    """Update an item's core information - ``PATCH /items/{item_id}/information``, wrapped in
    ``item``; send only what changes."""
    _require_payload(payload)
    return client.send_patch_request(
        items_urls.ITEM_INFORMATION,
        path_params={"item_id": item_id},
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=Item,
    )


def deactivate_item(
    client: Any,
    item_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[Item]:
    """Deactivate an item - ``POST /items/{item_id}/deactivate``; no body, and the recorded call
    answered ``500``."""
    return client.send_post_request(
        items_urls.ITEM_DEACTIVATE,
        path_params={"item_id": item_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=Item,
    )


def reactivate_item(
    client: Any,
    item_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[Item]:
    """Reactivate a deactivated item - ``POST /items/{item_id}/reactivate``; no body, and the
    recorded call answered ``500``."""
    return client.send_post_request(
        items_urls.ITEM_REACTIVATE,
        path_params={"item_id": item_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=Item,
    )


def delete_item(
    client: Any,
    item_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Delete an item - ``DELETE /items/{item_id}``. One an order references answers ``409``, which
    is not retryable."""
    return client.send_delete_request(
        items_urls.ITEM,
        path_params={"item_id": item_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def upload_item_image(
    client: Any,
    item_id: str,
    payload: ItemPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[Item]:
    """Set the item's image - ``POST /items/{item_id}/image``; ``image_base64`` at the top level,
    the one item write with no ``item`` wrapper."""
    _require_payload(payload)
    return client.send_post_request(
        items_urls.ITEM_IMAGE,
        path_params={"item_id": item_id},
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=Item,
    )


def get_item_sale(
    client: Any,
    item_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[ItemSaleView]:
    """Retrieve an item's sale configuration - ``GET /items/{item_id}/sale``; a stub
    ``{id, name, sale}`` whose ``id`` is an integer."""
    return client.send_get_request(
        items_urls.ITEM_SALE,
        path_params={"item_id": item_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=ItemSaleView,
    )


def create_item_sale(
    client: Any,
    item_id: str,
    payload: ItemPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[Item]:
    """Create an item's sale configuration - ``POST /items/{item_id}/sale``, the ``sale`` block
    inside ``item``; a second create is ``409 already_exists``."""
    _require_payload(payload)
    return client.send_post_request(
        items_urls.ITEM_SALE,
        path_params={"item_id": item_id},
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=Item,
    )


def update_item_sale(
    client: Any,
    item_id: str,
    payload: ItemPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[Item]:
    """Update an item's sale configuration - ``PATCH /items/{item_id}/sale``, partial, inside
    ``item``."""
    _require_payload(payload)
    return client.send_patch_request(
        items_urls.ITEM_SALE,
        path_params={"item_id": item_id},
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=Item,
    )


def get_item_purchase(
    client: Any,
    item_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[ItemPurchaseView]:
    """Retrieve an item's purchase configuration - ``GET /items/{item_id}/purchase``; a stub, as the
    sale read answers."""
    return client.send_get_request(
        items_urls.ITEM_PURCHASE,
        path_params={"item_id": item_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=ItemPurchaseView,
    )


def create_item_purchase(
    client: Any,
    item_id: str,
    payload: ItemPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[Item]:
    """Create an item's purchase configuration - ``POST /items/{item_id}/purchase``, the
    ``purchase`` block inside ``item``."""
    _require_payload(payload)
    return client.send_post_request(
        items_urls.ITEM_PURCHASE,
        path_params={"item_id": item_id},
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=Item,
    )


def update_item_purchase(
    client: Any,
    item_id: str,
    payload: ItemPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[Item]:
    """Update an item's purchase configuration - ``PATCH /items/{item_id}/purchase``."""
    _require_payload(payload)
    return client.send_patch_request(
        items_urls.ITEM_PURCHASE,
        path_params={"item_id": item_id},
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=Item,
    )


def get_item_inventories(
    client: Any,
    item_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[ItemInventoriesView]:
    """Retrieve an item's inventory configuration and stock - ``GET /items/{item_id}/inventories``;
    a stub whose warehouse quantities are integers."""
    return client.send_get_request(
        items_urls.ITEM_INVENTORIES,
        path_params={"item_id": item_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=ItemInventoriesView,
    )


def update_item_inventories(
    client: Any,
    item_id: str,
    payload: ItemPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[Item]:
    """Update an item's inventory configuration - ``PATCH /items/{item_id}/inventories``; warehouse
    management is written ``warehouse_enabled``."""
    _require_payload(payload)
    return client.send_patch_request(
        items_urls.ITEM_INVENTORIES,
        path_params={"item_id": item_id},
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=Item,
    )


def add_item_inventory(
    client: Any,
    item_id: str,
    payload: ItemPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[Item]:
    """Add stock to a warehouse - ``POST /items/{item_id}/inventory/add``, ``inventory`` singular;
    the warehouse is keyed ``name`` here."""
    _require_payload(payload)
    return client.send_post_request(
        items_urls.ITEM_INVENTORY_ADD,
        path_params={"item_id": item_id},
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=Item,
    )


def get_item_inventory_adjustments(
    client: Any,
    item_id: str,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[InventoryAdjustmentList]:
    """List an item's inventory movements - ``GET /items/{item_id}/inventory_adjustments``; every
    quantity here is text."""
    return client.send_get_request(
        items_urls.ITEM_INVENTORY_ADJUSTMENTS,
        path_params={"item_id": item_id},
        query_params=query_params,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=InventoryAdjustmentList,
    )


def get_item_warehouse_inventories(
    client: Any,
    item_id: str,
    warehouse_name: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[ItemInventoriesView]:
    """Retrieve one warehouse's stock for an item -
    ``GET /items/{item_id}/warehouses/{warehouse_name}/inventories``, by the warehouse's name."""
    return client.send_get_request(
        items_urls.ITEM_WAREHOUSE_INVENTORIES,
        path_params={"item_id": item_id, "warehouse_name": warehouse_name},
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=ItemInventoriesView,
    )


def update_item_bundle_details(
    client: Any,
    item_id: str,
    payload: ItemPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[Item]:
    """Set a bundle's components - ``PATCH /items/{item_id}/bundle_details``; a bare list, unlike
    ``family_details``."""
    _require_payload(payload)
    return client.send_patch_request(
        items_urls.ITEM_BUNDLE_DETAILS,
        path_params={"item_id": item_id},
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=Item,
    )


def update_item_variations(
    client: Any,
    item_id: str,
    payload: ItemPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[Item]:
    """Configure an item's variations - ``PATCH /items/{item_id}/variations``; a parent sends
    ``configure_variations``, a child ``parent_item_id`` and ``use_variations``."""
    _require_payload(payload)
    return client.send_patch_request(
        items_urls.ITEM_VARIATIONS,
        path_params={"item_id": item_id},
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=Item,
    )


def get_item_family_details(
    client: Any,
    item_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[Item]:
    """List the members of an item family - ``GET /items/{item_id}/family_details``."""
    return client.send_get_request(
        items_urls.ITEM_FAMILY_DETAILS,
        path_params={"item_id": item_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=Item,
    )


def create_item_family_details(
    client: Any,
    item_id: str,
    payload: ItemPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[Item]:
    """Add members to an item family - ``POST /items/{item_id}/family_details``; an object with an
    ``add`` list."""
    _require_payload(payload)
    return client.send_post_request(
        items_urls.ITEM_FAMILY_DETAILS,
        path_params={"item_id": item_id},
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=Item,
    )


def get_item_package_details(
    client: Any,
    item_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[Item]:
    """List an item's packages - ``GET /items/{item_id}/package_details``."""
    return client.send_get_request(
        items_urls.ITEM_PACKAGE_DETAILS,
        path_params={"item_id": item_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=Item,
    )


def get_item_package_detail(
    client: Any,
    item_id: str,
    package_detail_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[Item]:
    """Retrieve one package - ``GET /items/{item_id}/package_details/{package_detail_id}``, by its
    ``uuid``."""
    return client.send_get_request(
        items_urls.ITEM_PACKAGE_DETAIL,
        path_params={"item_id": item_id, "package_detail_id": package_detail_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=Item,
    )


def create_item_package_details(
    client: Any,
    item_id: str,
    payload: ItemPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[Item]:
    """Add a package to an item - ``POST /items/{item_id}/package_details``."""
    _require_payload(payload)
    return client.send_post_request(
        items_urls.ITEM_PACKAGE_DETAILS,
        path_params={"item_id": item_id},
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=Item,
    )


def delete_item_package_detail(
    client: Any,
    item_id: str,
    package_detail_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Delete one package - ``DELETE /items/{item_id}/package_details/{package_detail_id}``."""
    return client.send_delete_request(
        items_urls.ITEM_PACKAGE_DETAIL,
        path_params={"item_id": item_id, "package_detail_id": package_detail_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def get_item_notes(
    client: Any,
    item_id: str,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[NoteList]:
    """List an item's notes - ``GET /items/{item_id}/notes``; a paged listing, under ``data``."""
    return client.send_get_request(
        items_urls.ITEM_NOTES,
        path_params={"item_id": item_id},
        query_params=query_params,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=NoteList,
    )


def get_item_note(
    client: Any,
    item_id: str,
    note_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[NoteView]:
    """Retrieve one note - ``GET /items/{item_id}/notes/{note_id}``, under ``note``."""
    return client.send_get_request(
        items_urls.ITEM_NOTE,
        path_params={"item_id": item_id, "note_id": note_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=NoteView,
    )


def create_item_note(
    client: Any,
    item_id: str,
    note: str,
    files: Any = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[NoteView]:
    """Attach a note to an item - ``POST /items/{item_id}/notes``; multipart, the text as the
    ``note`` field."""
    _require_note(note)
    return client.send_post_request(
        items_urls.ITEM_NOTES,
        path_params={"item_id": item_id},
        form_data={"note": note},
        files=files,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=NoteView,
    )


def update_item_note(
    client: Any,
    item_id: str,
    note_id: str,
    note: str,
    files: Any = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[NoteView]:
    """Update a note's text - ``PATCH /items/{item_id}/notes/{note_id}``; a form, as the create
    is."""
    _require_note(note)
    return client.send_patch_request(
        items_urls.ITEM_NOTE,
        path_params={"item_id": item_id, "note_id": note_id},
        form_data={"note": note},
        files=files,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=NoteView,
    )


def delete_item_note(
    client: Any,
    item_id: str,
    note_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Delete one note - ``DELETE /items/{item_id}/notes/{note_id}``."""
    return client.send_delete_request(
        items_urls.ITEM_NOTE,
        path_params={"item_id": item_id, "note_id": note_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def get_item_note_files(
    client: Any,
    item_id: str,
    note_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[NoteFileList]:
    """List a note's attachments - ``GET /items/{item_id}/notes/{note_id}/files``."""
    return client.send_get_request(
        items_urls.ITEM_NOTE_FILES,
        path_params={"item_id": item_id, "note_id": note_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=NoteFileList,
    )


def get_item_note_file(
    client: Any,
    item_id: str,
    note_id: str,
    file_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[ItemNoteFile]:
    """Retrieve one attachment - ``GET /items/{item_id}/notes/{note_id}/files/{file_id}``;
    it answers a JSON descriptor of the
    file under ``file``, not the file's bytes."""
    return client.send_get_request(
        items_urls.ITEM_NOTE_FILE,
        path_params={"item_id": item_id, "note_id": note_id, "file_id": file_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=ItemNoteFile,
    )


def create_item_inventories(
    client: Any,
    item_id: str,
    payload: ItemPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[Item]:
    """Create an item's inventory section - ``POST /items/{item_id}/inventories``, once, on a
    ``STANDARD`` item with sale or purchase on; ``201`` with the whole item."""
    _require_payload(payload)
    return client.send_post_request(
        items_urls.ITEM_INVENTORIES,
        path_params={"item_id": item_id},
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=Item,
    )


def create_item_inventory(
    client: Any,
    item_id: str,
    payload: ItemPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[Item]:
    """Create an item's inventory section - ``POST /items/{item_id}/inventory``, ``inventory``
    singular; the same handler as ``create_item_inventories``."""
    _require_payload(payload)
    return client.send_post_request(
        items_urls.ITEM_INVENTORY,
        path_params={"item_id": item_id},
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=Item,
    )


def add_item_inventories(
    client: Any,
    item_id: str,
    payload: ItemPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[Item]:
    """Add stock to a warehouse - ``POST /items/{item_id}/inventories/add``, ``inventories``
    plural; the same handler as ``add_item_inventory``."""
    _require_payload(payload)
    return client.send_post_request(
        items_urls.ITEM_INVENTORIES_ADD,
        path_params={"item_id": item_id},
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=Item,
    )


def update_item_package_detail(
    client: Any,
    item_id: str,
    package_detail_id: str,
    payload: ItemPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[Item]:
    """Update one package - ``PATCH /items/{item_id}/package_details/{package_detail_id}``, by its
    ``uuid``; the body is ``{"item": {"package_details": {...}}}``."""
    _require_payload(payload)
    return client.send_patch_request(
        items_urls.ITEM_PACKAGE_DETAIL,
        path_params={"item_id": item_id, "package_detail_id": package_detail_id},
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=Item,
    )


def delete_item_note_file(
    client: Any,
    item_id: str,
    note_id: str,
    file_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Delete one attachment - ``DELETE /items/{item_id}/notes/{note_id}/files/{file_id}``, the
    ``uuid`` the note's files listing gives; any failure is answered ``404``."""
    return client.send_delete_request(
        items_urls.ITEM_NOTE_FILE,
        path_params={"item_id": item_id, "note_id": note_id, "file_id": file_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def get_item_kpis(
    client: Any,
    item_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Retrieve an item's KPI summary - ``GET /items/{item_id}/kpis``, under ``item_kpis``; empty
    for every item measured, so no typed view."""
    return client.send_get_request(
        items_urls.ITEM_KPIS,
        path_params={"item_id": item_id},
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
