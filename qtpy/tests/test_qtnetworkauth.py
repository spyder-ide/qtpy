import pytest
from qtpy import PYQT5, PYQT6, PYSIDE2, PYSIDE6

@pytest.mark.skipif(PYSIDE2 or PYQT5, reason="Not available in CI")
def test_qtnetworkauth():
    """Test the qtpy.QtNetworkAuth namespace"""
    from qtpy import QtNetworkAuth
    assert QtNetworkAuth.QAbstractOAuth is not None
    assert QtNetworkAuth.QAbstractOAuth2 is not None
    assert QtNetworkAuth.QAbstractOAuthReplyHandler is not None
    assert QtNetworkAuth.QOAuth1 is not None
    assert QtNetworkAuth.QOAuth1Signature is not None
    assert QtNetworkAuth.QOAuth2AuthorizationCodeFlow is not None
