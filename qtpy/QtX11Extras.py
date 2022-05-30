# -----------------------------------------------------------------------------
# Copyright © 2009- The Spyder Development Team
#
# Licensed under the terms of the MIT License
# (see LICENSE.txt for details)
# -----------------------------------------------------------------------------

"""Provides Linux-specific utilities"""

import sys
from . import PYQT5, PYQT6, PYSIDE2, PYSIDE6, PythonQtError, QtBindingsNotFoundError

if sys.platform == 'linux':
    if PYQT5:
        from PyQt5.QtX11Extras import *
    elif PYQT6:
        raise PythonQtError('QtX11Extras does not exist in Qt6')
    elif PYSIDE2:
        from PySide2.QtX11Extras import *
    elif PYSIDE6:
        raise PythonQtError('QtX11Extras does not exist in Qt6')
    else:
        raise QtBindingsNotFoundError()
else:
    raise PythonQtError('QtX11Extras does not exist on this operating system')
