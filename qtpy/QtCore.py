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

from packaging.version import parse

from . import PYQT6, PYQT5, PYSIDE2, PYSIDE6

__version__ = ''

if PYQT5:
    from PyQt5.QtCore import *
    from PyQt5.QtCore import pyqtSignal as Signal
    from PyQt5.QtCore import pyqtBoundSignal as SignalInstance
    from PyQt5.QtCore import pyqtSlot as Slot
    from PyQt5.QtCore import pyqtProperty as Property
    from PyQt5.QtCore import QT_VERSION_STR as __version__

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

    # Map missing methods
    if not hasattr(QModelIndex, 'siblingAtColumn'):  # appears in Qt5.11
        QModelIndex.siblingAtColumn = lambda self, column: self.sibling(self.row(), column)
    if not hasattr(QModelIndex, 'siblingAtRow'):  # appears in Qt5.11
        QModelIndex.siblingAtRow = lambda self, row: self.sibling(row, self.column())

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

    if not hasattr(QRegularExpression, 'anchoredPattern'):  # appears in Qt5.12
        QRegularExpression.anchoredPattern = lambda pattern: r'\A(?:' + pattern + r')\z'

    if not hasattr(QRegularExpression, 'wildcardToRegularExpression'):  # appears in Qt5.12
        def _wildcardToRegularExpression(pattern: str):
            import sys

            win = sys.platform.startswith('win')

            res = r'\A(?:'
            i = 0
            while i < len(pattern):
                c = pattern[i]
                if c == '?':
                    res += r'[^/\\]' if win else '[^/]'
                elif c == '*':
                    res += r'[^/\\]*' if win else '[^/]*'
                elif c == '[':
                    res += c
                    i += 1
                    if i >= len(pattern):
                        break
                    if pattern[i] == '!':
                        res += '^'
                        i += 1
                    while i < len(pattern) and pattern[i] != ']':
                        res += pattern[i]
                        i += 1
                    if i >= len(pattern):
                        break
                    res += pattern[i]
                elif c == '\\':
                    res += r'[/\\]' if win else r'\\'
                else:
                    res += c
                i += 1
            res += r')\z'
            return res


        QRegularExpression.wildcardToRegularExpression = _wildcardToRegularExpression

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

    if (not hasattr(QDateTime, 'YearRange')  # appears in Qt5.14
            or not isinstance(QDateTime.YearRange, enum.EnumMeta)):

        class _YearRange(enum.IntEnum):
            First = -292275056
            Last = +292278994

        QDateTime.YearRange = _YearRange

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


if PYQT5 or PYQT6:
    # For issue #153 and updated for issue #305
    QDate.toPython = lambda self, *args, **kwargs: self.toPyDate(*args, **kwargs)
    QDateTime.toPython = lambda self, *args, **kwargs: self.toPyDateTime(*args, **kwargs)
    QTime.toPython = lambda self, *args, **kwargs: self.toPyTime(*args, **kwargs)


if PYSIDE2 or PYSIDE6:
    # For issue #153 and updated for issue #305
    QDate.toPyDate = lambda self, *args, **kwargs: self.toPython(*args, **kwargs)
    QDateTime.toPyDateTime = lambda self, *args, **kwargs: self.toPython(*args, **kwargs)
    QTime.toPyTime = lambda self, *args, **kwargs: self.toPython(*args, **kwargs)

    # PyQt5/PyQt6 only function
    def qEnvironmentVariable(varName, defaultValue=''):
        import os
        return os.environ.get(varName, defaultValue)


if PYQT5 or PYSIDE2:
    QLibraryInfo.path = QLibraryInfo.location
    QLibraryInfo.LibraryPath = QLibraryInfo.LibraryLocation
if PYQT6 or PYSIDE6:
    QLibraryInfo.location = QLibraryInfo.path
    QLibraryInfo.LibraryLocation = QLibraryInfo.LibraryPath


if (not hasattr(QLocale, 'toLong')  # Qt5 < 5.13
        or isinstance(QLocale('C').toLong('42'), int)):  # all PySide6 up to 6.4.2 for now
    # follow https://bugreports.qt.io/browse/PYSIDE-2226
    QLocale.toLong = lambda self, s: self.toLongLong(s)
if (not hasattr(QLocale, 'toULong')  # Qt5 < 5.13
        or isinstance(QLocale('C').toULong('42'), int)):  # all PySide6 up to 6.4.2 for now
    # follow https://bugreports.qt.io/browse/PYSIDE-2226
    QLocale.toULong = lambda self, s: self.toULongLong(s)


if (PYQT5 or PYSIDE2) and parse(__version__) < parse('5.14'):
    QSize.grownBy = lambda self, margins: QSize(self.width() + margins.left() + margins.right(),
                                                self.height() + margins.top() + margins.bottom())
    QSize.shrunkBy = lambda self, margins: QSize(self.width() - margins.left() - margins.right(),
                                                 self.height() - margins.top() - margins.bottom())
    QSizeF.grownBy = lambda self, margins: QSizeF(self.width() + margins.left() + margins.right(),
                                                  self.height() + margins.top() + margins.bottom())
    QSizeF.shrunkBy = lambda self, margins: QSizeF(self.width() - margins.left() - margins.right(),
                                                   self.height() - margins.top() - margins.bottom())
    QDate.startOfDay = lambda self, *args: QDateTime(self, QTime(0, 0), *args)
    QDate.endOfDay = lambda self, *args: QDateTime(self, QTime(23, 59, 59, 999), *args)


if (PYQT5 or PYSIDE2) and parse(__version__) < parse('5.15'):

    if parse(__version__) < parse('5.10'):
        class _Base64Option(enum.IntFlag):
            Base64Encoding = 0
            Base64UrlEncoding = 1
            KeepTrailingEquals = 0
            OmitTrailingEquals = 2

        QByteArray.Base64Option = _Base64Option

    QByteArray.Base64Option.IgnoreBase64DecodingErrors = 0
    QByteArray.Base64Option.AbortOnBase64DecodingErrors = 4


    class _Base64DecodingStatus(enum.Enum):
        Ok = 0
        IllegalInputLength = 1
        IllegalCharacter = 2
        IllegalPadding = 3

    QByteArray.Base64DecodingStatus = _Base64DecodingStatus


    class FromBase64Result:
        """\
QByteArray.FromBase64Result()
QByteArray.FromBase64Result(QByteArray.FromBase64Result)\
"""

        def __init__(self, decodingStatus, decoded):
            self._decodingStatus = decodingStatus
            self._decoded = decoded

        @property
        def decodingStatus(self):
            return self._decodingStatus

        @property
        def decoded(self):
            return self._decoded

        def __bool__(self):
            return self._decodingStatus == QByteArray.Base64DecodingStatus.Ok

        def __eq__(self, other):
            return self._decodingStatus == other.decodingStatus and self._decoded == other.decoded


    def _fromBase64Encoding(base64, options=QByteArray.Base64Option.Base64Encoding):
        import binascii
        import string
        from base64 import b64decode

        if isinstance(base64, QByteArray):
            base64 = base64.data()

        if not base64:
            return FromBase64Result(QByteArray.Base64DecodingStatus.Ok, QByteArray(b''))

        if options & QByteArray.Base64Option.Base64UrlEncoding:
            _urlsafe_decode_translation = bytes.maketrans(b'-_', b'+/')
            base64 = base64.translate(_urlsafe_decode_translation)

        validate = bool(options & QByteArray.Base64Option.AbortOnBase64DecodingErrors)

        if options & QByteArray.Base64Option.OmitTrailingEquals:
            if (len(base64) % 4) and base64.endswith(b'=' * (len(base64) % 4)):
                base64 = base64[:-(len(base64) % 4)]
        elif validate and len(base64) - len(base64.rstrip(b'=')) > 2:
            return FromBase64Result(QByteArray.Base64DecodingStatus.IllegalPadding, QByteArray(b''))

        if not validate:
            if len(base64) % 4:  # number of data characters cannot be not a multiple of 4
                base64 = base64[:-(len(base64) % 4)]
            while base64:
                try:
                    b64decode(base64, validate=True)
                except binascii.Error as ex:
                    if 'Incorrect padding' in ex.args[0]:
                        base64 += b'='
                    elif 'Leading padding not allowed' in ex.args[0]:
                        base64 = base64.lstrip(b'=')
                    elif ('Discontinuous padding not allowed' in ex.args[0]
                          or 'Excess data after padding' in ex.args[0]):
                        base64 = base64.replace(b'=', b'', 1)
                    elif 'Only base64 data is allowed' in ex.args[0]:
                        if options & QByteArray.Base64Option.Base64UrlEncoding:
                            _legal_base64_characters = (string.ascii_letters + string.digits + '-_=').encode('ascii')
                        else:
                            _legal_base64_characters = (string.ascii_letters + string.digits + '+/=').encode('ascii')
                        base64 = bytes(b for b in base64 if b in _legal_base64_characters)
                    else:
                        break
                else:
                    break
        elif len(base64) % 4:  # number of data characters cannot be not a multiple of 4
            return FromBase64Result(QByteArray.Base64DecodingStatus.IllegalInputLength, QByteArray(b''))

        try:
            return FromBase64Result(QByteArray.Base64DecodingStatus.Ok,
                                    QByteArray(b64decode(base64, validate=validate)))
        except binascii.Error as ex:
            status = QByteArray.Base64DecodingStatus.Ok
            if 'number of data characters' in ex.args[0]:
                status = QByteArray.Base64DecodingStatus.IllegalInputLength
            if 'Only base64 data is allowed' in ex.args[0]:
                status = QByteArray.Base64DecodingStatus.IllegalCharacter
            if 'padding' in ex.args[0]:
                status = QByteArray.Base64DecodingStatus.IllegalPadding
            if 'Non-base64 digit found' in ex.args[0]:
                if len(base64) - len(base64.rstrip(b'=')) > 2:
                    status = QByteArray.Base64DecodingStatus.IllegalPadding
                else:
                    status = QByteArray.Base64DecodingStatus.IllegalCharacter
            return FromBase64Result(status, QByteArray(b''))


    QByteArray.fromBase64Encoding = _fromBase64Encoding


if (PYQT5 or PYSIDE2 or PYQT6 or PYSIDE6) and parse(__version__) < parse('6.4'):
    QLine.toLineF = lambda self: QLineF(float(self.x1()), float(self.x2()), float(self.y1()), float(self.y2()))
    QMargins.toMarginsF = lambda self: QMarginsF(float(self.left()), float(self.top()),
                                                 float(self.right()), float(self.bottom()))
    QPoint.toPointF = lambda self: QPointF(float(self.x()), float(self.y()))
    QRect.toRectF = lambda self: QRectF(float(self.left()), float(self.top()),
                                        float(self.width()), float(self.height()))
    QSize.toSizeF = lambda self: QSizeF(float(self.width()), float(self.height()))


# clean up the imports not for export
del enum, TYPE_CHECKING, parse
