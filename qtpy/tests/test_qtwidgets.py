"""Test QtWidgets."""
import os
import sys

import pytest

from qtpy import PYQT5, PYQT_VERSION, QtCore, QtGui, QtWidgets


@pytest.mark.skipif(sys.platform.startswith('linux') and os.environ.get('USE_CONDA', 'No') == 'No',
                    reason="Fatal Python error: Aborted on Linux CI when not using conda")
def test_qtextedit_functions(qtbot):
    """Test functions mapping for QtWidgets.QTextEdit."""
    assert QtWidgets.QTextEdit.setTabStopWidth
    assert QtWidgets.QTextEdit.tabStopWidth
    assert QtWidgets.QTextEdit.print_
    textedit_widget = QtWidgets.QTextEdit(None)    
    qtbot.addWidget(textedit_widget)
    textedit_widget.setTabStopWidth(90)
    assert textedit_widget.tabStopWidth() == 90
    print_device = QtGui.QPdfWriter('test.pdf')
    textedit_widget.print_(print_device)
    assert os.path.exists('test.pdf')
    os.remove('test.pdf')


@pytest.mark.skipif(sys.platform.startswith('linux') and os.environ.get('USE_CONDA', 'No') == 'No',
                    reason="Fatal Python error: Aborted on Linux CI when not using conda")
def test_qplaintextedit_functions(qtbot):
    """Test functions mapping for QtWidgets.QPlainTextEdit."""
    assert QtWidgets.QPlainTextEdit.setTabStopWidth
    assert QtWidgets.QPlainTextEdit.tabStopWidth
    assert QtWidgets.QPlainTextEdit.print_
    plaintextedit_widget = QtWidgets.QPlainTextEdit(None)
    qtbot.addWidget(plaintextedit_widget)
    plaintextedit_widget.setTabStopWidth(90)
    assert plaintextedit_widget.tabStopWidth() == 90
    print_device = QtGui.QPdfWriter('test.pdf')
    plaintextedit_widget.print_(print_device)
    assert os.path.exists('test.pdf')
    os.remove('test.pdf')


def test_qapplication_functions():
    """Test functions mapping for QtWidgets.QApplication."""
    assert QtWidgets.QApplication.exec_


@pytest.mark.skipif(sys.platform.startswith('linux') and os.environ.get('USE_CONDA', 'No') == 'No',
                    reason="Fatal Python error: Aborted on Linux CI when not using conda")
def test_qdialog_functions(qtbot):
    """Test functions mapping for QtWidgets.QDialog."""
    assert QtWidgets.QDialog.exec_
    dialog = QtWidgets.QDialog(None)
    qtbot.addWidget(dialog)
    QtCore.QTimer.singleShot(100, dialog.accept)
    dialog.exec_()


@pytest.mark.skipif(sys.platform.startswith('linux') and os.environ.get('USE_CONDA', 'No') == 'No',
                    reason="Fatal Python error: Aborted on Linux CI when not using conda")
def test_qmenu_functions(qtbot):
    """Test functions mapping for QtWidgets.QDialog."""
    assert QtWidgets.QMenu.exec_
    menu = QtWidgets.QMenu(None)
    qtbot.addWidget(menu)
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
