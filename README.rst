robotframework-jira
====================

.. image:: https://img.shields.io/pypi/v/robotframework-jira.svg
    :target: https://pypi.python.org/pypi/robotframework-jira
.. image:: https://img.shields.io/pypi/l/robotframework-jira.svg
    :target: https://pypi.python.org/pypi/robotframework-jira


Robot Framework keyword library wrapper for
`atlassian-python-api <https://atlassian-python-api.readthedocs.io/jira.html>`__

This module allows easy use of JIRA's functions

Any docstrings JIRA provides are passed through to Robot Framework, so
they're available in RIDE and in keyword documentation generated via
libdoc.

For more information on Robot Framework please visit `the Robot
Framework homepage! <http://robotframework.org/>`__

Installation
------------

.. code:: shell
    
    pip install robotframework-jira

Usage
-----

`JIRALibrary keywords
documentation <https://ilfirinpl.github.io/robotframework-jira/>`_


.. code:: robotframework

    *** Settings ***
    Library     Collections
    Library     JIRALibrary


    *** Variables ***
    ${URL}      https://jira.com
    ${USER}     mytestid
    ${PASS}     myPass


    *** Test Cases ***
    Connect To JIRA
        ${session}    Connect To Jira    ${URL}    ${USER}    ${PASS}
        ${projects}    Projects    ${session}
        Log Dictionary    ${projects}    WARN

    Connect To JIRA And Skip SSL Check
        Evaluate    urllib3.disable_warnings()
        ${session}    Connect To Jira    ${URL}    ${USER}    ${PASS}    verify_ssl=${False}
        ${projects}    Projects    ${session}
        Log Dictionary    ${projects}    WARN

    Add Comment to Issue
        ${session}    Connect To Jira    ${URL}    ${USER}    ${PASS}
        Issue Add Comment    ${session}    JIRAID-1234    My long comment !


Contribute
----------

If you like this module, please contribute! I welcome patches,
documentation, issues, ideas, and so on.
