"""Define module exceptions."""


class HTTPError(Exception):
    """Define a generic HTTP error (i.e., a wrapper for Requests)."""
    pass


class XcelSessionError(Exception):
    """Define a generic error for when an Xcel "API" request fails"""
    pass
