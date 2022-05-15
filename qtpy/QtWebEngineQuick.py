# -----------------------------------------------------------------------------
# Copyright © 2009- The Spyder Development Team
#
# Licensed under the terms of the MIT License
# (see LICENSE.txt for details)
# -----------------------------------------------------------------------------

"""
Provides QtWebEngineQuick classes and functions.
"""

from . import PYQT5, PYQT6, PYSIDE2, PYSIDE6, PythonQtError

if PYQT5:
    raise PythonQtError('QtWebEngineQuick not implemented in PyQt5')
elif PYQT6:
    try:
        from PyQt6.QtWebEngineQuick import *
    except ImportError as error:
        raise PythonQtError(
            'The QtWebEngineQuick module was not found. '
            'It needs to be installed separately for PyQt6.'
            ) from error
elif PYSIDE2:
    raise PythonQtError('QtWebEngineQuick not implemented in PySide2')
elif PYSIDE6:
    from PySide6.QtWebEngineQuick import *
else:
    raise PythonQtError('No Qt bindings could be found')
