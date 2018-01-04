"""Define an object that retrieves billing data."""

from json.decoder import JSONDecodeError

import pyxcel.api as api
import pyxcel.exceptions as exceptions


class Billing(api.BaseAPI):
    """Define an API to get billing information."""

    ENDPOINT = 'user/getMyBillsAccounts.req'

    def __init__(self, client, session):
        """Initialize."""
        self.client = client
        self.parent = super()
        self.parent.__init__(session)

    # pylint: disable=arguments-differ
    def get(self):
        """Get bill infomation for the account."""
        try:
            return self.parent.get(self.ENDPOINT).json()
        except JSONDecodeError:
            self.client.create_session()
            try:
                return self.parent.get(self.ENDPOINT).json()
            except JSONDecodeError:
                raise exceptions.XcelSessionError()
