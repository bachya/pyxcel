"""Define tests for the client."""

import pytest


@pytest.fixture(scope='session')
def password():
    """Define a password."""
    return 'password'


@pytest.fixture(scope='session')
def premise_id():
    """Define a premise ID."""
    return '1234567890'


@pytest.fixture(scope='session')
def username():
    """Define a username."""
    return 'username'
