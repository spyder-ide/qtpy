# coding=utf-8
import importlib
from types import ModuleType

from qtpy import API_NAME, QtWebChannel


def test_qtwebchannel():
    """Test the qtpy.QtWebChannel namespace"""
    assert QtWebChannel.QWebChannel is not None
    assert QtWebChannel.QWebChannelAbstractTransport is not None


def test_namespace_not_polluted():
    """Test that no extra members are exported into the module namespace."""
    qtpy_module: ModuleType = QtWebChannel
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
