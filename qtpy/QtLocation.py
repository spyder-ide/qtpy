# -----------------------------------------------------------------------------
# Copyright © 2009- The Spyder Development Team
#
# Licensed under the terms of the MIT License
# (see LICENSE.txt for details)
# -----------------------------------------------------------------------------

"""Provides QtLocation classes and functions."""

from . import (
    parse,
    PYQT5,
    PYQT6,
    PYSIDE2,
    PYSIDE6,
    PYQT_VERSION,
    PYSIDE_VERSION,
    QtBindingMissingModuleError,
)

if PYQT5:
    from PyQt5.QtLocation import *
elif PYQT6:
    if parse(PYQT_VERSION) >= parse('6.5'):
        from PyQt6.QtLocation import *
    else:
        raise QtBindingMissingModuleError(name='QtLocation')
elif PYSIDE2:
    from PySide2.QtLocation import *
elif PYSIDE6:
    if parse(PYSIDE_VERSION) >= parse('6.5'):
        from PySide6.QtLocation import *
    else:
        raise QtBindingMissingModuleError(name='QtLocation')
