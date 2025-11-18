# -----------------------------------------------------------------------------
# Copyright © 2009- The Spyder Development Team
#
# Licensed under the terms of the MIT License
# (see LICENSE.txt for details)
# -----------------------------------------------------------------------------

"""Provides QtStateMachine classes and functions."""

from . import (
    PYQT5,
    PYQT6,
    PYSIDE2,
    PYSIDE6,
)

if PYQT5:
    from PyQt5.QtCore import (
        QAbstractState,
        QAbstractTransition,
        QEventTransition,
        QFinalState,
        QHistoryState,
        QSignalTransition,
        QState,
        QStateMachine,
    )
    from PyQt5.QtWidgets import (
        QKeyEventTransition,
        QMouseEventTransition,
    )
elif PYSIDE2:
    from PySide2.QtCore import (
        QAbstractState,
        QAbstractTransition,
        QEventTransition,
        QFinalState,
        QHistoryState,
        QSignalTransition,
        QState,
        QStateMachine,
    )
    from PySide2.QtWidgets import (
        QKeyEventTransition,
        QMouseEventTransition,
    )
elif PYQT6:
    from PyQt6.QtCore import PYQT_VERSION_STR

    if int(PYQT_VERSION_STR.split(".")[1]) >= 9:
        from PyQt6 import QtStateMachine
        from PyQt6.QtStateMachine import *

        # Allow unscoped access for enums
        from .enums_compat import promote_enums

        promote_enums(QtStateMachine)
        del QtStateMachine
    else:
        from . import QtBindingInNewerVersionError

        raise QtBindingInNewerVersionError(name="QtStateMachine")
elif PYSIDE6:
    from PySide6.QtStateMachine import *
