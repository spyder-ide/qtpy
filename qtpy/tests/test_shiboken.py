# coding=utf-8
import importlib
from types import ModuleType

import pytest

from qtpy import API_NAME


def test_shiboken():
    """Test the qtpy.shiboken namespace"""
    shiboken = pytest.importorskip("qtpy.shiboken")

    assert shiboken.isValid is not None
    assert shiboken.wrapInstance is not None
    assert shiboken.getCppPointer is not None
    assert shiboken.delete is not None
    assert shiboken.dump is not None


def test_namespace_not_polluted():
    """Test that no extra members are exported into the module namespace."""
    qtpy_module: ModuleType = pytest.importorskip("qtpy.shiboken")
    original_module: ModuleType = importlib.import_module(
        f"shiboken{API_NAME[-1]}"
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
