# -*- coding: utf-8 -*-
#
# Copyright © 2009- The Spyder Development Team
#
# Licensed under the terms of the MIT License
# (see LICENSE.txt for details)

"""QtHelp Wrapper."""

from . import PYQT5
from . import PYQT4
from . import PYSIDE
from . import PYSIDE2

if PYQT5:
    from PyQt5.QtHelp import *
elif PYSIDE2:
    # Current wheels don't have this module
    # from PySide2.QtHelp
    pass
elif PYQT4:
    from PyQt4.QtHelp import *
elif PYSIDE:
    from PySide.QtHelp import *
