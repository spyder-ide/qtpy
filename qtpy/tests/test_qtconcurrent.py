import pytest

def test_qtconcurrent():
    """Test the qtpy.QtConcurrent namespace"""
    QtConcurrent = pytest.importorskip("qtpy.QtConcurrent")
  
    assert QtConcurrent.QtConcurrent is not None
    assert QtConcurrent.QFutureQString is not None
    assert QtConcurrent.QFutureVoid is not None
    assert QtConcurrent.QFutureWatcherQString is not None
    assert QtConcurrent.QFutureWatcherVoid is not None