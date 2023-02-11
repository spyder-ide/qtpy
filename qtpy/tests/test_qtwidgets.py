"""Test QtWidgets."""

import sys

import pytest

from qtpy import PYQT5, QtCore, QtWidgets
from qtpy.tests.utils import not_using_conda


@pytest.mark.skipif(
    PYQT5 and QtCore.__version__.startswith('5.9.'),
    reason="Doesn't seem to be present on PyQt5<5.10")
@pytest.mark.skipif(
    sys.platform.startswith('linux') and not_using_conda(),
    reason="Fatal Python error: Aborted on Linux CI when not using conda")
def test_qtextedit_functions(qtbot, pdf_writer):
    """Test functions mapping for QtWidgets.QTextEdit."""
    assert QtWidgets.QTextEdit.setTabStopWidth
    assert QtWidgets.QTextEdit.tabStopWidth
    assert QtWidgets.QTextEdit.setTabStopDistance
    assert QtWidgets.QTextEdit.tabStopDistance
    assert QtWidgets.QTextEdit.print_
    assert QtWidgets.QTextEdit.print
    textedit_widget = QtWidgets.QTextEdit(None)
    textedit_widget.setTabStopWidth(90)
    assert textedit_widget.tabStopWidth() == 90
    textedit_widget.setTabStopDistance(89.0)
    assert textedit_widget.tabStopDistance() == 89.0
    print_device, output_path = pdf_writer
    textedit_widget.print_(print_device)
    textedit_widget.print(print_device)
    assert output_path.exists()


def test_qlineedit_functions():
    """Test functions mapping for QtWidgets.QLineEdit"""
    assert QtWidgets.QLineEdit.getTextMargins
    assert QtWidgets.QLineEdit.selectionEnd
    assert QtWidgets.QLineEdit.selectionLength


def test_what_moved_to_qtgui_in_qt6():
    """Test that we move back what has been moved to QtGui in Qt6"""
    assert QtWidgets.QAction is not None
    assert QtWidgets.QActionGroup is not None
    assert QtWidgets.QFileSystemModel is not None
    assert QtWidgets.QShortcut is not None
    assert QtWidgets.QUndoCommand is not None


@pytest.mark.skipif(
    PYQT5 and QtCore.__version__.startswith('5.9.'),
    reason="Doesn't seem to be present on PyQt5<5.10")
@pytest.mark.skipif(
    sys.platform.startswith('linux') and not_using_conda(),
    reason="Fatal Python error: Aborted on Linux CI when not using conda")
def test_qplaintextedit_functions(qtbot, pdf_writer):
    """Test functions mapping for QtWidgets.QPlainTextEdit."""
    assert QtWidgets.QPlainTextEdit.setTabStopWidth
    assert QtWidgets.QPlainTextEdit.tabStopWidth
    assert QtWidgets.QPlainTextEdit.setTabStopDistance
    assert QtWidgets.QPlainTextEdit.tabStopDistance
    assert QtWidgets.QPlainTextEdit.print_
    assert QtWidgets.QPlainTextEdit.print
    plaintextedit_widget = QtWidgets.QPlainTextEdit(None)
    plaintextedit_widget.setTabStopWidth(90)
    assert plaintextedit_widget.tabStopWidth() == 90
    plaintextedit_widget.setTabStopDistance(89.0)
    assert plaintextedit_widget.tabStopDistance() == 89.0
    print_device, output_path = pdf_writer
    plaintextedit_widget.print_(print_device)
    plaintextedit_widget.print(print_device)
    assert output_path.exists()


def test_qapplication_functions():
    """Test functions mapping for QtWidgets.QApplication."""
    assert QtWidgets.QApplication.exec_
    assert QtWidgets.QApplication.exec


@pytest.mark.skipif(
    sys.platform.startswith('linux') and not_using_conda(),
    reason="Fatal Python error: Aborted on Linux CI when not using conda")
@pytest.mark.skipif(
    sys.platform == 'darwin' and sys.version_info[:2] == (3, 7),
    reason="Stalls on macOS CI with Python 3.7")
def test_qdialog_functions(qtbot):
    """Test functions mapping for QtWidgets.QDialog."""
    assert QtWidgets.QDialog.exec_
    dialog = QtWidgets.QDialog(None)
    QtCore.QTimer.singleShot(1000, dialog.accept)
    dialog.exec_()
    assert QtWidgets.QDialog.exec
    dialog = QtWidgets.QDialog(None)
    QtCore.QTimer.singleShot(1000, dialog.accept)
    dialog.exec()


@pytest.mark.skipif(
    sys.platform.startswith('linux') and not_using_conda(),
    reason="Fatal Python error: Aborted on Linux CI when not using conda")
@pytest.mark.skipif(
    sys.platform == 'darwin' and sys.version_info[:2] == (3, 7),
    reason="Stalls on macOS CI with Python 3.7")
def test_qdialog_subclass(qtbot):
    """Test functions mapping for QtWidgets.QDialog when using a subclass"""
    assert QtWidgets.QDialog.exec_
    assert QtWidgets.QDialog.exec

    class CustomDialog(QtWidgets.QDialog):
        def __init__(self):
            super().__init__(None)
            self.setWindowTitle("Testing")
    assert CustomDialog.exec_
    dialog = CustomDialog()
    QtCore.QTimer.singleShot(1000, dialog.accept)
    dialog.exec_()
    assert CustomDialog.exec
    dialog = CustomDialog()
    QtCore.QTimer.singleShot(1000, dialog.accept)
    dialog.exec()


@pytest.mark.skipif(
    sys.platform.startswith('linux') and not_using_conda(),
    reason="Fatal Python error: Aborted on Linux CI when not using conda")
@pytest.mark.skipif(
    sys.platform == 'darwin' and sys.version_info[:2] == (3, 7),
    reason="Stalls on macOS CI with Python 3.7")
def test_qmenu_functions(qtbot):
    """Test functions mapping for QtWidgets.QDialog."""
    window = QtWidgets.QMainWindow()  # required for static calls
    menu = QtWidgets.QMenu(window)
    menu.addAction('qtpy')
    window.show()

    # test calls to `exec_` and `exec` of a `QMenu` instance
    QtCore.QTimer.singleShot(100, menu.close)
    menu.exec_()
    QtCore.QTimer.singleShot(100, menu.close)
    menu.exec()

    # test static calls to `QMenu.exec_` and `QMenu.exec`
    QtCore.QTimer.singleShot(100, lambda: qtbot.keyClick(
        QtWidgets.QApplication.widgetAt(1, 1),
        QtCore.Qt.Key.Key_Escape)
    )
    QtWidgets.QMenu.exec_(menu.actions(), QtCore.QPoint(1, 1))
    QtCore.QTimer.singleShot(100, lambda: qtbot.keyClick(
        QtWidgets.QApplication.widgetAt(1, 1),
        QtCore.Qt.Key.Key_Escape)
    )
    QtWidgets.QMenu.exec(menu.actions(), QtCore.QPoint(1, 1))


@pytest.mark.skipif(
    sys.platform.startswith('linux') and not_using_conda(),
    reason="Fatal Python error: Aborted on Linux CI when not using conda")
def test_QWizardPage_registerField_changedSignal():
    """Test that `changedSignal` can be a `str`"""
    class Spam(QtWidgets.QWizardPage):
        def __init__(self):
            super().__init__()
            self.widget = QtWidgets.QWidget(self)
            self.registerField('title', self.widget, 'windowTitle', 'self.widget.windowTitleChanged')

    app = QtWidgets.QApplication.instance() or QtWidgets.QApplication([])
    Spam()


def test_enum_access():
    """Test scoped and unscoped enum access for qtpy.QtWidgets.*."""
    assert QtWidgets.QFileDialog.AcceptOpen == QtWidgets.QFileDialog.AcceptMode.AcceptOpen
    assert QtWidgets.QMessageBox.InvalidRole == QtWidgets.QMessageBox.ButtonRole.InvalidRole
    assert QtWidgets.QStyle.State_None == QtWidgets.QStyle.StateFlag.State_None
    assert QtWidgets.QSlider.TicksLeft == QtWidgets.QSlider.TickPosition.TicksAbove
    assert QtWidgets.QStyle.SC_SliderGroove == QtWidgets.QStyle.SubControl.SC_SliderGroove
