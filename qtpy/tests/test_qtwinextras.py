from __future__ import absolute_import

import os
import sys

import pytest
from qtpy import PYQT5, PYSIDE2

@pytest.mark.skipif(
    sys.platform != "win32" or not (PYQT5 or PYSIDE2) or
    os.environ['USE_CONDA'] == 'Yes' and PYQT5,
    reason="Only available in Qt5 bindings and Windows platform")
def test_qtwinextras():
    """Test the qtpy.QtWinExtras namespace"""
    from qtpy import QtWinExtras
    assert QtWinExtras.QWinJumpList is not None
    assert QtWinExtras.QWinJumpListCategory is not None
    assert QtWinExtras.QWinJumpListItem is not None
    assert QtWinExtras.QWinTaskbarButton is not None
    assert QtWinExtras.QWinTaskbarProgress is not None
    assert QtWinExtras.QWinThumbnailToolBar is not None
    assert QtWinExtras.QWinThumbnailToolButton is not None
    if not PYSIDE2:  # See https://bugreports.qt.io/browse/PYSIDE-1047
        assert QtWinExtras.QtWin is not None

    if PYSIDE2:
        assert QtWinExtras.QWinColorizationChangeEvent is not None
        assert QtWinExtras.QWinCompositionChangeEvent is not None
        assert QtWinExtras.QWinEvent is not None

