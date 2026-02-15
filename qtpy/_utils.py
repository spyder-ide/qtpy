# -----------------------------------------------------------------------------
# Copyright © 2023- The Spyder Development Team
#
# Released under the terms of the MIT License
# (see LICENSE.txt for details)
# -----------------------------------------------------------------------------

"""Provides utility functions for use by QtPy itself."""
from functools import wraps
from typing import TYPE_CHECKING

from . import QtModuleNotInstalledError

if TYPE_CHECKING:
    from .QtWidgets import QAction


def _wrap_missing_optional_dep_error(
    attr_error,
    *,
    import_error,
    wrapper=QtModuleNotInstalledError,
    **wrapper_kwargs,
):
    """Create a __cause__-chained wrapper error for a missing optional dep."""
    qtpy_error = wrapper(**wrapper_kwargs)
    import_error.__cause__ = attr_error
    qtpy_error.__cause__ = import_error
    return qtpy_error


def getattr_missing_optional_dep(name, module_name, optional_names):
    """Wrap AttributeError in a special error if it matches."""
    attr_error = AttributeError(
        f"module {module_name!r} has no attribute {name!r}",
    )
    if name in optional_names:
        return _wrap_missing_optional_dep_error(
            attr_error,
            **optional_names[name],
        )
    return attr_error


def possibly_static_exec(cls, *args, **kwargs):
    """Call `self.exec` when `self` is given or a static method otherwise."""
    if not args and not kwargs:
        # A special case (`cls.exec_()`) to avoid the function resolving error
        return cls.exec()
    if isinstance(args[0], cls):
        if len(args) == 1 and not kwargs:
            # A special case (`self.exec_()`) to avoid the function resolving error
            return args[0].exec()
        return args[0].exec(*args[1:], **kwargs)

    return cls.exec(*args, **kwargs)


def possibly_static_exec_(cls, *args, **kwargs):
    """Call `self.exec` when `self` is given or a static method otherwise."""
    if not args and not kwargs:
        # A special case (`cls.exec()`) to avoid the function resolving error
        return cls.exec_()
    if isinstance(args[0], cls):
        if len(args) == 1 and not kwargs:
            # A special case (`self.exec()`) to avoid the function resolving error
            return args[0].exec_()
        return args[0].exec_(*args[1:], **kwargs)

    return cls.exec_(*args, **kwargs)


def set_shortcut(self, shortcut, old_set_shortcut):
    """Ensure that the type of `shortcut` is compatible to `QAction.setShortcut`."""
    from .QtCore import Qt
    from .QtGui import QKeySequence

    if isinstance(shortcut, (QKeySequence.StandardKey, Qt.Key, int)):
        shortcut = QKeySequence(shortcut)
    old_set_shortcut(self, shortcut)


def set_shortcuts(self, shortcuts, old_set_shortcuts):
    """Ensure that the type of `shortcuts` is compatible to `QAction.setShortcuts`."""
    from .QtCore import Qt
    from .QtGui import QKeySequence

    if isinstance(
        shortcuts,
        (QKeySequence, QKeySequence.StandardKey, Qt.Key, int, str),
    ):
        shortcuts = (shortcuts,)

    shortcuts = tuple(
        (
            QKeySequence(shortcut)
            if isinstance(shortcut, (QKeySequence.StandardKey, Qt.Key, int))
            else shortcut
        )
        for shortcut in shortcuts
    )
    old_set_shortcuts(self, shortcuts)


def add_action(self, *args, old_add_action, **kwargs):
    """
    Re-order arguments when calling the `addAction` function with the signature
    introduced in Qt 6.3.
    """
    import warnings
    from collections.abc import Callable
    from .QtCore import Qt
    from .QtGui import QIcon, QKeySequence

    new_args = list(args)
    if new_args and isinstance(new_args[0], QIcon):
        icon = new_args.pop(0)
    else:
        icon = None
    shortcut = kwargs.pop("shortcut", None)
    connection_type = kwargs.pop("type", None)
    if connection_type:
        warnings.warn("type argument is not supported in Qt<6.3")

    shortcut_types = (QKeySequence, QKeySequence.StandardKey, Qt.Key, str, int)
    if len(new_args) > 1 and isinstance(new_args[1], shortcut_types):
        # Qt6.3 signature (text, shortcut, receiver, member)
        shortcut = new_args.pop(1)
    elif (
        len(new_args) > 2
        and isinstance(new_args[1], Callable)
        and isinstance(new_args[2], shortcut_types)
    ):
        # Qt5 signature (arg__1, arg__2, arg__3)
        shortcut = new_args.pop(2)
    elif len(new_args) > 3 and isinstance(new_args[3], shortcut_types):
        # Qt5 signature (text, receiver, member, shortcut)
        shortcut = new_args.pop(3)

    if icon is not None:
        new_args.insert(0, icon)
    action = old_add_action(self, *new_args, **kwargs)

    if shortcut is not None:
        action.setShortcut(shortcut)

    return action


def static_method_kwargs_wrapper(func, from_kwarg_name, to_kwarg_name):
    """
    Helper function to manage `from_kwarg_name` to `to_kwarg_name` kwargs name changes
    in static methods.

    Makes static methods accept the `from_kwarg_name` kwarg as `to_kwarg_name`.
    """

    @staticmethod
    @wraps(func)
    def _from_kwarg_name_to_kwarg_name_(*args, **kwargs):
        if from_kwarg_name in kwargs:
            kwargs[to_kwarg_name] = kwargs.pop(from_kwarg_name)
        return func(*args, **kwargs)

    return _from_kwarg_name_to_kwarg_name_
