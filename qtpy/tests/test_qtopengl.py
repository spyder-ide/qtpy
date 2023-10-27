# coding=utf-8
import importlib
from types import ModuleType

from qtpy import API_NAME, QtOpenGL


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


def test_namespace_not_polluted():
    """Test that no extra members are exported into the module namespace."""
    qtpy_module: ModuleType = QtOpenGL
    original_module: ModuleType = importlib.import_module(
        qtpy_module.__name__.replace('qtpy', API_NAME)
    )

    extra_members = (
        frozenset(dir(qtpy_module))
        - frozenset(dir(original_module))
        - frozenset(
            # These are unavoidable:
            [
                "__builtins__",
                "__cached__",
            ]
        )
        - frozenset(
            # These are imported from `QtGui`:
            [
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
                "QOpenGLTimeMonitor",
                "QOpenGLTimerQuery",
            ]
        )
    )
    assert not extra_members
