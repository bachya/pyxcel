"""Define tests for the client."""

import pytest


@pytest.fixture(scope='session')
def bills_response_200():
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


@pytest.fixture(scope='session')
def overview_response_200():
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


@pytest.fixture(scope='session')
def password():
    """Define a password."""
    return 'password'


@pytest.fixture(scope='session')
def premise_id():
    """Define a premise ID."""
    return '1234567890'


@pytest.fixture(scope='session')
def usages_response_200():
    """Define successful usages response."""
    return {
        "accountType":
        "RESIDENTIAL",
        "addressLine1":
        "1234 MAIN STREET",
        "addressLine2":
        "",
        "addressLine3":
        "AKRON, OHIO 12345",
        "complex":
        True,
        "current":
        True,
        "data": {
            "services": [{
                "name":
                "ELECTRICITY-1",
                "data": [{
                    "series": [{
                        "data": [
                            673.0, 456.0, 445.0, 371.0, 426.0, 691.0, 910.0,
                            684.0, 681.0, 452.0, 444.0, None
                        ],
                        "label":
                        "2017"
                    }, {
                        "data": [
                            669.0, 578.0, None, 543.0, 572.0, 744.0, 1089.0,
                            855.0, 576.0, 414.0, 386.0, 558.0
                        ],
                        "label":
                        "2016"
                    }, {
                        "data": [
                            None, None, None, None, None, None, None, None,
                            None, None, None, None
                        ],
                        "label":
                        "2015"
                    }],
                    "name":
                    "Total Usage",
                    "label":
                    "Total Usage (kWh)"
                }, {
                    "series": [{
                        "data": [
                            33.0, 44.0, 48.0, 50.0, 53.0, 67.0, 75.0, 70.0,
                            70.0, 52.0, 46.0, None
                        ],
                        "label":
                        "2017"
                    }, {
                        "data": [
                            31.0, 40.0, None, 49.0, 51.0, 67.0, 75.0, 73.0,
                            68.0, 58.0, 55.0, 32.0
                        ],
                        "label":
                        "2016"
                    }, {
                        "data": [
                            None, None, None, None, None, None, None, None,
                            None, None, None, None
                        ],
                        "label":
                        "2015"
                    }],
                    "name":
                    "Average Temperature",
                    "label":
                    "Average Temperature (° F)"
                }, {
                    "series": [{
                        "data": [
                            673.0, 456.0, 445.0, 371.0, 426.0, 691.0, 910.0,
                            684.0, 681.0, 452.0, 444.0, None
                        ],
                        "label":
                        "2017"
                    }, {
                        "data": [
                            669.0, 578.0, None, 543.0, 572.0, 744.0, 1089.0,
                            855.0, 576.0, 414.0, 386.0, 558.0
                        ],
                        "label":
                        "2016"
                    }, {
                        "data": [
                            None, None, None, None, None, None, None, None,
                            None, None, None, None
                        ],
                        "label":
                        "2015"
                    }],
                    "name":
                    "Total Energy",
                    "label":
                    "Total Energy (kWh)"
                }, {
                    "series": [{
                        "data": [
                            72.64, 50.56, 49.47, 41.84, 47.17, 80.11, 110.0,
                            78.53, 78.21, 49.98, 49.76, None
                        ],
                        "label":
                        "2017"
                    }, {
                        "data": [
                            69.08, 59.83, None, 58.28, 61.16, 86.83, 138.51,
                            107.12, 66.71, 48.55, 46.16, 63.24
                        ],
                        "label":
                        "2016"
                    }, {
                        "data": [
                            None, None, None, None, None, None, None, None,
                            None, None, None, None
                        ],
                        "label":
                        "2015"
                    }],
                    "name":
                    "Electric Charges",
                    "label":
                    "Electric Charges ($)"
                }, {
                    "series": [{
                        "data": [
                            77.55, 53.97, 52.8, 44.66, 50.35, 85.52, 117.43,
                            83.85, 83.5, 53.36, 53.13, None
                        ],
                        "label":
                        "2017"
                    }, {
                        "data": [
                            73.75, 63.88, None, 62.22, 65.3, 92.7, 147.87,
                            114.36, 71.21, 51.82, 49.27, 67.5
                        ],
                        "label":
                        "2016"
                    }, {
                        "data": [
                            None, None, None, None, None, None, None, None,
                            None, None, None, None
                        ],
                        "label":
                        "2015"
                    }],
                    "name":
                    "Total Electric Charges",
                    "label":
                    "Total Electric Charges ($)"
                }, {
                    "series": [{
                        "data": [
                            2.22, 1.86, 1.65, 1.54, 1.74, 2.67, 4.05, 2.89,
                            2.78, 1.72, 1.83, None
                        ],
                        "label":
                        "2017"
                    }, {
                        "data": [
                            2.17, 2.13, None, 2.22, 2.18, 3.2, 4.48, 3.94,
                            2.46, 1.62, 1.7, 2.25
                        ],
                        "label":
                        "2016"
                    }, {
                        "data": [
                            None, None, None, None, None, None, None, None,
                            None, None, None, None
                        ],
                        "label":
                        "2015"
                    }],
                    "name":
                    "Total Electric Charges / Day",
                    "label":
                    "Total Electric Charges / Day ($)"
                }, {
                    "series": [{
                        "data": [
                            None, None, None, None, None, None, None, None,
                            None, None, None, None
                        ],
                        "label":
                        "2017"
                    }, {
                        "data": [
                            None, None, None, None, None, None, None, None,
                            None, None, None, None
                        ],
                        "label":
                        "2016"
                    }, {
                        "data": [
                            None, None, None, None, None, None, None, None,
                            None, None, None, None
                        ],
                        "label":
                        "2015"
                    }],
                    "name":
                    "Cooling Degree Days",
                    "label":
                    "Cooling Degree Days"
                }, {
                    "series": [{
                        "data": [
                            None, None, None, None, None, None, None, None,
                            None, None, None, None
                        ],
                        "label":
                        "2017"
                    }, {
                        "data": [
                            None, None, None, None, None, None, None, None,
                            None, None, None, None
                        ],
                        "label":
                        "2016"
                    }, {
                        "data": [
                            None, None, None, None, None, None, None, None,
                            None, None, None, None
                        ],
                        "label":
                        "2015"
                    }],
                    "name":
                    "Heating Degree Days",
                    "label":
                    "Heating Degree Days"
                }]
            }, {
                "name":
                "NATURAL GAS-1",
                "data": [{
                    "series": [{
                        "data": [
                            None, 79.0, 59.0, 34.0, None, 16.0, 10.0, None,
                            10.0, 34.0, 64.0, None
                        ],
                        "label":
                        "2017"
                    }, {
                        "data": [
                            137.0, None, None, 52.0, 43.0, None, 12.0, 10.0,
                            None, 18.0, 35.0, None
                        ],
                        "label":
                        "2016"
                    }, {
                        "data": [
                            None, None, None, None, None, None, None, None,
                            None, None, None, None
                        ],
                        "label":
                        "2015"
                    }],
                    "name":
                    "Total Usage",
                    "label":
                    "Total Usage (therms)"
                }, {
                    "series": [{
                        "data": [
                            33.0, 44.0, 48.0, 50.0, 53.0, 67.0, 75.0, 70.0,
                            70.0, 52.0, 46.0, None
                        ],
                        "label":
                        "2017"
                    }, {
                        "data": [
                            31.0, 40.0, None, 49.0, 51.0, 67.0, 75.0, 73.0,
                            68.0, 58.0, 55.0, 32.0
                        ],
                        "label":
                        "2016"
                    }, {
                        "data": [
                            None, None, None, None, None, None, None, None,
                            None, None, None, None
                        ],
                        "label":
                        "2015"
                    }],
                    "name":
                    "Average Temperature",
                    "label":
                    "Average Temperature (° F)"
                }, {
                    "series": [{
                        "data": [
                            80.49, 55.02, 44.5, 29.74, 31.58, 21.22, 18.28,
                            17.34, 18.27, 30.1, 45.08, None
                        ],
                        "label":
                        "2017"
                    }, {
                        "data": [
                            76.26, 54.47, None, 33.8, 29.68, 17.35, 18.91,
                            18.2, 19.61, 22.2, 30.18, 66.56
                        ],
                        "label":
                        "2016"
                    }, {
                        "data": [
                            None, None, None, None, None, None, None, None,
                            None, None, None, None
                        ],
                        "label":
                        "2015"
                    }],
                    "name":
                    "Gas Charges",
                    "label":
                    "Gas Charges ($)"
                }, {
                    "series": [{
                        "data": [
                            85.92, 58.74, 47.51, 31.75, 33.72, 22.65, 19.52,
                            18.51, 19.51, 32.14, 48.14, None
                        ],
                        "label":
                        "2017"
                    }, {
                        "data": [
                            81.42, 58.16, None, 36.08, 31.68, 18.52, 20.19,
                            19.43, 20.94, 23.7, 32.21, 71.06
                        ],
                        "label":
                        "2016"
                    }, {
                        "data": [
                            None, None, None, None, None, None, None, None,
                            None, None, None, None
                        ],
                        "label":
                        "2015"
                    }],
                    "name":
                    "Total Gas Charges",
                    "label":
                    "Total Gas Charges ($)"
                }, {
                    "series": [{
                        "data": [
                            2.45, 2.03, 1.48, 1.09, 1.16, 0.71, 0.67, 0.64,
                            0.65, 1.04, 1.66, None
                        ],
                        "label":
                        "2017"
                    }, {
                        "data": [
                            2.39, 1.94, None, 1.29, 1.06, 0.64, 0.61, 0.67,
                            0.72, 0.74, 1.11, 2.37
                        ],
                        "label":
                        "2016"
                    }, {
                        "data": [
                            None, None, None, None, None, None, None, None,
                            None, None, None, None
                        ],
                        "label":
                        "2015"
                    }],
                    "name":
                    "Total Gas Charges / Day",
                    "label":
                    "Total Gas Charges / Day ($)"
                }, {
                    "series": [{
                        "data": [
                            None, None, None, None, None, None, None, None,
                            None, None, None, None
                        ],
                        "label":
                        "2017"
                    }, {
                        "data": [
                            None, None, None, None, None, None, None, None,
                            None, None, None, None
                        ],
                        "label":
                        "2016"
                    }, {
                        "data": [
                            None, None, None, None, None, None, None, None,
                            None, None, None, None
                        ],
                        "label":
                        "2015"
                    }],
                    "name":
                    "Heating Degree Days",
                    "label":
                    "Heating Degree Days"
                }]
            }],
            "labels": [
                "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep",
                "Oct", "Nov", "Dec"
            ]
        },
        "endDate":
        None,
        "greenEnergy": [],
        "intervalList": {},
        "number":
        "304502308",
        "overview": [{
            "cost": 53.13,
            "emissions": 594.072,
            "type": "ELECTRICITY-1",
            "usage": {
                "amount": 444.0,
                "unit": "kWh"
            }
        }, {
            "cost": 48.14,
            "emissions": 748.8,
            "type": "NATURAL GAS-1",
            "usage": {
                "amount": 64.0,
                "unit": "Therms"
            }
        }],
        "pilotType":
        "tou",
        "services": [{
            "reads": [{
                "billingDays":
                29,
                "details": [{
                    "amount": 444.0,
                    "unit": "kWh",
                    "label": "Total Energy"
                }, {
                    "amount": 49.76,
                    "unit": "$",
                    "label": "Electric Charges"
                }, {
                    "amount": 53.13,
                    "unit": "$",
                    "label": "Total Electric Charges"
                }, {
                    "amount": 1.83,
                    "unit": "$",
                    "label": "Total Electric Charges / Day"
                }, {
                    "amount": 2.23,
                    "unit": "$",
                    "label": "CACJA"
                }, {
                    "amount": 24.25,
                    "unit": "$",
                    "label": "Non-Summer"
                }, {
                    "amount": 2.06,
                    "unit": "$",
                    "label": "Purch Cap Cost Adj"
                }, {
                    "amount": 0.48,
                    "unit": "$",
                    "label": "Trans Cost Adj"
                }, {
                    "amount": 0.04,
                    "unit": "$",
                    "label": "GRSA"
                }, {
                    "amount": 0.67,
                    "unit": "$",
                    "label": "Demand Side Mgmt Cost"
                }, {
                    "amount": 13.67,
                    "unit": "$",
                    "label": "Elec Commodity Adj"
                }, {
                    "amount": 0.97,
                    "unit": "$",
                    "label": "Renew. Energy Std Adj"
                }, {
                    "amount": 5.39,
                    "unit": "$",
                    "label": "Service \u0026 Facility"
                }, {
                    "amount": 46.0,
                    "unit": "° F",
                    "label": "Average Temperature"
                }, {
                    "amount": 0.0,
                    "unit": "",
                    "label": "Cooling Degree Days"
                }, {
                    "amount": 0.0,
                    "unit": "",
                    "label": "Heating Degree Days"
                }],
                "lastReadDate":
                "November 21, 2017",
                "method":
                "Actual",
                "usage": {
                    "amount": 444.0,
                    "unit": ""
                }
            }, {
                "billingDays":
                31,
                "details": [{
                    "amount": 452.0,
                    "unit": "kWh",
                    "label": "Total Energy"
                }, {
                    "amount": 49.98,
                    "unit": "$",
                    "label": "Electric Charges"
                }, {
                    "amount": 53.36,
                    "unit": "$",
                    "label": "Total Electric Charges"
                }, {
                    "amount": 1.72,
                    "unit": "$",
                    "label": "Total Electric Charges / Day"
                }, {
                    "amount": 0.98,
                    "unit": "$",
                    "label": "Renew. Energy Std Adj"
                }, {
                    "amount": 3.02,
                    "unit": "$",
                    "label": "Elec Commodity Adj"
                }, {
                    "amount": 5.39,
                    "unit": "$",
                    "label": "Service \u0026 Facility"
                }, {
                    "amount": 0.68,
                    "unit": "$",
                    "label": "Demand Side Mgmt Cost"
                }, {
                    "amount": 18.31,
                    "unit": "$",
                    "label": "Non-Summer"
                }, {
                    "amount": 6.37,
                    "unit": "$",
                    "label": "Summer Tier 1*"
                }, {
                    "amount": 10.33,
                    "unit": "$",
                    "label": "Elec Commodity Adj"
                }, {
                    "amount": 0.49,
                    "unit": "$",
                    "label": "Trans Cost Adj"
                }, {
                    "amount": 2.1,
                    "unit": "$",
                    "label": "Purch Cap Cost Adj"
                }, {
                    "amount": 0.04,
                    "unit": "$",
                    "label": "GRSA"
                }, {
                    "amount": 2.27,
                    "unit": "$",
                    "label": "CACJA"
                }, {
                    "amount": 52.0,
                    "unit": "° F",
                    "label": "Average Temperature"
                }, {
                    "amount": 0.0,
                    "unit": "",
                    "label": "Cooling Degree Days"
                }, {
                    "amount": 0.0,
                    "unit": "",
                    "label": "Heating Degree Days"
                }],
                "lastReadDate":
                "October 23, 2017",
                "method":
                "Actual",
                "usage": {
                    "amount": 452.0,
                    "unit": ""
                }
            }, {
                "billingDays":
                30,
                "details": [{
                    "amount": 681.0,
                    "unit": "kWh",
                    "label": "Total Energy"
                }, {
                    "amount": 78.21,
                    "unit": "$",
                    "label": "Electric Charges"
                }, {
                    "amount": 83.5,
                    "unit": "$",
                    "label": "Total Electric Charges"
                }, {
                    "amount": 2.78,
                    "unit": "$",
                    "label": "Total Electric Charges / Day"
                }, {
                    "amount": 1.03,
                    "unit": "$",
                    "label": "Demand Side Mgmt Cost"
                }, {
                    "amount": 1.52,
                    "unit": "$",
                    "label": "Renew. Energy Std Adj"
                }, {
                    "amount": 17.64,
                    "unit": "$",
                    "label": "Elec Commodity Adj"
                }, {
                    "amount": 5.39,
                    "unit": "$",
                    "label": "Service \u0026 Facility"
                }, {
                    "amount": 27.31,
                    "unit": "$",
                    "label": "Summer Tier 1*"
                }, {
                    "amount": 17.92,
                    "unit": "$",
                    "label": "Summer Tier 2*"
                }, {
                    "amount": 3.43,
                    "unit": "$",
                    "label": "CACJA"
                }, {
                    "amount": 3.17,
                    "unit": "$",
                    "label": "Purch Cap Cost Adj"
                }, {
                    "amount": 0.74,
                    "unit": "$",
                    "label": "Trans Cost Adj"
                }, {
                    "amount": 0.06,
                    "unit": "$",
                    "label": "GRSA"
                }, {
                    "amount": 70.0,
                    "unit": "° F",
                    "label": "Average Temperature"
                }, {
                    "amount": 0.0,
                    "unit": "",
                    "label": "Cooling Degree Days"
                }, {
                    "amount": 0.0,
                    "unit": "",
                    "label": "Heating Degree Days"
                }],
                "lastReadDate":
                "September 22, 2017",
                "method":
                "Actual",
                "usage": {
                    "amount": 681.0,
                    "unit": ""
                }
            }, {
                "billingDays":
                29,
                "details": [{
                    "amount": 684.0,
                    "unit": "kWh",
                    "label": "Total Energy"
                }, {
                    "amount": 78.53,
                    "unit": "$",
                    "label": "Electric Charges"
                }, {
                    "amount": 83.85,
                    "unit": "$",
                    "label": "Total Electric Charges"
                }, {
                    "amount": 2.89,
                    "unit": "$",
                    "label": "Total Electric Charges / Day"
                }, {
                    "amount": 5.39,
                    "unit": "$",
                    "label": "Service \u0026 Facility"
                }, {
                    "amount": 27.31,
                    "unit": "$",
                    "label": "Summer Tier 1*"
                }, {
                    "amount": 18.22,
                    "unit": "$",
                    "label": "Summer Tier 2*"
                }, {
                    "amount": 3.44,
                    "unit": "$",
                    "label": "CACJA"
                }, {
                    "amount": 3.18,
                    "unit": "$",
                    "label": "Purch Cap Cost Adj"
                }, {
                    "amount": 0.75,
                    "unit": "$",
                    "label": "Trans Cost Adj"
                }, {
                    "amount": -0.05,
                    "unit": "$",
                    "label": "GRSA"
                }, {
                    "amount": 1.03,
                    "unit": "$",
                    "label": "Demand Side Mgmt Cost"
                }, {
                    "amount": 1.54,
                    "unit": "$",
                    "label": "Renew. Energy Std Adj"
                }, {
                    "amount": 17.72,
                    "unit": "$",
                    "label": "Elec Commodity Adj"
                }, {
                    "amount": 70.0,
                    "unit": "° F",
                    "label": "Average Temperature"
                }, {
                    "amount": 0.0,
                    "unit": "",
                    "label": "Cooling Degree Days"
                }, {
                    "amount": 0.0,
                    "unit": "",
                    "label": "Heating Degree Days"
                }],
                "lastReadDate":
                "August 23, 2017",
                "method":
                "Actual",
                "usage": {
                    "amount": 684.0,
                    "unit": ""
                }
            }, {
                "billingDays":
                29,
                "details": [{
                    "amount": 910.0,
                    "unit": "kWh",
                    "label": "Total Energy"
                }, {
                    "amount": 110.0,
                    "unit": "$",
                    "label": "Electric Charges"
                }, {
                    "amount": 117.43,
                    "unit": "$",
                    "label": "Total Electric Charges"
                }, {
                    "amount": 4.05,
                    "unit": "$",
                    "label": "Total Electric Charges / Day"
                }, {
                    "amount": 27.31,
                    "unit": "$",
                    "label": "Summer Tier 1*"
                }, {
                    "amount": 40.6,
                    "unit": "$",
                    "label": "Summer Tier 2*"
                }, {
                    "amount": 4.23,
                    "unit": "$",
                    "label": "Purch Cap Cost Adj"
                }, {
                    "amount": 20.33,
                    "unit": "$",
                    "label": "Elec Commodity Adj"
                }, {
                    "amount": 4.58,
                    "unit": "$",
                    "label": "CACJA"
                }, {
                    "amount": 1.18,
                    "unit": "$",
                    "label": "Demand Side Mgmt Cost"
                }, {
                    "amount": -0.69,
                    "unit": "$",
                    "label": "GRSA"
                }, {
                    "amount": 0.99,
                    "unit": "$",
                    "label": "Trans Cost Adj"
                }, {
                    "amount": 2.16,
                    "unit": "$",
                    "label": "Renew. Energy Std Adj"
                }, {
                    "amount": 3.75,
                    "unit": "$",
                    "label": "Elec Commodity Adj"
                }, {
                    "amount": 5.39,
                    "unit": "$",
                    "label": "Service \u0026 Facility"
                }, {
                    "amount": 0.17,
                    "unit": "$",
                    "label": "Demand Side Mgmt Cost"
                }, {
                    "amount": 75.0,
                    "unit": "° F",
                    "label": "Average Temperature"
                }, {
                    "amount": 0.0,
                    "unit": "",
                    "label": "Cooling Degree Days"
                }, {
                    "amount": 0.0,
                    "unit": "",
                    "label": "Heating Degree Days"
                }],
                "lastReadDate":
                "July 25, 2017",
                "method":
                "Actual",
                "usage": {
                    "amount": 910.0,
                    "unit": ""
                }
            }, {
                "billingDays":
                32,
                "details": [{
                    "amount": 691.0,
                    "unit": "kWh",
                    "label": "Total Energy"
                }, {
                    "amount": 80.11,
                    "unit": "$",
                    "label": "Electric Charges"
                }, {
                    "amount": 85.52,
                    "unit": "$",
                    "label": "Total Electric Charges"
                }, {
                    "amount": 2.67,
                    "unit": "$",
                    "label": "Total Electric Charges / Day"
                }, {
                    "amount": 0.91,
                    "unit": "$",
                    "label": "Demand Side Mgmt Cost"
                }, {
                    "amount": 1.57,
                    "unit": "$",
                    "label": "Renew. Energy Std Adj"
                }, {
                    "amount": 20.63,
                    "unit": "$",
                    "label": "Elec Commodity Adj"
                }, {
                    "amount": 5.39,
                    "unit": "$",
                    "label": "Service \u0026 Facility"
                }, {
                    "amount": 7.08,
                    "unit": "$",
                    "label": "Non-Summer"
                }, {
                    "amount": 22.19,
                    "unit": "$",
                    "label": "Summer Tier 1*"
                }, {
                    "amount": 15.37,
                    "unit": "$",
                    "label": "Summer Tier 2*"
                }, {
                    "amount": 3.48,
                    "unit": "$",
                    "label": "CACJA"
                }, {
                    "amount": 3.21,
                    "unit": "$",
                    "label": "Purch Cap Cost Adj"
                }, {
                    "amount": 0.75,
                    "unit": "$",
                    "label": "Trans Cost Adj"
                }, {
                    "amount": -0.47,
                    "unit": "$",
                    "label": "GRSA"
                }, {
                    "amount": 67.0,
                    "unit": "° F",
                    "label": "Average Temperature"
                }, {
                    "amount": 0.0,
                    "unit": "",
                    "label": "Cooling Degree Days"
                }, {
                    "amount": 0.0,
                    "unit": "",
                    "label": "Heating Degree Days"
                }],
                "lastReadDate":
                "June 26, 2017",
                "method":
                "Actual",
                "usage": {
                    "amount": 691.0,
                    "unit": ""
                }
            }, {
                "billingDays":
                29,
                "details": [{
                    "amount": 426.0,
                    "unit": "kWh",
                    "label": "Total Energy"
                }, {
                    "amount": 47.17,
                    "unit": "$",
                    "label": "Electric Charges"
                }, {
                    "amount": 50.35,
                    "unit": "$",
                    "label": "Total Electric Charges"
                }, {
                    "amount": 1.74,
                    "unit": "$",
                    "label": "Total Electric Charges / Day"
                }, {
                    "amount": 23.26,
                    "unit": "$",
                    "label": "Non-Summer"
                }, {
                    "amount": 2.14,
                    "unit": "$",
                    "label": "CACJA"
                }, {
                    "amount": 1.98,
                    "unit": "$",
                    "label": "Purch Cap Cost Adj"
                }, {
                    "amount": -0.27,
                    "unit": "$",
                    "label": "GRSA"
                }, {
                    "amount": 0.46,
                    "unit": "$",
                    "label": "Trans Cost Adj"
                }, {
                    "amount": 0.56,
                    "unit": "$",
                    "label": "Demand Side Mgmt Cost"
                }, {
                    "amount": 0.93,
                    "unit": "$",
                    "label": "Renew. Energy Std Adj"
                }, {
                    "amount": 12.72,
                    "unit": "$",
                    "label": "Elec Commodity Adj"
                }, {
                    "amount": 5.39,
                    "unit": "$",
                    "label": "Service \u0026 Facility"
                }, {
                    "amount": 53.0,
                    "unit": "° F",
                    "label": "Average Temperature"
                }, {
                    "amount": 0.0,
                    "unit": "",
                    "label": "Cooling Degree Days"
                }, {
                    "amount": 0.0,
                    "unit": "",
                    "label": "Heating Degree Days"
                }],
                "lastReadDate":
                "May 25, 2017",
                "method":
                "Actual",
                "usage": {
                    "amount": 426.0,
                    "unit": ""
                }
            }, {
                "billingDays":
                29,
                "details": [{
                    "amount": 371.0,
                    "unit": "kWh",
                    "label": "Total Energy"
                }, {
                    "amount": 41.84,
                    "unit": "$",
                    "label": "Electric Charges"
                }, {
                    "amount": 44.66,
                    "unit": "$",
                    "label": "Total Electric Charges"
                }, {
                    "amount": 1.54,
                    "unit": "$",
                    "label": "Total Electric Charges / Day"
                }, {
                    "amount": 0.83,
                    "unit": "$",
                    "label": "Renew. Energy Std Adj"
                }, {
                    "amount": 0.49,
                    "unit": "$",
                    "label": "Demand Side Mgmt Cost"
                }, {
                    "amount": 5.39,
                    "unit": "$",
                    "label": "Service \u0026 Facility"
                }, {
                    "amount": 1.18,
                    "unit": "$",
                    "label": "Elec Commodity Adj"
                }, {
                    "amount": 20.26,
                    "unit": "$",
                    "label": "Non-Summer"
                }, {
                    "amount": 9.93,
                    "unit": "$",
                    "label": "Elec Commodity Adj"
                }, {
                    "amount": 0.4,
                    "unit": "$",
                    "label": "Trans Cost Adj"
                }, {
                    "amount": -0.24,
                    "unit": "$",
                    "label": "GRSA"
                }, {
                    "amount": 1.73,
                    "unit": "$",
                    "label": "Purch Cap Cost Adj"
                }, {
                    "amount": 1.87,
                    "unit": "$",
                    "label": "CACJA"
                }, {
                    "amount": 50.0,
                    "unit": "° F",
                    "label": "Average Temperature"
                }, {
                    "amount": 0.0,
                    "unit": "",
                    "label": "Cooling Degree Days"
                }, {
                    "amount": 0.0,
                    "unit": "",
                    "label": "Heating Degree Days"
                }],
                "lastReadDate":
                "April 26, 2017",
                "method":
                "Actual",
                "usage": {
                    "amount": 371.0,
                    "unit": ""
                }
            }, {
                "billingDays":
                32,
                "details": [{
                    "amount": 445.0,
                    "unit": "kWh",
                    "label": "Total Energy"
                }, {
                    "amount": 49.47,
                    "unit": "$",
                    "label": "Electric Charges"
                }, {
                    "amount": 52.8,
                    "unit": "$",
                    "label": "Total Electric Charges"
                }, {
                    "amount": 1.65,
                    "unit": "$",
                    "label": "Total Electric Charges / Day"
                }, {
                    "amount": 24.3,
                    "unit": "$",
                    "label": "Non-Summer"
                }, {
                    "amount": 2.07,
                    "unit": "$",
                    "label": "Purch Cap Cost Adj"
                }, {
                    "amount": 2.24,
                    "unit": "$",
                    "label": "CACJA"
                }, {
                    "amount": 0.49,
                    "unit": "$",
                    "label": "Trans Cost Adj"
                }, {
                    "amount": -0.28,
                    "unit": "$",
                    "label": "GRSA"
                }, {
                    "amount": 0.59,
                    "unit": "$",
                    "label": "Demand Side Mgmt Cost"
                }, {
                    "amount": 0.97,
                    "unit": "$",
                    "label": "Renew. Energy Std Adj"
                }, {
                    "amount": 13.7,
                    "unit": "$",
                    "label": "Elec Commodity Adj"
                }, {
                    "amount": 5.39,
                    "unit": "$",
                    "label": "Service \u0026 Facility"
                }, {
                    "amount": 48.0,
                    "unit": "° F",
                    "label": "Average Temperature"
                }, {
                    "amount": 0.0,
                    "unit": "",
                    "label": "Cooling Degree Days"
                }, {
                    "amount": 0.0,
                    "unit": "",
                    "label": "Heating Degree Days"
                }],
                "lastReadDate":
                "March 28, 2017",
                "method":
                "Actual",
                "usage": {
                    "amount": 445.0,
                    "unit": ""
                }
            }, {
                "billingDays":
                29,
                "details": [{
                    "amount": 456.0,
                    "unit": "kWh",
                    "label": "Total Energy"
                }, {
                    "amount": 50.56,
                    "unit": "$",
                    "label": "Electric Charges"
                }, {
                    "amount": 53.97,
                    "unit": "$",
                    "label": "Total Electric Charges"
                }, {
                    "amount": 1.86,
                    "unit": "$",
                    "label": "Total Electric Charges / Day"
                }, {
                    "amount": 0.6,
                    "unit": "$",
                    "label": "Demand Side Mgmt Cost"
                }, {
                    "amount": 1.0,
                    "unit": "$",
                    "label": "Renew. Energy Std Adj"
                }, {
                    "amount": 14.04,
                    "unit": "$",
                    "label": "Elec Commodity Adj"
                }, {
                    "amount": 5.39,
                    "unit": "$",
                    "label": "Service \u0026 Facility"
                }, {
                    "amount": 2.29,
                    "unit": "$",
                    "label": "CACJA"
                }, {
                    "amount": 24.9,
                    "unit": "$",
                    "label": "Non-Summer"
                }, {
                    "amount": 2.12,
                    "unit": "$",
                    "label": "Purch Cap Cost Adj"
                }, {
                    "amount": -0.28,
                    "unit": "$",
                    "label": "GRSA"
                }, {
                    "amount": 0.5,
                    "unit": "$",
                    "label": "Trans Cost Adj"
                }, {
                    "amount": 44.0,
                    "unit": "° F",
                    "label": "Average Temperature"
                }, {
                    "amount": 0.0,
                    "unit": "",
                    "label": "Cooling Degree Days"
                }, {
                    "amount": 0.0,
                    "unit": "",
                    "label": "Heating Degree Days"
                }],
                "lastReadDate":
                "February 24, 2017",
                "method":
                "Actual",
                "usage": {
                    "amount": 456.0,
                    "unit": ""
                }
            }, {
                "billingDays":
                35,
                "details": [{
                    "amount": 673.0,
                    "unit": "kWh",
                    "label": "Total Energy"
                }, {
                    "amount": 72.64,
                    "unit": "$",
                    "label": "Electric Charges"
                }, {
                    "amount": 77.55,
                    "unit": "$",
                    "label": "Total Electric Charges"
                }, {
                    "amount": 2.22,
                    "unit": "$",
                    "label": "Total Electric Charges / Day"
                }, {
                    "amount": 0.66,
                    "unit": "$",
                    "label": "Demand Side Mgmt Cost"
                }, {
                    "amount": 2.51,
                    "unit": "$",
                    "label": "CACJA"
                }, {
                    "amount": 2.32,
                    "unit": "$",
                    "label": "Purch Cap Cost Adj"
                }, {
                    "amount": 5.88,
                    "unit": "$",
                    "label": "Elec Commodity Adj"
                }, {
                    "amount": 27.3,
                    "unit": "$",
                    "label": "Non-Summer"
                }, {
                    "amount": 7.97,
                    "unit": "$",
                    "label": "Non-Summer"
                }, {
                    "amount": 0.17,
                    "unit": "$",
                    "label": "Demand Side Mgmt Cost"
                }, {
                    "amount": 0.69,
                    "unit": "$",
                    "label": "CACJA"
                }, {
                    "amount": 0.98,
                    "unit": "$",
                    "label": "GRSA"
                }, {
                    "amount": 0.14,
                    "unit": "$",
                    "label": "Trans Cost Adj"
                }, {
                    "amount": 15.39,
                    "unit": "$",
                    "label": "Elec Commodity Adj"
                }, {
                    "amount": 0.54,
                    "unit": "$",
                    "label": "Trans Cost Adj"
                }, {
                    "amount": 0.95,
                    "unit": "$",
                    "label": "Purch Cap Cost Adj"
                }, {
                    "amount": 5.73,
                    "unit": "$",
                    "label": "Service \u0026 Facility"
                }, {
                    "amount": 1.41,
                    "unit": "$",
                    "label": "Renew. Energy Std Adj"
                }, {
                    "amount": 33.0,
                    "unit": "° F",
                    "label": "Average Temperature"
                }, {
                    "amount": 0.0,
                    "unit": "",
                    "label": "Cooling Degree Days"
                }, {
                    "amount": 0.0,
                    "unit": "",
                    "label": "Heating Degree Days"
                }],
                "lastReadDate":
                "January 26, 2017",
                "method":
                "Actual",
                "usage": {
                    "amount": 673.0,
                    "unit": ""
                }
            }, {
                "billingDays":
                30,
                "details": [{
                    "amount": 558.0,
                    "unit": "kWh",
                    "label": "Total Energy"
                }, {
                    "amount": 63.24,
                    "unit": "$",
                    "label": "Electric Charges"
                }, {
                    "amount": 67.5,
                    "unit": "$",
                    "label": "Total Electric Charges"
                }, {
                    "amount": 2.25,
                    "unit": "$",
                    "label": "Total Electric Charges / Day"
                }, {
                    "amount": 0.55,
                    "unit": "$",
                    "label": "Demand Side Mgmt Cost"
                }, {
                    "amount": 1.23,
                    "unit": "$",
                    "label": "Renew. Energy Std Adj"
                }, {
                    "amount": 18.95,
                    "unit": "$",
                    "label": "Elec Commodity Adj"
                }, {
                    "amount": 6.75,
                    "unit": "$",
                    "label": "Service \u0026 Facility"
                }, {
                    "amount": 25.69,
                    "unit": "$",
                    "label": "Non-Summer"
                }, {
                    "amount": 2.24,
                    "unit": "$",
                    "label": "CACJA"
                }, {
                    "amount": 3.07,
                    "unit": "$",
                    "label": "Purch Cap Cost Adj"
                }, {
                    "amount": 0.45,
                    "unit": "$",
                    "label": "Trans Cost Adj"
                }, {
                    "amount": 4.31,
                    "unit": "$",
                    "label": "GRSA"
                }, {
                    "amount": 32.0,
                    "unit": "° F",
                    "label": "Average Temperature"
                }, {
                    "amount": 0.0,
                    "unit": "",
                    "label": "Cooling Degree Days"
                }, {
                    "amount": 0.0,
                    "unit": "",
                    "label": "Heating Degree Days"
                }],
                "lastReadDate":
                "December 22, 2016",
                "method":
                "Actual",
                "usage": {
                    "amount": 558.0,
                    "unit": ""
                }
            }, {
                "billingDays":
                29,
                "details": [{
                    "amount": 386.0,
                    "unit": "kWh",
                    "label": "Total Energy"
                }, {
                    "amount": 46.16,
                    "unit": "$",
                    "label": "Electric Charges"
                }, {
                    "amount": 49.27,
                    "unit": "$",
                    "label": "Total Electric Charges"
                }, {
                    "amount": 1.7,
                    "unit": "$",
                    "label": "Total Electric Charges / Day"
                }, {
                    "amount": 6.75,
                    "unit": "$",
                    "label": "Service \u0026 Facility"
                }, {
                    "amount": 17.77,
                    "unit": "$",
                    "label": "Non-Summer"
                }, {
                    "amount": 1.55,
                    "unit": "$",
                    "label": "CACJA"
                }, {
                    "amount": 2.13,
                    "unit": "$",
                    "label": "Purch Cap Cost Adj"
                }, {
                    "amount": 3.25,
                    "unit": "$",
                    "label": "GRSA"
                }, {
                    "amount": 0.31,
                    "unit": "$",
                    "label": "Trans Cost Adj"
                }, {
                    "amount": 0.38,
                    "unit": "$",
                    "label": "Demand Side Mgmt Cost"
                }, {
                    "amount": 0.91,
                    "unit": "$",
                    "label": "Renew. Energy Std Adj"
                }, {
                    "amount": 13.11,
                    "unit": "$",
                    "label": "Elec Commodity Adj"
                }, {
                    "amount": 55.0,
                    "unit": "° F",
                    "label": "Average Temperature"
                }, {
                    "amount": 0.0,
                    "unit": "",
                    "label": "Cooling Degree Days"
                }, {
                    "amount": 0.0,
                    "unit": "",
                    "label": "Heating Degree Days"
                }],
                "lastReadDate":
                "November 22, 2016",
                "method":
                "Actual",
                "usage": {
                    "amount": 386.0,
                    "unit": ""
                }
            }, {
                "billingDays":
                32,
                "details": [{
                    "amount": 414.0,
                    "unit": "kWh",
                    "label": "Total Energy"
                }, {
                    "amount": 48.55,
                    "unit": "$",
                    "label": "Electric Charges"
                }, {
                    "amount": 51.82,
                    "unit": "$",
                    "label": "Total Electric Charges"
                }, {
                    "amount": 1.62,
                    "unit": "$",
                    "label": "Total Electric Charges / Day"
                }, {
                    "amount": 10.54,
                    "unit": "$",
                    "label": "Elec Commodity Adj"
                }, {
                    "amount": 14.3,
                    "unit": "$",
                    "label": "Non-Summer"
                }, {
                    "amount": 4.77,
                    "unit": "$",
                    "label": "Summer Tier 1*"
                }, {
                    "amount": 0.34,
                    "unit": "$",
                    "label": "Trans Cost Adj"
                }, {
                    "amount": 3.42,
                    "unit": "$",
                    "label": "GRSA"
                }, {
                    "amount": 2.28,
                    "unit": "$",
                    "label": "Purch Cap Cost Adj"
                }, {
                    "amount": 1.66,
                    "unit": "$",
                    "label": "CACJA"
                }, {
                    "amount": 0.95,
                    "unit": "$",
                    "label": "Renew. Energy Std Adj"
                }, {
                    "amount": 3.13,
                    "unit": "$",
                    "label": "Elec Commodity Adj"
                }, {
                    "amount": 6.75,
                    "unit": "$",
                    "label": "Service \u0026 Facility"
                }, {
                    "amount": 0.41,
                    "unit": "$",
                    "label": "Demand Side Mgmt Cost"
                }, {
                    "amount": 58.0,
                    "unit": "° F",
                    "label": "Average Temperature"
                }, {
                    "amount": 0.0,
                    "unit": "",
                    "label": "Cooling Degree Days"
                }, {
                    "amount": 0.0,
                    "unit": "",
                    "label": "Heating Degree Days"
                }],
                "lastReadDate":
                "October 24, 2016",
                "method":
                "Actual",
                "usage": {
                    "amount": 414.0,
                    "unit": ""
                }
            }, {
                "billingDays":
                29,
                "details": [{
                    "amount": 576.0,
                    "unit": "kWh",
                    "label": "Total Energy"
                }, {
                    "amount": 66.71,
                    "unit": "$",
                    "label": "Electric Charges"
                }, {
                    "amount": 71.21,
                    "unit": "$",
                    "label": "Total Electric Charges"
                }, {
                    "amount": 2.46,
                    "unit": "$",
                    "label": "Total Electric Charges / Day"
                }, {
                    "amount": 17.42,
                    "unit": "$",
                    "label": "Elec Commodity Adj"
                }, {
                    "amount": 6.75,
                    "unit": "$",
                    "label": "Service \u0026 Facility"
                }, {
                    "amount": 23.02,
                    "unit": "$",
                    "label": "Summer Tier 1*"
                }, {
                    "amount": 6.84,
                    "unit": "$",
                    "label": "Summer Tier 2*"
                }, {
                    "amount": 2.31,
                    "unit": "$",
                    "label": "CACJA"
                }, {
                    "amount": 3.17,
                    "unit": "$",
                    "label": "Purch Cap Cost Adj"
                }, {
                    "amount": 0.47,
                    "unit": "$",
                    "label": "Trans Cost Adj"
                }, {
                    "amount": 4.86,
                    "unit": "$",
                    "label": "GRSA"
                }, {
                    "amount": 0.57,
                    "unit": "$",
                    "label": "Demand Side Mgmt Cost"
                }, {
                    "amount": 1.3,
                    "unit": "$",
                    "label": "Renew. Energy Std Adj"
                }, {
                    "amount": 68.0,
                    "unit": "° F",
                    "label": "Average Temperature"
                }, {
                    "amount": 0.0,
                    "unit": "",
                    "label": "Cooling Degree Days"
                }, {
                    "amount": 0.0,
                    "unit": "",
                    "label": "Heating Degree Days"
                }],
                "lastReadDate":
                "September 22, 2016",
                "method":
                "Actual",
                "usage": {
                    "amount": 576.0,
                    "unit": ""
                }
            }, {
                "billingDays":
                29,
                "details": [{
                    "amount": 855.0,
                    "unit": "kWh",
                    "label": "Total Energy"
                }, {
                    "amount": 107.12,
                    "unit": "$",
                    "label": "Electric Charges"
                }, {
                    "amount": 114.36,
                    "unit": "$",
                    "label": "Total Electric Charges"
                }, {
                    "amount": 3.94,
                    "unit": "$",
                    "label": "Total Electric Charges / Day"
                }, {
                    "amount": 7.76,
                    "unit": "$",
                    "label": "GRSA"
                }, {
                    "amount": 0.69,
                    "unit": "$",
                    "label": "Trans Cost Adj"
                }, {
                    "amount": 0.85,
                    "unit": "$",
                    "label": "Demand Side Mgmt Cost"
                }, {
                    "amount": 2.1,
                    "unit": "$",
                    "label": "Renew. Energy Std Adj"
                }, {
                    "amount": 25.86,
                    "unit": "$",
                    "label": "Elec Commodity Adj"
                }, {
                    "amount": 6.75,
                    "unit": "$",
                    "label": "Service \u0026 Facility"
                }, {
                    "amount": 23.02,
                    "unit": "$",
                    "label": "Summer Tier 1*"
                }, {
                    "amount": 31.95,
                    "unit": "$",
                    "label": "Summer Tier 2*"
                }, {
                    "amount": 3.43,
                    "unit": "$",
                    "label": "CACJA"
                }, {
                    "amount": 4.71,
                    "unit": "$",
                    "label": "Purch Cap Cost Adj"
                }, {
                    "amount": 73.0,
                    "unit": "° F",
                    "label": "Average Temperature"
                }, {
                    "amount": 0.0,
                    "unit": "",
                    "label": "Cooling Degree Days"
                }, {
                    "amount": 0.0,
                    "unit": "",
                    "label": "Heating Degree Days"
                }],
                "lastReadDate":
                "August 24, 2016",
                "method":
                "Actual",
                "usage": {
                    "amount": 855.0,
                    "unit": ""
                }
            }, {
                "billingDays":
                33,
                "details": [{
                    "amount": 1089.0,
                    "unit": "kWh",
                    "label": "Total Energy"
                }, {
                    "amount": 138.51,
                    "unit": "$",
                    "label": "Electric Charges"
                }, {
                    "amount": 147.87,
                    "unit": "$",
                    "label": "Total Electric Charges"
                }, {
                    "amount": 4.48,
                    "unit": "$",
                    "label": "Total Electric Charges / Day"
                }, {
                    "amount": 0.85,
                    "unit": "$",
                    "label": "Demand Side Mgmt Cost"
                }, {
                    "amount": 4.37,
                    "unit": "$",
                    "label": "CACJA"
                }, {
                    "amount": 23.02,
                    "unit": "$",
                    "label": "Summer Tier 1*"
                }, {
                    "amount": 53.01,
                    "unit": "$",
                    "label": "Summer Tier 2*"
                }, {
                    "amount": 6.0,
                    "unit": "$",
                    "label": "Purch Cap Cost Adj"
                }, {
                    "amount": 25.95,
                    "unit": "$",
                    "label": "Elec Commodity Adj"
                }, {
                    "amount": 7.73,
                    "unit": "$",
                    "label": "GRSA"
                }, {
                    "amount": 0.88,
                    "unit": "$",
                    "label": "Trans Cost Adj"
                }, {
                    "amount": 2.72,
                    "unit": "$",
                    "label": "Renew. Energy Std Adj"
                }, {
                    "amount": 6.95,
                    "unit": "$",
                    "label": "Elec Commodity Adj"
                }, {
                    "amount": 0.28,
                    "unit": "$",
                    "label": "Demand Side Mgmt Cost"
                }, {
                    "amount": 6.75,
                    "unit": "$",
                    "label": "Service \u0026 Facility"
                }, {
                    "amount": 75.0,
                    "unit": "° F",
                    "label": "Average Temperature"
                }, {
                    "amount": 0.0,
                    "unit": "",
                    "label": "Cooling Degree Days"
                }, {
                    "amount": 0.0,
                    "unit": "",
                    "label": "Heating Degree Days"
                }],
                "lastReadDate":
                "July 26, 2016",
                "method":
                "Actual",
                "usage": {
                    "amount": 1089.0,
                    "unit": ""
                }
            }, {
                "billingDays":
                29,
                "details": [{
                    "amount": 744.0,
                    "unit": "kWh",
                    "label": "Total Energy"
                }, {
                    "amount": 86.83,
                    "unit": "$",
                    "label": "Electric Charges"
                }, {
                    "amount": 92.7,
                    "unit": "$",
                    "label": "Total Electric Charges"
                }, {
                    "amount": 3.2,
                    "unit": "$",
                    "label": "Total Electric Charges / Day"
                }, {
                    "amount": 0.92,
                    "unit": "$",
                    "label": "Demand Side Mgmt Cost"
                }, {
                    "amount": 1.7,
                    "unit": "$",
                    "label": "Renew. Energy Std Adj"
                }, {
                    "amount": 22.39,
                    "unit": "$",
                    "label": "Elec Commodity Adj"
                }, {
                    "amount": 6.75,
                    "unit": "$",
                    "label": "Service \u0026 Facility"
                }, {
                    "amount": 7.08,
                    "unit": "$",
                    "label": "Non-Summer"
                }, {
                    "amount": 18.26,
                    "unit": "$",
                    "label": "Summer Tier 1*"
                }, {
                    "amount": 17.42,
                    "unit": "$",
                    "label": "Summer Tier 2*"
                }, {
                    "amount": 2.98,
                    "unit": "$",
                    "label": "CACJA"
                }, {
                    "amount": 4.1,
                    "unit": "$",
                    "label": "Purch Cap Cost Adj"
                }, {
                    "amount": 4.63,
                    "unit": "$",
                    "label": "GRSA"
                }, {
                    "amount": 0.6,
                    "unit": "$",
                    "label": "Trans Cost Adj"
                }, {
                    "amount": 67.0,
                    "unit": "° F",
                    "label": "Average Temperature"
                }, {
                    "amount": 0.0,
                    "unit": "",
                    "label": "Cooling Degree Days"
                }, {
                    "amount": 0.0,
                    "unit": "",
                    "label": "Heating Degree Days"
                }],
                "lastReadDate":
                "June 23, 2016",
                "method":
                "Actual",
                "usage": {
                    "amount": 744.0,
                    "unit": ""
                }
            }, {
                "billingDays":
                30,
                "details": [{
                    "amount": 572.0,
                    "unit": "kWh",
                    "label": "Total Energy"
                }, {
                    "amount": 61.16,
                    "unit": "$",
                    "label": "Electric Charges"
                }, {
                    "amount": 65.3,
                    "unit": "$",
                    "label": "Total Electric Charges"
                }, {
                    "amount": 2.18,
                    "unit": "$",
                    "label": "Total Electric Charges / Day"
                }, {
                    "amount": 0.7,
                    "unit": "$",
                    "label": "Demand Side Mgmt Cost"
                }, {
                    "amount": 1.18,
                    "unit": "$",
                    "label": "Renew. Energy Std Adj"
                }, {
                    "amount": 17.21,
                    "unit": "$",
                    "label": "Elec Commodity Adj"
                }, {
                    "amount": 6.75,
                    "unit": "$",
                    "label": "Service \u0026 Facility"
                }, {
                    "amount": 26.33,
                    "unit": "$",
                    "label": "Non-Summer"
                }, {
                    "amount": 3.15,
                    "unit": "$",
                    "label": "Purch Cap Cost Adj"
                }, {
                    "amount": 2.29,
                    "unit": "$",
                    "label": "CACJA"
                }, {
                    "amount": 3.09,
                    "unit": "$",
                    "label": "GRSA"
                }, {
                    "amount": 0.46,
                    "unit": "$",
                    "label": "Trans Cost Adj"
                }, {
                    "amount": 51.0,
                    "unit": "° F",
                    "label": "Average Temperature"
                }, {
                    "amount": 0.0,
                    "unit": "",
                    "label": "Cooling Degree Days"
                }, {
                    "amount": 0.0,
                    "unit": "",
                    "label": "Heating Degree Days"
                }],
                "lastReadDate":
                "May 25, 2016",
                "method":
                "Actual",
                "usage": {
                    "amount": 572.0,
                    "unit": ""
                }
            }, {
                "billingDays":
                28,
                "details": [{
                    "amount": 543.0,
                    "unit": "kWh",
                    "label": "Total Energy"
                }, {
                    "amount": 58.28,
                    "unit": "$",
                    "label": "Electric Charges"
                }, {
                    "amount": 62.22,
                    "unit": "$",
                    "label": "Total Electric Charges"
                }, {
                    "amount": 2.22,
                    "unit": "$",
                    "label": "Total Electric Charges / Day"
                }, {
                    "amount": 1.13,
                    "unit": "$",
                    "label": "Renew. Energy Std Adj"
                }, {
                    "amount": 6.75,
                    "unit": "$",
                    "label": "Service \u0026 Facility"
                }, {
                    "amount": 1.56,
                    "unit": "$",
                    "label": "Elec Commodity Adj"
                }, {
                    "amount": 0.67,
                    "unit": "$",
                    "label": "Demand Side Mgmt Cost"
                }, {
                    "amount": 25.0,
                    "unit": "$",
                    "label": "Non-Summer"
                }, {
                    "amount": 14.59,
                    "unit": "$",
                    "label": "Elec Commodity Adj"
                }, {
                    "amount": 2.97,
                    "unit": "$",
                    "label": "GRSA"
                }, {
                    "amount": 0.44,
                    "unit": "$",
                    "label": "Trans Cost Adj"
                }, {
                    "amount": 2.99,
                    "unit": "$",
                    "label": "Purch Cap Cost Adj"
                }, {
                    "amount": 2.18,
                    "unit": "$",
                    "label": "CACJA"
                }, {
                    "amount": 49.0,
                    "unit": "° F",
                    "label": "Average Temperature"
                }, {
                    "amount": 0.0,
                    "unit": "",
                    "label": "Cooling Degree Days"
                }, {
                    "amount": 0.0,
                    "unit": "",
                    "label": "Heating Degree Days"
                }],
                "lastReadDate":
                "April 25, 2016",
                "method":
                "Actual",
                "usage": {
                    "amount": 543.0,
                    "unit": ""
                }
            }, {
                "billingDays":
                30,
                "details": [{
                    "amount": 578.0,
                    "unit": "kWh",
                    "label": "Total Energy"
                }, {
                    "amount": 59.83,
                    "unit": "$",
                    "label": "Electric Charges"
                }, {
                    "amount": 63.88,
                    "unit": "$",
                    "label": "Total Electric Charges"
                }, {
                    "amount": 2.13,
                    "unit": "$",
                    "label": "Total Electric Charges / Day"
                }, {
                    "amount": 0.71,
                    "unit": "$",
                    "label": "Demand Side Mgmt Cost"
                }, {
                    "amount": 1.16,
                    "unit": "$",
                    "label": "Renew. Energy Std Adj"
                }, {
                    "amount": 6.75,
                    "unit": "$",
                    "label": "Service \u0026 Facility"
                }, {
                    "amount": 15.51,
                    "unit": "$",
                    "label": "Elec Commodity Adj"
                }, {
                    "amount": 26.61,
                    "unit": "$",
                    "label": "Non-Summer"
                }, {
                    "amount": 2.32,
                    "unit": "$",
                    "label": "CACJA"
                }, {
                    "amount": 3.18,
                    "unit": "$",
                    "label": "Purch Cap Cost Adj"
                }, {
                    "amount": 3.12,
                    "unit": "$",
                    "label": "GRSA"
                }, {
                    "amount": 0.47,
                    "unit": "$",
                    "label": "Trans Cost Adj"
                }, {
                    "amount": 40.0,
                    "unit": "° F",
                    "label": "Average Temperature"
                }, {
                    "amount": 0.0,
                    "unit": "",
                    "label": "Cooling Degree Days"
                }, {
                    "amount": 0.0,
                    "unit": "",
                    "label": "Heating Degree Days"
                }],
                "lastReadDate":
                "February 25, 2016",
                "method":
                "Actual",
                "usage": {
                    "amount": 578.0,
                    "unit": ""
                }
            }, {
                "billingDays":
                34,
                "details": [{
                    "amount": 669.0,
                    "unit": "kWh",
                    "label": "Total Energy"
                }, {
                    "amount": 69.08,
                    "unit": "$",
                    "label": "Electric Charges"
                }, {
                    "amount": 73.75,
                    "unit": "$",
                    "label": "Total Electric Charges"
                }, {
                    "amount": 2.17,
                    "unit": "$",
                    "label": "Total Electric Charges / Day"
                }, {
                    "amount": 1.36,
                    "unit": "$",
                    "label": "Renew. Energy Std Adj"
                }, {
                    "amount": 0.63,
                    "unit": "$",
                    "label": "Demand Side Mgmt Cost"
                }, {
                    "amount": 2.05,
                    "unit": "$",
                    "label": "CACJA"
                }, {
                    "amount": 6.75,
                    "unit": "$",
                    "label": "Service \u0026 Facility"
                }, {
                    "amount": 2.82,
                    "unit": "$",
                    "label": "Purch Cap Cost Adj"
                }, {
                    "amount": 5.04,
                    "unit": "$",
                    "label": "Elec Commodity Adj"
                }, {
                    "amount": 30.8,
                    "unit": "$",
                    "label": "Non-Summer"
                }, {
                    "amount": 0.24,
                    "unit": "$",
                    "label": "Demand Side Mgmt Cost"
                }, {
                    "amount": 0.62,
                    "unit": "$",
                    "label": "CACJA"
                }, {
                    "amount": 3.51,
                    "unit": "$",
                    "label": "GRSA"
                }, {
                    "amount": 0.1,
                    "unit": "$",
                    "label": "Trans Cost Adj"
                }, {
                    "amount": 13.73,
                    "unit": "$",
                    "label": "Elec Commodity Adj"
                }, {
                    "amount": 0.41,
                    "unit": "$",
                    "label": "Trans Cost Adj"
                }, {
                    "amount": 1.02,
                    "unit": "$",
                    "label": "Purch Cap Cost Adj"
                }, {
                    "amount": 31.0,
                    "unit": "° F",
                    "label": "Average Temperature"
                }, {
                    "amount": 0.0,
                    "unit": "",
                    "label": "Cooling Degree Days"
                }, {
                    "amount": 0.0,
                    "unit": "",
                    "label": "Heating Degree Days"
                }],
                "lastReadDate":
                "January 26, 2016",
                "method":
                "Actual",
                "usage": {
                    "amount": 669.0,
                    "unit": ""
                }
            }, {
                "billingDays":
                33,
                "details": [{
                    "amount": 643.0,
                    "unit": "kWh",
                    "label": "Total Energy"
                }, {
                    "amount": 69.77,
                    "unit": "$",
                    "label": "Electric Charges"
                }, {
                    "amount": 74.49,
                    "unit": "$",
                    "label": "Total Electric Charges"
                }, {
                    "amount": 2.26,
                    "unit": "$",
                    "label": "Total Electric Charges / Day"
                }, {
                    "amount": 6.75,
                    "unit": "$",
                    "label": "Service \u0026 Facility"
                }, {
                    "amount": 29.6,
                    "unit": "$",
                    "label": "Non-Summer"
                }, {
                    "amount": 4.18,
                    "unit": "$",
                    "label": "Purch Cap Cost Adj"
                }, {
                    "amount": 2.52,
                    "unit": "$",
                    "label": "CACJA"
                }, {
                    "amount": 3.39,
                    "unit": "$",
                    "label": "GRSA"
                }, {
                    "amount": 0.41,
                    "unit": "$",
                    "label": "Trans Cost Adj"
                }, {
                    "amount": 1.0,
                    "unit": "$",
                    "label": "Demand Side Mgmt Cost"
                }, {
                    "amount": 1.35,
                    "unit": "$",
                    "label": "Renew. Energy Std Adj"
                }, {
                    "amount": 20.57,
                    "unit": "$",
                    "label": "Elec Commodity Adj"
                }, {
                    "amount": 36.0,
                    "unit": "° F",
                    "label": "Average Temperature"
                }, {
                    "amount": 0.0,
                    "unit": "",
                    "label": "Cooling Degree Days"
                }, {
                    "amount": 0.0,
                    "unit": "",
                    "label": "Heating Degree Days"
                }],
                "lastReadDate":
                "December 23, 2015",
                "method":
                "Actual",
                "usage": {
                    "amount": 643.0,
                    "unit": ""
                }
            }],
            "name":
            "ELECTRICITY-1"
        }, {
            "reads": [{
                "billingDays":
                29,
                "details": [{
                    "amount": 45.08,
                    "unit": "$",
                    "label": "Gas Charges"
                }, {
                    "amount": 48.14,
                    "unit": "$",
                    "label": "Total Gas Charges"
                }, {
                    "amount": 1.66,
                    "unit": "$",
                    "label": "Total Gas Charges / Day"
                }, {
                    "amount":
                    74.0,
                    "unit":
                    "",
                    "label":
                    "Heat Content Adjustment Conversion Factor"
                }, {
                    "amount": 46.0,
                    "unit": "° F",
                    "label": "Average Temperature"
                }, {
                    "amount": 0.0,
                    "unit": "",
                    "label": "Heating Degree Days"
                }],
                "lastReadDate":
                "November 21, 2017",
                "method":
                "Actual",
                "usage": {
                    "amount": 64.0,
                    "unit": ""
                }
            }, {
                "billingDays":
                31,
                "details": [{
                    "amount": 30.1,
                    "unit": "$",
                    "label": "Gas Charges"
                }, {
                    "amount": 32.14,
                    "unit": "$",
                    "label": "Total Gas Charges"
                }, {
                    "amount": 1.04,
                    "unit": "$",
                    "label": "Total Gas Charges / Day"
                }, {
                    "amount":
                    39.0,
                    "unit":
                    "",
                    "label":
                    "Heat Content Adjustment Conversion Factor"
                }, {
                    "amount": 52.0,
                    "unit": "° F",
                    "label": "Average Temperature"
                }, {
                    "amount": 0.0,
                    "unit": "",
                    "label": "Heating Degree Days"
                }],
                "lastReadDate":
                "October 23, 2017",
                "method":
                "Actual",
                "usage": {
                    "amount": 34.0,
                    "unit": ""
                }
            }, {
                "billingDays":
                30,
                "details": [{
                    "amount": 18.27,
                    "unit": "$",
                    "label": "Gas Charges"
                }, {
                    "amount": 19.51,
                    "unit": "$",
                    "label": "Total Gas Charges"
                }, {
                    "amount": 0.65,
                    "unit": "$",
                    "label": "Total Gas Charges / Day"
                }, {
                    "amount":
                    11.0,
                    "unit":
                    "",
                    "label":
                    "Heat Content Adjustment Conversion Factor"
                }, {
                    "amount": 70.0,
                    "unit": "° F",
                    "label": "Average Temperature"
                }, {
                    "amount": 0.0,
                    "unit": "",
                    "label": "Heating Degree Days"
                }],
                "lastReadDate":
                "September 22, 2017",
                "method":
                "Actual",
                "usage": {
                    "amount": 10.0,
                    "unit": ""
                }
            }, {
                "billingDays":
                29,
                "details": [{
                    "amount": 17.34,
                    "unit": "$",
                    "label": "Gas Charges"
                }, {
                    "amount": 18.51,
                    "unit": "$",
                    "label": "Total Gas Charges"
                }, {
                    "amount": 0.64,
                    "unit": "$",
                    "label": "Total Gas Charges / Day"
                }, {
                    "amount":
                    9.0,
                    "unit":
                    "",
                    "label":
                    "Heat Content Adjustment Conversion Factor"
                }, {
                    "amount": 70.0,
                    "unit": "° F",
                    "label": "Average Temperature"
                }, {
                    "amount": 0.0,
                    "unit": "",
                    "label": "Heating Degree Days"
                }],
                "lastReadDate":
                "August 23, 2017",
                "method":
                "Actual",
                "usage": {}
            }, {
                "billingDays":
                29,
                "details": [{
                    "amount": 18.28,
                    "unit": "$",
                    "label": "Gas Charges"
                }, {
                    "amount": 19.52,
                    "unit": "$",
                    "label": "Total Gas Charges"
                }, {
                    "amount": 0.67,
                    "unit": "$",
                    "label": "Total Gas Charges / Day"
                }, {
                    "amount":
                    12.0,
                    "unit":
                    "",
                    "label":
                    "Heat Content Adjustment Conversion Factor"
                }, {
                    "amount": 75.0,
                    "unit": "° F",
                    "label": "Average Temperature"
                }, {
                    "amount": 0.0,
                    "unit": "",
                    "label": "Heating Degree Days"
                }],
                "lastReadDate":
                "July 25, 2017",
                "method":
                "Actual",
                "usage": {
                    "amount": 10.0,
                    "unit": ""
                }
            }, {
                "billingDays":
                32,
                "details": [{
                    "amount": 21.22,
                    "unit": "$",
                    "label": "Gas Charges"
                }, {
                    "amount": 22.65,
                    "unit": "$",
                    "label": "Total Gas Charges"
                }, {
                    "amount": 0.71,
                    "unit": "$",
                    "label": "Total Gas Charges / Day"
                }, {
                    "amount":
                    18.0,
                    "unit":
                    "",
                    "label":
                    "Heat Content Adjustment Conversion Factor"
                }, {
                    "amount": 67.0,
                    "unit": "° F",
                    "label": "Average Temperature"
                }, {
                    "amount": 0.0,
                    "unit": "",
                    "label": "Heating Degree Days"
                }],
                "lastReadDate":
                "June 26, 2017",
                "method":
                "Actual",
                "usage": {
                    "amount": 16.0,
                    "unit": ""
                }
            }, {
                "billingDays":
                29,
                "details": [{
                    "amount": 31.58,
                    "unit": "$",
                    "label": "Gas Charges"
                }, {
                    "amount": 33.72,
                    "unit": "$",
                    "label": "Total Gas Charges"
                }, {
                    "amount": 1.16,
                    "unit": "$",
                    "label": "Total Gas Charges / Day"
                }, {
                    "amount":
                    43.0,
                    "unit":
                    "",
                    "label":
                    "Heat Content Adjustment Conversion Factor"
                }, {
                    "amount": 53.0,
                    "unit": "° F",
                    "label": "Average Temperature"
                }, {
                    "amount": 0.0,
                    "unit": "",
                    "label": "Heating Degree Days"
                }],
                "lastReadDate":
                "May 25, 2017",
                "method":
                "Actual",
                "usage": {}
            }, {
                "billingDays":
                29,
                "details": [{
                    "amount": 29.74,
                    "unit": "$",
                    "label": "Gas Charges"
                }, {
                    "amount": 31.75,
                    "unit": "$",
                    "label": "Total Gas Charges"
                }, {
                    "amount": 1.09,
                    "unit": "$",
                    "label": "Total Gas Charges / Day"
                }, {
                    "amount":
                    39.0,
                    "unit":
                    "",
                    "label":
                    "Heat Content Adjustment Conversion Factor"
                }, {
                    "amount": 50.0,
                    "unit": "° F",
                    "label": "Average Temperature"
                }, {
                    "amount": 0.0,
                    "unit": "",
                    "label": "Heating Degree Days"
                }],
                "lastReadDate":
                "April 26, 2017",
                "method":
                "Actual",
                "usage": {
                    "amount": 34.0,
                    "unit": ""
                }
            }, {
                "billingDays":
                32,
                "details": [{
                    "amount": 44.5,
                    "unit": "$",
                    "label": "Gas Charges"
                }, {
                    "amount": 47.51,
                    "unit": "$",
                    "label": "Total Gas Charges"
                }, {
                    "amount": 1.48,
                    "unit": "$",
                    "label": "Total Gas Charges / Day"
                }, {
                    "amount":
                    68.0,
                    "unit":
                    "",
                    "label":
                    "Heat Content Adjustment Conversion Factor"
                }, {
                    "amount": 48.0,
                    "unit": "° F",
                    "label": "Average Temperature"
                }, {
                    "amount": 0.0,
                    "unit": "",
                    "label": "Heating Degree Days"
                }],
                "lastReadDate":
                "March 28, 2017",
                "method":
                "Actual",
                "usage": {
                    "amount": 59.0,
                    "unit": ""
                }
            }, {
                "billingDays":
                29,
                "details": [{
                    "amount": 55.02,
                    "unit": "$",
                    "label": "Gas Charges"
                }, {
                    "amount": 58.74,
                    "unit": "$",
                    "label": "Total Gas Charges"
                }, {
                    "amount": 2.03,
                    "unit": "$",
                    "label": "Total Gas Charges / Day"
                }, {
                    "amount":
                    91.0,
                    "unit":
                    "",
                    "label":
                    "Heat Content Adjustment Conversion Factor"
                }, {
                    "amount": 44.0,
                    "unit": "° F",
                    "label": "Average Temperature"
                }, {
                    "amount": 0.0,
                    "unit": "",
                    "label": "Heating Degree Days"
                }],
                "lastReadDate":
                "February 24, 2017",
                "method":
                "Actual",
                "usage": {
                    "amount": 79.0,
                    "unit": ""
                }
            }, {
                "billingDays":
                35,
                "details": [{
                    "amount": 80.49,
                    "unit": "$",
                    "label": "Gas Charges"
                }, {
                    "amount": 85.92,
                    "unit": "$",
                    "label": "Total Gas Charges"
                }, {
                    "amount": 2.45,
                    "unit": "$",
                    "label": "Total Gas Charges / Day"
                }, {
                    "amount":
                    150.0,
                    "unit":
                    "",
                    "label":
                    "Heat Content Adjustment Conversion Factor"
                }, {
                    "amount": 33.0,
                    "unit": "° F",
                    "label": "Average Temperature"
                }, {
                    "amount": 0.0,
                    "unit": "",
                    "label": "Heating Degree Days"
                }],
                "lastReadDate":
                "January 26, 2017",
                "method":
                "Actual",
                "usage": {}
            }, {
                "billingDays":
                30,
                "details": [{
                    "amount": 66.56,
                    "unit": "$",
                    "label": "Gas Charges"
                }, {
                    "amount": 71.06,
                    "unit": "$",
                    "label": "Total Gas Charges"
                }, {
                    "amount": 2.37,
                    "unit": "$",
                    "label": "Total Gas Charges / Day"
                }, {
                    "amount":
                    128.0,
                    "unit":
                    "",
                    "label":
                    "Heat Content Adjustment Conversion Factor"
                }, {
                    "amount": 32.0,
                    "unit": "° F",
                    "label": "Average Temperature"
                }, {
                    "amount": 0.0,
                    "unit": "",
                    "label": "Heating Degree Days"
                }],
                "lastReadDate":
                "December 22, 2016",
                "method":
                "Actual",
                "usage": {}
            }, {
                "billingDays":
                29,
                "details": [{
                    "amount": 30.18,
                    "unit": "$",
                    "label": "Gas Charges"
                }, {
                    "amount": 32.21,
                    "unit": "$",
                    "label": "Total Gas Charges"
                }, {
                    "amount": 1.11,
                    "unit": "$",
                    "label": "Total Gas Charges / Day"
                }, {
                    "amount":
                    40.0,
                    "unit":
                    "",
                    "label":
                    "Heat Content Adjustment Conversion Factor"
                }, {
                    "amount": 55.0,
                    "unit": "° F",
                    "label": "Average Temperature"
                }, {
                    "amount": 0.0,
                    "unit": "",
                    "label": "Heating Degree Days"
                }],
                "lastReadDate":
                "November 22, 2016",
                "method":
                "Actual",
                "usage": {
                    "amount": 35.0,
                    "unit": ""
                }
            }, {
                "billingDays":
                32,
                "details": [{
                    "amount": 22.2,
                    "unit": "$",
                    "label": "Gas Charges"
                }, {
                    "amount": 23.7,
                    "unit": "$",
                    "label": "Total Gas Charges"
                }, {
                    "amount": 0.74,
                    "unit": "$",
                    "label": "Total Gas Charges / Day"
                }, {
                    "amount":
                    21.0,
                    "unit":
                    "",
                    "label":
                    "Heat Content Adjustment Conversion Factor"
                }, {
                    "amount": 58.0,
                    "unit": "° F",
                    "label": "Average Temperature"
                }, {
                    "amount": 0.0,
                    "unit": "",
                    "label": "Heating Degree Days"
                }],
                "lastReadDate":
                "October 24, 2016",
                "method":
                "Actual",
                "usage": {
                    "amount": 18.0,
                    "unit": ""
                }
            }, {
                "billingDays":
                29,
                "details": [{
                    "amount": 19.61,
                    "unit": "$",
                    "label": "Gas Charges"
                }, {
                    "amount": 20.94,
                    "unit": "$",
                    "label": "Total Gas Charges"
                }, {
                    "amount": 0.72,
                    "unit": "$",
                    "label": "Total Gas Charges / Day"
                }, {
                    "amount":
                    15.0,
                    "unit":
                    "",
                    "label":
                    "Heat Content Adjustment Conversion Factor"
                }, {
                    "amount": 68.0,
                    "unit": "° F",
                    "label": "Average Temperature"
                }, {
                    "amount": 0.0,
                    "unit": "",
                    "label": "Heating Degree Days"
                }],
                "lastReadDate":
                "September 22, 2016",
                "method":
                "Actual",
                "usage": {}
            }, {
                "billingDays":
                29,
                "details": [{
                    "amount": 18.2,
                    "unit": "$",
                    "label": "Gas Charges"
                }, {
                    "amount": 19.43,
                    "unit": "$",
                    "label": "Total Gas Charges"
                }, {
                    "amount": 0.67,
                    "unit": "$",
                    "label": "Total Gas Charges / Day"
                }, {
                    "amount":
                    11.0,
                    "unit":
                    "",
                    "label":
                    "Heat Content Adjustment Conversion Factor"
                }, {
                    "amount": 73.0,
                    "unit": "° F",
                    "label": "Average Temperature"
                }, {
                    "amount": 0.0,
                    "unit": "",
                    "label": "Heating Degree Days"
                }],
                "lastReadDate":
                "August 24, 2016",
                "method":
                "Actual",
                "usage": {
                    "amount": 10.0,
                    "unit": ""
                }
            }, {
                "billingDays":
                33,
                "details": [{
                    "amount": 18.91,
                    "unit": "$",
                    "label": "Gas Charges"
                }, {
                    "amount": 20.19,
                    "unit": "$",
                    "label": "Total Gas Charges"
                }, {
                    "amount": 0.61,
                    "unit": "$",
                    "label": "Total Gas Charges / Day"
                }, {
                    "amount":
                    14.0,
                    "unit":
                    "",
                    "label":
                    "Heat Content Adjustment Conversion Factor"
                }, {
                    "amount": 75.0,
                    "unit": "° F",
                    "label": "Average Temperature"
                }, {
                    "amount": 0.0,
                    "unit": "",
                    "label": "Heating Degree Days"
                }],
                "lastReadDate":
                "July 26, 2016",
                "method":
                "Actual",
                "usage": {
                    "amount": 12.0,
                    "unit": ""
                }
            }, {
                "billingDays":
                29,
                "details": [{
                    "amount": 17.35,
                    "unit": "$",
                    "label": "Gas Charges"
                }, {
                    "amount": 18.52,
                    "unit": "$",
                    "label": "Total Gas Charges"
                }, {
                    "amount": 0.64,
                    "unit": "$",
                    "label": "Total Gas Charges / Day"
                }, {
                    "amount":
                    12.0,
                    "unit":
                    "",
                    "label":
                    "Heat Content Adjustment Conversion Factor"
                }, {
                    "amount": 67.0,
                    "unit": "° F",
                    "label": "Average Temperature"
                }, {
                    "amount": 0.0,
                    "unit": "",
                    "label": "Heating Degree Days"
                }],
                "lastReadDate":
                "June 23, 2016",
                "method":
                "Actual",
                "usage": {}
            }, {
                "billingDays":
                30,
                "details": [{
                    "amount": 29.68,
                    "unit": "$",
                    "label": "Gas Charges"
                }, {
                    "amount": 31.68,
                    "unit": "$",
                    "label": "Total Gas Charges"
                }, {
                    "amount": 1.06,
                    "unit": "$",
                    "label": "Total Gas Charges / Day"
                }, {
                    "amount":
                    50.0,
                    "unit":
                    "",
                    "label":
                    "Heat Content Adjustment Conversion Factor"
                }, {
                    "amount": 51.0,
                    "unit": "° F",
                    "label": "Average Temperature"
                }, {
                    "amount": 0.0,
                    "unit": "",
                    "label": "Heating Degree Days"
                }],
                "lastReadDate":
                "May 25, 2016",
                "method":
                "Actual",
                "usage": {
                    "amount": 43.0,
                    "unit": ""
                }
            }, {
                "billingDays":
                28,
                "details": [{
                    "amount": 33.8,
                    "unit": "$",
                    "label": "Gas Charges"
                }, {
                    "amount": 36.08,
                    "unit": "$",
                    "label": "Total Gas Charges"
                }, {
                    "amount": 1.29,
                    "unit": "$",
                    "label": "Total Gas Charges / Day"
                }, {
                    "amount":
                    60.0,
                    "unit":
                    "",
                    "label":
                    "Heat Content Adjustment Conversion Factor"
                }, {
                    "amount": 49.0,
                    "unit": "° F",
                    "label": "Average Temperature"
                }, {
                    "amount": 0.0,
                    "unit": "",
                    "label": "Heating Degree Days"
                }],
                "lastReadDate":
                "April 25, 2016",
                "method":
                "Actual",
                "usage": {
                    "amount": 52.0,
                    "unit": ""
                }
            }, {
                "billingDays":
                30,
                "details": [{
                    "amount": 54.47,
                    "unit": "$",
                    "label": "Gas Charges"
                }, {
                    "amount": 58.16,
                    "unit": "$",
                    "label": "Total Gas Charges"
                }, {
                    "amount": 1.94,
                    "unit": "$",
                    "label": "Total Gas Charges / Day"
                }, {
                    "amount":
                    105.0,
                    "unit":
                    "",
                    "label":
                    "Heat Content Adjustment Conversion Factor"
                }, {
                    "amount": 40.0,
                    "unit": "° F",
                    "label": "Average Temperature"
                }, {
                    "amount": 0.0,
                    "unit": "",
                    "label": "Heating Degree Days"
                }],
                "lastReadDate":
                "February 25, 2016",
                "method":
                "Actual",
                "usage": {}
            }, {
                "billingDays":
                34,
                "details": [{
                    "amount": 76.26,
                    "unit": "$",
                    "label": "Gas Charges"
                }, {
                    "amount": 81.42,
                    "unit": "$",
                    "label": "Total Gas Charges"
                }, {
                    "amount": 2.39,
                    "unit": "$",
                    "label": "Total Gas Charges / Day"
                }, {
                    "amount":
                    157.0,
                    "unit":
                    "",
                    "label":
                    "Heat Content Adjustment Conversion Factor"
                }, {
                    "amount": 31.0,
                    "unit": "° F",
                    "label": "Average Temperature"
                }, {
                    "amount": 0.0,
                    "unit": "",
                    "label": "Heating Degree Days"
                }],
                "lastReadDate":
                "January 26, 2016",
                "method":
                "Actual",
                "usage": {
                    "amount": 137.0,
                    "unit": ""
                }
            }, {
                "billingDays":
                33,
                "details": [{
                    "amount": 65.03,
                    "unit": "$",
                    "label": "Gas Charges"
                }, {
                    "amount": 69.43,
                    "unit": "$",
                    "label": "Total Gas Charges"
                }, {
                    "amount": 2.1,
                    "unit": "$",
                    "label": "Total Gas Charges / Day"
                }, {
                    "amount":
                    121.0,
                    "unit":
                    "",
                    "label":
                    "Heat Content Adjustment Conversion Factor"
                }, {
                    "amount": 36.0,
                    "unit": "° F",
                    "label": "Average Temperature"
                }, {
                    "amount": 0.0,
                    "unit": "",
                    "label": "Heating Degree Days"
                }],
                "lastReadDate":
                "December 23, 2015",
                "method":
                "Actual",
                "usage": {
                    "amount": 105.0,
                    "unit": ""
                }
            }],
            "name":
            "NATURAL GAS-1"
        }],
        "startDate":
        "2015-10-13T12:00:00-07:00",
        "state":
        "co",
        "status":
        "CURRENT",
        "twelveMonthDataAvailable":
        False
    }


@pytest.fixture(scope='session')
def username():
    """Define a username."""
    return 'username'
