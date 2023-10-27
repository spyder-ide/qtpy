# coding=utf-8
import importlib
from types import ModuleType

from qtpy import API_NAME, PYQT6, PYSIDE6, QtMultimedia


def test_qtmultimedia():
    """Test the qtpy.QtMultimedia namespace"""
    assert QtMultimedia.QAudio is not None
    assert QtMultimedia.QAudioInput is not None

    if not (PYSIDE6 or PYQT6):
        assert QtMultimedia.QAbstractVideoBuffer is not None
        assert QtMultimedia.QAudioDeviceInfo is not None
        assert QtMultimedia.QSound is not None


def test_namespace_not_polluted():
    """Test that no extra members are exported into the module namespace."""
    qtpy_module: ModuleType = QtMultimedia
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
