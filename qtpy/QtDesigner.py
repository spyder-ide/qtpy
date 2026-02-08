# -----------------------------------------------------------------------------
# Copyright © 2014-2015 Colin Duquesnoy
#
# Licensed under the terms of the MIT License
# (see LICENSE for details)
# -----------------------------------------------------------------------------

"""Provides QtDesigner classes and functions."""

from . import (
    PYQT5,
    PYQT6,
    PYSIDE2,
    PYSIDE6,
    QtBindingMissingModuleError,
)

if PYQT5:
    from PyQt5.QtDesigner import *
elif PYQT6:
    from PyQt6 import QtDesigner
    from PyQt6.QtDesigner import *

    # Allow unscoped access for enums
    from .enums_compat import promote_enums

    promote_enums(QtDesigner)
    del QtDesigner
elif PYSIDE2:
    raise QtBindingMissingModuleError(name="QtDesigner")
elif PYSIDE6:
    from PySide6.QtDesigner import *
