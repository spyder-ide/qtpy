# -----------------------------------------------------------------------------
# Copyright © 2014-2015 Colin Duquesnoy
# Copyright © 2009- The Spyder Development Team
#
# Licensed under the terms of the MIT License
# (see LICENSE.txt for details)
# -----------------------------------------------------------------------------

"""Provides QtGui classes and functions."""

from . import PYQT6, PYQT5, PYSIDE2, PYSIDE6

if PYQT5:
    from PyQt5.QtGui import *
    # Backport items moved to QtGui in Qt6
    from PyQt5.QtWidgets import QAction, QActionGroup, QFileSystemModel, QShortcut, QUndoCommand

    # Map missing/renamed methods
    QColor.toTuple = lambda self: (self.red(), self.green(), self.blue(), self.alpha())
    QColor.isValidColorName = lambda name: QColor.isValidColor(name)
    QColor.fromString = lambda name: QColor(name)
    QMouseEvent.position = lambda *args: QMouseEvent.pos(*args).toPointF()
    if not hasattr(QFontMetrics, 'horizontalAdvance'):
        QFontMetrics.horizontalAdvance = lambda self, *args, **kwargs: self.width(*args, **kwargs)
    if not hasattr(QFontMetricsF, 'horizontalAdvance'):
        QFontMetricsF.horizontalAdvance = lambda self, *args, **kwargs: self.width(*args, **kwargs)
    if not hasattr(QImage, 'sizeInBytes'):  # appears in Qt5.10
        QImage.sizeInBytes = lambda self: self.numBytes() if hasattr(self, 'numBytes') else self.byteCount()

    # Fix enums in PyQt5 5.9.*
    from PyQt5.QtCore import QT_VERSION_STR as __version__
    if __version__.startswith('5.9.'):
        from .enums_compat import demote_enums
        from PyQt5 import QtGui
        demote_enums(QtGui)
        del QtGui, demote_enums
    del __version__

elif PYQT6:
    from PyQt6 import QtGui
    from PyQt6.QtGui import *
    from PyQt6.QtOpenGL import *
    QFontMetrics.width = lambda self, *args, **kwargs: self.horizontalAdvance(*args, **kwargs)
    QFontMetricsF.width = lambda self, *args, **kwargs: self.horizontalAdvance(*args, **kwargs)

    # Map missing/renamed methods
    QDrag.exec_ = lambda self, *args, **kwargs: self.exec(*args, **kwargs)
    QGuiApplication.exec_ = lambda self, *args, **kwargs: self.exec(*args, **kwargs)
    QTextDocument.print_ = lambda self, *args, **kwargs: self.print(*args, **kwargs)
    QColor.toTuple = lambda self: (self.red(), self.green(), self.blue(), self.alpha())
    if not hasattr(QColor, 'isValidColorName'):  # appears in Qt6.4
        QColor.isValidColorName = lambda name: QColor.isValidColor(name)
    if not hasattr(QColor, 'fromString'):  # appears in Qt6.4
        QColor.fromString = lambda name: QColor(name)

    # Allow unscoped access for enums inside the QtGui module
    from .enums_compat import promote_enums
    promote_enums(QtGui)
    del QtGui
elif PYSIDE2:
    from PySide2.QtGui import *
    # Backport items moved to QtGui in Qt6
    from PySide2.QtWidgets import QAction, QActionGroup, QFileSystemModel, QShortcut, QUndoCommand
    if hasattr(QFontMetrics, 'horizontalAdvance'):
        # Needed to prevent raising a DeprecationWarning when using QFontMetrics.width
        QFontMetrics.width = lambda self, *args, **kwargs: self.horizontalAdvance(*args, **kwargs)

    # Map missing/renamed methods
    QMouseEvent.position = lambda *args: QMouseEvent.pos(*args).toPointF()
    QDrag.exec = lambda self, *args, **kwargs: self.exec_(*args, **kwargs)
    QGuiApplication.exec = lambda self, *args, **kwargs: self.exec_(*args, **kwargs)
    QTextDocument.print = lambda self, *args, **kwargs: self.print_(*args, **kwargs)
    QColor.isValidColorName = lambda name: QColor.isValidColor(name)
    QColor.fromString = lambda name: QColor(name)

elif PYSIDE6:
    from PySide6.QtGui import *
    from PySide6.QtOpenGL import *
    from PySide6.QtWidgets import QFileSystemModel
    QFontMetrics.width = lambda self, *args, **kwargs: self.horizontalAdvance(*args, **kwargs)
    QFontMetricsF.width = lambda self, *args, **kwargs: self.horizontalAdvance(*args, **kwargs)

    # Map missing/renamed methods
    QTextDocument.print = lambda self, *args, **kwargs: self.print_(*args, **kwargs)
    if not hasattr(QColor, 'isValidColorName'):  # appears in Qt6.4
        QColor.isValidColorName = lambda name: QColor.isValidColor(name)
    if not hasattr(QColor, 'fromString'):  # appears in Qt6.4
        QColor.fromString = lambda name: QColor(name)

    # Map DeprecationWarning methods
    QDrag.exec_ = lambda self, *args, **kwargs: self.exec(*args, **kwargs)
    QGuiApplication.exec_ = lambda self, *args, **kwargs: self.exec(*args, **kwargs)
    QMouseEvent.pos = lambda *args: QMouseEvent.position(*args)

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
    #   i.e. passing the `mode` keyword argument has no effect and doesn’t
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
    if not hasattr(QWheelEvent, 'position'):  # appears in Qt 5.14
        QWheelEvent.position = lambda self: self.posF()
    if not hasattr(QWheelEvent, 'globalPosition'):  # appears in Qt 5.14
        QWheelEvent.globalPosition = lambda self: self.globalPosF()
    if not hasattr(QTabletEvent, 'deviceType'):  # appears in Qt 5.15
        QTabletEvent.deviceType = lambda self: self.device()

    if 'QColorConstants' not in globals():  # appears in Qt 5.14
        class QColorConstants:
            Color0 = QColor('#000000')
            Color1 = QColor('#ffffff')
            Black = QColor('#000000')
            White = QColor('#ffffff')
            DarkGray = QColor('#808080')
            Gray = QColor('#a0a0a4')
            LightGray = QColor('#c0c0c0')
            Red = QColor('#ff0000')
            Green = QColor('#00ff00')
            Blue = QColor('#0000ff')
            Cyan = QColor('#00ffff')
            Magenta = QColor('#ff00ff')
            Yellow = QColor('#ffff00')
            DarkRed = QColor('#800000')
            DarkGreen = QColor('#008000')
            DarkBlue = QColor('#000080')
            DarkCyan = QColor('#008080')
            DarkMagenta = QColor('#800080')
            DarkYellow = QColor('#808000')
            Transparent = QColor('#00000000')

            class Svg:
                aliceblue = QColor('#f0f8ff')
                antiquewhite = QColor('#faebd7')
                aqua = QColor('#00ffff')
                aquamarine = QColor('#7fffd4')
                azure = QColor('#f0ffff')
                beige = QColor('#f5f5dc')
                bisque = QColor('#ffe4c4')
                black = QColor('#000000')
                blanchedalmond = QColor('#ffebcd')
                blue = QColor('#0000ff')
                blueviolet = QColor('#8a2be2')
                brown = QColor('#a52a2a')
                burlywood = QColor('#deb887')
                cadetblue = QColor('#5f9ea0')
                chartreuse = QColor('#7fff00')
                chocolate = QColor('#d2691e')
                coral = QColor('#ff7f50')
                cornflowerblue = QColor('#6495ed')
                cornsilk = QColor('#fff8dc')
                crimson = QColor('#dc143c')
                cyan = QColor('#00ffff')
                darkblue = QColor('#00008b')
                darkcyan = QColor('#008b8b')
                darkgoldenrod = QColor('#b8860b')
                darkgray = QColor('#a9a9a9')
                darkgreen = QColor('#006400')
                darkgrey = QColor('#a9a9a9')
                darkkhaki = QColor('#bdb76b')
                darkmagenta = QColor('#8b008b')
                darkolivegreen = QColor('#556b2f')
                darkorange = QColor('#ff8c00')
                darkorchid = QColor('#9932cc')
                darkred = QColor('#8b0000')
                darksalmon = QColor('#e9967a')
                darkseagreen = QColor('#8fbc8f')
                darkslateblue = QColor('#483d8b')
                darkslategray = QColor('#2f4f4f')
                darkslategrey = QColor('#2f4f4f')
                darkturquoise = QColor('#00ced1')
                darkviolet = QColor('#9400d3')
                deeppink = QColor('#ff1493')
                deepskyblue = QColor('#00bfff')
                dimgray = QColor('#696969')
                dimgrey = QColor('#696969')
                dodgerblue = QColor('#1e90ff')
                firebrick = QColor('#b22222')
                floralwhite = QColor('#fffaf0')
                forestgreen = QColor('#228b22')
                fuchsia = QColor('#ff00ff')
                gainsboro = QColor('#dcdcdc')
                ghostwhite = QColor('#f8f8ff')
                gold = QColor('#ffd700')
                goldenrod = QColor('#daa520')
                gray = QColor('#808080')
                grey = QColor('#808080')
                green = QColor('#008000')
                greenyellow = QColor('#adff2f')
                honeydew = QColor('#f0fff0')
                hotpink = QColor('#ff69b4')
                indianred = QColor('#cd5c5c')
                indigo = QColor('#4b0082')
                ivory = QColor('#fffff0')
                khaki = QColor('#f0e68c')
                lavender = QColor('#e6e6fa')
                lavenderblush = QColor('#fff0f5')
                lawngreen = QColor('#7cfc00')
                lemonchiffon = QColor('#fffacd')
                lightblue = QColor('#add8e6')
                lightcoral = QColor('#f08080')
                lightcyan = QColor('#e0ffff')
                lightgoldenrodyellow = QColor('#fafad2')
                lightgray = QColor('#d3d3d3')
                lightgreen = QColor('#90ee90')
                lightgrey = QColor('#d3d3d3')
                lightpink = QColor('#ffb6c1')
                lightsalmon = QColor('#ffa07a')
                lightseagreen = QColor('#20b2aa')
                lightskyblue = QColor('#87cefa')
                lightslategray = QColor('#778899')
                lightslategrey = QColor('#778899')
                lightsteelblue = QColor('#b0c4de')
                lightyellow = QColor('#ffffe0')
                lime = QColor('#00ff00')
                limegreen = QColor('#32cd32')
                linen = QColor('#faf0e6')
                magenta = QColor('#ff00ff')
                maroon = QColor('#800000')
                mediumaquamarine = QColor('#66cdaa')
                mediumblue = QColor('#0000cd')
                mediumorchid = QColor('#ba55d3')
                mediumpurple = QColor('#9370db')
                mediumseagreen = QColor('#3cb371')
                mediumslateblue = QColor('#7b68ee')
                mediumspringgreen = QColor('#00fa9a')
                mediumturquoise = QColor('#48d1cc')
                mediumvioletred = QColor('#c71585')
                midnightblue = QColor('#191970')
                mintcream = QColor('#f5fffa')
                mistyrose = QColor('#ffe4e1')
                moccasin = QColor('#ffe4b5')
                navajowhite = QColor('#ffdead')
                navy = QColor('#000080')
                oldlace = QColor('#fdf5e6')
                olive = QColor('#808000')
                olivedrab = QColor('#6b8e23')
                orange = QColor('#ffa500')
                orangered = QColor('#ff4500')
                orchid = QColor('#da70d6')
                palegoldenrod = QColor('#eee8aa')
                palegreen = QColor('#98fb98')
                paleturquoise = QColor('#afeeee')
                palevioletred = QColor('#db7093')
                papayawhip = QColor('#ffefd5')
                peachpuff = QColor('#ffdab9')
                peru = QColor('#cd853f')
                pink = QColor('#ffc0cb')
                plum = QColor('#dda0dd')
                powderblue = QColor('#b0e0e6')
                purple = QColor('#800080')
                red = QColor('#ff0000')
                rosybrown = QColor('#bc8f8f')
                royalblue = QColor('#4169e1')
                saddlebrown = QColor('#8b4513')
                salmon = QColor('#fa8072')
                sandybrown = QColor('#f4a460')
                seagreen = QColor('#2e8b57')
                seashell = QColor('#fff5ee')
                sienna = QColor('#a0522d')
                silver = QColor('#c0c0c0')
                skyblue = QColor('#87ceeb')
                slateblue = QColor('#6a5acd')
                slategray = QColor('#708090')
                slategrey = QColor('#708090')
                snow = QColor('#fffafa')
                springgreen = QColor('#00ff7f')
                steelblue = QColor('#4682b4')
                tan = QColor('#d2b48c')
                teal = QColor('#008080')
                thistle = QColor('#d8bfd8')
                tomato = QColor('#ff6347')
                turquoise = QColor('#40e0d0')
                violet = QColor('#ee82ee')
                wheat = QColor('#f5deb3')
                white = QColor('#ffffff')
                whitesmoke = QColor('#f5f5f5')
                yellow = QColor('#ffff00')
                yellowgreen = QColor('#9acd32')
