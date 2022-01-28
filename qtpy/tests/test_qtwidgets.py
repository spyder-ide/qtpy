"""Test QtWidgets."""
import pytest

from qtpy import PYQT5, PYQT_VERSION, QtWidgets


def test_qtextedit_functions():
    """Test functions mapping for QtWidgets.QTextEdit."""
    assert QtWidgets.QTextEdit.setTabStopWidth
    assert QtWidgets.QTextEdit.tabStopWidth
    assert QtWidgets.QTextEdit.print_


def test_qplaintextedit_functions():
    """Test functions mapping for QtWidgets.QPlainTextEdit."""
    assert QtWidgets.QPlainTextEdit.setTabStopWidth
    assert QtWidgets.QPlainTextEdit.tabStopWidth
    assert QtWidgets.QPlainTextEdit.print_


def test_qapplication_functions():
    """Test functions mapping for QtWidgets.QApplication."""
    assert QtWidgets.QApplication.exec_


def test_qdialog_functions():
    """Test functions mapping for QtWidgets.QDialog."""
    assert QtWidgets.QDialog.exec_


def test_qmenu_functions():
    """Test functions mapping for QtWidgets.QDialog."""
    assert QtWidgets.QMenu.exec_


@pytest.mark.skipif(PYQT5 and PYQT_VERSION.startswith('5.9'),
                    reason="A specific setup with at least sip 4.9.9 is needed for PyQt5 5.9.*"
                           "to work with scoped enum access")
def test_enum_access():
    """Test scoped and unscoped enum access for qtpy.QtWidgets.*."""
    assert QtWidgets.QFileDialog.AcceptOpen == QtWidgets.QFileDialog.AcceptMode.AcceptOpen
    assert QtWidgets.QMessageBox.InvalidRole == QtWidgets.QMessageBox.ButtonRole.InvalidRole
    assert QtWidgets.QStyle.State_None == QtWidgets.QStyle.StateFlag.State_None
    assert QtWidgets.QStyle.SC_SliderGroove == QtWidgets.QStyle.SubControl.SC_SliderGroove
