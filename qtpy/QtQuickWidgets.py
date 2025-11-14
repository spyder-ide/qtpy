# -----------------------------------------------------------------------------
# Copyright © 2009- The Spyder Development Team
#
# Licensed under the terms of the MIT License
# (see LICENSE.txt for details)
# -----------------------------------------------------------------------------

"""Provides QtQuickWidgets classes and functions."""

from . import PYQT5, PYQT6, PYSIDE2, PYSIDE6

if PYQT5:
    from PyQt5.QtQuickWidgets import *
elif PYQT6:
    from PyQt6 import QtQuickWidgets
    from PyQt6.QtQuickWidgets import *

    # Allow unscoped access for enums
    from .enums_compat import promote_enums

    promote_enums(QtQuickWidgets)
    del QtQuickWidgets
elif PYSIDE6:
    from PySide6.QtQuickWidgets import *
elif PYSIDE2:
    from PySide2.QtQuickWidgets import *
