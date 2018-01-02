"""Define a set of tests for the usages API."""

# pylint: disable=wildcard-import,redefined-outer-name,unused-wildcard-import

import json

import pytest
import requests_mock

import pyxcel
from pyxcel.const import XCEL_API_BASE_URL
from tests.fixtures.general import *  # noqa
from tests.fixtures.usages import *  # noqa


def test_usages(password, premise_id, usages_get_200, username):
    """Test getting usage information."""
    with requests_mock.Mocker() as mock:
        mock.post('{0}/j_spring_security_check'.format(XCEL_API_BASE_URL))
        mock.get('{0}/user/login.req'.format(XCEL_API_BASE_URL))
        mock.get(
            '{0}/user/getJsonAccountUsages.req'.format(XCEL_API_BASE_URL),
            text=json.dumps(usages_get_200))

        client = pyxcel.Client(username, password)
        assert client.usages.get(premise_id) == usages_get_200
