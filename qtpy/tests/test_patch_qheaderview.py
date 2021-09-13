from __future__ import absolute_import

import sys

import pytest
from qtpy import PYSIDE2
from qtpy.QtWidgets import QApplication
from qtpy.QtWidgets import QHeaderView
from qtpy.QtCore import Qt
from qtpy.QtCore import QAbstractListModel


PY3 = sys.version[0] == "3"


def get_qapp(icon_path=None):
    qapp = QApplication.instance()
    if qapp is None:
        qapp = QApplication([''])
    return qapp


@pytest.mark.skipif(PY3 or PYSIDE2, reason="It fails on Python 3 and PySide2")
def test_patched_qheaderview():
    """
    This will test whether QHeaderView has the new methods introduced in Qt5.
    It will then create an instance of QHeaderView and test that no exceptions
    are raised and that some basic behaviour works.
    """
    assert QHeaderView.sectionsClickable is not None
    assert QHeaderView.sectionsMovable is not None
    assert QHeaderView.sectionResizeMode is not None
    assert QHeaderView.setSectionsClickable is not None
    assert QHeaderView.setSectionsMovable is not None
    assert QHeaderView.setSectionResizeMode is not None

    # setup a model and add it to a headerview
    qapp = get_qapp()
    headerview = QHeaderView(Qt.Horizontal)
    class Model(QAbstractListModel):
        pass
    model = Model()
    headerview.setModel(model)
    assert headerview.count() == 1

    # test it
    assert isinstance(headerview.sectionsClickable(), bool)
    assert isinstance(headerview.sectionsMovable(), bool)
    assert isinstance(headerview.sectionResizeMode(0), int)

    headerview.setSectionsClickable(True)
    assert headerview.sectionsClickable() == True
    headerview.setSectionsClickable(False)
    assert headerview.sectionsClickable() == False

    headerview.setSectionsMovable(True)
    assert headerview.sectionsMovable() == True
    headerview.setSectionsMovable(False)
    assert headerview.sectionsMovable() == False

    headerview.setSectionResizeMode(QHeaderView.Interactive)
    assert headerview.sectionResizeMode(0) == QHeaderView.Interactive
    headerview.setSectionResizeMode(QHeaderView.Fixed)
    assert headerview.sectionResizeMode(0) == QHeaderView.Fixed
    headerview.setSectionResizeMode(QHeaderView.Stretch)
    assert headerview.sectionResizeMode(0) == QHeaderView.Stretch
    headerview.setSectionResizeMode(QHeaderView.ResizeToContents)
    assert headerview.sectionResizeMode(0) == QHeaderView.ResizeToContents

    headerview.setSectionResizeMode(0, QHeaderView.Interactive)
    assert headerview.sectionResizeMode(0) == QHeaderView.Interactive
    headerview.setSectionResizeMode(0, QHeaderView.Fixed)
    assert headerview.sectionResizeMode(0) == QHeaderView.Fixed
    headerview.setSectionResizeMode(0, QHeaderView.Stretch)
    assert headerview.sectionResizeMode(0) == QHeaderView.Stretch
    headerview.setSectionResizeMode(0, QHeaderView.ResizeToContents)
    assert headerview.sectionResizeMode(0) == QHeaderView.ResizeToContents

