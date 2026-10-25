"""Path templates and body keys for the labour endpoints."""

from __future__ import annotations

LABOUR_AVAILABILITY = "/api/{api_version}/labour_availability"
LABOUR_PROFILES = "/api/{api_version}/labour_profiles"
LABOURS = "/api/{api_version}/labours"
LABOUR_PROFILE = "/api/{api_version}/labour_profiles/{labour_profile_id}"
LABOURS_AVAILABLE_FOR_BOOKING = "/api/{api_version}/labours/available_for_booking"
LABOUR = "/api/{api_version}/labours/{labour_uuid}"
LABOUR_CANCEL = "/api/{api_version}/labours/{labour_id}/cancel"
LABOUR_REACTIVATE = "/api/{api_version}/labours/{labour_id}/reactivate"
LABOUR_ORDERS = "/api/{api_version}/labours/{labour_uuid}/orders"
LABOUR_PROFILE_SESSIONS = "/api/{api_version}/labour_profiles/{labour_profile_id}/sessions"
LABOUR_PROFILE_SESSION = (
    "/api/{api_version}/labour_profiles/{labour_profile_id}/sessions/{session_id}"
)
LABOUR_CALENDAR = "/api/{api_version}/labours/{labour_id}/availability"

#: The key a listing's records sit under.
LABOURS_AVAILABLE_FOR_BOOKING_KEY = "data"
LABOURS_KEY = "data"
LABOUR_AVAILABILITY_KEY = "data"
LABOUR_PROFILES_KEY = "data"
LABOUR_PROFILE_SESSIONS_KEY = "data"

#: The envelope one record arrives under.
LABOUR_KEY = "labour"
LABOUR_CALENDAR_KEY = "labour_calendar"
LABOUR_PROFILE_SESSION_KEY = "labour_profile_session"
