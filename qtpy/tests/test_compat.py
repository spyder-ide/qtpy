"""Test the compat module."""

import sys

import pytest
from packaging import version

from qtpy import PYQT5, PYQT_VERSION, QtWidgets, compat
from qtpy.tests.utils import not_using_conda


@pytest.mark.skipif(
    (
        (sys.version_info.major == 3 and sys.version_info.minor == 7)
        and sys.platform.startswith("win")
        and not not_using_conda()
    ),
    reason="sip not included in Python3.7 on Windows",
)
def test_isalive(qtbot):
    """Test compat.isalive"""
    test_widget = QtWidgets.QWidget()
    assert compat.isalive(test_widget) is True
    with qtbot.waitSignal(test_widget.destroyed):
        test_widget.deleteLater()
    assert compat.isalive(test_widget) is False


def test_getenumasint():
    """Test compat.getenumasint"""
    if PYQT5 and version.parse(PYQT_VERSION) <= version.parse("5.9.2"):
        assert compat.getenumasint(QtWidgets.QSizePolicy.Maximum) == 4
    else:
        assert compat.getenumasint(QtWidgets.QSizePolicy.Policy.Maximum) == 4
    assert compat.getenumasint(5) == 5


def test_getenumfromint():
    """Test compat.getenumfromint"""
    enum_value = compat.getenumfromint(QtWidgets.QSizePolicy.Policy, 7)
    if PYQT5 and version.parse(PYQT_VERSION) <= version.parse("5.9.2"):
        assert enum_value == QtWidgets.QSizePolicy.Expanding
    else:
        assert enum_value == QtWidgets.QSizePolicy.Policy.Expanding
