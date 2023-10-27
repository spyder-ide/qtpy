# coding=utf-8
"""Test QtWinExtras."""
import importlib
import sys
from types import ModuleType

import pytest

from qtpy import API_NAME, PYQT6, PYSIDE2, PYSIDE6
from qtpy.tests.utils import using_conda


@pytest.mark.skipif(
    PYQT6 or PYSIDE6,
    reason="Not available on Qt6-based bindings",
)
@pytest.mark.skipif(
    sys.platform != "win32" or using_conda(),
    reason="Only available in Qt5 bindings > 5.9 with pip on Windows in CIs",
)
def test_qtwinextras():
    """Test the qtpy.QtWinExtras namespace"""
    from qtpy import QtWinExtras

    assert QtWinExtras.QWinJumpList is not None
    assert QtWinExtras.QWinJumpListCategory is not None
    assert QtWinExtras.QWinJumpListItem is not None
    assert QtWinExtras.QWinTaskbarButton is not None
    assert QtWinExtras.QWinTaskbarProgress is not None
    assert QtWinExtras.QWinThumbnailToolBar is not None
    assert QtWinExtras.QWinThumbnailToolButton is not None
    if not PYSIDE2:  # See https://bugreports.qt.io/browse/PYSIDE-1047
        assert QtWinExtras.QtWin is not None

    if PYSIDE2:
        assert QtWinExtras.QWinColorizationChangeEvent is not None
        assert QtWinExtras.QWinCompositionChangeEvent is not None
        assert QtWinExtras.QWinEvent is not None


@pytest.mark.skipif(
    PYQT6 or PYSIDE6,
    reason="Not available on Qt6-based bindings",
)
@pytest.mark.skipif(
    sys.platform != "win32" or using_conda(),
    reason="Only available in Qt5 bindings > 5.9 with pip on Windows in CIs",
)
def test_namespace_not_polluted():
    """Test that no extra members are exported into the module namespace."""
    from qtpy import QtWinExtras

    qtpy_module: ModuleType = QtWinExtras
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
