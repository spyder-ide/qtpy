# coding=utf-8
import importlib
from types import ModuleType

import pytest
from packaging import version

from qtpy import API_NAME, PYQT5, PYQT6, PYQT_VERSION, PYSIDE6, QtTest


def test_qttest():
    """Test the qtpy.QtTest namespace"""
    assert QtTest.QTest is not None

    if PYQT5 or PYQT6 or PYSIDE6:
        assert QtTest.QSignalSpy is not None

        if (
            (PYQT5 and version.parse(PYQT_VERSION) >= version.parse("5.11"))
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


def test_namespace_not_polluted():
    """Test that no extra members are exported into the module namespace."""
    qtpy_module: ModuleType = QtTest
    original_module: ModuleType = importlib.import_module(
        qtpy_module.__name__.replace('qtpy', API_NAME)
    )

    extra_members = (
        frozenset(dir(qtpy_module))
        - frozenset(dir(original_module))
        - frozenset(
            # These are unavoidable:
            [
                "__builtins__",
                "__cached__",
            ]
        )
    )
    assert not extra_members
