# -----------------------------------------------------------------------------
# Copyright © 2014-2015 Colin Duquesnoy
# Copyright © 2009- The Spyder Development Team
#
# Licensed under the terms of the MIT License
# (see LICENSE.txt for details)
# -----------------------------------------------------------------------------

"""Provides widget classes and functions."""
from functools import partial, partialmethod

from packaging.version import parse

from . import PYQT5, PYQT6, PYSIDE2, PYSIDE6, QT_VERSION, _utils


def __getattr__(attr):
    """Custom getattr to chain and wrap errors due to missing optional deps."""
    from ._utils import getattr_missing_optional_dep

    raise getattr_missing_optional_dep(
        attr,
        module_name=__name__,
        optional_names=__getattr__.missing_optional_names,
    )


__getattr__.missing_optional_names = {}


if PYQT5:
    from PyQt5.QtWidgets import *
elif PYQT6:
    from PyQt6 import QtWidgets
    from PyQt6.QtGui import (
        QAction,
        QActionGroup,
        QFileSystemModel,
        QShortcut,
        QUndoCommand,
    )
    from PyQt6.QtWidgets import *

    # Attempt to import QOpenGLWidget, but if that fails,
    # don't raise an exception until the name is explicitly accessed.
    # See https://github.com/spyder-ide/qtpy/pull/387/
    try:
        from PyQt6.QtOpenGLWidgets import QOpenGLWidget
    except ImportError as error:
        __getattr__.missing_optional_names["QOpenGLWidget"] = {
            "name": "PyQt6.QtOpenGLWidgets",
            "missing_package": "pyopengl",
            "import_error": error,
        }

    # Map missing/renamed methods
    QTextEdit.setTabStopWidth = partialmethod(QTextEdit.setTabStopDistance)
    QTextEdit.tabStopWidth = partialmethod(QTextEdit.tabStopDistance)
    QTextEdit.print_ = partialmethod(QTextEdit.print)
    QPlainTextEdit.setTabStopWidth = partialmethod(
        QPlainTextEdit.setTabStopDistance,
    )
    QPlainTextEdit.tabStopWidth = partialmethod(QPlainTextEdit.tabStopDistance)
    QPlainTextEdit.print_ = partialmethod(QPlainTextEdit.print)
    QApplication.exec_ = partial(
        lambda *args, _function, **kwargs: _function(
            QApplication,
            *args,
            **kwargs,
        ),
        _function=_utils.possibly_static_exec,
    )
    QDialog.exec_ = partialmethod(QDialog.exec)
    QMenu.exec_ = partialmethod(
        lambda *args, _function, **kwargs: _function(QMenu, *args, **kwargs),
        _function=_utils.possibly_static_exec,
    )
    QLineEdit.getTextMargins = lambda self: (
        self.textMargins().left(),
        self.textMargins().top(),
        self.textMargins().right(),
        self.textMargins().bottom(),
    )

    # Add removed definition for `QFileDialog.Options` as an alias of `QFileDialog.Option`
    # passing as default value 0 in the same way PySide6 6.5+ does.
    # Note that for PyQt5 and PySide2 those definitions are two different classes
    # (one is the flag definition and the other the enum definition)
    QFileDialog.Options = lambda value=0: QFileDialog.Option(value)

    # Allow unscoped access for enums inside the QtWidgets module
    from .enums_compat import promote_enums

    promote_enums(QtWidgets)
    del QtWidgets, promote_enums
elif PYSIDE2:
    from PySide2.QtWidgets import *
elif PYSIDE6:
    from PySide6.QtGui import QAction, QActionGroup, QShortcut, QUndoCommand
    from PySide6.QtWidgets import *

    # Attempt to import QOpenGLWidget, but if that fails,
    # don't raise an exception until the name is explicitly accessed.
    # See https://github.com/spyder-ide/qtpy/pull/387/
    try:
        from PySide6.QtOpenGLWidgets import QOpenGLWidget
    except ImportError as error:
        __getattr__.missing_optional_names["QOpenGLWidget"] = {
            "name": "PySide6.QtOpenGLWidgets",
            "missing_package": "pyopengl",
            "import_error": error,
        }

    # Map missing/renamed methods
    QTextEdit.setTabStopWidth = partialmethod(QTextEdit.setTabStopDistance)
    QTextEdit.tabStopWidth = partialmethod(QTextEdit.tabStopDistance)
    QPlainTextEdit.setTabStopWidth = partialmethod(
        QPlainTextEdit.setTabStopDistance,
    )
    QPlainTextEdit.tabStopWidth = partialmethod(QPlainTextEdit.tabStopDistance)
    QLineEdit.getTextMargins = lambda self: (
        self.textMargins().left(),
        self.textMargins().top(),
        self.textMargins().right(),
        self.textMargins().bottom(),
    )

    # Map DeprecationWarning methods
    QApplication.exec_ = partial(
        lambda *args, _function, **kwargs: _function(
            QApplication,
            *args,
            **kwargs,
        ),
        _function=_utils.possibly_static_exec,
    )
    QDialog.exec_ = partialmethod(QDialog.exec)
    QMenu.exec_ = partialmethod(
        lambda *args, _function, **kwargs: _function(QMenu, *args, **kwargs),
        _function=_utils.possibly_static_exec,
    )

    # Passing as default value 0 in the same way PySide6 < 6.3.2 does for the `QFileDialog.Options` definition.
    if parse(QT_VERSION) > parse("6.3"):
        QFileDialog.Options = lambda value=0: QFileDialog.Option(value)


if PYSIDE2 or PYSIDE6:
    # Make PySide2/6 `QFileDialog` static methods accept the `directory` kwarg as `dir`
    QFileDialog.getExistingDirectory = _utils.static_method_kwargs_wrapper(
        QFileDialog.getExistingDirectory,
        "directory",
        "dir",
    )
    QFileDialog.getOpenFileName = _utils.static_method_kwargs_wrapper(
        QFileDialog.getOpenFileName,
        "directory",
        "dir",
    )
    QFileDialog.getOpenFileNames = _utils.static_method_kwargs_wrapper(
        QFileDialog.getOpenFileNames,
        "directory",
        "dir",
    )
    QFileDialog.getSaveFileName = _utils.static_method_kwargs_wrapper(
        QFileDialog.getSaveFileName,
        "directory",
        "dir",
    )
else:
    # Make PyQt5/6 `QFileDialog` static methods accept the `dir` kwarg as `directory`
    QFileDialog.getExistingDirectory = _utils.static_method_kwargs_wrapper(
        QFileDialog.getExistingDirectory,
        "dir",
        "directory",
    )
    QFileDialog.getOpenFileName = _utils.static_method_kwargs_wrapper(
        QFileDialog.getOpenFileName,
        "dir",
        "directory",
    )
    QFileDialog.getOpenFileNames = _utils.static_method_kwargs_wrapper(
        QFileDialog.getOpenFileNames,
        "dir",
        "directory",
    )
    QFileDialog.getSaveFileName = _utils.static_method_kwargs_wrapper(
        QFileDialog.getSaveFileName,
        "dir",
        "directory",
    )

# Make `addAction` compatible with Qt6 >= 6.3
if PYQT5 or PYSIDE2 or parse(QT_VERSION) < parse("6.3"):
    QMenu.addAction = partialmethod(
        _utils.add_action,
        old_add_action=QMenu.addAction,
    )
    QToolBar.addAction = partialmethod(
        _utils.add_action,
        old_add_action=QToolBar.addAction,
    )

# Clean up the namespace
del PYQT5, PYQT6, PYSIDE2, PYSIDE6, QT_VERSION, _utils
del parse
del partial, partialmethod
