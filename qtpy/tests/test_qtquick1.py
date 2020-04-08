from __future__ import absolute_import

import pytest
from qtpy import PYQT4, PYSIDE

@pytest.mark.skipif(not (PYQT4 or PYSIDE), reason="Only available in Qt4 bindings")
def test_QtQuick1():
    """Test the qtpy.QtQuick1 namespace"""
    from qtpy import QtQuick1
    # assert QtQuick1.ListProperty is not None
    assert QtQuick1.QDeclarativeComponent is not None
    assert QtQuick1.QDeclarativeContext is not None
    assert QtQuick1.QDeclarativeEngine is not None
    assert QtQuick1.QDeclarativeError is not None
    assert QtQuick1.QDeclarativeExpression is not None
    # assert QtQuick1.QDeclarativeExtensionInterface is not None
    assert QtQuick1.QDeclarativeExtensionPlugin is not None
    assert QtQuick1.QDeclarativeImageProvider is not None
    assert QtQuick1.QDeclarativeItem is not None
    assert QtQuick1.QDeclarativeNetworkAccessManagerFactory is not None
    assert QtQuick1.QDeclarativeParserStatus is not None
    assert QtQuick1.QDeclarativeProperty is not None
    assert QtQuick1.QDeclarativePropertyMap is not None
    assert QtQuick1.QDeclarativePropertyValueSource is not None
    assert QtQuick1.QDeclarativeScriptString is not None
    assert QtQuick1.QDeclarativeView is not None
    # assert QtQuick1.QML_HAS_ATTACHED_PROPERTIES is not None
    # assert QtQuick1.qmlRegisterType is not None
    if not PYSIDE:
        assert QtQuick1.QPyDeclarativeListProperty is not None
        assert QtQuick1.QPyDeclarativePropertyValueSource is not None
