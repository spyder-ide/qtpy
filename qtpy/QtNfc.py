# -----------------------------------------------------------------------------
# Copyright © 2009- The Spyder Development Team
#
# Licensed under the terms of the MIT License
# (see LICENSE.txt for details)
# -----------------------------------------------------------------------------

"""
Provides QtNfc classes and functions.
"""

from . import PYQT5, PYQT6, PYSIDE2, PYSIDE6, PythonQtError

if PYQT5:
    from PyQt5.QtNfc import *
elif PYQT6:
    from PyQt6.QtNfc import *
elif PYSIDE2:
    raise PythonQtError('QtNfc not implemented in PySide2')
elif PYSIDE6:
    from PySide6.QtNfc import *
else:
    raise PythonQtError('No Qt bindings could be found')
