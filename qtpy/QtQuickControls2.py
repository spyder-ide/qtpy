# -----------------------------------------------------------------------------
# Copyright © 2009- The Spyder Development Team
#
# Licensed under the terms of the MIT License
# (see LICENSE.txt for details)
# -----------------------------------------------------------------------------

"""Provides QtQuickControls2 classes and functions."""

from . import PYQT5, PYQT6, PYSIDE2, PYSIDE6, PythonQtError

if PYQT5:
    raise PythonQtError('QtQuickControls2 not implemented in PyQt5')
elif PYQT6:
    raise PythonQtError('QtQuickControls2 not implemented in PyQt6')
elif PYSIDE2:
    from PySide2.QtQuickControls2 import *
elif PYSIDE6:
    from PySide6.QtQuickControls2 import *
else:
    raise PythonQtError('No Qt bindings could be found')
