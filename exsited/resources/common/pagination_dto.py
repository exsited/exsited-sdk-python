"""The ``pagination`` block every v4 list envelope carries, in any of its three shapes."""

from __future__ import annotations

from exsited.dto import Dto

__all__ = [
    "Pagination",
    "PaginationLinks",
]


class Pagination(Dto):
    """A list envelope's ``pagination`` block. One response fills only one shape: cursor
    (``has_more`` present), offset (``records`` present) or the external database listings'
    (``has_next`` present), and the others read None."""

    #: The page size the API applied; the one field both shapes carry.
    limit: int | None = None

    #: Authoritative over :attr:`next_cursor`, which can be stale on the last page.
    has_more: bool | None = None
    next_cursor: str | None = None
    prev_cursor: str | None = None
    links: PaginationLinks | None = None

    #: Total matching records, not the page's length.
    records: int | None = None
    offset: int | None = None
    #: The literal string ``"NULL"`` at the end of a listing, not ``null``, so never truth-test
    #: it; a real link can point at another path, so the pager never follows one.
    next_page: str | None = None
    #: The empty string, never a URL: the offset shape has no backward paging.
    previous_page: str | None = None

    #: The external database listings page with these three instead.
    has_next: bool | None = None
    has_prev: bool | None = None
    per_page: int | None = None


class PaginationLinks(Dto):
    """A :class:`Pagination`'s ``links``."""

    next: str | None = None
    prev: str | None = None
