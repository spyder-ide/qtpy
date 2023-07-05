# -----------------------------------------------------------------------------
# Copyright © 2014-2015 Colin Duquesnoy
# Copyright © 2009- The Spyder Development Team
#
# Licensed under the terms of the MIT License
# (see LICENSE.txt for details)
# -----------------------------------------------------------------------------

"""Provides widget classes and functions."""
from functools import partialmethod, wraps

from packaging.version import parse

from . import PYQT5, PYQT6, PYSIDE2, PYSIDE6, QtModuleNotInstalledError
from ._utils import add_action, possibly_static_exec, getattr_missing_optional_dep
from .QtCore import __version__ as _qt_version


_missing_optional_names = {}


def __getattr__(name):
    """Custom getattr to chain and wrap errors due to missing optional deps."""
    raise getattr_missing_optional_dep(
        name, module_name=__name__, optional_names=_missing_optional_names)

def _dir_to_directory(func):
    @wraps(func)
    def _dir_to_directory_(*args, **kwargs):
        if "dir" in kwargs:
            kwargs["directory"] = kwargs.pop("dir")
        return func(*args, **kwargs)
    return _dir_to_directory_

def _directory_to_dir(func):
    @wraps(func)
    def _directory_to_dir_(*args, **kwargs):
        if "directory" in kwargs:
            kwargs["dir"] = kwargs.pop("directory")
        return func(*args, **kwargs)
    return _directory_to_dir_


if PYQT5:
    from PyQt5.QtWidgets import *
elif PYQT6:
    from PyQt6 import QtWidgets
    from PyQt6.QtWidgets import *
    from PyQt6.QtGui import QAction, QActionGroup, QShortcut, QFileSystemModel, QUndoCommand

    # Attempt to import QOpenGLWidget, but if that fails,
    # don't raise an exception until the name is explicitly accessed.
    # See https://github.com/spyder-ide/qtpy/pull/387/
    try:
        from PyQt6.QtOpenGLWidgets import QOpenGLWidget
    except ImportError as error:
        _missing_optional_names['QOpenGLWidget'] = {
           'name': 'PyQt6.QtOpenGLWidgets',
           'missing_package': 'pyopengl',
           'import_error': error,
        }

    # Map missing/renamed methods
    QTextEdit.setTabStopWidth = lambda self, *args, **kwargs: self.setTabStopDistance(*args, **kwargs)
    QTextEdit.tabStopWidth = lambda self, *args, **kwargs: self.tabStopDistance(*args, **kwargs)
    QTextEdit.print_ = lambda self, *args, **kwargs: self.print(*args, **kwargs)
    QPlainTextEdit.setTabStopWidth = lambda self, *args, **kwargs: self.setTabStopDistance(*args, **kwargs)
    QPlainTextEdit.tabStopWidth = lambda self, *args, **kwargs: self.tabStopDistance(*args, **kwargs)
    QPlainTextEdit.print_ = lambda self, *args, **kwargs: self.print(*args, **kwargs)
    QApplication.exec_ = lambda *args, **kwargs: possibly_static_exec(QApplication, *args, **kwargs)
    QDialog.exec_ = lambda self, *args, **kwargs: self.exec(*args, **kwargs)
    QMenu.exec_ = lambda *args, **kwargs: possibly_static_exec(QMenu, *args, **kwargs)
    QLineEdit.getTextMargins = lambda self: (self.textMargins().left(), self.textMargins().top(), self.textMargins().right(), self.textMargins().bottom())

    # Allow unscoped access for enums inside the QtWidgets module
    from .enums_compat import promote_enums
    promote_enums(QtWidgets)
    del QtWidgets
elif PYSIDE2:
    from PySide2.QtWidgets import *
elif PYSIDE6:
    from PySide6.QtWidgets import *
    from PySide6.QtGui import QAction, QActionGroup, QShortcut, QUndoCommand

    # Attempt to import QOpenGLWidget, but if that fails,
    # don't raise an exception until the name is explicitly accessed.
    # See https://github.com/spyder-ide/qtpy/pull/387/
    try:
        from PySide6.QtOpenGLWidgets import QOpenGLWidget
    except ImportError as error:
        _missing_optional_names['QOpenGLWidget'] = {
           'name': 'PySide6.QtOpenGLWidgets',
           'missing_package': 'pyopengl',
           'import_error': error,
        }

    # Map missing/renamed methods
    QTextEdit.setTabStopWidth = lambda self, *args, **kwargs: self.setTabStopDistance(*args, **kwargs)
    QTextEdit.tabStopWidth = lambda self, *args, **kwargs: self.tabStopDistance(*args, **kwargs)
    QPlainTextEdit.setTabStopWidth = lambda self, *args, **kwargs: self.setTabStopDistance(*args, **kwargs)
    QPlainTextEdit.tabStopWidth = lambda self, *args, **kwargs: self.tabStopDistance(*args, **kwargs)
    QLineEdit.getTextMargins = lambda self: (self.textMargins().left(), self.textMargins().top(), self.textMargins().right(), self.textMargins().bottom())

    # Map DeprecationWarning methods
    QApplication.exec_ = lambda *args, **kwargs: possibly_static_exec(QApplication, *args, **kwargs)
    QDialog.exec_ = lambda self, *args, **kwargs: self.exec(*args, **kwargs)
    QMenu.exec_ = lambda *args, **kwargs: possibly_static_exec(QMenu, *args, **kwargs)


if PYSIDE2 or PYSIDE6:
    QFileDialog.getExistingDirectory = _directory_to_dir(QFileDialog.getExistingDirectory)
    QFileDialog.getOpenFileName = _directory_to_dir(QFileDialog.getOpenFileName)
    QFileDialog.getOpenFileNames = _directory_to_dir(QFileDialog.getOpenFileNames)
    QFileDialog.getSaveFileName = _directory_to_dir(QFileDialog.getSaveFileName)
else:
    QFileDialog.getExistingDirectory = _dir_to_directory(QFileDialog.getExistingDirectory)
    QFileDialog.getOpenFileName = _dir_to_directory(QFileDialog.getOpenFileName)
    QFileDialog.getOpenFileNames = _dir_to_directory(QFileDialog.getOpenFileNames)
    QFileDialog.getSaveFileName = _dir_to_directory(QFileDialog.getSaveFileName)

# Make `addAction` compatible with Qt6 >= 6.3
if PYQT5 or PYSIDE2 or parse(_qt_version) < parse('6.3'):
    QMenu.addAction = partialmethod(add_action, old_add_action=QMenu.addAction)
    QToolBar.addAction = partialmethod(add_action, old_add_action=QToolBar.addAction)
