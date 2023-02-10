"""Test QtCore."""

import sys
from datetime import datetime

import pytest
from packaging.version import parse

from qtpy import (
    PYQT5,
    PYQT6,
    PYSIDE2,
    PYSIDE6,
    PYSIDE_VERSION,
    QtCore,
)
from qtpy.tests.utils import not_using_conda

NOW = datetime.now()
NOW = NOW.replace(microsecond=(NOW.microsecond // 1000 * 1000))  # make integer milliseconds


def test_qtmsghandler():
    """Test qtpy.QtMsgHandler"""
    assert QtCore.qInstallMessageHandler is not None


def test_qEnvironmentVariable():
    """Test `QtCore.qEnvironmentVariable`"""
    import os

    assert QtCore.qEnvironmentVariable('PATH') == os.environ.get('PATH', '')


def test_qbytearray_functions():
    """Text `QByteArray.chopped`, `QByteArray.isUpper`, and `QByteArray.isLower`"""
    assert QtCore.QByteArray(b'123456789').chopped(3) == QtCore.QByteArray(b'123456')
    assert not QtCore.QByteArray(b'spam').isUpper()
    assert not QtCore.QByteArray(b'Spam').isUpper()
    assert QtCore.QByteArray(b'SPAM').isUpper()
    assert QtCore.QByteArray(b'spam').isLower()
    assert not QtCore.QByteArray(b'Spam').isLower()
    assert not QtCore.QByteArray(b'SPAM').isLower()


def test_qbytearray_base64_functions():
    """Test `QByteArray.Base64Option`, `QByteArray.Base64DecodingStatus`, and `QByteArray.fromBase64Encoding`"""
    # NB: store the result of `QByteArray.fromBase64Encoding` into a variable to avoid
    #  RuntimeError: Internal C++ object (PySide2.QtCore.QByteArray) already deleted.
    #  on PySide2>=5.15 on Python3.11
    decoding_result = QtCore.QByteArray.fromBase64Encoding(b'MTIzNDU2Nzg5')
    assert decoding_result.decodingStatus == QtCore.QByteArray.Base64DecodingStatus.Ok
    assert decoding_result.decoded == QtCore.QByteArray(b'123456789')
    decoding_result = QtCore.QByteArray.fromBase64Encoding(b'MTIzNDU2Nzg5=')
    assert decoding_result.decodingStatus == QtCore.QByteArray.Base64DecodingStatus.Ok
    assert decoding_result.decoded == QtCore.QByteArray(b'123456789')
    decoding_result = QtCore.QByteArray.fromBase64Encoding(b'MTIzNDU2Nzg5=',
                                                           QtCore.QByteArray.Base64Option.AbortOnBase64DecodingErrors)
    assert decoding_result.decodingStatus == QtCore.QByteArray.Base64DecodingStatus.IllegalInputLength
    decoding_result = QtCore.QByteArray.fromBase64Encoding(b'MTIzNDU2Nzg5====',
                                                           QtCore.QByteArray.Base64Option.AbortOnBase64DecodingErrors)
    assert decoding_result.decodingStatus == QtCore.QByteArray.Base64DecodingStatus.IllegalPadding
    decoding_result = QtCore.QByteArray.fromBase64Encoding(b'MTIzNDU2Nzg5:-)=',
                                                           QtCore.QByteArray.Base64Option.AbortOnBase64DecodingErrors)
    assert decoding_result.decodingStatus == QtCore.QByteArray.Base64DecodingStatus.IllegalCharacter


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


def test_qdate_functions():
    """Test `QDate.startOfDay` and `QDate.endOfDay`"""
    q_date = QtCore.QDateTime(NOW).date()
    time_zone = QtCore.QTimeZone(QtCore.QByteArray(b'America/Chicago'))
    spec = QtCore.Qt.TimeSpec.UTC
    offset = 314

    assert q_date.startOfDay() == QtCore.QDateTime(q_date, QtCore.QTime(0, 0))
    assert q_date.startOfDay(time_zone) == QtCore.QDateTime(q_date, QtCore.QTime(0, 0), time_zone)
    assert q_date.startOfDay(spec) == QtCore.QDateTime(q_date, QtCore.QTime(0, 0), spec)
    assert q_date.startOfDay(spec, offset) == QtCore.QDateTime(q_date, QtCore.QTime(0, 0), spec, offset)

    assert q_date.endOfDay() == QtCore.QDateTime(q_date, QtCore.QTime(23, 59, 59, 999))
    assert q_date.endOfDay(time_zone) == QtCore.QDateTime(q_date, QtCore.QTime(23, 59, 59, 999), time_zone)
    assert q_date.endOfDay(spec) == QtCore.QDateTime(q_date, QtCore.QTime(23, 59, 59, 999), spec)
    assert q_date.endOfDay(spec, offset) == QtCore.QDateTime(q_date, QtCore.QTime(23, 59, 59, 999), spec, offset)


def test_qdatetime_YearRange():
    """Test `QDateTime.YearRange` and the access to `First` and `Last` of its"""
    if PYSIDE6 and parse(QtCore.__version__) < parse('6.4'):
        assert QtCore.QDateTime.YearRange.First < QtCore.QDateTime.YearRange.Last
    else:
        assert QtCore.QDateTime.YearRange.First.value < QtCore.QDateTime.YearRange.Last.value


def test_qline_toLineF():
    """Test `QLine.toLineF` and `QLineF.toLine`"""
    assert QtCore.QLine.toLineF is not None
    assert QtCore.QLineF.toLine is not None


def test_qmargins_toMarginsF():
    """Test `QMargins.toMarginsF` and `QMarginsF.toMargins`"""
    assert QtCore.QMargins.toMarginsF is not None
    assert QtCore.QMarginsF.toMargins is not None


def test_qpoint_toPointF():
    """Test `QPoint.toPointF` and `QPointF.toPoint`"""
    assert QtCore.QPoint.toPointF is not None
    assert QtCore.QPointF.toPoint is not None


def test_qrect_toRectF():
    """Test `QRect.toRectF` and `QRectF.toRect`"""
    assert QtCore.QRect.toRectF is not None
    assert QtCore.QRectF.toRect is not None


def test_qsize_functions():
    """Test `QSize` functions"""
    assert QtCore.QSize.toSizeF is not None
    assert QtCore.QSize.grownBy is not None
    assert QtCore.QSize.shrunkBy is not None


def test_qsizef_functions():
    """Test `QSizeF` functions"""
    assert QtCore.QSizeF.toSize is not None
    assert QtCore.QSizeF.grownBy is not None
    assert QtCore.QSizeF.shrunkBy is not None


def test_qmodelindex_functions():
    """Test `QModelIndex` functions"""
    assert QtCore.QModelIndex.siblingAtColumn is not None
    assert QtCore.QModelIndex.siblingAtRow is not None


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
    assert QtCore.QTextStreamManipulator.exec_ is not None
    assert QtCore.QTextStreamManipulator.exec is not None


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
