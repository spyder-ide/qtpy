"""Test QtCore."""

import sys
from datetime import datetime

import pytest

from qtpy import (
    PYQT5,
    PYQT6,
    PYSIDE2,
    PYSIDE_VERSION,
    QtCore,
)
from qtpy.tests.utils import not_using_conda

NOW = datetime.now()
NOW = NOW.replace(microsecond=round(NOW.microsecond, -3))


def test_qtmsghandler():
    """Test qtpy.QtMsgHandler"""
    assert QtCore.qInstallMessageHandler is not None


def test_qdatetime_toPython():
    """Test QDateTime.toPython"""
    q_datetime = QtCore.QDateTime(NOW)
    py_date = q_datetime.toPython()
    assert py_date == NOW


def test_qdate_toPython():
    """Test QDate.toPython"""
    q_date = QtCore.QDateTime(NOW).date()
    py_date = q_date.toPython()
    assert py_date == NOW.date()


def test_qtime_toPython():
    """Test QTime.toPython"""
    q_time = QtCore.QDateTime(NOW).time()
    py_time = q_time.toPython()
    assert py_time == NOW.time()


def test_qdatetime_toPyDateTime():
    """Test QDateTime.toPyDateTime"""
    q_datetime = QtCore.QDateTime(NOW)
    py_date = q_datetime.toPyDateTime()
    assert py_date == NOW


def test_qdate_toPyDate():
    """Test QDate.toPyDate"""
    q_date = QtCore.QDateTime(NOW).date()
    py_date = q_date.toPyDate()
    assert py_date == NOW.date()


def test_qtime_toPyTime():
    """Test QTime.toPyTime"""
    q_time = QtCore.QDateTime(NOW).time()
    py_time = q_time.toPyTime()
    assert py_time == NOW.time()


def test_qpoint_toPointF():
    """Test `QPoint.toPointF` and `QPointF.toPoint`"""
    assert QtCore.QPoint.toPointF is not None
    assert QtCore.QPointF.toPoint is not None


@pytest.mark.skipif(
    sys.platform.startswith('linux') and not_using_conda(),
    reason="Fatal Python error: Aborted on Linux CI when not using conda")
def test_qeventloop_exec_(qtbot):
    """Test `QEventLoop.exec_` and `QEventLoop.exec`"""
    assert QtCore.QEventLoop.exec_ is not None
    assert QtCore.QEventLoop.exec is not None
    event_loop = QtCore.QEventLoop(None)
    QtCore.QTimer.singleShot(100, event_loop.quit)
    event_loop.exec_()


def test_qthread_exec_():
    """Test `QThread.exec_` and `QThread.exec`"""
    assert QtCore.QThread.exec_ is not None
    assert QtCore.QThread.exec is not None


def test_qlibraryinfo_location():
    """Test `QLibraryInfo.location` and `QLibraryInfo.LibraryLocation`"""
    assert QtCore.QLibraryInfo.location is not None
    assert QtCore.QLibraryInfo.location(QtCore.QLibraryInfo.PrefixPath) is not None
    assert QtCore.QLibraryInfo.LibraryLocation is not None


def test_qlibraryinfo_path():
    """Test `QLibraryInfo.path` and `QLibraryInfo.LibraryPath`"""
    assert QtCore.QLibraryInfo.path is not None
    assert QtCore.QLibraryInfo.path(QtCore.QLibraryInfo.LibraryPath.PrefixPath) is not None
    assert QtCore.QLibraryInfo.LibraryPath is not None


def test_qlibraryinfo_path_is_location():
    """Test `QLibraryInfo.path` is `QLibraryInfo.location`
       and `QLibraryInfo.LibraryPath` is `QLibraryInfo.LibraryLocation`"""
    assert (QtCore.QLibraryInfo.path(QtCore.QLibraryInfo.LibraryPath.PrefixPath)
            == QtCore.QLibraryInfo.location(QtCore.QLibraryInfo.LibraryLocation.PrefixPath))
    assert QtCore.QLibraryInfo.LibraryPath is QtCore.QLibraryInfo.LibraryLocation


@pytest.mark.skipif(PYQT5 or PYQT6,
                    reason="Doesn't seem to be present on PyQt5 and PyQt6")
def test_qtextstreammanipulator_exec_():
    """Test `QTextStreamManipulator.exec_` and `QTextStreamManipulator.exec`"""
    QtCore.QTextStreamManipulator.exec_ is not None
    QtCore.QTextStreamManipulator.exec is not None


@pytest.mark.skipif(PYSIDE2 or PYQT6,
                    reason="Doesn't seem to be present on PySide2 and PyQt6")
def test_QtCore_SignalInstance():
    class ClassWithSignal(QtCore.QObject):
        signal = QtCore.Signal()

    instance = ClassWithSignal()

    assert isinstance(instance.signal, QtCore.SignalInstance)


def test_enum_access():
    """Test scoped and unscoped enum access for qtpy.QtCore.*."""
    assert QtCore.QAbstractAnimation.Stopped == QtCore.QAbstractAnimation.State.Stopped
    assert QtCore.QEvent.ActionAdded == QtCore.QEvent.Type.ActionAdded
    assert QtCore.Qt.AlignLeft == QtCore.Qt.AlignmentFlag.AlignLeft
    assert QtCore.Qt.Key_Return == QtCore.Qt.Key.Key_Return
    assert QtCore.Qt.transparent == QtCore.Qt.GlobalColor.transparent
    assert QtCore.Qt.Widget == QtCore.Qt.WindowType.Widget
    assert QtCore.Qt.BackButton == QtCore.Qt.MouseButton.BackButton
    assert QtCore.Qt.XButton1 == QtCore.Qt.MouseButton.XButton1
    assert QtCore.Qt.BackgroundColorRole == QtCore.Qt.ItemDataRole.BackgroundColorRole
    assert QtCore.Qt.TextColorRole == QtCore.Qt.ItemDataRole.TextColorRole
    assert QtCore.Qt.MidButton == QtCore.Qt.MouseButton.MiddleButton


@pytest.mark.skipif(PYSIDE2 and PYSIDE_VERSION.startswith('5.12.0'),
                    reason="Utility functions unavailable for PySide2 5.12.0")
def test_qtgui_namespace_mightBeRichText():
    """
    Test included elements (mightBeRichText) from module QtGui.

    See: https://doc.qt.io/qt-5/qt-sub-qtgui.html
    """
    assert QtCore.Qt.mightBeRichText is not None
