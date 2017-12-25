"""Define a set of base API tests."""

# pylint: disable=wildcard-import,redefined-outer-name,unused-wildcard-import

import json

import pytest
import requests_mock

import pyxcel
from pyxcel.const import XCEL_API_BASE_URL
from tests.fixtures.client import *  # noqa


def test_account_overview(overview_response_200, password, username):
    """Test getting the account overview."""
    with requests_mock.Mocker() as mock:
        mock.post('{0}/j_spring_security_check'.format(XCEL_API_BASE_URL))
        mock.get('{0}/user/login.req'.format(XCEL_API_BASE_URL))
        mock.get(
            '{0}/user/getJsonAccountOverview.req'.format(XCEL_API_BASE_URL),
            text=json.dumps(overview_response_200))

        client = pyxcel.Client(username, password)
        assert client.get_account_overview() == overview_response_200


def test_bills(bills_response_200, password, username):
    """Test getting bill information."""
    with requests_mock.Mocker() as mock:
        mock.post('{0}/j_spring_security_check'.format(XCEL_API_BASE_URL))
        mock.get('{0}/user/login.req'.format(XCEL_API_BASE_URL))
        mock.get(
            '{0}/user/getMyBillsAccounts.req'.format(XCEL_API_BASE_URL),
            text=json.dumps(bills_response_200))

        client = pyxcel.Client(username, password)
        assert client.get_bills() == bills_response_200


def test_usages(password, premise_id, usages_response_200, username):
    """Test getting usage information."""
    with requests_mock.Mocker() as mock:
        mock.post('{0}/j_spring_security_check'.format(XCEL_API_BASE_URL))
        mock.get('{0}/user/login.req'.format(XCEL_API_BASE_URL))
        mock.get(
            '{0}/user/getJsonAccountUsages.req'.format(XCEL_API_BASE_URL),
            text=json.dumps(usages_response_200))

        client = pyxcel.Client(username, password)
        assert client.get_usages(premise_id) == usages_response_200
