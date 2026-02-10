# -----------------------------------------------------------------------------
# Copyright © 2009- The Spyder Development Team
#
# Licensed under the terms of the MIT License
# (see LICENSE for details)
# -----------------------------------------------------------------------------

"""QtHelp Wrapper."""

from . import PYQT5, PYQT6, PYSIDE2, PYSIDE6

if PYQT5:
    from PyQt5.QtHelp import *
elif PYQT6:
    from PyQt6 import QtHelp
    from PyQt6.QtHelp import *

    # Allow unscoped access for enums
    from .enums_compat import promote_enums

    promote_enums(QtHelp)
    del QtHelp
elif PYSIDE2:
    from PySide2.QtHelp import *
elif PYSIDE6:
    from PySide6.QtHelp import *
