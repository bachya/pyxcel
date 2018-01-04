"""Define an object that retrieves usage data."""

import weakref
from json.decoder import JSONDecodeError

import pyxcel.api as api
import pyxcel.exceptions as exceptions


class Usages(api.BaseAPI):
    """Define an API to get usage information."""

    ENDPOINT = 'user/getJsonAccountUsages.req'

    def __init__(self, client, session):
        """Initialize."""
        self.client = weakref.ref(client)
        self.parent = super()
        self.parent.__init__(session)

    # pylint: disable=arguments-differ
    def get(self, premise_id):
        """Get the usage information for a particular "premise"."""
        try:
            return self.parent.get(
                self.ENDPOINT, params={'premise': premise_id}).json()
        except JSONDecodeError:
            self.client.create_session()
            try:
                return self.parent.get(
                    self.ENDPOINT, params={'premise': premise_id}).json()
            except JSONDecodeError:
                raise exceptions.XcelSessionError()
