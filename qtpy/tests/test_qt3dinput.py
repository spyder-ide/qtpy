import importlib
from typing import TYPE_CHECKING

import pytest

from qtpy import API_NAME

if TYPE_CHECKING:
    from types import ModuleType


def test_qt3dinput():
    """Test the qtpy.Qt3DInput namespace"""
    Qt3DInput = pytest.importorskip("qtpy.Qt3DInput")

    assert Qt3DInput.QAxisAccumulator is not None
    assert Qt3DInput.QInputSettings is not None
    assert Qt3DInput.QAnalogAxisInput is not None
    assert Qt3DInput.QAbstractAxisInput is not None
    assert Qt3DInput.QMouseHandler is not None
    assert Qt3DInput.QButtonAxisInput is not None
    assert Qt3DInput.QInputSequence is not None
    assert Qt3DInput.QWheelEvent is not None
    assert Qt3DInput.QActionInput is not None
    assert Qt3DInput.QKeyboardDevice is not None
    assert Qt3DInput.QMouseDevice is not None
    assert Qt3DInput.QAxis is not None
    assert Qt3DInput.QInputChord is not None
    assert Qt3DInput.QMouseEvent is not None
    assert Qt3DInput.QKeyboardHandler is not None
    assert Qt3DInput.QKeyEvent is not None
    assert Qt3DInput.QAbstractActionInput is not None
    assert Qt3DInput.QInputAspect is not None
    assert Qt3DInput.QLogicalDevice is not None
    assert Qt3DInput.QAction is not None
    assert Qt3DInput.QAbstractPhysicalDevice is not None
    assert Qt3DInput.QAxisSetting is not None


def test_namespace_not_polluted():
    """Test that no extra members are exported into the module namespace."""
    qtpy_module: ModuleType = pytest.importorskip("qtpy.Qt3DInput")
    original_module: ModuleType = importlib.import_module(
        qtpy_module.__name__.replace("qtpy", API_NAME),
    )

    extra_members = (
        frozenset(object.__dir__(qtpy_module))
        - frozenset(object.__dir__(original_module))
        - frozenset(
            # These are unavoidable:
            [
                "__builtins__",
                "__cached__",
            ],
        )
        - frozenset(
            # These don't show up in `dir()` when on PySide:
            {
                "QAbstractActionInput",
                "QAbstractAxisInput",
                "QAbstractPhysicalDevice",
                "QAction",
                "QActionInput",
                "QAnalogAxisInput",
                "QAxis",
                "QAxisAccumulator",
                "QAxisSetting",
                "QButtonAxisInput",
                "QInputAspect",
                "QInputChord",
                "QInputSequence",
                "QInputSettings",
                "QKeyEvent",
                "QKeyboardDevice",
                "QKeyboardHandler",
                "QLogicalDevice",
                "QMouseDevice",
                "QMouseEvent",
                "QMouseHandler",
                "QWheelEvent",
                "__annotations__",
                "__dict__",
                "__module__",
            },
        )
    )
    assert not extra_members
