# coding=utf-8
import importlib
from types import ModuleType

import pytest

from qtpy import API_NAME


def test_qtscxml():
    """Test the qtpy.QtScxml namespace"""
    QtScxml = pytest.importorskip("qtpy.QtScxml")

    assert QtScxml.QScxmlCompiler is not None
    assert QtScxml.QScxmlDynamicScxmlServiceFactory is not None
    assert QtScxml.QScxmlExecutableContent is not None


def test_namespace_not_polluted():
    """Test that no extra members are exported into the module namespace."""
    qtpy_module: ModuleType = pytest.importorskip("qtpy.QtScxml")
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
