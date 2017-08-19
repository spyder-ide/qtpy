"""Test for QtHelp namespace."""

from __future__ import absolute_import
import warnings

import pytest
from qtpy import PYSIDE2, PythonQtWarning


@pytest.mark.skipif(PYSIDE2, reason="QtHelp binding is missing in PySide2")
def test_qthelp():
    """Test the qtpy.QtHelp namespace."""
    from qtpy import QtHelp

    assert QtHelp.QHelpContentItem is not None
    assert QtHelp.QHelpContentModel is not None
    assert QtHelp.QHelpContentWidget is not None
    assert QtHelp.QHelpEngine is not None
    assert QtHelp.QHelpEngineCore is not None
    assert QtHelp.QHelpIndexModel is not None
    assert QtHelp.QHelpIndexWidget is not None
    assert QtHelp.QHelpSearchEngine is not None
    assert QtHelp.QHelpSearchQuery is not None
    assert QtHelp.QHelpSearchQueryWidget is not None
    assert QtHelp.QHelpSearchResultWidget is not None


@pytest.mark.skipif(not PYSIDE2, reason="Only runs in not implemented bindings")
def test_qthelp_not_implemented():
    with warnings.catch_warnings(record=True) as w:
        # Cause all warnings to always be triggered.
        warnings.simplefilter("always")
        # Try to  import QtHelp.
        from qtpy import QtHelp

        assert len(w) == 1
        assert issubclass(w[-1].category, PythonQtWarning)
        assert "missing" in str(w[-1].message)
