"""Test for QtHelp namespace."""

import pytest

from qtpy import PYQT5, PYQT_VERSION, QtHelp


def test_qthelp():
    """Test the qtpy.QtHelp namespace."""
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
        QtHelp.QHelpSearchQuery.DEFAULT
        == QtHelp.QHelpSearchQuery.FieldName.DEFAULT
    )
