"""Define a set of base API tests."""

# pylint: disable=wildcard-import,redefined-outer-name,unused-wildcard-import

import pytest
import requests_mock

import pyxcel
from pyxcel.const import XCEL_API_BASE_URL
from tests.fixtures.client import *  # noqa


def test_api_exception(password, username):
    """Test what happens some HTTP error occurs."""
    with requests_mock.Mocker() as mock:
        mock.post(
            '{0}/j_spring_security_check'.format(XCEL_API_BASE_URL),
            status_code=404)

        with pytest.raises(pyxcel.exceptions.HTTPError) as exc_info:
            pyxcel.Client(username, password)
            assert '404' in str(exc_info)
