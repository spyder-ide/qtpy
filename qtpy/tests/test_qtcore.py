"""Test QtCore."""

import pytest

from qtpy import PYQT5, PYQT6, PYSIDE2, PYQT_VERSION, QtCore


def test_qtmsghandler():
    """Test qtpy.QtMsgHandler"""
    assert QtCore.qInstallMessageHandler is not None


def test_DateTime_toPython():
    """Test QDateTime.toPython"""
    assert QtCore.QDateTime.toPython is not None


@pytest.mark.skipif(PYSIDE2 or PYQT6,
                    reason="Doesn't seem to be present on PySide2 and PyQt6")
def test_QtCore_SignalInstance():
    class ClassWithSignal(QtCore.QObject):
        signal = QtCore.Signal()

    instance = ClassWithSignal()

    assert isinstance(instance.signal, QtCore.SignalInstance)


@pytest.mark.skipif(PYQT5 and PYQT_VERSION.startswith('5.9'),
                    reason="A specific setup with at least sip 4.9.9 is needed for PyQt5 5.9.*"
                           "to work with scoped enum access")
def test_enum_access():
    """Test scoped and unscoped enum access for qtpy.QtCore.*."""
    assert QtCore.QAbstractAnimation.Stopped == QtCore.QAbstractAnimation.State.Stopped
    assert QtCore.QEvent.ActionAdded == QtCore.QEvent.Type.ActionAdded
    assert QtCore.Qt.AlignLeft == QtCore.Qt.AlignmentFlag.AlignLeft
    assert QtCore.Qt.Key_Return == QtCore.Qt.Key.Key_Return
    assert QtCore.Qt.transparent == QtCore.Qt.GlobalColor.transparent
    assert QtCore.Qt.Widget == QtCore.Qt.WindowType.Widget


def test_qtgui_namespace_mightBeRichText():
    """
    Test included elements (mightBeRichText) from module QtGui.

    See: https://doc.qt.io/qt-5/qt-sub-qtgui.html
    """
    assert QtCore.Qt.mightBeRichText is not None
