# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Copyright © 2009- The Spyder Development Team
#
# Licensed under the terms of the MIT License
# (see LICENSE.txt for details)
# -----------------------------------------------------------------------------
"""Provides QtQuick1 classes and functions."""

# Local imports
from . import PYQT4, PYSIDE, PythonQtError

if PYQT4:
    from PyQt4.QtDeclarative import *
elif PYSIDE:
    from PySide.QtDeclarative import *
else:
    raise PythonQtError('No Qt bindings could be found')
