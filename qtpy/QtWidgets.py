# -----------------------------------------------------------------------------
# Copyright © 2014-2015 Colin Duquesnoy
# Copyright © 2009- The Spyder Development Team
#
# Licensed under the terms of the MIT License
# (see LICENSE.txt for details)
# -----------------------------------------------------------------------------

"""Provides widget classes and functions."""

from . import PYQT5, PYQT6, PYSIDE2, PYSIDE6

if PYQT5:
    from PyQt5.QtWidgets import *

    # Fix enums in PyQt5 5.9.*
    from PyQt5.QtCore import QT_VERSION_STR as __version__
    if __version__.startswith('5.9.'):
        from .enums_compat import demote_enums
        from PyQt5 import QtWidgets
        demote_enums(QtWidgets)
        del QtWidgets, demote_enums
    del __version__
elif PYQT6:
    from PyQt6 import QtWidgets
    from PyQt6.QtWidgets import *
    from PyQt6.QtGui import QAction, QActionGroup, QShortcut, QFileSystemModel, QUndoCommand
    from PyQt6.QtOpenGLWidgets import QOpenGLWidget

    # Map missing/renamed methods
    QTextEdit.setTabStopWidth = lambda self, width: self.setTabStopDistance(round(width))
    QTextEdit.tabStopWidth = lambda self: round(self.tabStopDistance())
    QTextEdit.print_ = lambda self, *args, **kwargs: self.print(*args, **kwargs)
    QPlainTextEdit.setTabStopWidth = lambda self, width: self.setTabStopDistance(round(width))
    QPlainTextEdit.tabStopWidth = lambda self: round(self.tabStopDistance())
    QPlainTextEdit.print_ = lambda self, *args, **kwargs: self.print(*args, **kwargs)
    QApplication.exec_ = lambda self, *args, **kwargs: self.exec(*args, **kwargs)
    QDialog.exec_ = lambda self, *args, **kwargs: self.exec(*args, **kwargs)
    QMenu.exec_ = lambda self, *args, **kwargs: self.exec(*args, **kwargs)
    QLineEdit.getTextMargins = lambda self: (self.textMargins().left(), self.textMargins().top(), self.textMargins().right(), self.textMargins().bottom())

    # Allow unscoped access for enums inside the QtWidgets module
    from .enums_compat import promote_enums
    promote_enums(QtWidgets)
    del QtWidgets
elif PYSIDE2:
    from PySide2.QtWidgets import *

    # Map missing/renamed methods
    QApplication.exec = lambda self, *args, **kwargs: self.exec_(*args, **kwargs)
    QDialog.exec = lambda self, *args, **kwargs: self.exec_(*args, **kwargs)
    QMenu.exec = lambda self, *args, **kwargs: self.exec_(*args, **kwargs)
    QTextEdit.print = lambda self, *args, **kwargs: self.print_(*args, **kwargs)
    QPlainTextEdit.print = lambda self, *args, **kwargs: self.print_(*args, **kwargs)
elif PYSIDE6:
    from PySide6.QtWidgets import *
    from PySide6.QtGui import QAction, QActionGroup, QShortcut, QUndoCommand
    from PySide6.QtOpenGLWidgets import QOpenGLWidget

    # Map missing/renamed methods
    QTextEdit.setTabStopWidth = lambda self, width: self.setTabStopDistance(round(width))
    QTextEdit.tabStopWidth = lambda self: round(self.tabStopDistance())
    QTextEdit.print = lambda self, *args, **kwargs: self.print_(*args, **kwargs)
    QPlainTextEdit.setTabStopWidth = lambda self, width: self.setTabStopDistance(round(width))
    QPlainTextEdit.tabStopWidth = lambda self: round(self.tabStopDistance())
    QPlainTextEdit.print = lambda self, *args, **kwargs: self.print_(*args, **kwargs)
    QLineEdit.getTextMargins = lambda self: (self.textMargins().left(), self.textMargins().top(), self.textMargins().right(), self.textMargins().bottom())

    # Map DeprecationWarning methods
    QApplication.exec_ = lambda self, *args, **kwargs: self.exec(*args, **kwargs)
    QDialog.exec_ = lambda self, *args, **kwargs: self.exec(*args, **kwargs)
    QMenu.exec_ = lambda self, *args, **kwargs: self.exec(*args, **kwargs)
