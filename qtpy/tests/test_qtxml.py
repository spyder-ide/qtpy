# coding=utf-8
import importlib
from types import ModuleType

from qtpy import API_NAME, QtXml


def test_qtxml():
    """Test the qtpy.QtXml namespace"""
    assert QtXml.QDomAttr is not None
    assert QtXml.QDomCDATASection is not None
    assert QtXml.QDomCharacterData is not None
    assert QtXml.QDomComment is not None
    assert QtXml.QDomDocument is not None
    assert QtXml.QDomDocumentFragment is not None
    assert QtXml.QDomDocumentType is not None
    assert QtXml.QDomElement is not None
    assert QtXml.QDomEntity is not None
    assert QtXml.QDomEntityReference is not None
    assert QtXml.QDomImplementation is not None
    assert QtXml.QDomNamedNodeMap is not None
    assert QtXml.QDomNode is not None
    assert QtXml.QDomNodeList is not None
    assert QtXml.QDomNotation is not None
    assert QtXml.QDomProcessingInstruction is not None
    assert QtXml.QDomText is not None


def test_namespace_not_polluted():
    """Test that no extra members are exported into the module namespace."""
    qtpy_module: ModuleType = QtXml
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
