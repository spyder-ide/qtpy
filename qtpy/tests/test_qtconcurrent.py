import pytest

from qtpy import PYSIDE2, PYSIDE_VERSION, _parse_version
from qtpy.tests.utils import pytest_importorskip


def test_qtconcurrent():
    """Test the qtpy.QtConcurrent namespace"""
    QtConcurrent = pytest_importorskip("qtpy.QtConcurrent")

    assert QtConcurrent.QtConcurrent is not None

    if PYSIDE2 and _parse_version(PYSIDE_VERSION) >= _parse_version("5.15.2"):
        assert QtConcurrent.QFutureQString is not None
        assert QtConcurrent.QFutureVoid is not None
        assert QtConcurrent.QFutureWatcherQString is not None
        assert QtConcurrent.QFutureWatcherVoid is not None
