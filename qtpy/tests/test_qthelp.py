# coding=utf-8
"""Test for QtHelp namespace."""
import importlib
from types import ModuleType

from qtpy import API_NAME, QtHelp


def test_qthelp():
    """Test the qtpy.QtHelp namespace."""
    assert QtHelp.QHelpContentItem is not None
    assert QtHelp.QHelpContentModel is not None
    assert QtHelp.QHelpContentWidget is not None
    assert QtHelp.QHelpEngine is not None
    assert QtHelp.QHelpEngineCore is not None
    assert QtHelp.QHelpIndexModel is not None
    assert QtHelp.QHelpIndexWidget is not None
    assert QtHelp.QHelpSearchEngine is not None
    assert QtHelp.QHelpSearchQuery is not None
    assert QtHelp.QHelpSearchQueryWidget is not None
    assert QtHelp.QHelpSearchResultWidget is not None


def test_namespace_not_polluted():
    """Test that no extra members are exported into the module namespace."""
    qtpy_module: ModuleType = QtHelp
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
