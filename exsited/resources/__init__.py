"""Endpoint modules, one folder per path family.

Each holds the functions for that family and a ``*_urls.py`` of path templates::

    resources/accounts/accounts.py
    resources/accounts/accounts_urls.py
    resources/accounts/accounts_dto.py

Each is registered by default and reachable on a client as ``client.<name>``;
:func:`exsited.register_resource_module` registers another.
"""
