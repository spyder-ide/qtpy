import importlib
from typing import TYPE_CHECKING

import pytest

from qtpy import API_NAME, PYSIDE2

if TYPE_CHECKING:
    from types import ModuleType


@pytest.mark.skipif(PYSIDE2, reason="Not available for PySide2")
def test_qtnetworkauth():
    """Test the qtpy.QtNetworkAuth namespace"""
    QtNetworkAuth = pytest.importorskip("qtpy.QtNetworkAuth")

    assert QtNetworkAuth.QAbstractOAuth is not None
    assert QtNetworkAuth.QAbstractOAuth2 is not None
    assert QtNetworkAuth.QAbstractOAuthReplyHandler is not None
    assert QtNetworkAuth.QOAuth1 is not None
    assert QtNetworkAuth.QOAuth1Signature is not None
    assert QtNetworkAuth.QOAuth2AuthorizationCodeFlow is not None


@pytest.mark.skipif(PYSIDE2, reason="Not available for PySide2")
def test_namespace_not_polluted():
    """Test that no extra members are exported into the module namespace."""
    qtpy_module: ModuleType = pytest.importorskip("qtpy.QtNetworkAuth")
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
