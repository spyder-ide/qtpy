"""Test QtGui."""

import sys

import pytest

from qtpy import PYQT5, PYQT_VERSION, PYSIDE2, PYSIDE6, QtGui
from qtpy.tests.utils import not_using_conda


@pytest.mark.skipif(
    sys.platform.startswith('linux') and not_using_conda(),
    reason="Fatal Python error: Aborted on Linux CI when not using conda")
def test_qfontmetrics_width(qtbot):
    """Test QFontMetrics and QFontMetricsF width"""
    assert QtGui.QFontMetrics.width is not None
    assert QtGui.QFontMetricsF.width is not None
    assert QtGui.QFontMetrics.horizontalAdvance is not None
    assert QtGui.QFontMetricsF.horizontalAdvance is not None
    font = QtGui.QFont("times", 24)
    font_metrics = QtGui.QFontMetrics(font)
    font_metricsF = QtGui.QFontMetricsF(font)
    width = font_metrics.width("Test")
    widthF = font_metricsF.width("Test")
    assert width in range(40, 62)
    assert 39 <= widthF <= 63
    assert width == font_metrics.horizontalAdvance("Test")
    assert widthF == font_metricsF.horizontalAdvance("Test")


@pytest.mark.skipif(
    sys.platform.startswith('linux') and not_using_conda(),
    reason="Fatal Python error: Aborted on Linux CI when not using conda")
def test_qdrag_functions(qtbot):
    """Test functions mapping for QtGui.QDrag."""
    assert QtGui.QDrag.exec_ is not None
    assert QtGui.QDrag.exec is not None
    drag = QtGui.QDrag(None)
    drag.exec_()


def test_qcolor_functions():
    """Test functions mapping for QtGui.QColor."""
    assert QtGui.QColor('green').toTuple() == (0, 128, 0, 255)
    assert QtGui.QColor.isValidColor('green')
    assert QtGui.QColor.isValidColorName('green')
    assert QtGui.QColor.fromString('#008000').isValid()


def test_qimage_functions():
    """Test functions mapping for QtGui.QImage."""
    assert QtGui.QImage.sizeInBytes is not None


def test_qmouseevent_functions():
    """Test functions mapping for QtGui.QMouseEvent."""
    from qtpy import QtCore
    e = QtGui.QMouseEvent(QtCore.QEvent.Type.MouseMove,
                          QtCore.QPointF(42, 6 * 9),
                          QtCore.QPointF(42, 6 * 9),
                          QtCore.Qt.MouseButton.LeftButton,
                          QtCore.Qt.MouseButton.AllButtons,
                          QtCore.Qt.KeyboardModifier.NoModifier)
    assert e.position() == QtCore.QPointF(42, 54)
    assert e.pos() == QtCore.QPoint(42, 54)


def test_qwheelevent_functions():
    """Test functions mapping for QtGui.QWheelEvent."""
    from qtpy import QtCore
    e = QtGui.QWheelEvent(QtCore.QPointF(42, 6 * 9),
                          QtCore.QPointF(42, 6 * 9),
                          QtCore.QPoint(0, 0),
                          QtCore.QPoint(0, 0),
                          0,
                          QtCore.Qt.Orientation.Vertical,
                          QtCore.Qt.MouseButton.LeftButton,
                          QtCore.Qt.KeyboardModifier.NoModifier)
    assert e.position() == QtCore.QPointF(42.0, 54.0)
    assert e.globalPosition() == QtCore.QPointF(42.0, 54.0)


def test_qtabletevent_functions():
    """Test functions mapping for QtGui.QTabletEvent."""
    assert QtGui.QTabletEvent.deviceType is not None


def test_qguiapplication_functions():
    """Test functions mapping for QtGui.QGuiApplication."""
    assert QtGui.QGuiApplication.exec_ is not None
    assert QtGui.QGuiApplication.exec is not None


def test_what_moved_to_qtgui_in_qt6():
    """Test what has been moved to QtGui in Qt6"""
    assert QtGui.QAction is not None
    assert QtGui.QActionGroup is not None
    assert QtGui.QFileSystemModel is not None
    assert QtGui.QShortcut is not None
    assert QtGui.QUndoCommand is not None


@pytest.mark.skipif(
    sys.platform.startswith('linux') and not_using_conda(),
    reason="Segmentation fault/Aborted on Linux CI when not using conda")
def test_qtextdocument_functions(pdf_writer):
    """Test functions mapping for QtGui.QTextDocument."""
    assert QtGui.QTextDocument.print_ is not None
    assert QtGui.QTextDocument.print is not None
    text_document = QtGui.QTextDocument("Test")
    print_device, output_path = pdf_writer
    text_document.print_(print_device)
    text_document.print(print_device)
    assert output_path.exists()


def test_enum_access():
    """Test scoped and unscoped enum access for qtpy.QtWidgets.*."""
    assert QtGui.QColor.Rgb == QtGui.QColor.Spec.Rgb
    assert QtGui.QFont.AllUppercase == QtGui.QFont.Capitalization.AllUppercase
    assert QtGui.QIcon.Normal == QtGui.QIcon.Mode.Normal
    assert QtGui.QImage.Format_Invalid == QtGui.QImage.Format.Format_Invalid
    assert QtGui.QColorConstants.Black == QtGui.QColorConstants.Svg.black


@pytest.mark.skipif(not (PYSIDE2 or PYSIDE6), reason="PySide{2,6} specific test")
def test_qtextcursor_moveposition():
    """Test monkeypatched QTextCursor.movePosition"""
    doc = QtGui.QTextDocument("foo bar baz")
    cursor = QtGui.QTextCursor(doc)

    assert not cursor.movePosition(QtGui.QTextCursor.Start)
    assert cursor.movePosition(QtGui.QTextCursor.EndOfWord, mode=QtGui.QTextCursor.KeepAnchor)
    assert cursor.selectedText() == "foo"

    assert cursor.movePosition(QtGui.QTextCursor.Start)
    assert cursor.movePosition(QtGui.QTextCursor.WordRight, n=2, mode=QtGui.QTextCursor.KeepAnchor)
    assert cursor.selectedText() == "foo bar "

    assert cursor.movePosition(QtGui.QTextCursor.Start)
    assert cursor.position() == cursor.anchor()
    assert cursor.movePosition(QtGui.QTextCursor.NextWord, QtGui.QTextCursor.KeepAnchor, 3)
    assert cursor.selectedText() == "foo bar baz"
