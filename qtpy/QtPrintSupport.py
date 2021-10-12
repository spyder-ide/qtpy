# -*- coding: utf-8 -*-
#
# Copyright © 2009- The Spyder Development Team
#
# Licensed under the terms of the MIT License
# (see LICENSE.txt for details)

"""
Provides QtPrintSupport classes and functions.
"""

from . import PYQT5, PYSIDE6, PYSIDE2, PythonQtError


if PYQT5:
    from PyQt5.QtPrintSupport import *
elif PYSIDE6:
    from PySide6.QtPrintSupport import *
elif PYSIDE2:
    from PySide2.QtPrintSupport import *
else:
    raise PythonQtError('No Qt bindings could be found')
