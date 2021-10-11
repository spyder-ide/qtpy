import pytest
from qtpy import PYQT5

@pytest.mark.skipif(not PYQT5, reason="Only available in Qt5 bindings, but still not in PySide2")
def test_qtserialport():
    """Test the qtpy.QtSerialPort namespace"""
    from qtpy import QtSerialPort

    assert QtSerialPort.QSerialPort is not None
    assert QtSerialPort.QSerialPortInfo is not None
