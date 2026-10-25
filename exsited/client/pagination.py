"""Walking a paginated listing without hand-rolling the loop. v4 pages some listings by cursor
(``has_more``/``next_cursor``) and others by offset (``next_page``/``offset``), so the shape is
detected per page: a cursor walk over an offset listing would end silently after page one."""

from __future__ import annotations

from typing import Any, Iterator, Mapping

from exsited.client.api_response import ApiResponse
from exsited.errors import SdkError, SdkUsageError

__all__ = ["iter_pages", "iter_records"]

_PAGINATION_KEY = "pagination"
_HAS_MORE_KEY = "has_more"
_NEXT_CURSOR_KEY = "next_cursor"
_NEXT_PAGE_KEY = "next_page"

#: Owned by :func:`iter_pages`, which sets both from each page.
CURSOR_PARAM = "cursor"
OFFSET_PARAM = "offset"

LIMIT_PARAM = "limit"

#: A default rather than a rule: an envelope may key its records under another name.
DEFAULT_RECORD_KEY = "data"

#: The offset shape ends a listing with this string in ``next_page``, not with ``null``.
NO_NEXT_PAGE = "NULL"


def iter_pages(
    client: Any,
    path: str,
    *,
    path_params: Mapping[str, Any] | None = None,
    query_params: Mapping[str, Any] | None = None,
    record_key: str = DEFAULT_RECORD_KEY,
    max_pages: int | None = None,
    raise_on_error: bool = True,
) -> Iterator[ApiResponse]:
    """Yield one :class:`ApiResponse` per page, whichever shape the listing uses. ``query_params``
    is re-sent with every page, since a cursor or offset addresses one filtered, sorted listing;
    a revisited position is an error, not a loop."""
    if max_pages is not None and (
        not isinstance(max_pages, int) or isinstance(max_pages, bool) or max_pages < 1
    ):
        raise SdkUsageError(f"max_pages: expected a positive integer or None, got {max_pages!r}")
    for owned in (CURSOR_PARAM, OFFSET_PARAM):
        if query_params is not None and owned in query_params:
            # Sent on page one and replaced on page two, so the walk would start elsewhere.
            raise SdkUsageError(
                f"query_params: {owned!r} is owned by iter_pages, which sets it "
                f"from each page; to resume from a saved position call "
                f"send_get_request directly with it"
            )

    base_params = dict(query_params or {})
    page_params = dict(base_params)
    visited_cursors: set[str] = set()
    visited_offsets: set[int] = set()
    pages_yielded = 0

    while True:
        response = client.send_get_request(
            path,
            path_params=path_params,
            query_params=page_params,
            raise_on_error=raise_on_error,
        )
        yield response
        pages_yielded += 1

        if not response.succeeded:
            # Only reachable with raise_on_error off; a failed page has no position to trust.
            return
        if max_pages is not None and pages_yielded >= max_pages:
            return

        block = _read_pagination(response.map)
        if block is None:
            # No pagination block: one page is the whole answer.
            return

        cursor = _read_next_cursor(block)
        if cursor is not None:
            if cursor in visited_cursors:
                raise SdkError(
                    "pagination loop: the API handed back the same next_cursor a "
                    "second time, so following it again would never terminate - "
                    "report this listing; the pages already yielded are good"
                )
            visited_cursors.add(cursor)
            page_params = {**base_params, CURSOR_PARAM: cursor}
            continue

        offset = _read_next_offset(block, _count_records(response.map, record_key))
        if offset is None:
            return
        if offset in visited_offsets:
            raise SdkError(
                f"pagination loop: the walk arrived back at offset {offset}, so "
                f"advancing further would re-read records already yielded - "
                f"report this listing; the pages already yielded are good"
            )
        visited_offsets.add(offset)
        page_params = {**base_params, OFFSET_PARAM: offset}


def iter_records(
    client: Any,
    path: str,
    record_key: str = DEFAULT_RECORD_KEY,
    *,
    path_params: Mapping[str, Any] | None = None,
    query_params: Mapping[str, Any] | None = None,
    max_pages: int | None = None,
) -> Iterator[Any]:
    """Yield each record of a listing, across every page, as the API sent it. A first page with
    no list under ``record_key`` is refused with the keys it does carry."""
    if not isinstance(record_key, str) or not record_key.strip():
        raise SdkUsageError(
            f"record_key: expected the envelope key holding the records, "
            f"like {DEFAULT_RECORD_KEY!r}, got {record_key!r}"
        )
    for page_index, page in enumerate(
        iter_pages(
            client,
            path,
            path_params=path_params,
            query_params=query_params,
            record_key=record_key,
            max_pages=max_pages,
            raise_on_error=True,
        )
    ):
        records = page.map.get(record_key) if isinstance(page.map, Mapping) else None
        if not isinstance(records, list):
            if page_index > 0:
                # The end of the records, not a wrong key: earlier pages were already consumed.
                continue
            available = (
                ", ".join(sorted(str(key) for key in page.map))
                if isinstance(page.map, Mapping)
                else f"a {type(page.map).__name__} body"
            )
            raise SdkUsageError(
                f"record_key {record_key!r}: this page has no list under that "
                f"key; it carries {available}"
            )
        yield from records


def _read_pagination(data: Any) -> Mapping[str, Any] | None:
    """The ``pagination`` block, or ``None`` when the body carries none."""
    if not isinstance(data, Mapping):
        return None
    block = data.get(_PAGINATION_KEY)
    return block if isinstance(block, Mapping) else None


def _read_next_cursor(block: Mapping[str, Any]) -> str | None:
    """The next cursor, or ``None`` for an offset block or the end. ``has_more: false`` wins over
    a stale ``next_cursor``, which some last pages still carry."""
    if _HAS_MORE_KEY in block and not block[_HAS_MORE_KEY]:
        return None
    cursor = block.get(_NEXT_CURSOR_KEY)
    if isinstance(cursor, str) and cursor.strip():
        return cursor
    return None


def _read_next_offset(block: Mapping[str, Any], records_on_page: int) -> int | None:
    """The offset to ask for next, or ``None`` at the end. The offset is computed, never taken
    from the link, because an offset ``next_page`` link can point at another path."""
    if _NEXT_PAGE_KEY not in block:
        return None
    next_page = block[_NEXT_PAGE_KEY]
    if next_page is None:
        return None
    if isinstance(next_page, str):
        text = next_page.strip()
        if not text or text.upper() == NO_NEXT_PAGE:
            return None

    offset = block.get(OFFSET_PARAM)
    limit = block.get(LIMIT_PARAM)
    current = offset if isinstance(offset, int) and not isinstance(offset, bool) else 0
    if isinstance(limit, int) and not isinstance(limit, bool) and limit > 0:
        step = limit
    else:
        # A fallback: every measured offset block carries an integer limit.
        step = records_on_page
    if step <= 0:
        return None
    return current + step


def _count_records(data: Any, record_key: str) -> int:
    """How many records a page carried under ``record_key``, for the offset fallback."""
    if not isinstance(data, Mapping):
        return 0
    records = data.get(record_key)
    return len(records) if isinstance(records, list) else 0
