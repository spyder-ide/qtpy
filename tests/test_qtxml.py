import pytest

from qtpy import PYQT5, PYQT_VERSION, QtXml


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


@pytest.mark.skipif(
    PYQT5 and PYQT_VERSION.startswith("5.9"),
    reason=(
        "A specific setup with at least sip 4.9.9 is needed for PyQt5 5.9.* "
        "to work with scoped enum access"
    ),
)
def test_enum_access():
    """Test scoped and unscoped enum access."""
    assert (
        QtXml.QDomNode.EncodingFromDocument
        == QtXml.QDomNode.EncodingPolicy.EncodingFromDocument
    )
