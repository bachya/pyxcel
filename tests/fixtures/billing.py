"""Define tests for the client."""

import pytest


@pytest.fixture(scope='session')
def billing_get_200():
    """Define successful bills response."""
    return {
        "avgMonthlyPayment":
        None,
        "csr":
        False,
        "currentBalance":
        0.0,
        "currentCharges": [{
            "amount": 49.76,
            "name": "Electricity Service"
        }, {
            "amount": 45.08,
            "name": "Natural Gas Service"
        }, {
            "amount": 6.430000000000001,
            "name": "Taxes \u0026 Fees"
        }],
        "disabled":
        False,
        "dueDate":
        "2017-12-12T12:00:00-07:00",
        "ebillEnrolled":
        True,
        "hasManySchedPayments":
        0,
        "hasScheduledPayment":
        None,
        "isRapOrAutoPay":
        True,
        "lastPaymentAmt":
        101.2699966430664,
        "lastPaymentDate":
        "Tue Dec 12 00:00:00 UTC 2017",
        "lastStmtDate":
        "2017-11-21T12:00:00-07:00",
        "lastStmtNum":
        1234567890,
        "nextPaymentDate":
        "",
        "nextSchedStatus":
        None,
        "nextScheduledPaymentAmount":
        None,
        "nextScheduledPaymentDate":
        None,
        "nickname":
        "JIMMY DEAN",
        "number":
        "1234567890",
        "overdue":
        False,
        "paymentStatus":
        "NO_BAL",
        "payments": []
    }
