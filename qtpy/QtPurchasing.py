# -----------------------------------------------------------------------------
# Copyright © 2009- The Spyder Development Team
#
# Licensed under the terms of the MIT License
# (see LICENSE.txt for details)
# -----------------------------------------------------------------------------

"""Provides QtPurchasing classes and functions."""

from . import PYQT5, PYQT6, PYSIDE2, PYSIDE6, PythonQtError, QtBindingMissingModuleError

if PYQT5:
    from PyQt5.QtQml import *
elif PYQT6:
    raise QtBindingMissingModuleError(name='QtPurchasing')
elif PYSIDE2:
    raise QtBindingMissingModuleError(name='QtPurchasing')
elif PYSIDE6:
    raise QtBindingMissingModuleError(name='QtPurchasing')
else:
    raise PythonQtError('No Qt bindings could be found')
