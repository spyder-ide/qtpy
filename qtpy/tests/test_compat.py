"""Test the compat module."""

import sys

import pytest

from qtpy import QtWidgets, compat
from qtpy.QtCore import QRectF, QSize, Qt
from qtpy.QtGui import QBrush, QImage, QPainter
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


def test_getimagebytes(qtbot):
    """Test compat.getimagebytes"""
    image = QImage(QSize(100, 100), QImage.Format_RGB32)
    _bytes = compat.getimagebytes(image)
    assert len(_bytes) == 100 * 100 * 4
