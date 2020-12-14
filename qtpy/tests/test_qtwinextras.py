from __future__ import absolute_import

import os
import sys

import pytest
from qtpy import PYSIDE2, PYSIDE6

@pytest.mark.skipif(
    sys.platform != "win32" or os.environ['USE_CONDA'] == 'Yes' or PYSIDE6,
    reason="Only available in Qt5 bindings > 5.9 (only available with pip in the current CI setup) and Windows platform")
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

