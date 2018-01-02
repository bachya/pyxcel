"""Define an object that retrieves usage data."""

import pyxcel.api as api


class Usages(api.BaseAPI):
    """Define an API to get usage information."""

    def __init__(self, session):
        """Initialize."""
        self.parent = super()
        self.parent.__init__(session)

    # pylint: disable=arguments-differ
    def get(self, premise_id):
        """Get the usage information for a particular "premise"."""
        return self.parent.get(
            'user/getJsonAccountUsages.req',
            params={'premise': premise_id}).json()
