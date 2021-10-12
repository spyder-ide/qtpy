from __future__ import absolute_import
import os
import sys

import pytest
from qtpy import PYSIDE6


@pytest.mark.skipif(sys.version_info[0] == 3,
                    reason="Conda packages don't seem to include QtMultimedia")
def test_qtmultimedia():
    """Test the qtpy.QtMultimedia namespace"""
    from qtpy import QtMultimedia

    assert QtMultimedia.QAbstractVideoBuffer is not None
    assert QtMultimedia.QAudio is not None
    assert QtMultimedia.QAudioDeviceInfo is not None
    assert QtMultimedia.QAudioInput is not None
    assert QtMultimedia.QSound is not None
