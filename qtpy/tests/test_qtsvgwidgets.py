import importlib
from typing import TYPE_CHECKING

import pytest

from qtpy import API_NAME

if TYPE_CHECKING:
    from types import ModuleType


def test_qtsvgwidgets():
    """Test the qtpy.QtSvgWidgets namespace"""
    QtSvgWidgets = pytest.importorskip("qtpy.QtSvgWidgets")

    assert QtSvgWidgets.QGraphicsSvgItem is not None
    assert QtSvgWidgets.QSvgWidget is not None


def test_namespace_not_polluted():
    """Test that no extra members are exported into the module namespace."""
    qtpy_module: ModuleType = pytest.importorskip("qtpy.QtSvgWidgets")
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
