import importlib
from typing import TYPE_CHECKING

import pytest

from qtpy import API_NAME

if TYPE_CHECKING:
    from types import ModuleType


def test_qtdatavisualization():
    """Test the qtpy.QtDataVisualization namespace"""
    # Using import skip here since with Python 3 you need to install another package
    # besides the base `PyQt5` or `PySide2`.
    # For example in the case of `PyQt5` you need `PyQtDataVisualization`

    # QtDataVisualization
    QtDataVisualization = pytest.importorskip("qtpy.QtDataVisualization")
    assert QtDataVisualization.QScatter3DSeries is not None
    assert QtDataVisualization.QSurfaceDataItem is not None
    assert QtDataVisualization.QSurface3DSeries is not None
    assert QtDataVisualization.QAbstract3DInputHandler is not None
    assert QtDataVisualization.QHeightMapSurfaceDataProxy is not None
    assert QtDataVisualization.QAbstractDataProxy is not None
    assert QtDataVisualization.Q3DCamera is not None
    assert QtDataVisualization.QAbstract3DGraph is not None
    assert QtDataVisualization.QCustom3DVolume is not None
    assert QtDataVisualization.Q3DInputHandler is not None
    assert QtDataVisualization.QBarDataProxy is not None
    assert QtDataVisualization.QSurfaceDataProxy is not None
    assert QtDataVisualization.QScatterDataItem is not None
    assert QtDataVisualization.Q3DLight is not None
    assert QtDataVisualization.QScatterDataProxy is not None
    assert QtDataVisualization.QValue3DAxis is not None
    assert QtDataVisualization.Q3DBars is not None
    assert QtDataVisualization.QBarDataItem is not None
    assert QtDataVisualization.QItemModelBarDataProxy is not None
    assert QtDataVisualization.Q3DTheme is not None
    assert QtDataVisualization.QCustom3DItem is not None
    assert QtDataVisualization.QItemModelScatterDataProxy is not None
    assert QtDataVisualization.QValue3DAxisFormatter is not None
    assert QtDataVisualization.QItemModelSurfaceDataProxy is not None
    assert QtDataVisualization.Q3DScatter is not None
    assert QtDataVisualization.QTouch3DInputHandler is not None
    assert QtDataVisualization.QBar3DSeries is not None
    assert QtDataVisualization.QAbstract3DAxis is not None
    assert QtDataVisualization.Q3DScene is not None
    assert QtDataVisualization.QCategory3DAxis is not None
    assert QtDataVisualization.QAbstract3DSeries is not None
    assert QtDataVisualization.Q3DObject is not None
    assert QtDataVisualization.QCustom3DLabel is not None
    assert QtDataVisualization.Q3DSurface is not None
    assert QtDataVisualization.QLogValue3DAxisFormatter is not None

    # QtDatavisualization
    # import qtpy to get alias for `QtDataVisualization` with lower `v`
    qtpy = pytest.importorskip("qtpy")

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


def test_namespace_not_polluted():
    """Test that no extra members are exported into the module namespace."""
    qtpy_module: ModuleType = pytest.importorskip("qtpy.QtDataVisualization")
    original_module: ModuleType = importlib.import_module(
        qtpy_module.__name__.replace("qtpy", API_NAME),
    )

    extra_members = (
        frozenset(object.__dir__(qtpy_module))
        - frozenset(dir(original_module))
        - frozenset(
            # These are unavoidable:
            [
                "__builtins__",
                "__cached__",
            ],
        )
        - frozenset(
            # These don't show up in `dir()` when on PySide:
            [*dir(object), "Q3DBars", "Q3DCamera", "Q3DInputHandler", "Q3DLight", "Q3DObject", "Q3DScatter", "Q3DScene", "Q3DSurface", "Q3DTheme", "QAbstract3DAxis", "QAbstract3DGraph", "QAbstract3DInputHandler", "QAbstract3DSeries", "QAbstractDataProxy", "QBar3DSeries", "QBarDataItem", "QBarDataProxy", "QCategory3DAxis", "QCustom3DItem", "QCustom3DLabel", "QCustom3DVolume", "QHeightMapSurfaceDataProxy", "QItemModelBarDataProxy", "QItemModelScatterDataProxy", "QItemModelSurfaceDataProxy", "QLogValue3DAxisFormatter", "QScatter3DSeries", "QScatterDataItem", "QScatterDataProxy", "QSurface3DSeries", "QSurfaceDataItem", "QSurfaceDataProxy", "QTouch3DInputHandler", "QValue3DAxis", "QValue3DAxisFormatter", "__annotations__", "__dict__", "__module__", "qDefaultSurfaceFormat"],
        )
    )
    assert not extra_members
