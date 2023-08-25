# -----------------------------------------------------------------------------
# Copyright © 2009- The Spyder Development Team
#
# Licensed under the terms of the MIT License
# (see LICENSE.txt for details)
# -----------------------------------------------------------------------------

"""Provides QtSerialBus classes and functions."""

from . import (
    parse,
    PYQT5,
    PYQT6,
    PYSIDE2,
    PYSIDE6,
    PYSIDE_VERSION,
    QtBindingMissingModuleError,
)

if PYQT5:
    from PyQt5.QtSerialBus import *
elif PYQT6:
    from PyQt6.QtSerialBus import *
elif PYSIDE2:
    from PySide2.QtSerialBus import *
elif PYSIDE6:
    if parse(PYSIDE_VERSION) >= parse('6.5'):
        from PySide6.QtSerialBus import *
    else:
        raise QtBindingMissingModuleError(name='QtSerialBus')
