"""

This is a very thin wrapper for jira. You can access all of jira's usual
methods via JIRALibrary calls in Robot Framework.

"""
# pylint: disable=no-value-for-parameter,unused-argument,useless-object-inheritance,broad-except,consider-iterating-dictionary
import ast

import wrapt
from atlassian import Jira
from robot.api import logger


def _str_to_data(string):
    try:
        return ast.literal_eval(str(string).strip())
    except Exception:
        return string


@wrapt.decorator
def _str_vars_to_data(function, instance, args, kwargs):
    args = [_str_to_data(arg) for arg in args]
    kwargs = dict((arg_name, _str_to_data(arg)) for arg_name, arg in kwargs.items())
    result = function(*args, **kwargs)
    return result


class JIRAKeywords(object):
    """
    This looks tricky but it's just the Robot Framework Hybrid Library API.
    https://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#hybrid-library-api
    """

    ROBOT_LIBRARY_SCOPE = "Global"
    _jira = Jira
    _session = None

    def get_keyword_names(self):
        """
        Generate List of keywords from jira lib
        """
        keywords = [
            name
            for name, function in self._jira.__dict__.items()
            if hasattr(function, "__call__")
        ]

        keywords.append("connect_to_jira")
        keywords.remove("__init__")
        keywords.remove("get_issue_remotelinks")

        return keywords

    def connect_to_jira(self, url=None, username=None, password=None, **kwargs):
        """
        Connect To Jira    https://localhost:443/jira    user   password
        Full list of arguments https://atlassian-python-api.readthedocs.io/index.html
        """
        self._session = Jira(url=url, username=username, password=password, **kwargs)
        logger.debug("Connected to JIRA")
        return self._session

    def __getattr__(self, name):
        func = None
        if name in self._jira.__dict__.keys():
            func = getattr(self._jira, name)

        if func:
            return _str_vars_to_data(func)
        raise AttributeError("Non-existing keyword " + name)
