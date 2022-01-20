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
        from PyQt5.QtChart import *
        from PyQt5 import QtChart as QtCharts
    except ImportError as error:
        raise PythonQtError(
            'The QtChart module was not found. '
            'It needs to be installed separately for PyQt5.'
            ) from error
elif PYQT6:
    try:
        from PyQt6.QtCharts import *
        from PyQt6 import QtCharts
    except ImportError as error:
        raise PythonQtError(
            'The QtCharts module was not found. '
            'It needs to be installed separately for PyQt6.'
            ) from error
elif PYSIDE6:
    from PySide6.QtCharts import *
    from PySide6 import QtCharts
elif PYSIDE2:
    from PySide2.QtCharts import *
    # https://bugreports.qt.io/projects/PYSIDE/issues/PYSIDE-1026
    import PySide2.QtCharts as __temp
    import inspect
    for __name in inspect.getmembers(__temp.QtCharts):
        globals()[__name[0]] = __name[1]
else:
    raise PythonQtError('No Qt bindings could be found')
