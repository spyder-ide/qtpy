"""Test QtMultimediaWidgets."""
import importlib
from typing import TYPE_CHECKING

from qtpy import API_NAME, PYQT5, PYSIDE2, QtMultimediaWidgets

if TYPE_CHECKING:
    from types import ModuleType


def test_qtmultimediawidgets():
    """Test the qtpy.QtMultimediaWidgets namespace"""
    if PYQT5 or PYSIDE2:
        assert QtMultimediaWidgets.QCameraViewfinder is not None
        # assert QtMultimediaWidgets.QVideoWidgetControl is not None
    assert QtMultimediaWidgets.QGraphicsVideoItem is not None
    assert QtMultimediaWidgets.QVideoWidget is not None


def test_namespace_not_polluted():
    """Test that no extra members are exported into the module namespace."""
    qtpy_module: ModuleType = QtMultimediaWidgets
    original_module: ModuleType = importlib.import_module(
        qtpy_module.__name__.replace("qtpy", API_NAME),
    )

    extra_members = (
        frozenset(dir(qtpy_module))
        - frozenset(dir(original_module))
        - frozenset(
            # These are unavoidable:
            [
                "__builtins__",
                "__cached__",
            ],
        )
    )
    assert not extra_members
