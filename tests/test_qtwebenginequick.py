import pytest

from qtpy import PYQT5, PYSIDE2
from tests.utils import pytest_importorskip, using_conda


@pytest.mark.skipif(not using_conda(), reason="Fails with pip packages")
@pytest.mark.skipif(PYQT5 or PYSIDE2, reason="Only available in Qt6 bindings")
def test_qtwebenginequick():
    """Test the qtpy.QtWebEngineQuick namespace"""
    QtWebEngineQuick = pytest_importorskip("qtpy.QtWebEngineQuick")

    assert QtWebEngineQuick.QtWebEngineQuick is not None
    assert QtWebEngineQuick.QQuickWebEngineProfile is not None


@pytest.mark.skipif(not using_conda(), reason="Fails with pip packages")
@pytest.mark.skipif(PYQT5 or PYSIDE2, reason="Only available in Qt6 bindings")
def test_enum_access():
    """Test scoped and unscoped enum access."""
    QtWebEngineQuick = pytest_importorskip("qtpy.QtWebEngineQuick")

    assert (
        QtWebEngineQuick.QQuickWebEngineProfile.NoPersistentCookies
        == QtWebEngineQuick.QQuickWebEngineProfile.PersistentCookiesPolicy.NoPersistentCookies
    )
