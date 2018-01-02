"""Define an object that retrieves billing data."""

import pyxcel.api as api


class Billing(api.BaseAPI):
    """Define an API to get billing information."""

    def __init__(self, session):
        """Initialize."""
        self.parent = super()
        self.parent.__init__(session)

    # pylint: disable=arguments-differ
    def get(self):
        """Get bill infomation for the account."""
        return self.parent.get('user/getMyBillsAccounts.req').json()
