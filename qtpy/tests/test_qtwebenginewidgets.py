from __future__ import absolute_import

import pytest


def test_qtwebenginewidgets():
    """Test the qtpy.QtWebSockets namespace"""
    from qtpy import QtWebEngineWidgets

    assert QtWebEngineWidgets.QWebEnginePage is not None
    assert QtWebEngineWidgets.QWebEngineView is not None
    assert QtWebEngineWidgets.QWebEngineSettings is not None
