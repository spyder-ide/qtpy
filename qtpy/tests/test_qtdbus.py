# coding=utf-8
import importlib
from types import ModuleType

import pytest

from qtpy import API_NAME


def test_qtdbus():
    """Test the qtpy.QtDBus namespace"""
    QtDBus = pytest.importorskip("qtpy.QtDBus")

    assert QtDBus.QDBusAbstractAdaptor is not None
    assert QtDBus.QDBusAbstractInterface is not None
    assert QtDBus.QDBusArgument is not None
    assert QtDBus.QDBusConnection is not None


def test_namespace_not_polluted():
    """Test that no extra members are exported into the module namespace."""
    qtpy_module: ModuleType = pytest.importorskip("qtpy.QtDBus")
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
