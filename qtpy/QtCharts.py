# -----------------------------------------------------------------------------
# Copyright © 2019- The Spyder Development Team
#
# Licensed under the terms of the MIT License
# (see LICENSE.txt for details)
# -----------------------------------------------------------------------------
"""Provides QtChart classes and functions."""

# Local imports
from . import PYQT5, PYQT6, PYSIDE2, PYSIDE6, PythonQtError

if PYQT5:
    try:
        from PyQt5 import QtChart as QtCharts
    except ImportError:
        raise PythonQtError('The QtChart module was not found. '
                            'It needs to be installed separately for PyQt5.')
elif PYQT6:
    from PyQt6 import QtCharts
elif PYSIDE6:
    from PySide6 import QtCharts
elif PYSIDE2:
    from PySide2.QtCharts import *
else:
    raise PythonQtError('No Qt bindings could be found')
