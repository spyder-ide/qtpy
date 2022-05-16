import pytest
import sys
from qtpy import PYSIDE2, PYSIDE6, PYQT5, PYQT6

@pytest.mark.skipif(PYSIDE2, reason="Not available in PySide2")
@pytest.mark.skipif(sys.platform != 'linux', reason="Only available on Linux")
def test_qtdbus():
    """Test the qtpy.QtDBus namespace"""
    from qtpy import QtDBus

    assert QtDBus.QDBusAbstractAdaptor is not None
    assert QtDBus.QDBusAbstractInterface is not None
    assert QtDBus.QDBusArgument is not None
    assert QtDBus.QDBusConnection is not None
