from __future__ import absolute_import

import pytest
import warnings
from qtpy import PYSIDE2, PythonQtWarning


@pytest.mark.skipif(PYSIDE2, reason="It fails on PySide2")
def test_qtmultimedia():
    """Test the qtpy.QtMultimedia namespace"""
    from qtpy import QtMultimedia

    assert QtMultimedia.QAbstractVideoBuffer is not None
    assert QtMultimedia.QAudio is not None
    assert QtMultimedia.QAudioDeviceInfo is not None
    assert QtMultimedia.QAudioInput is not None
    assert QtMultimedia.QSound is not None


@pytest.mark.skipif(not PYSIDE2, reason="Only runs in not implemented bindings")
def test_qtmultimedia_not_implemented():
    with warnings.catch_warnings(record=True) as w:
        # Cause all warnings to always be triggered.
        warnings.simplefilter("always")
        # Try to  import QtMultimedia.
        from qtpy import QtMultimedia

        assert len(w) == 1
        assert issubclass(w[-1].category, PythonQtWarning)
        assert "missing" in str(w[-1].message)
