import importlib
from typing import TYPE_CHECKING

from qtpy import API_NAME, QtWebSockets

if TYPE_CHECKING:
    from types import ModuleType


def test_qtwebsockets():
    """Test the qtpy.QtWebSockets namespace"""
    assert QtWebSockets.QMaskGenerator is not None
    assert QtWebSockets.QWebSocket is not None
    assert QtWebSockets.QWebSocketCorsAuthenticator is not None
    assert QtWebSockets.QWebSocketProtocol is not None
    assert QtWebSockets.QWebSocketServer is not None


def test_namespace_not_polluted():
    """Test that no extra members are exported into the module namespace."""
    qtpy_module: ModuleType = QtWebSockets
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
