"""Define an Xcel Energy® client."""

import requests

import pyxcel.api as api


class Client(api.BaseAPI):
    """Define an Xcel Energy® client."""

    def __init__(self, username, password):
        """Initialize."""
        self._username = username
        self._password = password

        super().__init__(requests.Session())
        self.create_session()

    def create_session(self):
        """Create a session."""
        self.post(
            'j_spring_security_check',
            data={
                'j_callingsystem': 'xe',
                'j_username': self._username,
                'j_password': self._password
            })
        self.get('user/login.req')

    def get_account_overview(self):
        """Get the "dashboard data" for the account."""
        return self.get('user/getJsonAccountOverview.req').json()

    def get_bills(self):
        """Get bill infomation for the account."""
        return self.get('user/getMyBillsAccounts.req').json()

    def get_usages(self, premise_id):
        """Get the usage information for a particular "premise"."""
        return self.get(
            'user/getJsonAccountUsages.req',
            params={'premise': premise_id}).json()
