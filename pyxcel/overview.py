"""Define an object that retrieves overview data."""

import pyxcel.api as api


class Overview(api.BaseAPI):
    """Define an API to get overview information."""

    def __init__(self, session):
        """Initialize."""
        self.parent = super()
        self.parent.__init__(session)

    # pylint: disable=arguments-differ
    def get(self):
        """Get the "dashboard data" for the account."""
        return self.parent.get('user/getJsonAccountOverview.req').json()
