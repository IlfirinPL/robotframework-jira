"""

This is a very thin wrapper for jira. You can access all of jira's usual
methods via JIRALibrary calls in Robot Framework.

"""
# pylint: disable=invalid-name,empty-docstring
import pkg_resources
from .keywords import JIRAKeywords


__version__ = pkg_resources.get_distribution("robotframework-jira").version


class JIRALibrary(JIRAKeywords):
    """"""

    ROBOT_LIBRARY_SCOPE = "GLOBAL"
