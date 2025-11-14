"""Test QtPrintSupport."""

import pytest

from qtpy import PYQT5, PYQT_VERSION, QtPrintSupport


def test_qtprintsupport():
    """Test the qtpy.QtPrintSupport namespace"""
    assert QtPrintSupport.QAbstractPrintDialog is not None
    assert QtPrintSupport.QPageSetupDialog is not None
    assert QtPrintSupport.QPrintDialog is not None
    assert QtPrintSupport.QPrintPreviewDialog is not None
    assert QtPrintSupport.QPrintEngine is not None
    assert QtPrintSupport.QPrinter is not None
    assert QtPrintSupport.QPrinterInfo is not None
    assert QtPrintSupport.QPrintPreviewWidget is not None


def test_qpagesetupdialog_exec_():
    """Test qtpy.QtPrintSupport.QPageSetupDialog exec_"""
    assert QtPrintSupport.QPageSetupDialog.exec_ is not None


def test_qprintdialog_exec_():
    """Test qtpy.QtPrintSupport.QPrintDialog exec_"""
    assert QtPrintSupport.QPrintDialog.exec_ is not None


def test_qprintpreviewwidget_print_(qtbot):
    """Test qtpy.QtPrintSupport.QPrintPreviewWidget print_"""
    assert QtPrintSupport.QPrintPreviewWidget.print_ is not None
    preview_widget = QtPrintSupport.QPrintPreviewWidget()
    preview_widget.print_()


@pytest.mark.skipif(
    PYQT5 and PYQT_VERSION.startswith("5.9"),
    reason=(
        "A specific setup with at least sip 4.9.9 is needed for PyQt5 5.9.* "
        "to work with scoped enum access"
    ),
)
def test_enum_access():
    """Test scoped and unscoped enum access"""
    assert (
        QtPrintSupport.QPrinter.HighResolution
        == QtPrintSupport.QPrinter.PrinterMode.HighResolution
    )
