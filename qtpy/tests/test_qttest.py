from __future__ import absolute_import

import pytest
from qtpy import PYSIDE2, QtTest


@pytest.mark.skipif(PYSIDE2, reason="It fails on PySide2")
def test_qttest():
    """Test the qtpy.QtTest namespace"""
    assert QtTest.QTest is not None
