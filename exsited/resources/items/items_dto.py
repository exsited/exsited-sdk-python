"""Typed views over the item bodies. The sale, purchase and inventories reads answer a stub
under ``item``, so each has its own view beside :class:`Item`; the sale and purchase stubs
carry an integer ``id``, the inventories stub the string code."""

from __future__ import annotations

from typing import Any

from exsited.dto import Dto
from exsited.resources.common.pagination_dto import Pagination

__all__ = [
    "Reference",
    "User",
    "CustomForm",
    "ItemCode",
    "ItemCurrency",
    "BundleDetail",
    "FamilyDetail",
    "VariationOption",
    "PackageDetail",
    "TaxConfiguration",
    "Pricing",
    "SaleCharge",
    "ItemSale",
    "ItemPurchase",
    "InventoryProperties",
    "WarehouseInventory",
    "ItemInventories",
    "Note",
    "NoteAttachment",
    "Item",
    "ItemList",
    "ItemSaleView",
    "ItemPurchaseView",
    "ItemInventoriesView",
    "InventoryAdjustment",
    "InventoryAdjustmentList",
    "NoteList",
    "NoteFileList",
    "NoteView",
    "ItemCreate",
    "ItemInformationUpdate",
    "ItemSaleWrite",
    "ItemPurchaseWrite",
    "ItemInventoriesWrite",
    "InventoryAdd",
    "ItemVariationsWrite",
    "ItemBundleDetailsWrite",
    "ItemFamilyDetailsWrite",
    "ItemPackageDetailsWrite",
    "ItemImageUpload",
    "ItemNoteFile",
    "ItemCustomAttribute",
    "NoteViewWatcher",
    "NoteViewLastUpdatedBy",
    "ItemSalePricingLevel",
    "ItemSalePaymentProperty",
    "ItemSaleWidth",
    "ItemSaleHeight",
    "ItemSaleLength",
    "ItemSaleWeight",
    "ItemPurchasePurchaseProperty",
    "ItemPurchaseSupplier",
    "VariationOptionValue",
    "PackageDetailItem",
    "PackageDetailBillingPeriod",
    "NoteWatcher",
    "NoteLastUpdatedBy",
    "SaleChargeProperty",
    "PricingPricingModule",
    "ItemPurchaseSupplierTaxConfiguration",
    "InventoryPropertiesPreorderConfiguration",
]


class Reference(Dto):
    """A pointer to another record: ``{object, id, name, href}``."""

    object: str | None = None
    id: str | None = None
    name: str | None = None
    href: str | None = None


class User(Dto):
    """Whoever created or last updated a record."""

    object: str | None = None
    name: str | None = None
    id: str | None = None
    email: str | None = None
    href: str | None = None


class CustomForm(Dto):
    """The custom form an item was created under. Present on all 665 items."""

    object: str | None = None
    id: str | None = None
    name: str | None = None
    href: str | None = None


class ItemCode(Dto):
    """One entry of ``codes``: a named code slot."""

    name: str | None = None
    value: str | None = None


class ItemCurrency(Dto):
    """One entry of ``currencies``: which currency the item sells or buys in."""

    name: str | None = None
    used_for_sale: bool | None = None
    default_for_sale: bool | None = None
    used_for_purchase: bool | None = None
    default_for_purchase: bool | None = None
    suppliers: list[Any] | None = None


class BundleDetail(Dto):
    """One component of a bundle item."""

    id: str | None = None
    name: str | None = None
    quantity: float | None = None
    uom: str | None = None


class FamilyDetail(Dto):
    """One member of an item family."""

    item_id: str | None = None
    item_name: str | None = None


class VariationOption(Dto):
    """One variation axis, in ``configure_variations`` or ``use_variations``."""

    object: str | None = None
    id: str | None = None
    name: str | None = None
    href: str | None = None
    values: list[VariationOptionValue] | None = None


class PackageDetail(Dto):
    """One package on an item."""

    object: str | None = None
    id: str | None = None
    uuid: str | None = None
    name: str | None = None
    display_name: str | None = None
    status: str | None = None
    rank: int | None = None
    items: list[PackageDetailItem] | None = None
    billing_periods: list[PackageDetailBillingPeriod] | None = None
    custom_attributes: list[Any] | None = None
    created_on: str | None = None
    created_by: User | None = None
    last_updated_on: Any = None
    last_updated_by: Any = None


class TaxConfiguration(Dto):
    """Whether a price is entered inclusive of tax."""

    sale_price_entered_inclusive_of_tax: bool | None = None
    purchase_price_entered_inclusive_of_tax: bool | None = None
    sale_price_based_on: str | None = None
    tax_code: Reference | None = None


class Pricing(Dto):
    """The pricing block on a sale or purchase."""

    type: str | None = None
    version: int | None = None
    latest_used_pricing_version: int | None = None
    pricing_module: list[PricingPricingModule] | None = None


class SaleCharge(Dto):
    """The charge block on a sale."""

    type: str | None = None
    price_period: str | None = None
    properties: list[SaleChargeProperty] | None = None


class ItemSale(Dto):
    """An item's sale configuration."""

    enabled: bool | None = None
    enable_back_order: bool | None = None
    invoice_note: str | None = None
    default_sale_price: float | None = None
    pricing_method: str | None = None
    sale_price_variant: str | None = None
    use_on_sale_price: bool | None = None
    tax_exempt_when_sold: bool | None = None
    tax_configuration: TaxConfiguration | None = None
    charge: SaleCharge | None = None
    pricing: Pricing | None = None
    pricing_levels: list[ItemSalePricingLevel] | None = None
    pricing_schedules: list[Any] | None = None
    payment_properties: list[ItemSalePaymentProperty] | None = None
    accounting_code: Any = None
    discount_profile: Any = None
    pricing_profile: Any = None
    shipping_profile: Any = None
    sale_price: Any = None
    start_date: Any = None
    end_date: Any = None
    height: ItemSaleHeight | None = None
    length: ItemSaleLength | None = None
    weight: ItemSaleWeight | None = None
    width: ItemSaleWidth | None = None


class ItemPurchase(Dto):
    """An item's purchase configuration."""

    enabled: bool | None = None
    supplier_management_enabled: bool | None = None
    purchase_order_note: str | None = None
    default_purchase_price: float | None = None
    tax_exempt_when_purchase: bool | None = None
    tax_configuration: TaxConfiguration | None = None
    pricing: Pricing | None = None
    purchase_properties: list[ItemPurchasePurchaseProperty] | None = None
    accounting_code: Any = None
    pricing_profile: Any = None
    suppliers: list[ItemPurchaseSupplier] | None = None


class InventoryProperties(Dto):
    """The inventory settings block."""

    enabled: bool | None = None
    enable_batch_tracking: bool | None = None
    enable_serialization: bool | None = None
    enable_inventory_costing: bool | None = None
    enable_low_stock_notification: bool | None = None
    enable_preorder: bool | None = None
    enable_reordering: bool | None = None
    low_stock_threshold_based_on: str | None = None
    reordering_threshold_based_on: str | None = None
    quantity_available_for_sale: str | None = None
    quantity_available_for_sale_determination: list[Any] | None = None
    use_atp_value_as_quantity_available_for_webhook: bool | None = None
    default_cost_per_unit: Any = None
    preorder_configuration: list[InventoryPropertiesPreorderConfiguration] | None = None
    preorder_period: str | None = None


class WarehouseInventory(Dto):
    """One warehouse's stock line."""

    quantity_on_hand: int | None = None
    quantity_on_hand_value: str | None = None
    quantity_available: float | None = None
    quantity_available_value: str | None = None
    quantity_on_order: int | None = None
    quantity_promised: float | None = None
    quantity_on_return: int | None = None
    quantity_on_purchase_return: int | None = None
    warehouse: Reference | None = None
    uom: str | None = None


class ItemInventories(Dto):
    """An item's inventory block."""

    enabled: bool | None = None
    enable_warehouse_management: bool | None = None
    default_warehouse: str | None = None
    inventory_properties: InventoryProperties | None = None
    warehouses: list[WarehouseInventory] | None = None


class NoteAttachment(Dto):
    """One file on a note. The element shape was not established in the sample."""

    object: str | None = None
    id: str | None = None
    name: str | None = None
    href: str | None = None
    content_type: str | None = None
    filename: str | None = None
    size: int | None = None
    uuid: str | None = None


class Note(Dto):
    """One note on an item."""

    ENVELOPE_KEY = "note"

    object: str | None = None
    id: str | None = None
    content: str | None = None
    version: int | None = None
    href: str | None = None
    created_on: str | None = None
    created_by: User | None = None
    item: Reference | None = None
    attachments: list[NoteAttachment] | None = None
    watchers: list[NoteWatcher] | None = None
    group: Any = None
    user: Any = None
    last_updated_on: str | None = None
    last_updated_by: NoteLastUpdatedBy | None = None


class Item(Dto):
    """One item, as ``get_item`` and the listing return it."""

    ENVELOPE_KEY = "item"

    object: str | None = None
    id: str | None = None
    name: str | None = None
    display_name: str | None = None
    description: str | None = None
    type: str | None = None
    status: str | None = None
    origin: str | None = None
    invoice_note: str | None = None
    version: int | None = None
    href: str | None = None

    # Capability flags. All four present and boolean on all 665.
    sale_enabled: bool | None = None
    purchase_enabled: bool | None = None
    inventory_enabled: bool | None = None
    variations_enabled: bool | None = None

    # Family position. Both booleans on all 665.
    parent: bool | None = None
    child: bool | None = None
    parent_item_id: str | None = None

    custom_form: CustomForm | None = None
    manager: Reference | None = None
    #: Set on 2 of 665 - nearly always null.
    group: Reference | None = None

    created_on: str | None = None
    created_by: User | None = None
    #: Both null on 369 of 665 - an item that has never been edited.
    last_updated_on: str | None = None
    last_updated_by: User | None = None

    codes: list[ItemCode] | None = None
    currencies: list[ItemCurrency] | None = None

    # A plain get_item sends sale, purchase and inventories inline; activity_logs and the detail
    # lists below arrive only from their own endpoints.
    sale: ItemSale | None = None
    purchase: ItemPurchase | None = None
    inventories: ItemInventories | None = None
    bundle_details: list[BundleDetail] | None = None
    family_details: list[FamilyDetail] | None = None
    package_details: list[PackageDetail] | None = None
    configure_variations: list[VariationOption] | None = None
    use_variations: list[VariationOption] | None = None
    custom_objects: list[Any] | None = None

    #: Present but empty on every record measured, so the element type is unknown.
    uoms: list[Any] | None = None
    custom_attributes: list[ItemCustomAttribute] | None = None
    activity_logs: list[Any] | None = None

    #: Null on every record measured.
    base_uom: Any = None
    image_url: Any = None


class ItemList(Dto):
    """The listing envelope: ``{object, url, data, pagination}``."""

    object: str | None = None
    url: str | None = None
    data: list[Item] | None = None
    pagination: Pagination | None = None


class ItemSaleView(Dto):
    """What ``get_item_sale`` answers: a stub ``{id, name, sale}`` whose ``id`` is an integer, not
    the item's string code. ``ENVELOPE_KEY`` is ``"item"``."""

    ENVELOPE_KEY = "item"

    id: int | None = None
    name: str | None = None
    sale: ItemSale | None = None


class ItemPurchaseView(Dto):
    """What ``get_item_purchase`` answers: ``{id, name, purchase}``, ``id`` an integer.
    ``ENVELOPE_KEY`` is ``"item"``."""

    ENVELOPE_KEY = "item"

    id: int | None = None
    name: str | None = None
    purchase: ItemPurchase | None = None


class ItemInventoriesView(Dto):
    """What ``get_item_inventories`` answers: ``{id, name, inventories}``, ``id`` the string code.
    ``ENVELOPE_KEY`` is ``"item"``."""

    ENVELOPE_KEY = "item"

    id: str | None = None
    name: str | None = None
    inventories: ItemInventories | None = None


class InventoryAdjustment(Dto):
    """One inventory movement."""

    ENVELOPE_KEY = "inventory_adjustment"

    object: str | None = None
    id: str | None = None
    item_id: str | None = None
    item_name: str | None = None
    warehouse_name: str | None = None
    adjustment_amount: str | None = None
    adjustment_type: str | None = None
    reference: str | None = None
    status: str | None = None
    quantity_on_hand: str | None = None
    quantity_available: str | None = None
    quantity_on_order: str | None = None
    quantity_promised: str | None = None
    quantity_on_return: str | None = None
    quantity_on_purchase_return: str | None = None
    quantity_on_reserve: str | None = None
    created_on: str | None = None
    last_updated_on: str | None = None
    href: str | None = None
    created_by: Any = None
    last_updated_by: Any = None


class InventoryAdjustmentList(Dto):
    """The listing envelope for inventory adjustments."""

    object: str | None = None
    url: str | None = None
    data: list[InventoryAdjustment] | None = None
    pagination: Pagination | None = None


class NoteList(Dto):
    """The listing envelope for an item's notes."""

    object: str | None = None
    url: str | None = None
    data: list[Note] | None = None
    pagination: Pagination | None = None


class NoteFileList(Dto):
    """The listing envelope for a note's attachments."""

    object: str | None = None
    url: str | None = None
    data: list[NoteAttachment] | None = None
    pagination: Pagination | None = None


class NoteView(Note):
    """The single-note envelope: ``{"note": {...}}``."""

    last_updated_by: NoteViewLastUpdatedBy | None = None
    last_updated_on: str | None = None
    watchers: list[NoteViewWatcher] | None = None


# Every write body is wrapped in ``item``, the sale, purchase and inventories writes included;
# the image upload is the one whose field sits at the top level.


class ItemCreate(Dto):
    """The body ``create_item`` takes."""

    ENVELOPE_KEY = "item"

    name: str | None = None
    type: str | None = None
    display_name: str | None = None
    description: str | None = None
    origin: str | None = None
    invoice_note: str | None = None
    manager: str | None = None
    custom_form: str | None = None
    group: str | None = None
    #: The write spelling. Reads back as ``parent`` / ``child``.
    is_parent: bool | None = None
    is_child: bool | None = None
    parent_item_id: str | None = None
    currencies: list[ItemCurrency] | None = None
    uoms: list[Any] | None = None
    sale: Any = None
    purchase: Any = None
    inventories: Any = None
    bundle_details: list[Any] | None = None


class ItemInformationUpdate(Dto):
    """The body ``update_item_information`` takes."""

    ENVELOPE_KEY = "item"

    name: str | None = None
    display_name: str | None = None
    description: str | None = None
    origin: str | None = None
    invoice_note: str | None = None
    manager: str | None = None
    custom_form: str | None = None


class ItemSaleWrite(Dto):
    """The body the sale create and update take."""

    ENVELOPE_KEY = "item"

    sale: Any = None
    currencies: list[ItemCurrency] | None = None


class ItemPurchaseWrite(Dto):
    """The body the purchase create and update take."""

    ENVELOPE_KEY = "item"

    purchase: Any = None
    currencies: list[ItemCurrency] | None = None


class ItemInventoriesWrite(Dto):
    """The body ``update_item_inventories`` takes."""

    ENVELOPE_KEY = "item"

    inventories: Any = None


class InventoryAdd(Dto):
    """The body ``add_item_inventory`` takes."""

    ENVELOPE_KEY = "item"

    inventories: Any = None


class ItemVariationsWrite(Dto):
    """The body ``update_item_variations`` takes."""

    ENVELOPE_KEY = "item"

    configure_variations: list[Any] | None = None
    use_variations: list[Any] | None = None
    parent_item_id: str | None = None


class ItemBundleDetailsWrite(Dto):
    """The body ``update_item_bundle_details`` takes."""

    ENVELOPE_KEY = "item"

    bundle_details: list[Any] | None = None


class ItemFamilyDetailsWrite(Dto):
    """The body ``create_item_family_details`` takes."""

    ENVELOPE_KEY = "item"

    family_details: Any = None


class ItemPackageDetailsWrite(Dto):
    """The body ``create_item_package_details`` takes."""

    ENVELOPE_KEY = "item"

    package_details: Any = None


class ItemImageUpload(Dto):
    """Base64 in a JSON body, as on an account - not a multipart upload."""

    image_base64: str | None = None


class ItemNoteFile(Dto):
    """What ``get_item_note_file`` answers, under ``file``."""

    ENVELOPE_KEY = "file"

    content_type: str | None = None
    filename: str | None = None
    href: str | None = None
    size: int | None = None
    uuid: str | None = None


class ItemCustomAttribute(Dto):
    """One entry of a :class:`Item`'s ``custom_attributes``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None
    type: str | None = None
    value: str | None = None


class NoteViewWatcher(Dto):
    """One entry of a :class:`NoteView`'s ``watchers``."""

    email: str | None = None
    name: str | None = None
    type: str | None = None


class NoteViewLastUpdatedBy(Dto):
    """A :class:`NoteView`'s ``last_updated_by``."""

    name: str | None = None
    object: str | None = None


class ItemSalePricingLevel(Dto):
    """One entry of a :class:`ItemSale`'s ``pricing_levels``."""

    name: str | None = None
    uuid: str | None = None


class ItemSalePaymentProperty(Dto):
    """One entry of a :class:`ItemSale`'s ``payment_properties``."""

    name: str | None = None
    value: str | None = None


class ItemSaleWidth(Dto):
    """A :class:`ItemSale`'s ``width``."""

    uom: str | None = None
    value: float | None = None


class ItemSaleHeight(Dto):
    """A :class:`ItemSale`'s ``height``."""

    uom: str | None = None
    value: float | None = None


class ItemSaleLength(Dto):
    """A :class:`ItemSale`'s ``length``."""

    uom: str | None = None
    value: float | None = None


class ItemSaleWeight(Dto):
    """A :class:`ItemSale`'s ``weight``."""

    uom: str | None = None
    value: float | None = None


class ItemPurchasePurchaseProperty(Dto):
    """One entry of a :class:`ItemPurchase`'s ``purchase_properties``."""

    name: str | None = None
    value: str | None = None


class ItemPurchaseSupplier(Dto):
    """One entry of a :class:`ItemPurchase`'s ``suppliers``."""

    # Null in every record measured, so untyped.
    accounting_code: Any = None
    default_purchase_price: float | None = None
    # Null in every record measured, so untyped.
    id: Any = None
    name: str | None = None
    pricing: Pricing | None = None
    # Null in every record measured, so untyped.
    purchase_order_note: Any = None
    tax_configuration: ItemPurchaseSupplierTaxConfiguration | None = None
    tax_exempt_when_purchase: bool | None = None


class VariationOptionValue(Dto):
    """One entry of a :class:`VariationOption`'s ``values``."""

    name: str | None = None
    uuid: str | None = None


class PackageDetailItem(Dto):
    """One entry of a :class:`PackageDetail`'s ``items``."""

    item_id: str | None = None
    item_name: str | None = None
    quantity: float | None = None
    # Null in every record measured, so untyped.
    uom: Any = None


class PackageDetailBillingPeriod(Dto):
    """One entry of a :class:`PackageDetail`'s ``billing_periods``."""

    name: str | None = None
    rank: int | None = None


class NoteWatcher(Dto):
    """One entry of a :class:`Note`'s ``watchers``."""

    email: str | None = None
    name: str | None = None
    type: str | None = None


class NoteLastUpdatedBy(Dto):
    """A :class:`Note`'s ``last_updated_by``."""

    name: str | None = None
    object: str | None = None


class SaleChargeProperty(Dto):
    """One entry of a :class:`SaleCharge`'s ``properties``."""

    name: str | None = None
    value: str | None = None


class PricingPricingModule(Dto):
    """One entry of a :class:`Pricing`'s ``pricing_module``."""

    # Null in every record measured, so untyped.
    average_purchase_price: Any = None
    currency: str | None = None
    # Null in every record measured, so untyped.
    last_purchase_price: Any = None
    price: float | None = None
    price_type: str | None = None
    pricing_level: str | None = None
    unit: str | None = None


class ItemPurchaseSupplierTaxConfiguration(Dto):
    """A :class:`ItemPurchaseSupplier`'s ``tax_configuration``."""

    purchase_price_entered_inclusive_of_tax: bool | None = None
    tax_code: Reference | None = None


class InventoryPropertiesPreorderConfiguration(Dto):
    """One entry of a :class:`InventoryProperties`'s ``preorder_configuration``."""

    end_date: str | None = None
    name: str | None = None
    start_date: str | None = None
