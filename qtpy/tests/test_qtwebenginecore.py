import pytest

from qtpy import PYQT5, PYQT_VERSION
from qtpy.tests.utils import pytest_importorskip


def test_qtwebenginecore():
    """Test the qtpy.QtWebEngineCore namespace"""
    QtWebEngineCore = pytest_importorskip("qtpy.QtWebEngineCore")

    assert QtWebEngineCore.QWebEngineHttpRequest is not None


@pytest.mark.skipif(
    PYQT5 and PYQT_VERSION.startswith("5.9"),
    reason=(
        "A specific setup with at least sip 4.9.9 is needed for PyQt5 5.9.* "
        "to work with scoped enum access"
    ),
)
def test_enum_access():
    """Test scoped and unscoped enum access."""
    QtWebEngineCore = pytest_importorskip("qtpy.QtWebEngineCore")

    assert (
        QtWebEngineCore.QWebEngineHttpRequest.Get
        == QtWebEngineCore.QWebEngineHttpRequest.Method.Get
    )
