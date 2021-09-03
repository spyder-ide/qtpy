from __future__ import absolute_import

import pytest
from qtpy import PYQT5, PYSIDE2
from qtpy.py3compat import PY3

@pytest.mark.skipif(
    not (PYQT5 or PYSIDE2) or PY3,
    reason="Only available in Qt5 bindings and Python 2")
def test_qtdatavisualization():
    """Test the qtpy.QtDataVisualization namespace"""
    # QtDataVisualization
    assert qtpy.QtDataVisualization.QScatter3DSeries is not None
    assert qtpy.QtDataVisualization.QSurfaceDataItem is not None
    assert qtpy.QtDataVisualization.QSurface3DSeries is not None
    assert qtpy.QtDataVisualization.QAbstract3DInputHandler is not None
    assert qtpy.QtDataVisualization.QHeightMapSurfaceDataProxy is not None
    assert qtpy.QtDataVisualization.QAbstractDataProxy is not None
    assert qtpy.QtDataVisualization.Q3DCamera is not None
    assert qtpy.QtDataVisualization.QAbstract3DGraph is not None
    assert qtpy.QtDataVisualization.QCustom3DVolume is not None
    assert qtpy.QtDataVisualization.Q3DInputHandler is not None
    assert qtpy.QtDataVisualization.QBarDataProxy is not None
    assert qtpy.QtDataVisualization.QSurfaceDataProxy is not None
    assert qtpy.QtDataVisualization.QScatterDataItem is not None
    assert qtpy.QtDataVisualization.Q3DLight is not None
    assert qtpy.QtDataVisualization.QScatterDataProxy is not None
    assert qtpy.QtDataVisualization.QValue3DAxis is not None
    assert qtpy.QtDataVisualization.Q3DBars is not None
    assert qtpy.QtDataVisualization.QBarDataItem is not None
    assert qtpy.QtDataVisualization.QItemModelBarDataProxy is not None
    assert qtpy.QtDataVisualization.Q3DTheme is not None
    assert qtpy.QtDataVisualization.QCustom3DItem is not None
    assert qtpy.QtDataVisualization.QItemModelScatterDataProxy is not None
    assert qtpy.QtDataVisualization.QValue3DAxisFormatter is not None
    assert qtpy.QtDataVisualization.QItemModelSurfaceDataProxy is not None
    assert qtpy.QtDataVisualization.Q3DScatter is not None
    assert qtpy.QtDataVisualization.QTouch3DInputHandler is not None
    assert qtpy.QtDataVisualization.QBar3DSeries is not None
    assert qtpy.QtDataVisualization.QAbstract3DAxis is not None
    assert qtpy.QtDataVisualization.Q3DScene is not None
    assert qtpy.QtDataVisualization.QCategory3DAxis is not None
    assert qtpy.QtDataVisualization.QAbstract3DSeries is not None
    assert qtpy.QtDataVisualization.Q3DObject is not None
    assert qtpy.QtDataVisualization.QCustom3DLabel is not None
    assert qtpy.QtDataVisualization.Q3DSurface is not None
    assert qtpy.QtDataVisualization.QLogValue3DAxisFormatter is not None

    # QtDatavisualization
    assert qtpy.QtDatavisualization.QScatter3DSeries is not None
    assert qtpy.QtDatavisualization.QSurfaceDataItem is not None
    assert qtpy.QtDatavisualization.QSurface3DSeries is not None
    assert qtpy.QtDatavisualization.QAbstract3DInputHandler is not None
    assert qtpy.QtDatavisualization.QHeightMapSurfaceDataProxy is not None
    assert qtpy.QtDatavisualization.QAbstractDataProxy is not None
    assert qtpy.QtDatavisualization.Q3DCamera is not None
    assert qtpy.QtDatavisualization.QAbstract3DGraph is not None
    assert qtpy.QtDatavisualization.QCustom3DVolume is not None
    assert qtpy.QtDatavisualization.Q3DInputHandler is not None
    assert qtpy.QtDatavisualization.QBarDataProxy is not None
    assert qtpy.QtDatavisualization.QSurfaceDataProxy is not None
    assert qtpy.QtDatavisualization.QScatterDataItem is not None
    assert qtpy.QtDatavisualization.Q3DLight is not None
    assert qtpy.QtDatavisualization.QScatterDataProxy is not None
    assert qtpy.QtDatavisualization.QValue3DAxis is not None
    assert qtpy.QtDatavisualization.Q3DBars is not None
    assert qtpy.QtDatavisualization.QBarDataItem is not None
    assert qtpy.QtDatavisualization.QItemModelBarDataProxy is not None
    assert qtpy.QtDatavisualization.Q3DTheme is not None
    assert qtpy.QtDatavisualization.QCustom3DItem is not None
    assert qtpy.QtDatavisualization.QItemModelScatterDataProxy is not None
    assert qtpy.QtDatavisualization.QValue3DAxisFormatter is not None
    assert qtpy.QtDatavisualization.QItemModelSurfaceDataProxy is not None
    assert qtpy.QtDatavisualization.Q3DScatter is not None
    assert qtpy.QtDatavisualization.QTouch3DInputHandler is not None
    assert qtpy.QtDatavisualization.QBar3DSeries is not None
    assert qtpy.QtDatavisualization.QAbstract3DAxis is not None
    assert qtpy.QtDatavisualization.Q3DScene is not None
    assert qtpy.QtDatavisualization.QCategory3DAxis is not None
    assert qtpy.QtDatavisualization.QAbstract3DSeries is not None
    assert qtpy.QtDatavisualization.Q3DObject is not None
    assert qtpy.QtDatavisualization.QCustom3DLabel is not None
    assert qtpy.QtDatavisualization.Q3DSurface is not None
    assert qtpy.QtDatavisualization.QLogValue3DAxisFormatter is not None
