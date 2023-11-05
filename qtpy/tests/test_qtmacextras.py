import importlib
import sys
from typing import TYPE_CHECKING

import pytest

from qtpy import API_NAME, PYQT6, PYSIDE6
from qtpy.tests.utils import using_conda

if TYPE_CHECKING:
    from types import ModuleType


@pytest.mark.skipif(
    PYQT6 or PYSIDE6,
    reason="Not available on Qt6-based bindings",
)
@pytest.mark.skipif(
    sys.platform != "darwin" or using_conda(),
    reason="Only available in Qt5 bindings > 5.9 with pip on mac in CIs",
)
def test_qtmacextras():
    """Test the qtpy.QtMacExtras namespace"""
    QtMacExtras = pytest.importorskip("qtpy.QtMacExtras")

    assert QtMacExtras.QMacPasteboardMime is not None
    assert QtMacExtras.QMacToolBar is not None
    assert QtMacExtras.QMacToolBarItem is not None


@pytest.mark.skipif(
    PYQT6 or PYSIDE6,
    reason="Not available on Qt6-based bindings",
)
@pytest.mark.skipif(
    sys.platform != "darwin" or using_conda(),
    reason="Only available in Qt5 bindings > 5.9 with pip on mac in CIs",
)
def test_namespace_not_polluted():
    """Test that no extra members are exported into the module namespace."""
    qtpy_module: ModuleType = pytest.importorskip("qtpy.QtMacExtras")
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
