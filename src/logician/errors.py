from vt.utils.errors.error_specs.exceptions import (
    VTCmdException,
    VTCmdNotFoundError,
    VTException,
    VTExitingException,
)


class LogicianException(VTException):
    """
    Exception particular to ``logician``.
    """


class LogicianExitingException(LogicianException, VTExitingException):
    """
    A ``logician`` exception that allows exiting with an ``error_code``.
    """


class LogicianCmdException(LogicianExitingException, VTCmdException):
    """
    A ``logician`` exception that can denote exceptional scenario from a command run.
    """


class LogicianCmdNotFoundError(LogicianExitingException, VTCmdNotFoundError):
    """
    A ``logician`` exception that specifies a command not found.
    """
