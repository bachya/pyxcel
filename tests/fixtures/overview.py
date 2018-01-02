"""Define tests for the overview module."""

import pytest


@pytest.fixture(scope='session')
def overview_get_200():
    """Define successful account overview response."""
    return {
        "alert":
        None,
        "currentBalance":
        0.0,
        "disabled":
        False,
        "dueDate":
        "2017-12-12T12:00:00-07:00",
        "hasManySchedPayments":
        0,
        "lastPaymentAmt":
        101.27,
        "lastPaymentDate":
        "2017-12-12T12:00:00-07:00",
        "lastStatementDate":
        "2017-11-21T12:00:00-07:00",
        "nextSchedPaymentAmt":
        None,
        "nextSchedPaymentDate":
        None,
        "nextSchedStatus":
        None,
        "nickname":
        "1234567890",
        "number":
        "1234567890",
        "overdue":
        False,
        "paymentStatus":
        "NO_BAL",
        "premises": [{
            "addressLine1":
            "1234 MAIN STREET",
            "addressLine2":
            "",
            "addressLine3":
            "AKRON, OH 12345",
            "comparisons": [{
                "efficientNeighbors": "723",
                "name": "Energy",
                "you": "896",
                "unitLabel": "Units",
                "allNeighbors": "1045"
            }, {
                "efficientNeighbors": "44",
                "name": "Natural Gas",
                "you": "64",
                "unitLabel": "Therms",
                "allNeighbors": "64"
            }, {
                "efficientNeighbors": "311",
                "name": "Electricity",
                "you": "444",
                "unitLabel": "kWh",
                "allNeighbors": "592"
            }],
            "cost":
            101.27,
            "grade":
            "A+",
            "number":
            "1234567890",
            "programs": {
                "windSource": False,
                "solarReward": True
            }
        }],
        "programs": {
            "eBill": True,
            "priceOption": True,
            "averageMonthlyPayment": True,
            "autoPay": True
        },
        "scheduledPayments": [],
        "trendData": {
            "series": [{
                "data": [
                    0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
                    "143.92"
                ],
                "label":
                "2015"
            }, {
                "data": [
                    "155.17", "122.04", "246.67", "98.30", "96.98", "111.22",
                    "168.06", "133.79", "92.15", "75.52", "81.48", "138.56"
                ],
                "label":
                "2016"
            }, {
                "data": [
                    "163.47", "112.71", "100.31", "76.41", "84.07", "108.17",
                    "136.95", "102.36", "103.01", "85.50", "101.27", 0.0
                ],
                "label":
                "2017"
            }],
            "labels": [
                "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep",
                "Oct", "Nov", "Dec"
            ]
        }
    }
