import importlib
from typing import TYPE_CHECKING

import pytest

from qtpy import API_NAME, PYQT6, PYSIDE2, PYSIDE6

if TYPE_CHECKING:
    from types import ModuleType


@pytest.mark.skipif((PYSIDE6 or PYQT6), reason="not available with qt 6.0")
def test_qtxmlpatterns():
    """Test the qtpy.QtXmlPatterns namespace"""
    from qtpy import QtXmlPatterns

    assert QtXmlPatterns.QAbstractMessageHandler is not None
    assert QtXmlPatterns.QAbstractUriResolver is not None
    assert QtXmlPatterns.QAbstractXmlNodeModel is not None
    assert QtXmlPatterns.QAbstractXmlReceiver is not None
    if not PYSIDE2:
        assert QtXmlPatterns.QSimpleXmlNodeModel is not None
    assert QtXmlPatterns.QSourceLocation is not None
    assert QtXmlPatterns.QXmlFormatter is not None
    assert QtXmlPatterns.QXmlItem is not None
    assert QtXmlPatterns.QXmlName is not None
    assert QtXmlPatterns.QXmlNamePool is not None
    assert QtXmlPatterns.QXmlNodeModelIndex is not None
    assert QtXmlPatterns.QXmlQuery is not None
    assert QtXmlPatterns.QXmlResultItems is not None
    assert QtXmlPatterns.QXmlSchema is not None
    assert QtXmlPatterns.QXmlSchemaValidator is not None
    assert QtXmlPatterns.QXmlSerializer is not None


@pytest.mark.skipif((PYSIDE6 or PYQT6), reason="not available with qt 6.0")
def test_namespace_not_polluted():
    """Test that no extra members are exported into the module namespace."""
    from qtpy import QtXmlPatterns

    qtpy_module: ModuleType = QtXmlPatterns
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
