# -----------------------------------------------------------------------------
# Copyright © 2014-2015 Colin Duquesnoy
# Copyright © 2009- The Spyder Development Team
#
# Licensed under the terms of the MIT License
# (see LICENSE.txt for details)
# -----------------------------------------------------------------------------

"""Provides QtGui classes and functions."""
from functools import partial, partialmethod

from . import PYQT5, PYQT6, PYSIDE2, PYSIDE6
from ._utils import possibly_static_exec, to_q_point_f


_QTOPENGL_NAMES = {
    "QOpenGLBuffer",
    "QOpenGLContext",
    "QOpenGLContextGroup",
    "QOpenGLDebugLogger",
    "QOpenGLDebugMessage",
    "QOpenGLFramebufferObject",
    "QOpenGLFramebufferObjectFormat",
    "QOpenGLPixelTransferOptions",
    "QOpenGLShader",
    "QOpenGLShaderProgram",
    "QOpenGLTexture",
    "QOpenGLTextureBlitter",
    "QOpenGLVersionProfile",
    "QOpenGLVertexArrayObject",
    "QOpenGLWindow",
}


def __getattr__(name):
    """Custom getattr to chain and wrap errors due to missing optional deps."""
    from ._utils import getattr_missing_optional_dep

    raise getattr_missing_optional_dep(
        name,
        module_name=__name__,
        optional_names=getattr(__getattr__, "_missing_optional_names", dict()),
    )


setattr(__getattr__, "_missing_optional_names", dict())


if PYQT5:
    from PyQt5.QtGui import *

    # Backport items moved to QtGui in Qt6
    from PyQt5.QtWidgets import (
        QAction,
        QActionGroup,
        QFileSystemModel,
        QShortcut,
        QUndoCommand,
    )

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
            getattr(__getattr__, "_missing_optional_names")[name] = {
                "name": "PyQt6.QtOpenGL",
                "missing_package": "pyopengl",
                "import_error": error,
            }

    QFontMetrics.width = lambda self, *args, **kwargs: self.horizontalAdvance(
        *args,
        **kwargs,
    )
    QFontMetricsF.width = lambda self, *args, **kwargs: self.horizontalAdvance(
        *args,
        **kwargs,
    )

    # Map missing/renamed methods
    QDrag.exec_ = partialmethod(QDrag.exec)
    QGuiApplication.exec_ = partial(
        lambda *args, _function, **kwargs: _function(
            QGuiApplication, *args, **kwargs
        ),
        _function=possibly_static_exec,
    )
    QTextDocument.print_ = partialmethod(QTextDocument.print)

    # Allow unscoped access for enums inside the QtGui module
    from .enums_compat import promote_enums

    promote_enums(QtGui)
    del QtGui, promote_enums
elif PYSIDE2:
    from PySide2.QtGui import *

    # Backport items moved to QtGui in Qt6
    from PySide2.QtWidgets import (
        QAction,
        QActionGroup,
        QFileSystemModel,
        QShortcut,
        QUndoCommand,
    )

    if hasattr(QFontMetrics, "horizontalAdvance"):
        # Needed to prevent raising a DeprecationWarning when using QFontMetrics.width
        QFontMetrics.width = partialmethod(QFontMetrics.horizontalAdvance)
elif PYSIDE6:
    from PySide6.QtGui import *

    # Attempt to import QOpenGL* classes, but if that fails,
    # don't raise an exception until the name is explicitly accessed.
    # See https://github.com/spyder-ide/qtpy/pull/387/
    try:
        from PySide6.QtOpenGL import *
    except ImportError as error:
        for name in _QTOPENGL_NAMES:
            getattr(__getattr__, "_missing_optional_names")[name] = {
                "name": "PySide6.QtOpenGL",
                "missing_package": "pyopengl",
                "import_error": error,
            }

    # Backport `QFileSystemModel` moved to QtGui in Qt6
    from PySide6.QtWidgets import QFileSystemModel

    QFontMetrics.width = partialmethod(QFontMetrics.horizontalAdvance)
    QFontMetricsF.width = partialmethod(QFontMetricsF.horizontalAdvance)

    # Map DeprecationWarning methods
    QDrag.exec_ = partialmethod(QDrag.exec)
    QGuiApplication.exec_ = partial(
        lambda *args, _function, **kwargs: _function(
            QGuiApplication, *args, **kwargs
        ),
        _function=possibly_static_exec,
    )

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
    #   i.e. passing the `mode` keyword argument has no effect and doesn't
    #   raise an exception. Older versions, down to PySide 1, are probably
    #   affected as well [1]. At least PySide2 5.15.3 and PySide6 6.3.0 raise an
    #   exception when `mode` or any other invalid keyword argument is passed.
    #
    # [1] https://bugreports.qt.io/browse/PYSIDE-185

    def movePositionPatched(
        self,
        operation: QTextCursor.MoveOperation,
        mode: QTextCursor.MoveMode = QTextCursor.MoveAnchor,
        n: int = 1,
        *,
        movePosition,
    ) -> bool:
        return movePosition(self, operation, mode, n)

    QTextCursor.movePosition = partialmethod(
        movePositionPatched,
        movePosition=QTextCursor.movePosition,
    )

    del movePositionPatched

if PYQT5 or PYSIDE2:
    # Part of the fix for https://github.com/spyder-ide/qtpy/issues/394
    QNativeGestureEvent.x = lambda self: self.localPos().toPoint().x()
    QNativeGestureEvent.y = lambda self: self.localPos().toPoint().y()
    QNativeGestureEvent.position = lambda self: self.localPos()
    QNativeGestureEvent.globalX = lambda self: self.globalPos().x()
    QNativeGestureEvent.globalY = lambda self: self.globalPos().y()
    QNativeGestureEvent.globalPosition = partialmethod(
        to_q_point_f, get_point_method="globalPos"
    )
    QEnterEvent.position = lambda self: self.localPos()
    QEnterEvent.globalPosition = partialmethod(
        to_q_point_f, get_point_method="globalPos"
    )
    QTabletEvent.position = lambda self: self.posF()
    QTabletEvent.globalPosition = lambda self: self.globalPosF()
    QHoverEvent.x = lambda self: self.pos().x()
    QHoverEvent.y = lambda self: self.pos().y()
    QHoverEvent.position = lambda self: self.posF()
    # No `QHoverEvent.globalPosition`, `QHoverEvent.globalX`,
    # nor `QHoverEvent.globalY` in the Qt5 docs.
    QMouseEvent.position = lambda self: self.localPos()
    QMouseEvent.globalPosition = partialmethod(
        to_q_point_f, get_point_method="globalPos"
    )

    # Follow similar approach for `QDropEvent` and child classes
    QDropEvent.position = lambda self: self.posF()
if PYQT6 or PYSIDE6:
    # Part of the fix for https://github.com/spyder-ide/qtpy/issues/394
    for _class in (
        QNativeGestureEvent,
        QEnterEvent,
        QTabletEvent,
        QHoverEvent,
        QMouseEvent,
    ):
        for _obsolete_function in (
            "pos",
            "x",
            "y",
            "globalPos",
            "globalX",
            "globalY",
        ):
            if hasattr(_class, _obsolete_function):
                delattr(_class, _obsolete_function)
    del _class, _obsolete_function

    QSinglePointEvent.pos = lambda self: self.position().toPoint()
    QSinglePointEvent.posF = lambda self: self.position()
    QSinglePointEvent.localPos = lambda self: self.position()
    QSinglePointEvent.x = lambda self: self.position().toPoint().x()
    QSinglePointEvent.y = lambda self: self.position().toPoint().y()
    QSinglePointEvent.globalPos = lambda self: self.globalPosition().toPoint()
    QSinglePointEvent.globalX = (
        lambda self: self.globalPosition().toPoint().x()
    )
    QSinglePointEvent.globalY = (
        lambda self: self.globalPosition().toPoint().y()
    )

    # Follow similar approach for `QDropEvent` and child classes
    QDropEvent.pos = lambda self: self.position().toPoint()
    QDropEvent.posF = lambda self: self.position()

# Clean up the namespace
del PYQT5, PYQT6, PYSIDE2, PYSIDE6
del partial, partialmethod
del possibly_static_exec, to_q_point_f
del _QTOPENGL_NAMES
