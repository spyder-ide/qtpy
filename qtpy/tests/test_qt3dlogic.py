# coding=utf-8
import importlib
from types import ModuleType

import pytest

from qtpy import API_NAME


def test_qt3dlogic():
    """Test the qtpy.Qt3DLogic namespace"""
    Qt3DLogic = pytest.importorskip("qtpy.Qt3DLogic")

    assert Qt3DLogic.QLogicAspect is not None
    assert Qt3DLogic.QFrameAction is not None


def test_namespace_not_polluted():
    """Test that no extra members are exported into the module namespace."""
    qtpy_module: ModuleType = pytest.importorskip("qtpy.Qt3DLogic")
    original_module: ModuleType = importlib.import_module(
        qtpy_module.__name__.replace('qtpy', API_NAME)
    )

    extra_members = (
        frozenset(object.__dir__(qtpy_module))
        - frozenset(dir(original_module))
        - frozenset(
            # These are unavoidable:
            [
                "__builtins__",
                "__cached__",
            ]
        )
        - frozenset(
            # These don't show up in `dir()` when on PySide:
            dir(object)
            + [
                "QFrameAction",
                "QLogicAspect",
                "__annotations__",
                "__dict__",
                "__module__",
            ]
        )
    )
    assert not extra_members
