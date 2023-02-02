# -----------------------------------------------------------------------------
# Copyright © 2014-2015 Colin Duquesnoy
# Copyright © 2009- The Spyder Development Team
#
# Licensed under the terms of the MIT License
# (see LICENSE.txt for details)
# -----------------------------------------------------------------------------

"""Provides QtGui classes and functions."""

from . import PYQT6, PYQT5, PYSIDE2, PYSIDE6

if PYQT5:
    from PyQt5.QtGui import *
    # Backport items moved to QtGui in Qt6
    from PyQt5.QtWidgets import QAction, QActionGroup, QFileSystemModel, QShortcut, QUndoCommand

    # Map missing/renamed methods
    QColor.toTuple = lambda self: (self.red(), self.green(), self.blue(), self.alpha())
    QColor.isValidColorName = QColor.isValidColor
    QColor.fromString = lambda name: QColor(name)
    QMouseEvent.position = lambda *args: QMouseEvent.pos(*args)

    # Fix enums in PyQt5 5.9.*
    from .enums_compat import demote_enums
    from PyQt5.QtCore import QT_VERSION_STR as __version__
    if PYQT5 and __version__.startswith('5.9.'):
        from PyQt5 import QtGui
        demote_enums(QtGui)
        del QtGui
    del __version__, demote_enums

elif PYQT6:
    from PyQt6 import QtGui
    from PyQt6.QtGui import *
    from PyQt6.QtOpenGL import *
    QFontMetrics.width = lambda self, *args, **kwargs: self.horizontalAdvance(*args, **kwargs)
    QFontMetricsF.width = lambda self, *args, **kwargs: self.horizontalAdvance(*args, **kwargs)

    # Map missing/renamed methods
    QDrag.exec_ = lambda self, *args, **kwargs: self.exec(*args, **kwargs)
    QGuiApplication.exec_ = QGuiApplication.exec
    QTextDocument.print_ = lambda self, *args, **kwargs: self.print(*args, **kwargs)
    QColor.toTuple = lambda self: (self.red(), self.green(), self.blue(), self.alpha())
    QColor.isValidColorName = QColor.isValidColor
    QColor.fromString = lambda name: QColor(name)

    # Allow unscoped access for enums inside the QtGui module
    from .enums_compat import promote_enums
    promote_enums(QtGui)
    del QtGui
elif PYSIDE2:
    from PySide2.QtGui import *
    # Backport items moved to QtGui in Qt6
    from PySide2.QtWidgets import QAction, QActionGroup, QFileSystemModel, QShortcut, QUndoCommand
    if hasattr(QFontMetrics, 'horizontalAdvance'):
        # Needed to prevent raising a DeprecationWarning when using QFontMetrics.width
        QFontMetrics.width = lambda self, *args, **kwargs: self.horizontalAdvance(*args, **kwargs)

    # Map missing/renamed methods
    QMouseEvent.position = lambda *args: QMouseEvent.pos(*args)
    QGuiApplication.exec = QGuiApplication.exec_
elif PYSIDE6:
    from PySide6.QtGui import *
    from PySide6.QtOpenGL import *
    from PySide6.QtWidgets import QFileSystemModel
    QFontMetrics.width = lambda self, *args, **kwargs: self.horizontalAdvance(*args, **kwargs)
    QFontMetricsF.width = lambda self, *args, **kwargs: self.horizontalAdvance(*args, **kwargs)

    # Map missing/renamed methods
    QTextDocument.print = lambda self, *args, **kwargs: self.print_(*args, **kwargs)

    # Map DeprecationWarning methods
    QDrag.exec_ = lambda self, *args, **kwargs: self.exec(*args, **kwargs)
    QGuiApplication.exec_ = QGuiApplication.exec
    QMouseEvent.pos = lambda *args: QMouseEvent.position(*args)

if PYSIDE2 or PYSIDE6:
    # PySide{2,6} do not accept the `mode` keyword argument in
    # QTextCursor.movePosition() even though it is a valid optional argument
    # as per C++ API. Fix this by monkeypatching.
    #
    # Notes:
    #
    # * The `mode` argument is called `arg__2` in PySide{2,6} as per
    #   QTextCursor.movePosition.__doc__ and __signature__. Using `arg__2` as
    #   keyword argument works as intended, so does using a positional
    #   argument. Tested with PySide2 5.15.0, 5.15.2.1 and 5.15.3 and PySide6
    #   6.3.0; older version, down to PySide 1, are probably affected as well [1].
    #
    # * PySide2 5.15.0 and 5.15.2.1 silently ignore invalid keyword arguments,
    #   i.e. passing the `mode` keyword argument has no effect and doesn’t
    #   raise an exception. Older versions, down to PySide 1, are probably
    #   affected as well [1]. At least PySide2 5.15.3 and PySide6 6.3.0 raise an
    #   exception when `mode` or any other invalid keyword argument is passed.
    #
    # [1] https://bugreports.qt.io/browse/PYSIDE-185
    movePosition = QTextCursor.movePosition
    def movePositionPatched(
        self,
        operation: QTextCursor.MoveOperation,
        mode: QTextCursor.MoveMode = QTextCursor.MoveAnchor,
        n: int = 1,
    ) -> bool:
        return movePosition(self, operation, mode, n)
    QTextCursor.movePosition = movePositionPatched
