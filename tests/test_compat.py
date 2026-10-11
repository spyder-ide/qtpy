"""Test the compat module."""

import os
import sys

import pytest
from packaging import version

from qtpy import PYQT5, PYQT_VERSION, QtCore, QtWidgets, compat
from qtpy.QtCore import QSize
from qtpy.QtGui import QImage
from tests.utils import not_using_conda


@pytest.mark.skipif(
    (
        (sys.version_info.major == 3 and sys.version_info.minor == 7)
        and sys.platform.startswith("win")
        and not not_using_conda()
    ),
    reason="sip not included in Python3.7 on Windows",
)
def test_isalive(qtbot):
    """Test compat.isalive"""
    test_widget = QtWidgets.QWidget()
    assert compat.isalive(test_widget) is True
    with qtbot.waitSignal(test_widget.destroyed):
        test_widget.deleteLater()
    assert compat.isalive(test_widget) is False


def test_getenumasint():
    """Test compat.getenumasint"""
    if PYQT5 and version.parse(PYQT_VERSION) <= version.parse("5.9.2"):
        assert compat.getenumasint(QtWidgets.QSizePolicy.Maximum) == 4
    else:
        assert compat.getenumasint(QtWidgets.QSizePolicy.Policy.Maximum) == 4
    assert compat.getenumasint(5) == 5


def test_getenumfromint():
    """Test compat.getenumfromint"""
    enum_value = compat.getenumfromint(QtWidgets.QSizePolicy.Policy, 7)
    if PYQT5 and version.parse(PYQT_VERSION) <= version.parse("5.9.2"):
        assert enum_value == QtWidgets.QSizePolicy.Expanding
    else:
        assert enum_value == QtWidgets.QSizePolicy.Policy.Expanding


def test_getimagebytes(qtbot):
    """Test compat.getimagebytes"""
    image = QImage(QSize(100, 100), QImage.Format_RGB32)
    _bytes = compat.getimagebytes(image)
    assert len(_bytes) == 100 * 100 * 4


def test_getexistingdirectory_accept_label(tmp_path, qtbot):
    """Test compat.getexistingdirectory with a custom accept button label"""
    seen = {}

    def accept_dialog():
        app = QtWidgets.QApplication.instance()
        for dlg in app.topLevelWidgets():
            if isinstance(dlg, QtWidgets.QFileDialog) and dlg.isVisible():
                seen["accept_label"] = dlg.labelText(
                    QtWidgets.QFileDialog.Accept,
                )
                seen["accept_mode"] = dlg.acceptMode()
                dlg.accept()
                return
        QtCore.QTimer.singleShot(50, accept_dialog)

    QtCore.QTimer.singleShot(50, accept_dialog)
    result = compat.getexistingdirectory(
        caption="Select a directory",
        basedir=str(tmp_path),
        options=QtWidgets.QFileDialog.ShowDirsOnly
        | QtWidgets.QFileDialog.DontUseNativeDialog,
        accept_label="Select",
    )
    assert seen["accept_label"] == "Select"
    assert seen["accept_mode"] == QtWidgets.QFileDialog.AcceptOpen
    assert os.path.samefile(result, tmp_path)
