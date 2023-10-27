# coding=utf-8
import importlib
from types import ModuleType

import pytest

from qtpy import API_NAME


def test_qtuitools():
    """Test the qtpy.QtUiTools namespace"""
    QtUiTools = pytest.importorskip("qtpy.QtUiTools")

    assert QtUiTools.QUiLoader is not None


def test_namespace_not_polluted():
    """Test that no extra members are exported into the module namespace."""
    qtpy_module: ModuleType = pytest.importorskip("qtpy.QtUiTools")
    original_module: ModuleType = importlib.import_module(
        qtpy_module.__name__.replace('qtpy', API_NAME)
    )

    extra_members = (
        frozenset(dir(qtpy_module))
        - frozenset(dir(original_module))
        - frozenset(
            # These are unavoidable:
            [
                "__builtins__",
                "__cached__",
            ]
        )
    )
    assert not extra_members
