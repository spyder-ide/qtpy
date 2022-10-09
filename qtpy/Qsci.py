# -----------------------------------------------------------------------------
# Copyright © 2009- The Spyder Development Team
#
# Licensed under the terms of the MIT License
# (see LICENSE.txt for details)
# -----------------------------------------------------------------------------

"""Provides Qsci classes and functions."""

from . import (
    PYQT5,
    PYQT6,
    PYSIDE2,
    PYSIDE6,
    QtBindingsNotFoundError,
    QtBindingMissingModuleError,
)

if PYQT5:
    from PyQt5.Qsci import *
elif PYQT6:
    from PyQt6.Qsci import *
elif PYSIDE2:
    raise QtBindingMissingModuleError(name='Qsci')
elif PYSIDE6:
    raise QtBindingMissingModuleError(name='Qsci')
else:
    raise QtBindingsNotFoundError()
