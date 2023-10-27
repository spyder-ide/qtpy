# coding=utf-8
import importlib
from types import ModuleType

import pytest

from qtpy import API_NAME, PYQT5, PYSIDE2


@pytest.mark.skipif(PYQT5 or PYSIDE2, reason="Only available in Qt6 bindings")
def test_qtwebenginequick():
    """Test the qtpy.QtWebEngineQuick namespace"""

    QtWebEngineQuick = pytest.importorskip("qtpy.QtWebEngineQuick")

    assert QtWebEngineQuick.QtWebEngineQuick is not None
    assert QtWebEngineQuick.QQuickWebEngineProfile is not None


@pytest.mark.skipif(PYQT5 or PYSIDE2, reason="Only available in Qt6 bindings")
def test_namespace_not_polluted():
    """Test that no extra members are exported into the module namespace."""
    qtpy_module: ModuleType = pytest.importorskip("qtpy.QtWebEngineQuick")
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
    )
    assert not extra_members
