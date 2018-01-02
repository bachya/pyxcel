"""Define an Xcel Energy® client."""

import requests

import pyxcel.api as api
from pyxcel.billing import Billing
from pyxcel.overview import Overview
from pyxcel.usages import Usages


class Client(api.BaseAPI):
    """Define an Xcel Energy® client."""

    def __init__(self, username, password):
        """Initialize."""
        self._username = username
        self._password = password
        self.session = requests.Session()

        super().__init__(self.session)
        self.create_session()

        self.billing = Billing(self.session)
        self.overview = Overview(self.session)
        self.usages = Usages(self.session)

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
