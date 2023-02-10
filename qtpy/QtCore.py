# -----------------------------------------------------------------------------
# Copyright © 2014-2015 Colin Duquesnoy
# Copyright © 2009- The Spyder Development Team
#
# Licensed under the terms of the MIT License
# (see LICENSE.txt for details)
# -----------------------------------------------------------------------------

"""Provides QtCore classes and functions."""
import enum
from typing import TYPE_CHECKING

from . import PYQT6, PYQT5, PYSIDE2, PYSIDE6

if PYQT5:
    from PyQt5.QtCore import *
    from PyQt5.QtCore import pyqtSignal as Signal
    from PyQt5.QtCore import pyqtBoundSignal as SignalInstance
    from PyQt5.QtCore import pyqtSlot as Slot
    from PyQt5.QtCore import pyqtProperty as Property
    from PyQt5.QtCore import QT_VERSION_STR as __version__

    # For issue #153 and updated for issue #305
    QDate.toPython = lambda self, *args, **kwargs: self.toPyDate(*args, **kwargs)
    QDateTime.toPython = lambda self, *args, **kwargs: self.toPyDateTime(*args, **kwargs)
    QTime.toPython = lambda self, *args, **kwargs: self.toPyTime(*args, **kwargs)

    # Fix enums in PyQt5 5.9.*
    if __version__.startswith('5.9.'):
        from .enums_compat import demote_enums
        from PyQt5 import QtCore
        demote_enums(QtCore)
        del QtCore, demote_enums
    if 'qEnvironmentVariable' not in locals():  # appears in Qt5.10
        def qEnvironmentVariable(varName, defaultValue=''):
            import os
            return os.environ.get(varName, defaultValue)

    QLibraryInfo.path = QLibraryInfo.location
    QLibraryInfo.LibraryPath = QLibraryInfo.LibraryLocation

    # Map missing methods
    if not hasattr(QModelIndex, 'siblingAtColumn'):  # appears in Qt5.11
        QModelIndex.siblingAtColumn = lambda self, column: self.sibling(self.row(), column)
    if not hasattr(QModelIndex, 'siblingAtRow'):  # appears in Qt5.11
        QModelIndex.siblingAtRow = lambda self, row: self.sibling(row, self.column())
    QLine.toLineF = lambda self: QLineF(float(self.x1()), float(self.x2()), float(self.y1()), float(self.y2()))
    QMargins.toMarginsF = lambda self: QMarginsF(float(self.left()), float(self.top()),
                                                 float(self.right()), float(self.bottom()))
    QPoint.toPointF = lambda self: QPointF(float(self.x()), float(self.y()))
    QRect.toRectF = lambda self: QRectF(float(self.left()), float(self.top()),
                                        float(self.width()), float(self.height()))
    QSize.toSizeF = lambda self: QSizeF(float(self.width()), float(self.height()))
    if not hasattr(QSize, 'grownBy'):  # appears in Qt5.14
        QSize.grownBy = lambda self, margins: QSize(self.width() + margins.left() + margins.right(),
                                                    self.height() + margins.top() + margins.bottom())
    if not hasattr(QSize, 'shrunkBy'):  # appears in Qt5.14
        QSize.shrunkBy = lambda self, margins: QSize(self.width() - margins.left() - margins.right(),
                                                     self.height() - margins.top() - margins.bottom())
    if not hasattr(QSizeF, 'grownBy'):  # appears in Qt5.14
        QSizeF.grownBy = lambda self, margins: QSizeF(self.width() + margins.left() + margins.right(),
                                                      self.height() + margins.top() + margins.bottom())
    if not hasattr(QSizeF, 'shrunkBy'):  # appears in Qt5.14
        QSizeF.shrunkBy = lambda self, margins: QSizeF(self.width() - margins.left() - margins.right(),
                                                       self.height() - margins.top() - margins.bottom())
    if not hasattr(QDate, 'startOfDay'):  # appears in Qt5.14
        QDate.startOfDay = lambda self, *args: QDateTime(self, QTime(0, 0), *args)
    if not hasattr(QDate, 'endOfDay'):  # appears in Qt5.14
        QDate.endOfDay = lambda self, *args: QDateTime(self, QTime(23, 59, 59, 999), *args)
    if (not hasattr(QDateTime, 'YearRange')  # appears in Qt5.14
            or not isinstance(QDateTime.YearRange, enum.EnumMeta)):

        class _YearRange(enum.IntEnum):
            First = -292275056
            Last = +292278994

        QDateTime.YearRange = _YearRange
    if not hasattr(QByteArray, 'chopped'):  # appears in Qt5.10
        QByteArray.chopped = lambda self, length: QByteArray(self.data()[:-length])
    if not hasattr(QByteArray, 'isUpper'):  # appears in Qt5.12
        QByteArray.isUpper = lambda self: self.data().isupper()
    if not hasattr(QByteArray, 'isLower'):  # appears in Qt5.12
        QByteArray.isLower = lambda self: self.data().islower()

    # Those are imported from `import *`
    del pyqtSignal, pyqtBoundSignal, pyqtSlot, pyqtProperty, QT_VERSION_STR

elif PYQT6:
    from PyQt6 import QtCore
    from PyQt6.QtCore import *
    from PyQt6.QtCore import pyqtSignal as Signal
    from PyQt6.QtCore import pyqtBoundSignal as SignalInstance
    from PyQt6.QtCore import pyqtSlot as Slot
    from PyQt6.QtCore import pyqtProperty as Property
    from PyQt6.QtCore import QT_VERSION_STR as __version__

    # For issue #153 and updated for issue #305
    QDate.toPython = lambda self, *args, **kwargs: self.toPyDate(*args, **kwargs)
    QDateTime.toPython = lambda self, *args, **kwargs: self.toPyDateTime(*args, **kwargs)
    QTime.toPython = lambda self, *args, **kwargs: self.toPyTime(*args, **kwargs)

    # For issue #311
    # Seems like there is an error with sip. Without first
    # trying to import `PyQt6.QtGui.Qt`, some functions like
    # `PyQt6.QtCore.Qt.mightBeRichText` are missing.
    if not TYPE_CHECKING:
        try:
            from PyQt6.QtGui import Qt
        except ImportError:
            pass

    # Map missing methods
    QCoreApplication.exec_ = QCoreApplication.exec
    QEventLoop.exec_ = lambda self, *args, **kwargs: self.exec(*args, **kwargs)
    QThread.exec_ = lambda self, *args, **kwargs: self.exec(*args, **kwargs)

    if not hasattr(QLine, 'toLineF'):  # appears in Qt6.4
        QLine.toLineF = lambda self: QLineF(float(self.x1()), float(self.x2()), float(self.y1()), float(self.y2()))
    if not hasattr(QMargins, 'toMarginsF'):  # appears in Qt6.4
        QMargins.toMarginsF = lambda self: QMarginsF(float(self.left()), float(self.top()),
                                                     float(self.right()), float(self.bottom()))
    if not hasattr(QPoint, 'toPointF'):  # appears in Qt6.4
        QPoint.toPointF = lambda self: QPointF(float(self.x()), float(self.y()))
    if not hasattr(QRect, 'toRectF'):  # appears in Qt6.4
        QRect.toRectF = lambda self: QRectF(float(self.left()), float(self.top()),
                                            float(self.width()), float(self.height()))
    if not hasattr(QSize, 'toSizeF'):  # appears in Qt6.4
        QSize.toSizeF = lambda self: QSizeF(float(self.width()), float(self.height()))

    QLibraryInfo.location = QLibraryInfo.path
    QLibraryInfo.LibraryLocation = QLibraryInfo.LibraryPath

    # Those are imported from `import *`
    del pyqtSignal, pyqtBoundSignal, pyqtSlot, pyqtProperty, QT_VERSION_STR

    # Allow unscoped access for enums inside the QtCore module
    from .enums_compat import promote_enums
    promote_enums(QtCore)
    del QtCore

    # Alias deprecated ItemDataRole enum values removed in Qt6
    Qt.BackgroundColorRole = Qt.ItemDataRole.BackgroundColorRole = Qt.ItemDataRole.BackgroundRole
    Qt.TextColorRole = Qt.ItemDataRole.TextColorRole = Qt.ItemDataRole.ForegroundRole
    # Alias for MiddleButton removed in Qt6
    Qt.MidButton = Qt.MouseButton.MidButton = Qt.MouseButton.MiddleButton

elif PYSIDE2:
    from PySide2.QtCore import *

    try:  # may be limited to PySide-5.11a1 only
        from PySide2.QtGui import QStringListModel
    except Exception:
        pass

    import PySide2.QtCore
    __version__ = PySide2.QtCore.__version__

    # Map missing methods
    QCoreApplication.exec = lambda self, *args, **kwargs: self.exec_(*args, **kwargs)
    QEventLoop.exec = lambda self, *args, **kwargs: self.exec_(*args, **kwargs)
    QThread.exec = lambda self, *args, **kwargs: self.exec_(*args, **kwargs)
    QTextStreamManipulator.exec = lambda self, *args, **kwargs: self.exec_(*args, **kwargs)
    QLine.toLineF = lambda self: QLineF(float(self.x1()), float(self.x2()), float(self.y1()), float(self.y2()))
    QMargins.toMarginsF = lambda self: QMarginsF(float(self.left()), float(self.top()),
                                                 float(self.right()), float(self.bottom()))
    QPoint.toPointF = lambda self: QPointF(float(self.x()), float(self.y()))
    QRect.toRectF = lambda self: QRectF(float(self.left()), float(self.top()),
                                        float(self.width()), float(self.height()))
    QSize.toSizeF = lambda self: QSizeF(float(self.width()), float(self.height()))
    if not hasattr(QSize, 'grownBy'):  # appears in Qt5.14
        QSize.grownBy = lambda self, margins: QSize(self.width() + margins.left() + margins.right(),
                                                    self.height() + margins.top() + margins.bottom())
    if not hasattr(QSize, 'shrunkBy'):  # appears in Qt5.14
        QSize.shrunkBy = lambda self, margins: QSize(self.width() - margins.left() - margins.right(),
                                                     self.height() - margins.top() - margins.bottom())
    if not hasattr(QSizeF, 'grownBy'):  # appears in Qt5.14
        QSizeF.grownBy = lambda self, margins: QSizeF(self.width() + margins.left() + margins.right(),
                                                      self.height() + margins.top() + margins.bottom())
    if not hasattr(QSizeF, 'shrunkBy'):  # appears in Qt5.14
        QSizeF.shrunkBy = lambda self, margins: QSizeF(self.width() - margins.left() - margins.right(),
                                                       self.height() - margins.top() - margins.bottom())
    if not hasattr(QDate, 'startOfDay'):  # appears in Qt5.14
        QDate.startOfDay = lambda self, *args: QDateTime(self, QTime(0, 0), *args)
    if not hasattr(QDate, 'endOfDay'):  # appears in Qt5.14
        QDate.endOfDay = lambda self, *args: QDateTime(self, QTime(23, 59, 59, 999), *args)
    if (not hasattr(QDateTime, 'YearRange')  # appears in Qt5.14
            or not isinstance(QDateTime.YearRange, enum.EnumMeta)):
        class _YearRange(enum.IntEnum):
            First = -292275056
            Last = +292278994

        QDateTime.YearRange = _YearRange

    QLibraryInfo.path = QLibraryInfo.location
    QLibraryInfo.LibraryPath = QLibraryInfo.LibraryLocation

    # For issue #153 and updated for issue #305
    QDate.toPyDate = lambda self, *args, **kwargs: self.toPython(*args, **kwargs)
    QDateTime.toPyDateTime = lambda self, *args, **kwargs: self.toPython(*args, **kwargs)
    QTime.toPyTime = lambda self, *args, **kwargs: self.toPython(*args, **kwargs)

    # Missing QtGui utility functions on Qt
    if getattr(Qt, 'mightBeRichText', None) is None:
        try:
            from PySide2.QtGui import Qt as guiQt
            Qt.mightBeRichText = guiQt.mightBeRichText
            del guiQt
        except ImportError:
            # Fails with PySide2 5.12.0
            pass

elif PYSIDE6:
    from PySide6.QtCore import *
    import PySide6.QtCore
    __version__ = PySide6.QtCore.__version__

    # Missing QtGui utility functions on Qt
    if getattr(Qt, 'mightBeRichText', None) is None:
        from PySide6.QtGui import Qt as guiQt
        Qt.mightBeRichText = guiQt.mightBeRichText
        del guiQt

    # For issue #153 and updated for issue #305
    QDate.toPyDate = lambda self, *args, **kwargs: self.toPython(*args, **kwargs)
    QDateTime.toPyDateTime = lambda self, *args, **kwargs: self.toPython(*args, **kwargs)
    QTime.toPyTime = lambda self, *args, **kwargs: self.toPython(*args, **kwargs)

    # Map missing methods
    if not hasattr(QLine, 'toLineF'):  # appears in Qt6.4
        QLine.toLineF = lambda self: QLineF(float(self.x1()), float(self.x2()), float(self.y1()), float(self.y2()))
    if not hasattr(QMargins, 'toMarginsF'):  # appears in Qt6.4
        QMargins.toMarginsF = lambda self: QMarginsF(float(self.left()), float(self.top()),
                                                     float(self.right()), float(self.bottom()))
    if not hasattr(QPoint, 'toPointF'):  # appears in Qt6.4
        QPoint.toPointF = lambda self: QPointF(float(self.x()), float(self.y()))
    if not hasattr(QRect, 'toRectF'):  # appears in Qt6.4
        QRect.toRectF = lambda self: QRectF(float(self.left()), float(self.top()),
                                            float(self.width()), float(self.height()))
    if not hasattr(QSize, 'toSizeF'):  # appears in Qt6.4
        QSize.toSizeF = lambda self: QSizeF(float(self.width()), float(self.height()))

    # Alias deprecated ItemDataRole enum values removed in Qt6
    Qt.BackgroundColorRole = Qt.ItemDataRole.BackgroundColorRole = Qt.ItemDataRole.BackgroundRole
    Qt.TextColorRole = Qt.ItemDataRole.TextColorRole = Qt.ItemDataRole.ForegroundRole
    # Alias for MiddleButton removed in Qt6
    Qt.MidButton = Qt.MouseButton.MidButton = Qt.MouseButton.MiddleButton

    # Map DeprecationWarning methods
    QCoreApplication.exec_ = lambda self, *args, **kwargs: self.exec(*args, **kwargs)
    QEventLoop.exec_ = lambda self, *args, **kwargs: self.exec(*args, **kwargs)
    QThread.exec_ = lambda self, *args, **kwargs: self.exec(*args, **kwargs)
    QTextStreamManipulator.exec_ = lambda self, *args, **kwargs: self.exec(*args, **kwargs)
    QLibraryInfo.location = QLibraryInfo.path
    QLibraryInfo.LibraryLocation = QLibraryInfo.LibraryPath


if PYSIDE2 or PYSIDE6:
    # PyQt5/PyQt6 only function
    def qEnvironmentVariable(varName, defaultValue=''):
        import os
        return os.environ.get(varName, defaultValue)


# clean up the imports not for export
del enum, TYPE_CHECKING
