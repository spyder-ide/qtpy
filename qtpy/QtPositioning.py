# -----------------------------------------------------------------------------
# Copyright 2020 Antonio Valentino
#
# Licensed under the terms of the MIT License
# (see LICENSE for details)
# -----------------------------------------------------------------------------

"""Provides QtPositioning classes and functions."""

from . import PYQT5, PYQT6, PYSIDE2, PYSIDE6

if PYQT5:
    from PyQt5.QtPositioning import *
elif PYQT6:
    from PyQt6 import QtPositioning
    from PyQt6.QtPositioning import *

    # Allow unscoped access for enums
    from .enums_compat import promote_enums

    promote_enums(QtPositioning)
    del QtPositioning
elif PYSIDE2:
    from PySide2.QtPositioning import *
elif PYSIDE6:
    from PySide6.QtPositioning import *
