"""Path templates and body keys for the custom feature endpoints."""

from __future__ import annotations

CUSTOM_FEATURE = "/api/{api_version}/custom_feature"
CUSTOM_FEATURE_BY_ID = "/api/{api_version}/custom_feature/{custom_feature_id}"

#: The key the listing's records sit under.
CUSTOM_FEATURE_LIST_KEY = "data"

#: The envelope one record arrives under. Its ``href`` names ``/custom_features``, which v4
#: answers ``405``; the served path is the singular one.
CUSTOM_FEATURE_KEY = "custom_feature"

#: The envelope a create or an update body is sent under.
COMPONENT_KEY = "component"
