# -----------------------------------------------------------------------------
# Copyright © 2009- The Spyder Development Team
#
# Licensed under the terms of the MIT License
# (see LICENSE.txt for details)
# -----------------------------------------------------------------------------

"""Provides QtSvgWidgets classes and functions."""

from . import PYQT5, PYQT6, PYSIDE2, PYSIDE6, PythonQtError

if PYQT5:
    raise PythonQtError('QtSvgWidgets not implemented in PyQt5')
elif PYQT6:
    from PyQt6.QtSvgWidgets import *
elif PYSIDE2:
    raise PythonQtError('QtSvgWidgets not implemented in PySide2')
elif PYSIDE6:
    from PySide6.QtSvgWidgets import *
else:
    raise PythonQtError('No Qt bindings could be found')
