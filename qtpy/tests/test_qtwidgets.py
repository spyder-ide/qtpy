"""Test QtWidgets."""
import os
import sys

import pytest

from qtpy import PYQT5, PYQT_VERSION, QtCore, QtWidgets, QtPrintSupport


@pytest.mark.skipif(sys.platform.startswith('linux') and os.environ.get('USE_CONDA', 'No') == 'No',
                    reason="Fatal Python error: Aborted on Linux CI when not using conda")
def test_qtextedit_functions(qtbot):
    """Test functions mapping for QtWidgets.QTextEdit."""
    assert QtWidgets.QTextEdit.setTabStopWidth
    assert QtWidgets.QTextEdit.tabStopWidth
    assert QtWidgets.QTextEdit.print_
    textedit_widget = QtWidgets.QTextEdit(None)
    textedit_widget.setTabStopWidth(90)
    assert textedit_widget.tabStopWidth() == 90
    printer = QtPrintSupport.QPrinter()
    textedit_widget.print_(printer)


@pytest.mark.skipif(sys.platform.startswith('linux') and os.environ.get('USE_CONDA', 'No') == 'No',
                    reason="Fatal Python error: Aborted on Linux CI when not using conda")
def test_qplaintextedit_functions(qtbot):
    """Test functions mapping for QtWidgets.QPlainTextEdit."""
    assert QtWidgets.QPlainTextEdit.setTabStopWidth
    assert QtWidgets.QPlainTextEdit.tabStopWidth
    assert QtWidgets.QPlainTextEdit.print_
    plaintextedit_widget = QtWidgets.QPlainTextEdit(None)
    plaintextedit_widget.setTabStopWidth(90)
    assert plaintextedit_widget.tabStopWidth() == 90
    printer = QtPrintSupport.QPrinter()
    plaintextedit_widget.print_(printer)


def test_qapplication_functions():
    """Test functions mapping for QtWidgets.QApplication."""
    assert QtWidgets.QApplication.exec_


@pytest.mark.skipif(sys.platform.startswith('linux') and os.environ.get('USE_CONDA', 'No') == 'No',
                    reason="Fatal Python error: Aborted on Linux CI when not using conda")
def test_qdialog_functions(qtbot):
    """Test functions mapping for QtWidgets.QDialog."""
    assert QtWidgets.QDialog.exec_
    dialog = QtWidgets.QDialog(None)
    QtCore.QTimer.singleShot(100, dialog.accept)
    dialog.exec_()


@pytest.mark.skipif(sys.platform.startswith('linux') and os.environ.get('USE_CONDA', 'No') == 'No',
                    reason="Fatal Python error: Aborted on Linux CI when not using conda")
def test_qmenu_functions(qtbot):
    """Test functions mapping for QtWidgets.QDialog."""
    assert QtWidgets.QMenu.exec_
    menu = QtWidgets.QMenu(None)
    QtCore.QTimer.singleShot(100, menu.close)
    menu.exec_()

@pytest.mark.skipif(PYQT5 and PYQT_VERSION.startswith('5.9'),
                    reason="A specific setup with at least sip 4.9.9 is needed for PyQt5 5.9.*"
                           "to work with scoped enum access")
def test_enum_access():
    """Test scoped and unscoped enum access for qtpy.QtWidgets.*."""
    assert QtWidgets.QFileDialog.AcceptOpen == QtWidgets.QFileDialog.AcceptMode.AcceptOpen
    assert QtWidgets.QMessageBox.InvalidRole == QtWidgets.QMessageBox.ButtonRole.InvalidRole
    assert QtWidgets.QStyle.State_None == QtWidgets.QStyle.StateFlag.State_None
