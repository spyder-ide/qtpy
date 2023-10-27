import importlib
from typing import TYPE_CHECKING

import pytest

from qtpy import API_NAME

if TYPE_CHECKING:
    from types import ModuleType


def test_qtstatemachine():
    """Test the qtpy.QtStateMachine namespace"""
    QtStateMachine = pytest.importorskip("qtpy.QtStateMachine")

    assert QtStateMachine.QAbstractState is not None
    assert QtStateMachine.QAbstractTransition is not None
    assert QtStateMachine.QEventTransition is not None
    assert QtStateMachine.QFinalState is not None
    assert QtStateMachine.QHistoryState is not None
    assert QtStateMachine.QKeyEventTransition is not None
    assert QtStateMachine.QMouseEventTransition is not None
    assert QtStateMachine.QSignalTransition is not None
    assert QtStateMachine.QState is not None


def test_namespace_not_polluted():
    """Test that no extra members are exported into the module namespace."""
    qtpy_module: ModuleType = pytest.importorskip("qtpy.QtStateMachine")
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
