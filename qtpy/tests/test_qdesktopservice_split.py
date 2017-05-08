from __future__ import absolute_import

import pytest
from qtpy.QtCore import QStandardPaths
from qtpy.QtGui import QDesktopServices

"""Test QDesktopServices split in Qt5."""

def test_qstandarpath():
    """Test the qtpy.QStandardPaths namespace"""

    assert QStandardPaths.StandardLocation is not None

    # Attributes from QDesktopServices shouldn't be in QStandardPaths
    with pytest.raises(AttributeError) as excinfo:
        QStandardPaths.setUrlHandler

def test_qdesktopservice():
    """Test the qtpy.QDesktopServices namespace"""

    assert QDesktopServices.setUrlHandler is not None

    # Attributes from QStandardPaths shouldn't be in QDesktopServices
    with pytest.raises(AttributeError) as excinfo:
        QDesktopServices.StandardLocation