import pytest

from qtpy import PYQT5, PYQT_VERSION, QtQuickWidgets


def test_qtquickwidgets():
    """Test the qtpy.QtQuickWidgets namespace"""
    assert QtQuickWidgets.QQuickWidget is not None


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
        QtQuickWidgets.QQuickWidget.Null
        == QtQuickWidgets.QQuickWidget.Status.Null
    )
