"""Test QtSerialBus."""

import pytest
from qtpy import (
    parse,
    PYSIDE6,
    PYSIDE_VERSION,
    QtBindingMissingModuleError,
)


@pytest.mark.skipif(not PYSIDE6 or parse(PYSIDE_VERSION) >= parse('6.5'), reason='.')
def test_qtserialbus_pyside6_below_6_5():
    with pytest.raises(QtBindingMissingModuleError) as excinfo:
        from qtpy import QtSerialBus


@pytest.mark.skipif(not PYSIDE6 or parse(PYSIDE_VERSION) < parse('6.5'), reason='.')
def test_qtserialbus_pyside6_above_6_5():
    """Test the qtpy.QtSerialBus namespace"""
    from qtpy import QtSerialBus

    assert QtSerialBus.QCanBus is not None
    assert QtSerialBus.QCanBusDevice is not None
    assert QtSerialBus.QCanBusDeviceInfo is not None
    assert QtSerialBus.QModbusClient is not None
    assert QtSerialBus.QModbusServer is not None
    assert QtSerialBus.QModbusDevice is not None
