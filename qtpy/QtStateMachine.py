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
    QtBindingMissingModuleError,
)

if PYQT5:
    from PyQt5.QtCore import (
        QAbstractState,
        QAbstractTransition,
        QEventTransition,
        QFinalState,
        QHistoryState,
        QKeyEventTransition,
        QMouseEventTransition,
        QSignalTransition,
        QState,
        QStateMachine,
    )
elif PYSIDE2:
    from PySide2.QtCore import (
        QAbstractState,
        QAbstractTransition,
        QEventTransition,
        QFinalState,
        QHistoryState,
        QKeyEventTransition,
        QMouseEventTransition,
        QSignalTransition,
        QState,
        QStateMachine,
    )
elif PYQT6:
    from PyQt6.QtStateMachine import *
elif PYSIDE6:
    from PySide6.QtStateMachine import *
