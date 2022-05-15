# -----------------------------------------------------------------------------
# Copyright © 2009- The Spyder Development Team
#
# Licensed under the terms of the MIT License
# (see LICENSE.txt for details)
# -----------------------------------------------------------------------------

"""
Provides QtXmlPatterns classes and functions.
"""

from . import PYQT5, PYQT6, PYSIDE2, PYSIDE6, PythonQtError

if PYQT5:
    from PyQt5.QtXmlPatterns import *
elif PYQT6:
    raise PythonQtError('QtXmlPatterns does not exist in Qt6')
elif PYSIDE2:
    from PySide2.QtXmlPatterns import *
elif PYSIDE6:
    raise PythonQtError('QtXmlPatterns does not exist in Qt6')
else:
    raise PythonQtError('No Qt bindings could be found')
