import importlib
from typing import TYPE_CHECKING

import pytest
from packaging import version

from qtpy import API_NAME, PYQT5, PYQT_VERSION, PYSIDE2

if TYPE_CHECKING:
    from types import ModuleType


@pytest.mark.skipif(
    not (
        (PYQT5 and version.parse(PYQT_VERSION) >= version.parse("5.15.1"))
        or PYSIDE2
    ),
    reason="Only available in Qt5 bindings (PyQt5 >= 5.15.1 or PySide2)",
)
def test_qttexttospeech():
    """Test the qtpy.QtTextToSpeech namespace."""
    from qtpy import QtTextToSpeech

    assert QtTextToSpeech.QTextToSpeech is not None
    assert QtTextToSpeech.QVoice is not None

    if PYSIDE2:
        assert QtTextToSpeech.QTextToSpeechEngine is not None


@pytest.mark.skipif(
    not (
        (PYQT5 and version.parse(PYQT_VERSION) >= version.parse("5.15.1"))
        or PYSIDE2
    ),
    reason="Only available in Qt5 bindings (PyQt5 >= 5.15.1 or PySide2)",
)
def test_namespace_not_polluted():
    """Test that no extra members are exported into the module namespace."""
    from qtpy import QtTextToSpeech

    qtpy_module: ModuleType = QtTextToSpeech
    original_module: ModuleType = importlib.import_module(
        qtpy_module.__name__.replace("qtpy", API_NAME),
    )

    extra_members = (
        frozenset(dir(qtpy_module))
        - frozenset(dir(original_module))
        - frozenset(
            # These are unavoidable:
            [
                "__builtins__",
                "__cached__",
            ],
        )
    )
    assert not extra_members
