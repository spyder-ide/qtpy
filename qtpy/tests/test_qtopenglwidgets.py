import importlib
from typing import TYPE_CHECKING

import pytest

from qtpy import API_NAME, PYQT5, PYSIDE2

if TYPE_CHECKING:
    from types import ModuleType


@pytest.mark.skipif(PYSIDE2 or PYQT5, reason="Not available in PySide2/PyQt5")
def test_qtopenglwidgets():
    """Test the qtpy.QtOpenGLWidgets namespace"""
    from qtpy import QtOpenGLWidgets

    assert QtOpenGLWidgets.QOpenGLWidget is not None


@pytest.mark.skipif(PYSIDE2 or PYQT5, reason="Not available in PySide2/PyQt5")
def test_namespace_not_polluted():
    """Test that no extra members are exported into the module namespace."""
    from qtpy import QtOpenGLWidgets

    qtpy_module: ModuleType = QtOpenGLWidgets
    original_module: ModuleType = importlib.import_module(
        qtpy_module.__name__.replace("qtpy", API_NAME),
    )

    extra_members = (
        frozenset(dir(qtpy_module))
        - frozenset(dir(original_module))
        - frozenset(
            # These are unavoidable:
            [
                "__builtins__",
                "__cached__",
            ],
        )
    )
    assert not extra_members
