import pytest
from qtpy import PYSIDE2, PYSIDE6, PYQT5, PYQT6

def test_qtopengl():
    """Test the qtpy.QtOpenGL namespace"""
    from qtpy import QtOpenGL

    assert QtOpenGL.QOpenGLBuffer is not None
    assert QtOpenGL.QOpenGLContext is not None
    assert QtOpenGL.QOpenGLContextGroup is not None
    assert QtOpenGL.QOpenGLDebugLogger is not None
    assert QtOpenGL.QOpenGLDebugMessage is not None
    assert QtOpenGL.QOpenGLFramebufferObject is not None
    assert QtOpenGL.QOpenGLFramebufferObjectFormat is not None
    assert QtOpenGL.QOpenGLPixelTransferOptions is not None
    assert QtOpenGL.QOpenGLShader is not None
    assert QtOpenGL.QOpenGLShaderProgram is not None
    assert QtOpenGL.QOpenGLTexture is not None
    assert QtOpenGL.QOpenGLTextureBlitter is not None
    # These are not present on some architectures
    # assert QtOpenGL.QOpenGLTimeMonitor is not None
    # assert QtOpenGL.QOpenGLTimerQuery is not None
    assert QtOpenGL.QOpenGLVersionProfile is not None
    assert QtOpenGL.QOpenGLVertexArrayObject is not None
    assert QtOpenGL.QOpenGLWindow is not None


