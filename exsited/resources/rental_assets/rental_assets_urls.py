"""Path templates and body keys for the rental asset endpoints."""

from __future__ import annotations

RENTAL_ASSET_AVAILABILITY = "/api/{api_version}/rental_asset_availability"
RENTAL_ASSET_PROFILES = "/api/{api_version}/rental_asset_profiles"
RENTAL_ASSETS = "/api/{api_version}/rental_assets"
RENTAL_ASSET_PROFILE = "/api/{api_version}/rental_asset_profiles/{rental_asset_profile_id}"
RENTAL_ASSET = "/api/{api_version}/rental_assets/{rental_asset_uuid}"
RENTAL_ASSET_CANCEL = "/api/{api_version}/rental_assets/{rental_asset_id}/cancel"
RENTAL_ASSET_REACTIVATE = "/api/{api_version}/rental_assets/{rental_asset_id}/reactivate"

#: The key a listing's records sit under.
RENTAL_ASSETS_KEY = "data"
RENTAL_ASSET_AVAILABILITY_KEY = "data"
RENTAL_ASSET_PROFILES_KEY = "data"

#: The envelope one record arrives under.
RENTAL_ASSET_KEY = "rental_asset"
