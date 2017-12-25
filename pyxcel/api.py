"""Define a base object for interacting with the Xcel Energy® website."""

import requests

import pyxcel.const as const
import pyxcel.exceptions as exceptions


class BaseAPI(object):
    """Define a class that represents an API request."""

    def __init__(self, session):
        """Initialize."""
        self.session = session

    def request(self, method_type, url, **kwargs):
        """Define a generic request."""
        full_url = '{0}/{1}'.format(const.XCEL_API_BASE_URL, url)
        method = getattr(self.session, method_type)
        resp = method(full_url, **kwargs)

        # I don't think it's good form to make end users of pytile have to
        #  explicitly catch exceptions from a sub-library, so here, I wrap the
        # Requests HTTPError in my own:
        try:
            resp.raise_for_status()
        except requests.exceptions.HTTPError as exc_info:
            raise exceptions.HTTPError(str(exc_info)) from None

        return resp

    def get(self, url, **kwargs):
        """Define a generic GET request."""
        return self.request('get', url, **kwargs)

    def post(self, url, **kwargs):
        """Define a generic POST request."""
        return self.request('post', url, **kwargs)
