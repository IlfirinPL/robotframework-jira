import pkg_resources
from .keywords import JIRAKeywords


__version__ = pkg_resources.get_distribution("robotframework-jira").version


class JIRALibrary(JIRAKeywords):
    """"""

    ROBOT_LIBRARY_SCOPE = "GLOBAL"
