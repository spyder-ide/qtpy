import pytest

from qtpy import (
    PYQT5,
    PYQT6,
    PYQT_VERSION,
    PYSIDE2,
    PYSIDE6,
    PYSIDE_VERSION,
    _parse_version,
)
from tests.utils import pytest_importorskip


@pytest.mark.skipif(
    not (
        (PYQT6 and _parse_version(PYQT_VERSION) >= _parse_version("6.2"))
        or (
            PYSIDE6 and _parse_version(PYSIDE_VERSION) >= _parse_version("6.2")
        )
        or PYQT5
        or PYSIDE2
    ),
    reason="Only available in Qt<6,>=6.2 bindings",
)
def test_qtwebenginewidgets():
    """Test the qtpy.QtWebEngineWidget namespace"""

    QtWebEngineWidgets = pytest_importorskip("qtpy.QtWebEngineWidgets")

    assert QtWebEngineWidgets.QWebEnginePage is not None
    assert QtWebEngineWidgets.QWebEngineView is not None
    assert QtWebEngineWidgets.QWebEngineSettings is not None
    assert QtWebEngineWidgets.QWebEngineScript is not None
