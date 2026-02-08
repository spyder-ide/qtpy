# -----------------------------------------------------------------------------
# Copyright © 2014-2015 Colin Duquesnoy
# Copyright © 2009- The Spyder Development Team
#
# Licensed under the terms of the MIT License
# (see LICENSE for details)
# -----------------------------------------------------------------------------

"""Provides QtGui classes and functions."""

from functools import partialmethod

from . import PYQT5, PYQT6, PYSIDE2, PYSIDE6, _parse_version
from . import QT_VERSION as _qt_version
from ._utils import (
    getattr_missing_optional_dep,
    possibly_static_exec,
    set_shortcut,
    set_shortcuts,
)

_missing_optional_names = {}

_QTOPENGL_NAMES = {
    "QOpenGLBuffer",
    "QOpenGLContext",
    "QOpenGLContextGroup",
    "QOpenGLDebugLogger",
    "QOpenGLDebugMessage",
    "QOpenGLFramebufferObject",
    "QOpenGLFramebufferObjectFormat",
    "QOpenGLPixelTransferOptions",
    "QOpenGLShader",
    "QOpenGLShaderProgram",
    "QOpenGLTexture",
    "QOpenGLTextureBlitter",
    "QOpenGLVersionProfile",
    "QOpenGLVertexArrayObject",
    "QOpenGLWindow",
}


def __getattr__(name):
    """Custom getattr to chain and wrap errors due to missing optional deps."""
    raise getattr_missing_optional_dep(
        name,
        module_name=__name__,
        optional_names=_missing_optional_names,
    )


if PYQT5:
    from PyQt5.QtGui import *

    # Backport items moved to QtGui in Qt6
    from PyQt5.QtWidgets import (
        QAction,
        QActionGroup,
        QFileSystemModel,
        QShortcut,
        QUndoCommand,
    )

elif PYQT6:
    from PyQt6 import QtGui
    from PyQt6.QtGui import *

    # Attempt to import QOpenGL* classes, but if that fails,
    # don't raise an exception until the name is explicitly accessed.
    # See https://github.com/spyder-ide/qtpy/pull/387/
    try:
        from PyQt6.QtOpenGL import *
    except ImportError as error:
        for name in _QTOPENGL_NAMES:
            _missing_optional_names[name] = {
                "name": "PyQt6.QtOpenGL",
                "missing_package": "pyopengl",
                "import_error": error,
            }

    QFontMetrics.width = lambda self, *args, **kwargs: self.horizontalAdvance(
        *args,
        **kwargs,
    )
    QFontMetricsF.width = lambda self, *args, **kwargs: self.horizontalAdvance(
        *args,
        **kwargs,
    )

    # Map missing/renamed methods
    QDrag.exec_ = lambda self, *args, **kwargs: self.exec(*args, **kwargs)
    QGuiApplication.exec_ = lambda *args, **kwargs: possibly_static_exec(
        QGuiApplication,
        *args,
        **kwargs,
    )
    QTextDocument.print_ = lambda self, *args, **kwargs: self.print(
        *args,
        **kwargs,
    )

    # Allow unscoped access for enums inside the QtGui module
    from .enums_compat import promote_enums

    promote_enums(QtGui)
    del QtGui
elif PYSIDE2:
    from PySide2.QtGui import *

    # Backport items moved to QtGui in Qt6
    from PySide2.QtWidgets import (
        QAction,
        QActionGroup,
        QFileSystemModel,
        QShortcut,
        QUndoCommand,
    )

    if hasattr(QFontMetrics, "horizontalAdvance"):
        # Needed to prevent raising a DeprecationWarning when using QFontMetrics.width
        QFontMetrics.width = (
            lambda self, *args, **kwargs: self.horizontalAdvance(
                *args,
                **kwargs,
            )
        )
elif PYSIDE6:
    from PySide6.QtGui import *

    # Attempt to import QOpenGL* classes, but if that fails,
    # don't raise an exception until the name is explicitly accessed.
    # See https://github.com/spyder-ide/qtpy/pull/387/
    try:
        from PySide6.QtOpenGL import *
    except ImportError as error:
        for name in _QTOPENGL_NAMES:
            _missing_optional_names[name] = {
                "name": "PySide6.QtOpenGL",
                "missing_package": "pyopengl",
                "import_error": error,
            }

    # Backport `QFileSystemModel` moved to QtGui in Qt6
    from PySide6.QtWidgets import QFileSystemModel

    QFontMetrics.width = lambda self, *args, **kwargs: self.horizontalAdvance(
        *args,
        **kwargs,
    )
    QFontMetricsF.width = lambda self, *args, **kwargs: self.horizontalAdvance(
        *args,
        **kwargs,
    )

    # Map DeprecationWarning methods
    QDrag.exec_ = lambda self, *args, **kwargs: self.exec(*args, **kwargs)
    QGuiApplication.exec_ = lambda *args, **kwargs: possibly_static_exec(
        QGuiApplication,
        *args,
        **kwargs,
    )

if PYSIDE2 or PYSIDE6:
    # PySide{2,6} do not accept the `mode` keyword argument in
    # QTextCursor.movePosition() even though it is a valid optional argument
    # as per C++ API. Fix this by monkeypatching.
    #
    # Notes:
    #
    # * The `mode` argument is called `arg__2` in PySide{2,6} as per
    #   QTextCursor.movePosition.__doc__ and __signature__. Using `arg__2` as
    #   keyword argument works as intended, so does using a positional
    #   argument. Tested with PySide2 5.15.0, 5.15.2.1 and 5.15.3 and PySide6
    #   6.3.0; older version, down to PySide 1, are probably affected as well [1].
    #
    # * PySide2 5.15.0 and 5.15.2.1 silently ignore invalid keyword arguments,
    #   i.e. passing the `mode` keyword argument has no effect and doesn`t
    #   raise an exception. Older versions, down to PySide 1, are probably
    #   affected as well [1]. At least PySide2 5.15.3 and PySide6 6.3.0 raise an
    #   exception when `mode` or any other invalid keyword argument is passed.
    #
    # [1] https://bugreports.qt.io/browse/PYSIDE-185
    movePosition = QTextCursor.movePosition

    def movePositionPatched(
        self,
        operation: QTextCursor.MoveOperation,
        mode: QTextCursor.MoveMode = QTextCursor.MoveAnchor,
        n: int = 1,
    ) -> bool:
        return movePosition(self, operation, mode, n)

    QTextCursor.movePosition = movePositionPatched

if PYQT5 or PYSIDE2:
    # Part of the fix for https://github.com/spyder-ide/qtpy/issues/394
    from qtpy.QtCore import QPointF as __QPointF

    QNativeGestureEvent.x = lambda self: self.localPos().toPoint().x()
    QNativeGestureEvent.y = lambda self: self.localPos().toPoint().y()
    QNativeGestureEvent.position = lambda self: self.localPos()
    QNativeGestureEvent.globalX = lambda self: self.globalPos().x()
    QNativeGestureEvent.globalY = lambda self: self.globalPos().y()
    QNativeGestureEvent.globalPosition = lambda self: __QPointF(
        float(self.globalPos().x()),
        float(self.globalPos().y()),
    )
    QEnterEvent.position = lambda self: self.localPos()
    QEnterEvent.globalPosition = lambda self: __QPointF(
        float(self.globalX()),
        float(self.globalY()),
    )
    QTabletEvent.position = lambda self: self.posF()
    QTabletEvent.globalPosition = lambda self: self.globalPosF()
    QHoverEvent.x = lambda self: self.pos().x()
    QHoverEvent.y = lambda self: self.pos().y()
    QHoverEvent.position = lambda self: self.posF()
    # No `QHoverEvent.globalPosition`, `QHoverEvent.globalX`,
    # nor `QHoverEvent.globalY` in the Qt5 docs.
    QMouseEvent.position = lambda self: self.localPos()
    QMouseEvent.globalPosition = lambda self: __QPointF(
        float(self.globalX()),
        float(self.globalY()),
    )

    # Follow similar approach for `QDropEvent` and child classes
    QDropEvent.position = lambda self: self.posF()

if PYQT6 or PYSIDE6:
    # Part of the fix for https://github.com/spyder-ide/qtpy/issues/394
    for _class in (
        QNativeGestureEvent,
        QEnterEvent,
        QTabletEvent,
        QHoverEvent,
        QMouseEvent,
    ):
        for _obsolete_function in (
            "pos",
            "x",
            "y",
            "globalPos",
            "globalX",
            "globalY",
        ):
            if hasattr(_class, _obsolete_function):
                delattr(_class, _obsolete_function)
    QSinglePointEvent.pos = lambda self: self.position().toPoint()
    QSinglePointEvent.posF = lambda self: self.position()
    QSinglePointEvent.localPos = lambda self: self.position()
    QSinglePointEvent.x = lambda self: self.position().toPoint().x()
    QSinglePointEvent.y = lambda self: self.position().toPoint().y()
    QSinglePointEvent.globalPos = lambda self: self.globalPosition().toPoint()
    QSinglePointEvent.globalX = (
        lambda self: self.globalPosition().toPoint().x()
    )
    QSinglePointEvent.globalY = (
        lambda self: self.globalPosition().toPoint().y()
    )

    # Follow similar approach for `QDropEvent` and child classes
    QDropEvent.pos = lambda self: self.position().toPoint()
    QDropEvent.posF = lambda self: self.position()


if PYQT5 or PYSIDE2 or _parse_version(_qt_version) < _parse_version("6.4"):
    # Make `QAction.setShortcut` and `QAction.setShortcuts` compatible with Qt>=6.4
    _action_set_shortcut = partialmethod(
        set_shortcut,
        old_set_shortcut=QAction.setShortcut,
    )
    _action_set_shortcuts = partialmethod(
        set_shortcuts,
        old_set_shortcuts=QAction.setShortcuts,
    )
    QAction.setShortcut = _action_set_shortcut
    QAction.setShortcuts = _action_set_shortcuts


if PYQT5 or PYSIDE2 or _parse_version(_qt_version) < _parse_version("6.7"):
    # Make `QIcon.ThemeIcon` enum for Qt < 6.7

    # Make an `StrEnum` for Python < 3.11
    try:
        from enum import StrEnum as _StrEnum
    except ImportError:
        from enum import Enum as _Enum

        class _StrEnum(str, _Enum):
            pass

    class _ThemeIcon(_StrEnum):
        AddressBookNew = "address-book-new"
        ApplicationExit = "application-exit"
        AppointmentNew = "appointment-new"
        CallStart = "call-start"
        CallStop = "call-stop"
        ContactNew = "contact-new"
        DocumentNew = "document-new"
        DocumentOpen = "document-open"
        DocumentOpenRecent = "document-open-recent"
        DocumentPageSetup = "document-page-setup"
        DocumentPrint = "document-print"
        DocumentPrintPreview = "document-print-preview"
        DocumentProperties = "document-properties"
        DocumentRevert = "document-revert"
        DocumentSave = "document-save"
        DocumentSaveAs = "document-save-as"
        DocumentSend = "document-send"
        EditClear = "edit-clear"
        EditCopy = "edit-copy"
        EditCut = "edit-cut"
        EditDelete = "edit-delete"
        EditFind = "edit-find"
        EditPaste = "edit-paste"
        EditRedo = "edit-redo"
        EditSelectAll = "edit-select-all"
        EditUndo = "edit-undo"
        FolderNew = "folder-new"
        FormatIndentLess = "format-indent-less"
        FormatIndentMore = "format-indent-more"
        FormatJustifyCenter = "format-justify-center"
        FormatJustifyFill = "format-justify-fill"
        FormatJustifyLeft = "format-justify-left"
        FormatJustifyRight = "format-justify-right"
        FormatTextDirectionLtr = "format-text-direction-ltr"
        FormatTextDirectionRtl = "format-text-direction-rtl"
        FormatTextBold = "format-text-bold"
        FormatTextItalic = "format-text-italic"
        FormatTextUnderline = "format-text-underline"
        FormatTextStrikethrough = "format-text-strikethrough"
        GoDown = "go-down"
        GoHome = "go-home"
        GoNext = "go-next"
        GoPrevious = "go-previous"
        GoUp = "go-up"
        HelpAbout = "help-about"
        HelpFaq = "help-faq"
        InsertImage = "insert-image"
        InsertLink = "insert-link"
        InsertText = "insert-text"
        ListAdd = "list-add"
        ListRemove = "list-remove"
        MailForward = "mail-forward"
        MailMarkImportant = "mail-mark-important"
        MailMarkRead = "mail-mark-read"
        MailMarkUnread = "mail-mark-unread"
        MailMessageNew = "mail-message-new"
        MailReplyAll = "mail-reply-all"
        MailReplySender = "mail-reply-sender"
        MailSend = "mail-send"
        MediaEject = "media-eject"
        MediaPlaybackPause = "media-playback-pause"
        MediaPlaybackStart = "media-playback-start"
        MediaPlaybackStop = "media-playback-stop"
        MediaRecord = "media-record"
        MediaSeekBackward = "media-seek-backward"
        MediaSeekForward = "media-seek-forward"
        MediaSkipBackward = "media-skip-backward"
        MediaSkipForward = "media-skip-forward"
        ObjectRotateLeft = "object-rotate-left"
        ObjectRotateRight = "object-rotate-right"
        ProcessStop = "process-stop"
        SystemLockScreen = "system-lock-screen"
        SystemLogOut = "system-log-out"
        SystemSearch = "system-search"
        SystemReboot = "system-reboot"
        SystemShutdown = "system-shutdown"
        ToolsCheckSpelling = "tools-check-spelling"
        ViewFullscreen = "view-fullscreen"
        ViewRefresh = "view-refresh"
        ViewRestore = "view-restore"
        WindowClose = "window-close"
        WindowNew = "window-new"
        ZoomFitBest = "zoom-fit-best"
        ZoomIn = "zoom-in"
        ZoomOut = "zoom-out"
        AudioCard = "audio-card"
        AudioInputMicrophone = "audio-input-microphone"
        Battery = "battery"
        CameraPhoto = "camera-photo"
        CameraVideo = "camera-video"
        CameraWeb = "camera-web"
        Computer = "computer"
        DriveHarddisk = "drive-harddisk"
        DriveOptical = "drive-optical"
        InputGaming = "input-gaming"
        InputKeyboard = "input-keyboard"
        InputMouse = "input-mouse"
        InputTablet = "input-tablet"
        MediaFlash = "media-flash"
        MediaOptical = "media-optical"
        MediaTape = "media-tape"
        MultimediaPlayer = "multimedia-player"
        NetworkWired = "network-wired"
        NetworkWireless = "network-wireless"
        Phone = "phone"
        Printer = "printer"
        Scanner = "scanner"
        VideoDisplay = "video-display"
        AppointmentMissed = "appointment-missed"
        AppointmentSoon = "appointment-soon"
        AudioVolumeHigh = "audio-volume-high"
        AudioVolumeLow = "audio-volume-low"
        AudioVolumeMedium = "audio-volume-medium"
        AudioVolumeMuted = "audio-volume-muted"
        BatteryCaution = "battery-caution"
        BatteryLow = "battery-low"
        DialogError = "dialog-error"
        DialogInformation = "dialog-information"
        DialogPassword = "dialog-password"
        DialogQuestion = "dialog-question"
        DialogWarning = "dialog-warning"
        FolderDragAccept = "folder-drag-accept"
        FolderOpen = "folder-open"
        FolderVisiting = "folder-visiting"
        ImageLoading = "image-loading"
        ImageMissing = "image-missing"
        MailAttachment = "mail-attachment"
        MailUnread = "mail-unread"
        MailRead = "mail-read"
        MailReplied = "mail-replied"
        MediaPlaylistRepeat = "media-playlist-repeat"
        MediaPlaylistShuffle = "media-playlist-shuffle"
        NetworkOffline = "network-offline"
        PrinterPrinting = "printer-printing"
        SecurityHigh = "security-high"
        SecurityLow = "security-low"
        SoftwareUpdateAvailable = "software-update-available"
        SoftwareUpdateUrgent = "software-update-urgent"
        SyncError = "sync-error"
        SyncSynchronizing = "sync-synchronizing"
        UserAvailable = "user-available"
        UserOffline = "user-offline"
        WeatherClear = "weather-clear"
        WeatherClearNight = "weather-clear-night"
        WeatherFewClouds = "weather-few-clouds"
        WeatherFewCloudsNight = "weather-few-clouds-night"
        WeatherFog = "weather-fog"
        WeatherShowers = "weather-showers"
        WeatherSnow = "weather-snow"
        WeatherStorm = "weather-storm"

    QIcon.ThemeIcon = _ThemeIcon
