import pytest

from qtpy import PYQT5, PYQT6, PYQT_VERSION, PYSIDE6, QtTest, _parse_version


def test_qttest():
    """Test the qtpy.QtTest namespace"""
    assert QtTest.QTest is not None

    if PYQT5 or PYQT6 or PYSIDE6:
        assert QtTest.QSignalSpy is not None

        if (
            (PYQT5 and _parse_version(PYQT_VERSION) >= _parse_version("5.11"))
            or PYQT6
            or PYSIDE6
        ):
            assert QtTest.QAbstractItemModelTester is not None


@pytest.mark.skipif(
    PYQT5 and PYQT_VERSION.startswith("5.9"),
    reason="A specific setup with at least sip 4.9.9 is needed for PyQt5 5.9.*"
    "to work with scoped enum access",
)
def test_enum_access():
    """Test scoped and unscoped enum access for qtpy.QtTest.*."""
    assert QtTest.QTest.Click == QtTest.QTest.KeyAction.Click
