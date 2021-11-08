#!/usr/bin/env python
from setuptools import setup

short_description = "Robot Framework wrapper for JIRA using atlassian-python-api"
try:
    description = open("README.rst").read()
except IOError:
    description = short_description


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
    package_dir={"": "robotframework-jira"},
    packages=["JIRALibrary"],  # this must be the same as the name above
    version="0.0.1",
    description=short_description,
    author="Marcin Koperski",
    author_email="marcin.koperski+github@gmail.com",
    url="https://github.com/IlfirinPL/robotframework-jira",
    download_url="https://pypi.python.org/pypi/robotframework-jira",
    keywords=("robotframework testing jira"),  # arbitrary keywords
    install_requires=["atlassian-python-api", "robotframework", "wrapt"],
    long_description=short_description,
    license="MIT",
    classifiers=classifiers,
    platforms="any",
)
