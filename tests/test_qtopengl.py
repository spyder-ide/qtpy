import pytest

from qtpy import PYQT5, PYQT_VERSION, QtOpenGL


def test_qtopengl():
    """Test the qtpy.QtOpenGL namespace"""
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
    assert QtOpenGL.QOpenGLVersionProfile is not None
    assert QtOpenGL.QOpenGLVertexArrayObject is not None
    assert QtOpenGL.QOpenGLWindow is not None
    # We do not test for QOpenGLTimeMonitor or QOpenGLTimerQuery as
    # they are not present on some architectures such as armhf


@pytest.mark.skipif(
    PYQT5 and PYQT_VERSION.startswith("5.9"),
    reason=(
        "A specific setup with at least sip 4.9.9 is needed for PyQt5 5.9.* "
        "to work with scoped enum access"
    ),
)
def test_enum_access():
    """Test scoped and unscoped enum access."""
    assert (
        QtOpenGL.QOpenGLBuffer.RangeRead
        == QtOpenGL.QOpenGLBuffer.RangeAccessFlag.RangeRead
    )
