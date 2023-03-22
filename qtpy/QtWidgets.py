# -----------------------------------------------------------------------------
# Copyright © 2014-2015 Colin Duquesnoy
# Copyright © 2009- The Spyder Development Team
#
# Licensed under the terms of the MIT License
# (see LICENSE.txt for details)
# -----------------------------------------------------------------------------

"""Provides widget classes and functions."""

from . import PYQT5, PYQT6, PYSIDE2, PYSIDE6, QtModuleNotInstalledError


MISSING_SYMBOL_ERRORS = {}


if PYQT5:
    from PyQt5.QtWidgets import *
elif PYQT6:
    from PyQt6 import QtWidgets
    from PyQt6.QtWidgets import *
    from PyQt6.QtGui import QAction, QActionGroup, QShortcut, QFileSystemModel, QUndoCommand

    # Attempt to import QOpenGLWidget, but if that fails, don't throw an exception until the
    # symbol is explicitly asked for
    # this allows removing the sizeable OpenGL binaries from pyinstaller bundles, but
    # maintains compatibility with apps that expect this symbol to be automatically imported
    try:
        from PyQt6.QtOpenGLWidgets import QOpenGLWidget
    except ImportError:
        MISSING_SYMBOL_ERRORS['QOpenGLWidget'] = QtModuleNotInstalledError(name='PyQt6.QtOpenGLWidgets', missing_package='pyopengl')

    # Map missing/renamed methods
    QTextEdit.setTabStopWidth = lambda self, *args, **kwargs: self.setTabStopDistance(*args, **kwargs)
    QTextEdit.tabStopWidth = lambda self, *args, **kwargs: self.tabStopDistance(*args, **kwargs)
    QTextEdit.print_ = lambda self, *args, **kwargs: self.print(*args, **kwargs)
    QPlainTextEdit.setTabStopWidth = lambda self, *args, **kwargs: self.setTabStopDistance(*args, **kwargs)
    QPlainTextEdit.tabStopWidth = lambda self, *args, **kwargs: self.tabStopDistance(*args, **kwargs)
    QPlainTextEdit.print_ = lambda self, *args, **kwargs: self.print(*args, **kwargs)
    QApplication.exec_ = QApplication.exec
    QDialog.exec_ = lambda self, *args, **kwargs: self.exec(*args, **kwargs)
    QMenu.exec_ = lambda self, *args, **kwargs: self.exec(*args, **kwargs)
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

    # Attempt to import QOpenGLWidget, but if that fails, don't throw an exception until the
    # symbol is explicitly asked for
    # this allows removing the sizeable OpenGL binaries from pyinstaller bundles, but
    # maintains compatibility with apps that expect this symbol to be automatically imported
    try:
        from PySide6.QtOpenGLWidgets import QOpenGLWidget
    except ImportError:
        MISSING_SYMBOL_ERRORS['QOpenGLWidget'] = QtModuleNotInstalledError(name='PySide6.QtOpenGLWidgets', missing_package='pyopengl')

    # Map missing/renamed methods
    QTextEdit.setTabStopWidth = lambda self, *args, **kwargs: self.setTabStopDistance(*args, **kwargs)
    QTextEdit.tabStopWidth = lambda self, *args, **kwargs: self.tabStopDistance(*args, **kwargs)
    QPlainTextEdit.setTabStopWidth = lambda self, *args, **kwargs: self.setTabStopDistance(*args, **kwargs)
    QPlainTextEdit.tabStopWidth = lambda self, *args, **kwargs: self.tabStopDistance(*args, **kwargs)
    QLineEdit.getTextMargins = lambda self: (self.textMargins().left(), self.textMargins().top(), self.textMargins().right(), self.textMargins().bottom())

    # Map DeprecationWarning methods
    QApplication.exec_ = QApplication.exec
    QDialog.exec_ = lambda self, *args, **kwargs: self.exec(*args, **kwargs)
    QMenu.exec_ = lambda self, *args, **kwargs: self.exec(*args, **kwargs)


def __getattr__(name):
    if name in MISSING_SYMBOL_ERRORS:
        raise MISSING_SYMBOL_ERRORS[name]
    else:
        raise AttributeError(f'module {__name__!r} has no attribute {name!r}')
