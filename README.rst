pyxcel: A Simple Python API for Xcel Energy® Data
=================================================

.. image:: https://travis-ci.org/bachya/pyxcel.svg?branch=master
  :target: https://travis-ci.org/bachya/pyxcel

.. image:: https://img.shields.io/pypi/v/pyxcel.svg
  :target: https://pypi.python.org/pypi/pyxcel

.. image:: https://img.shields.io/pypi/pyversions/pyxcel.svg
  :target: https://pypi.python.org/pypi/pyxcel

.. image:: https://img.shields.io/pypi/l/pyxcel.svg
  :target: https://github.com/bachya/pyxcel/blob/master/LICENSE

.. image:: https://codecov.io/gh/bachya/pyxcel/branch/master/graph/badge.svg
  :target: https://codecov.io/gh/bachya/pyxcel

.. image:: https://api.codeclimate.com/v1/badges/71eb642c735e33adcdfc/maintainability
  :target: https://codeclimate.com/github/bachya/pyxcel

.. image:: https://img.shields.io/badge/SayThanks-!-1EAEDB.svg
  :target: https://saythanks.io/to/bachya

pyxcel is a simple Python library for energy data from
`Xcel Energy® <https://www.xcelenergy.com/>`_.

This library works by repeating the same HTTP requests performed by users who
view the Xcel Energy® website. Because there is no official "API," this
library may stop working at any time.

Installation
============

.. code-block:: bash

  $ pip install pyxcel

Usage
=====

.. code-block:: python

  import pyxcel

  client = pyxcel.Client('username', 'password12345')

  # Retrieves the account overview (including energy usage, grades, etc.):
  client.get_account_overview()

  # Retrieves all billing information for the account
  client.get_bills()

  # Retrives detailed information for a particular premise:
  client.get_usages('PREMISE_ID')

Contributing
============

#. `Check for open features/bugs <https://github.com/bachya/pyxcel/issues>`_
   or `initiate a discussion on one <https://github.com/bachya/pyxcel/issues/new>`_.
#. `Fork the repository <https://github.com/bachya/pyxcel/fork>`_.
#. Install the dev environment: :code:`make init`.
#. Enter the virtual environment: :code:`pipenv shell`
#. Code your new feature or bug fix.
#. Write a test that covers your new functionality.
#. Run tests: :code:`make test`
#. Build new docs: :code:`make docs`
#. Add yourself to AUTHORS.rst.
#. Submit a pull request!
