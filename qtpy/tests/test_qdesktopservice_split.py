"""Test QDesktopServices split in Qt5."""

from __future__ import absolute_import

import pytest
import warnings


def test_qstandarpath():
    """Test the qtpy.QStandardPaths namespace"""
    from qtpy.QtCore import QStandardPaths

    assert QStandardPaths.StandardLocation is not None

    # Attributes from QDesktopServices shouldn't be in QStandardPaths
    with pytest.raises(AttributeError) as excinfo:
        QStandardPaths.setUrlHandler


def test_qdesktopservice():
    """Test the qtpy.QDesktopServices namespace"""
    from qtpy.QtGui import QDesktopServices

    assert QDesktopServices.setUrlHandler is not None


