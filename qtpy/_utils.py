# -----------------------------------------------------------------------------
# Copyright © 2023- The Spyder Development Team
#
# Released under the terms of the MIT License
# (see LICENSE.txt for details)
# -----------------------------------------------------------------------------

"""Provides utility functions for use by QtPy itself."""
from functools import wraps
from typing import TYPE_CHECKING

import qtpy

if TYPE_CHECKING:
    from qtpy.QtWidgets import QAction


def _wrap_missing_optional_dep_error(
    attr_error,
    *,
    import_error,
    wrapper=qtpy.QtModuleNotInstalledError,
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


def add_action(self, *args, old_add_action):
    """Re-order arguments of `addAction` to backport compatibility with Qt>=6.3."""
    from qtpy.QtCore import QObject
    from qtpy.QtGui import QIcon, QKeySequence

    action: QAction
    icon: QIcon
    text: str
    shortcut: QKeySequence | QKeySequence.StandardKey | str | int

    # if args and isinstance(args[0], QIcon):
    if any(
        isinstance(arg, QIcon) for arg in args[:1]
    ):  # Better to use previous line instead of this
        icon, *args = args
    else:
        icon = QIcon()

    if (
        all(
            isinstance(arg, t)
            for arg, t in zip(
                args,
                [
                    str,
                    (QKeySequence, QKeySequence.StandardKey, str, int),
                    QObject,
                    bytes,
                ],
            )
        )
        and len(args) >= 2
    ):
        text, shortcut, *args = args
        action = old_add_action(self, icon, text, *args)
        action.setShortcut(shortcut)
        return action

    return old_add_action(self, *args)


def static_method_kwargs_wrapper(func, from_kwarg_name, to_kwarg_name):
    """
    Helper function to manage `from_kwarg_name` to `to_kwarg_name` kwargs name changes in static methods.

    Makes static methods accept the `from_kwarg_name` kwarg as `to_kwarg_name`.
    """

    @staticmethod
    @wraps(func)
    def _from_kwarg_name_to_kwarg_name_(*args, **kwargs):
        if from_kwarg_name in kwargs:
            kwargs[to_kwarg_name] = kwargs.pop(from_kwarg_name)
        return func(*args, **kwargs)

    return _from_kwarg_name_to_kwarg_name_
