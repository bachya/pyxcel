"""Define a set of tests for the overview API."""

# pylint: disable=wildcard-import,redefined-outer-name,unused-wildcard-import

import json

import pytest
import requests_mock

import pyxcel
from pyxcel.const import XCEL_API_BASE_URL
from tests.fixtures.general import *  # noqa
from tests.fixtures.overview import *  # noqa


def test_overview_get(overview_get_200, password, username):
    """Test getting the account overview."""
    with requests_mock.Mocker() as mock:
        mock.post('{0}/j_spring_security_check'.format(XCEL_API_BASE_URL))
        mock.get('{0}/user/login.req'.format(XCEL_API_BASE_URL))
        mock.get(
            '{0}/user/getJsonAccountOverview.req'.format(XCEL_API_BASE_URL),
            text=json.dumps(overview_get_200))

        client = pyxcel.Client(username, password)
        assert client.overview.get() == overview_get_200
