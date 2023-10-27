# coding=utf-8
import importlib
from types import ModuleType

import pytest
from packaging import version

from qtpy import (
    API_NAME,
    PYQT5,
    PYQT6,
    PYQT_VERSION,
    PYSIDE2,
    PYSIDE6,
    PYSIDE_VERSION,
)


@pytest.mark.skipif(
    not (
        (PYQT6 and version.parse(PYQT_VERSION) >= version.parse("6.2"))
        or (PYSIDE6 and version.parse(PYSIDE_VERSION) >= version.parse("6.2"))
        or PYQT5
        or PYSIDE2
    ),
    reason="Only available in Qt<6,>=6.2 bindings",
)
def test_qtwebenginewidgets():
    """Test the qtpy.QtWebEngineWidget namespace"""

    QtWebEngineWidgets = pytest.importorskip("qtpy.QtWebEngineWidgets")

    assert QtWebEngineWidgets.QWebEnginePage is not None
    assert QtWebEngineWidgets.QWebEngineView is not None
    assert QtWebEngineWidgets.QWebEngineSettings is not None
    assert QtWebEngineWidgets.QWebEngineScript is not None


@pytest.mark.skipif(
    not (
        (PYQT6 and version.parse(PYQT_VERSION) >= version.parse("6.2"))
        or (PYSIDE6 and version.parse(PYSIDE_VERSION) >= version.parse("6.2"))
        or PYQT5
        or PYSIDE2
    ),
    reason="Only available in Qt<6,>=6.2 bindings",
)
def test_namespace_not_polluted():
    """Test that no extra members are exported into the module namespace."""
    qtpy_module: ModuleType = pytest.importorskip("qtpy.QtWebEngineWidgets")
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
            # To test if we are using WebEngine or WebKit
            # NOTE: This constant is imported by other projects
            # (e.g. Spyder), so please don't remove it.
            [
                "WEBENGINE",
            ]
        )
        - frozenset(
            # These are imported from `QtWebEngineCore`:
            [
                "QWebEnginePage",
                "QWebEngineProfile",
                "QWebEngineScript",
                "QWebEngineSettings",
            ]
        )
    )
    assert not extra_members
