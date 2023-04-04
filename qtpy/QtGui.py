# -----------------------------------------------------------------------------
# Copyright © 2014-2015 Colin Duquesnoy
# Copyright © 2009- The Spyder Development Team
#
# Licensed under the terms of the MIT License
# (see LICENSE.txt for details)
# -----------------------------------------------------------------------------

"""Provides QtGui classes and functions."""

from . import PYQT6, PYQT5, PYSIDE2, PYSIDE6, QtModuleNotInstalledError
from .utils import _getattr_missing_optional_dep


_missing_optional_names = {}

_QTOPENGL_NAMES = {
    'QOpenGLBuffer',
    'QOpenGLFramebufferObject',
    'QOpenGLFramebufferObjectFormat',
    'QOpenGLShader',
    'QOpenGLShaderProgram',
    'QOpenGLContext',
    'QOpenGLContextGroup',
    'QOpenGLDebugLogger',
    'QOpenGLDebugMessage',
    'QOpenGLPixelTransferOptions',
    'QOpenGLTexture',
    'QOpenGLTextureBlitter',
    'QOpenGLVersionProfile',
    'QOpenGLVertexArrayObject',
    'QOpenGLWindow',
}


if PYQT5:
    from PyQt5.QtGui import *

    # Backport items moved to QtGui in Qt6
    from PyQt5.QtWidgets import QAction, QActionGroup, QFileSystemModel, QShortcut, QUndoCommand
elif PYQT6:
    from PyQt6 import QtGui
    from PyQt6.QtGui import *

    # Attempt to import QOpenGL* classes, but if that fails,
    # don't raise an exception until the name is explicitly accessed.
    # See https://github.com/spyder-ide/qtpy/pull/387/
    try:
        from PyQt6.QtOpenGL import *
    except ImportError as error:
        for name in _QTOPENGL_NAMES:
            _missing_optional_names[name] = {
                'name': 'PyQt6.QtOpenGL',
                'missing_package': 'pyopengl',
                'import_error': error,
            }

    QFontMetrics.width = lambda self, *args, **kwargs: self.horizontalAdvance(*args, **kwargs)
    QFontMetricsF.width = lambda self, *args, **kwargs: self.horizontalAdvance(*args, **kwargs)

    # Map missing/renamed methods
    QDrag.exec_ = lambda self, *args, **kwargs: self.exec(*args, **kwargs)
    QGuiApplication.exec_ = QGuiApplication.exec
    QTextDocument.print_ = lambda self, *args, **kwargs: self.print(*args, **kwargs)

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
elif PYSIDE6:
    from PySide6.QtGui import *

    # Attempt to import QOpenGL* classes, but if that fails,
    # don't raise an exception until the name is explicitly accessed.
    # See https://github.com/spyder-ide/qtpy/pull/387/
    try:
        from PySide6.QtOpenGL import *
    except ImportError as error:
        for name in _QTOPENGL_NAMES:
            _missing_optional_names[name] = {
                'name': 'PySide6.QtOpenGL',
                'missing_package': 'pyopengl',
                'import_error': error,
            }

    # Backport `QFileSystemModel` moved to QtGui in Qt6
    from PySide6.QtWidgets import QFileSystemModel

    QFontMetrics.width = lambda self, *args, **kwargs: self.horizontalAdvance(*args, **kwargs)
    QFontMetricsF.width = lambda self, *args, **kwargs: self.horizontalAdvance(*args, **kwargs)

    # Map DeprecationWarning methods
    QDrag.exec_ = lambda self, *args, **kwargs: self.exec(*args, **kwargs)
    QGuiApplication.exec_ = QGuiApplication.exec

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

# Fix https://github.com/spyder-ide/qtpy/issues/394
if PYQT5 or PYSIDE2:
    from qtpy.QtCore import QPointF as __QPointF
    QMouseEvent.position = lambda self: __QPointF(float(self.x()), float(self.y()))
    QMouseEvent.globalPosition = lambda self: __QPointF(float(self.globalX()), float(self.globalY()))
if PYQT6 or PYSIDE6:
    QMouseEvent.pos = lambda self: self.position().toPoint()
    QMouseEvent.x = lambda self: self.position().toPoint().x()
    QMouseEvent.y = lambda self: self.position().toPoint().y()
    QMouseEvent.globalPos = lambda self: self.globalPosition().toPoint()
    QMouseEvent.globalX = lambda self: self.globalPosition().toPoint().x()
    QMouseEvent.globalY = lambda self: self.globalPosition().toPoint().y()

def __getattr__(name):
    """Custom getattr to chain and wrap errors due to missing optional deps."""
    raise _getattr_missing_optional_dep(
        name, module_name=__name__, optional_names=_missing_optional_names)
