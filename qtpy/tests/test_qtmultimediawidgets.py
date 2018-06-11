from __future__ import absolute_import

import pytest
from qtpy import PYQT5, PYSIDE2

@pytest.mark.skipif(not (PYQT5 or PYSIDE2), reason="Only available in Qt5 bindings")
def test_qtmultimediawidgets():
    """Test the qtpy.QtMultimediaWidgets namespace"""
    from qtpy import QtMultimediaWidgets

    assert QtMultimediaWidgets.QCameraViewfinder is not None
    assert QtMultimediaWidgets.QGraphicsVideoItem is not None
    assert QtMultimediaWidgets.QVideoWidget is not None
    #assert QtMultimediaWidgets.QVideoWidgetControl is not None
