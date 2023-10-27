import importlib
from typing import TYPE_CHECKING

import pytest
from packaging.version import parse

from qtpy import API_NAME, PYSIDE2, PYSIDE_VERSION

if TYPE_CHECKING:
    from types import ModuleType


def test_qtconcurrent():
    """Test the qtpy.QtConcurrent namespace"""
    QtConcurrent = pytest.importorskip("qtpy.QtConcurrent")

    assert QtConcurrent.QtConcurrent is not None

    if PYSIDE2 and parse(PYSIDE_VERSION) >= parse("5.15.2"):
        assert QtConcurrent.QFutureQString is not None
        assert QtConcurrent.QFutureVoid is not None
        assert QtConcurrent.QFutureWatcherQString is not None
        assert QtConcurrent.QFutureWatcherVoid is not None


def test_namespace_not_polluted():
    """Test that no extra members are exported into the module namespace."""
    qtpy_module: ModuleType = pytest.importorskip("qtpy.QtConcurrent")
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
