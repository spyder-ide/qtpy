# coding=utf-8
import importlib
from types import ModuleType

import pytest

from qtpy import API_NAME, QT6
from qtpy.tests.utils import using_conda


@pytest.mark.skipif(
    QT6 and using_conda(),
    reason="QPositioning bindings not included in Conda qt-main >= 6.4.3.",
)
def test_qtpositioning():
    """Test the qtpy.QtPositioning namespace"""
    from qtpy import QtPositioning

    assert QtPositioning.QGeoAddress is not None
    assert QtPositioning.QGeoAreaMonitorInfo is not None
    assert QtPositioning.QGeoAreaMonitorSource is not None
    assert QtPositioning.QGeoCircle is not None
    assert QtPositioning.QGeoCoordinate is not None
    assert QtPositioning.QGeoLocation is not None
    assert QtPositioning.QGeoPath is not None
    # CI for 3.7 uses Qt 5.9
    # assert QtPositioning.QGeoPolygon is not None  # New in Qt 5.10
    assert QtPositioning.QGeoPositionInfo is not None
    assert QtPositioning.QGeoPositionInfoSource is not None
    # QGeoPositionInfoSourceFactory is not available in PyQt
    # assert QtPositioning.QGeoPositionInfoSourceFactory is not None  # New in Qt 5.2
    # assert QtPositioning.QGeoPositionInfoSourceFactoryV2 is not None  # New in Qt 5.14
    assert QtPositioning.QGeoRectangle is not None
    assert QtPositioning.QGeoSatelliteInfo is not None
    assert QtPositioning.QGeoSatelliteInfoSource is not None
    assert QtPositioning.QGeoShape is not None
    assert QtPositioning.QNmeaPositionInfoSource is not None


@pytest.mark.skipif(
    QT6 and using_conda(),
    reason="QPositioning bindings not included in Conda qt-main >= 6.4.3.",
)
def test_namespace_not_polluted():
    """Test that no extra members are exported into the module namespace."""
    from qtpy import QtPositioning

    qtpy_module: ModuleType = QtPositioning
    original_module: ModuleType = importlib.import_module(
        qtpy_module.__name__.replace('qtpy', API_NAME)
    )

    extra_members = (
        frozenset(dir(qtpy_module))
        - frozenset(dir(original_module))
        - frozenset(
            # These are unavoidable:
            [
                "__builtins__",
                "__cached__",
            ]
        )
    )
    assert not extra_members
