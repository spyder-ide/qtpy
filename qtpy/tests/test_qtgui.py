"""Test QtGui."""
import pytest

from qtpy import PYQT5, PYQT_VERSION, QtGui


def test_qdrag_functions():
    """Test functions mapping for QtGui.QDrag."""
    assert QtGui.QDrag.exec_


def test_qguiapplication_functions():
    """Test functions mapping for QtGui.QGuiApplication."""
    assert QtGui.QGuiApplication.exec_


def test_qtextdocument_functions():
    """Test functions mapping for QtGui.QTextDocument."""
    assert QtGui.QTextDocument.print_


@pytest.mark.skipif(PYQT5 and PYQT_VERSION.startswith('5.9'),
                    reason="A specific setup with at least sip 4.9.9 is needed for PyQt5 5.9.*"
                           "to work with scoped enum access")
def test_enum_access():
    """Test scoped and unscoped enum access for qtpy.QtWidgets.*."""
    assert QtGui.QColor.Rgb == QtGui.QColor.Spec.Rgb
    assert QtGui.QFont.AllUppercase == QtGui.QFont.Capitalization.AllUppercase
    assert QtGui.QIcon.Normal == QtGui.QIcon.Mode.Normal
    assert QtGui.QImage.Format_Invalid == QtGui.QImage.Format.Format_Invalid