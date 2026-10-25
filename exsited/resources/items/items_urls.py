"""Path templates, body keys and filter names for the item endpoints. ``{item_id}`` is the
listing's ``id`` (``"ITEM-0001"``), never the ``uuid`` or the integer ``id`` the sale,
purchase and inventories reads carry; ``{warehouse_name}`` is a warehouse name."""

from __future__ import annotations

ITEMS = "/api/{api_version}/items"
ITEM = "/api/{api_version}/items/{item_id}"
ITEM_INFORMATION = "/api/{api_version}/items/{item_id}/information"

#: Both answer HTTP 500. See the functions.
ITEM_DEACTIVATE = "/api/{api_version}/items/{item_id}/deactivate"
ITEM_REACTIVATE = "/api/{api_version}/items/{item_id}/reactivate"

ITEM_IMAGE = "/api/{api_version}/items/{item_id}/image"

#: The sale, purchase and inventories trio. Each is readable, creatable once and
#: patchable, and each answers a stub item rather than the whole record.
ITEM_SALE = "/api/{api_version}/items/{item_id}/sale"
ITEM_PURCHASE = "/api/{api_version}/items/{item_id}/purchase"
ITEM_INVENTORIES = "/api/{api_version}/items/{item_id}/inventories"

ITEM_INVENTORY_ADD = "/api/{api_version}/items/{item_id}/inventory/add"
#: The singular and plural spellings are one handler each way: create, and add stock.
ITEM_INVENTORY = "/api/{api_version}/items/{item_id}/inventory"
ITEM_INVENTORIES_ADD = "/api/{api_version}/items/{item_id}/inventories/add"
ITEM_KPIS = "/api/{api_version}/items/{item_id}/kpis"
ITEM_INVENTORY_ADJUSTMENTS = "/api/{api_version}/items/{item_id}/inventory_adjustments"

#: Inventory for one warehouse. ``{warehouse_name}`` is a name, not an id.
ITEM_WAREHOUSE_INVENTORIES = (
    "/api/{api_version}/items/{item_id}/warehouses/{warehouse_name}/inventories"
)

ITEM_BUNDLE_DETAILS = "/api/{api_version}/items/{item_id}/bundle_details"
ITEM_VARIATIONS = "/api/{api_version}/items/{item_id}/variations"

ITEM_FAMILY_DETAILS = "/api/{api_version}/items/{item_id}/family_details"

ITEM_PACKAGE_DETAILS = "/api/{api_version}/items/{item_id}/package_details"
ITEM_PACKAGE_DETAIL = "/api/{api_version}/items/{item_id}/package_details/{package_detail_id}"

ITEM_NOTES = "/api/{api_version}/items/{item_id}/notes"
ITEM_NOTE = "/api/{api_version}/items/{item_id}/notes/{note_id}"
ITEM_NOTE_FILES = "/api/{api_version}/items/{item_id}/notes/{note_id}/files"
ITEM_NOTE_FILE = "/api/{api_version}/items/{item_id}/notes/{note_id}/files/{file_id}"

#: The key a listing's records sit under.
ITEMS_KEY = "data"
ITEM_INVENTORY_ADJUSTMENTS_KEY = "data"
ITEM_NOTES_KEY = "data"
ITEM_NOTE_FILES_KEY = "data"

#: The envelope one record arrives under.
ITEM_KEY = "item"
ITEM_KPIS_KEY = "item_kpis"
NOTE_KEY = "note"

#: The names that shape the listing, which pages by cursor; every other name is a
#: ``filter_<field>``. ``order_by`` and ``direction`` are accepted and ignored, and a bare
#: ``filter`` expression is ``400``.
ITEMS_QUERY_PARAMS = ("limit", "cursor", "sort")

#: The top-level item fields ``filter_<field>`` accepts, each with ``_neq`` too.
FILTERABLE_FIELDS: frozenset[str] = frozenset(
    {
        "id",
        "uuid",
        "name",
        "display_name",
        "description",
        "status",
        "type",
        "origin",
        "invoice_note",
        "image_uri",
        "base_uom",
        "group",
        "manager",
        "custom_form",
        "created_by",
        "last_updated_by",
        "version",
    }
)

#: The subset that also takes ``_contains`` and ``_not_contains``.
TEXT_FILTER_FIELDS: frozenset[str] = frozenset(
    {
        "id",
        "name",
        "display_name",
        "description",
        "origin",
        "invoice_note",
        "image_uri",
    }
)

#: The fields ``filter_<field>`` reaches inside the ``sale``, ``purchase`` and
#: ``inventories`` blocks. All answer ``200``; an unmatched value is ``data: []``, not an error.
NESTED_BLOCK_FILTERS: frozenset[str] = frozenset(
    {
        "item_number",
        "upc_code",
        "sale_enabled",
        "sales_accounting_code_revenue",
        "sales_billing_mode",
        "sales_charge_type",
        "sales_currency",
        "sales_fulfillment_mode",
        "sales_payment_mode",
        "sales_pricing_method",
        "sales_tax_inclusive_based_on",
        "purchase_enabled",
        "purchase_currency",
        "purchase_order_note",
        "purchase_profile",
        "purchase_receive_mode",
        "inventory_enabled",
        "inventory_quantity_available",
        "inventory_quantity_on_hand",
        "inventory_qty_avl_on_sale_determination",
    }
)
