#!/usr/bin/env python
# pylint: disable=consider-using-with,missing-module-docstring
from setuptools import setup


SHORT_DESCRIPTION = "Robot Framework wrapper for JIRA using atlassian-python-api"
try:
    DESCRIPTION = open("README.rst", encoding="utf-8").read()
except IOError:
    DESCRIPTION = SHORT_DESCRIPTION


classifiers = """
Development Status :: 5 - Production/Stable
License :: OSI Approved :: MIT License
Operating System :: OS Independent
Programming Language :: Python
Programming Language :: Python :: 3
Programming Language :: Python :: 3 :: Only
Programming Language :: Python :: 3.7
Programming Language :: Python :: 3.8
Programming Language :: Python :: 3.9
Topic :: Software Development :: Testing
Topic :: Software Development :: Quality Assurance
""".strip().splitlines()

setup(
    name="robotframework-jira",
    package_dir={"": "robotframework_jira"},
    packages=["JIRALibrary"],  # this must be the same as the name above
    version="0.0.3",
    description=SHORT_DESCRIPTION,
    author="Marcin Koperski",
    author_email="marcin.koperski+github@gmail.com",
    url="https://github.com/IlfirinPL/robotframework-jira",
    download_url="https://pypi.python.org/pypi/robotframework-jira",
    keywords=("robotframework testing jira"),  # arbitrary keywords
    install_requires=["atlassian-python-api", "robotframework", "wrapt"],
    long_description=DESCRIPTION,
    license="MIT",
    classifiers=classifiers,
    platforms="any",
)
