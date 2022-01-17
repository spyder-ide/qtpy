#
# Copyright © 2014-2015 Colin Duquesnoy
# Copyright © 2009- The Spyder Development Team
#
# Licensed under the terms of the MIT License
# (see LICENSE.txt for details)

"""
Provides QtCore classes and functions.
"""
from . import PYQT6, PYQT5, PYSIDE2, PYSIDE6, PythonQtError


if PYQT6:
    from PyQt6 import QtCore
    from PyQt6.QtCore import *
    from PyQt6.QtCore import pyqtSignal as Signal
    from PyQt6.QtCore import pyqtBoundSignal as SignalInstance
    from PyQt6.QtCore import pyqtSlot as Slot
    from PyQt6.QtCore import pyqtProperty as Property
    from PyQt6.QtCore import QT_VERSION_STR as __version__

    # For issue #153
    from PyQt6.QtCore import QDateTime
    QDateTime.toPython = QDateTime.toPyDateTime

    # For issue #311
    # Seems like there is an error with sip. Without first
    # trying to import `PyQt6.QtGui.Qt`, some functions like
    # `PyQt6.QtCore.Qt.mightBeRichText` are missing.
    try:
        from PyQt6.QtGui import Qt
    except ImportError:
        pass

    # Map missing methods
    QCoreApplication.exec_ = QCoreApplication.exec
    QEventLoop.exec_ = QEventLoop.exec
    QThread.exec_ = QThread.exec
    
    QLibraryInfo.location = QLibraryInfo.path 

    # Those are imported from `import *`
    del pyqtSignal, pyqtBoundSignal, pyqtSlot, pyqtProperty, QT_VERSION_STR

    # Allow unscoped access for enums inside the QtCore module
    from .enums_compat import promote_enums
    promote_enums(QtCore)
    del QtCore

    # Map missing unscoped access enum values
    Qt.BackButton = Qt.XButton1
    Qt.ForwardButton = Qt.XButton2

    # Alias deprecated ItemDataRole enum values removed in Qt6
    Qt.BackgroundColorRole = Qt.ItemDataRole.BackgroundColorRole = Qt.BackgroundRole
    Qt.TextColorRole = Qt.ItemDataRole.TextColorRole = Qt.ForegroundRole

elif PYQT5:
    from PyQt5.QtCore import *
    from PyQt5.QtCore import pyqtSignal as Signal
    from PyQt5.QtCore import pyqtBoundSignal as SignalInstance
    from PyQt5.QtCore import pyqtSlot as Slot
    from PyQt5.QtCore import pyqtProperty as Property
    from PyQt5.QtCore import QT_VERSION_STR as __version__

    # For issue #153
    from PyQt5.QtCore import QDateTime
    QDateTime.toPython = QDateTime.toPyDateTime

    # Those are imported from `import *`
    del pyqtSignal, pyqtBoundSignal, pyqtSlot, pyqtProperty, QT_VERSION_STR

elif PYSIDE6:
    from PySide6.QtCore import *
    import PySide6.QtCore
    __version__ = PySide6.QtCore.__version__

    # Missing QtGui utility functions on Qt
    if getattr(Qt, 'mightBeRichText', None) is None:
        from PySide6.QtGui import Qt as guiQt
        Qt.mightBeRichText = guiQt.mightBeRichText
        del guiQt

    # Alias deprecated ItemDataRole enum values removed in Qt6
    Qt.BackgroundColorRole = Qt.ItemDataRole.BackgroundColorRole = Qt.BackgroundRole
    Qt.TextColorRole = Qt.ItemDataRole.TextColorRole = Qt.ForegroundRole
    Qt.MidButton = Qt.MouseButton.MiddleButton = Qt.MiddleButton

    # Map DeprecationWarning methods
    QCoreApplication.exec_ = QCoreApplication.exec
    QEventLoop.exec_ = QEventLoop.exec
    QThread.exec_ = QThread.exec
    QTextStreamManipulator.exec_ = QTextStreamManipulator.exec

elif PYSIDE2:
    from PySide2.QtCore import *

    try:  # may be limited to PySide-5.11a1 only
        from PySide2.QtGui import QStringListModel
    except Exception:
        pass

    import PySide2.QtCore
    __version__ = PySide2.QtCore.__version__

    # Missing QtGui utility functions on Qt
    if getattr(Qt, 'mightBeRichText', None) is None:
        try:
            from PySide2.QtGui import Qt as guiQt
            Qt.mightBeRichText = guiQt.mightBeRichText
            del guiQt
        except ImportError:
            # Fails with PySide2 5.12.0
            pass
else:
    raise PythonQtError('No Qt bindings could be found')
