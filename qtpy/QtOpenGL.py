# -----------------------------------------------------------------------------
# Copyright © 2009- The Spyder Development Team
#
# Licensed under the terms of the MIT License
# (see LICENSE.txt for details)
# -----------------------------------------------------------------------------
"""Provides QtOpenGL classes and functions."""

# Local imports
from . import PYQT5, PYQT6, PYSIDE2, PYSIDE6, PythonQtError

if PYQT5:
    from PyQt5.QtOpenGL import *
    from PyQt5.QtGui import (QOpenGLBuffer, QOpenGLFramebufferObject, QOpenGLFramebufferObjectFormat, QOpenGLShader,
                             QOpenGLShaderProgram, QOpenGLContext, QOpenGLContextGroup, QOpenGLDebugLogger,
                             QOpenGLDebugMessage,QOpenGLPixelTransferOptions, QOpenGLTexture, QOpenGLTextureBlitter,
                             QOpenGLTimeMonitor, QOpenGLTimerQuery, QOpenGLVersionProfile, QOpenGLVertexArrayObject,
                             QOpenGLWindow)
elif PYQT6:
    from PyQt6.QtOpenGL import *
    from PyQt6.QtGui import (QOpenGLContext, QOpenGLContextGroup)
elif PYSIDE6:
    from PySide6.QtOpenGL import *
    from PySide6.QtGui import (QOpenGLContext, QOpenGLContextGroup)
elif PYSIDE2:
    from PySide2.QtOpenGL import *
    from PySide2.QtGui import (QOpenGLBuffer, QOpenGLFramebufferObject, QOpenGLFramebufferObjectFormat, QOpenGLShader,
                               QOpenGLShaderProgram, QOpenGLContext, QOpenGLContextGroup, QOpenGLDebugLogger,
                               QOpenGLDebugMessage,QOpenGLPixelTransferOptions, QOpenGLTexture, QOpenGLTextureBlitter,
                               QOpenGLTimeMonitor, QOpenGLTimerQuery, QOpenGLVersionProfile, QOpenGLVertexArrayObject,
                               QOpenGLWindow)
else:
    raise PythonQtError('No Qt bindings could be found')

