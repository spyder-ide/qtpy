from qtpy import PYQT5
from qtpy import PYQT4
from qtpy import PYSIDE


if PYQT5:
    from PyQt5.QtMultimedia import *
elif PYQT4:
    from PyQt4.QtMultimedia import *
    from PyQt4.QtGui import QSound
elif PYSIDE:
    from PySide.QtMultimedia import *
    from PySide.QtGui import QSound
