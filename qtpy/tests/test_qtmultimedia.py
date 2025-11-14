import pytest

from qtpy import PYQT5, PYQT6, PYQT_VERSION, PYSIDE6, QtMultimedia


def test_qtmultimedia():
    """Test the qtpy.QtMultimedia namespace"""
    assert QtMultimedia.QAudio is not None
    assert QtMultimedia.QAudioInput is not None

    if not (PYSIDE6 or PYQT6):
        assert QtMultimedia.QAbstractVideoBuffer is not None
        assert QtMultimedia.QAudioDeviceInfo is not None
        assert QtMultimedia.QSound is not None


@pytest.mark.skipif(
    PYQT5 and PYQT_VERSION.startswith("5.9"),
    reason=(
        "A specific setup with at least sip 4.9.9 is needed for PyQt5 5.9.* "
        "to work with scoped enum access"
    ),
)
def test_enum_access():
    """Test scoped and unscoped enum access."""
    assert (
        QtMultimedia.QAudio.LinearVolumeScale
        == QtMultimedia.QAudio.VolumeScale.LinearVolumeScale
    )
