"""Define an object that retrieves overview data."""

from json.decoder import JSONDecodeError

import pyxcel.api as api
import pyxcel.exceptions as exceptions


class Overview(api.BaseAPI):
    """Define an API to get overview information."""

    ENDPOINT = 'user/getJsonAccountOverview.req'

    def __init__(self, client, session):
        """Initialize."""
        self.client = client
        self.parent = super()
        self.parent.__init__(session)

    # pylint: disable=arguments-differ
    def get(self):
        """Get the "dashboard data" for the account."""
        try:
            return self.parent.get(self.ENDPOINT).json()
        except JSONDecodeError:
            self.client.create_session()
            try:
                return self.parent.get(self.ENDPOINT).json()
            except JSONDecodeError:
                raise exceptions.XcelSessionError()
