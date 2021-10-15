import warnings

from . import PYQT5
from . import PYSIDE2
from . import PYSIDE6

if PYQT5:
    from PyQt5.QtMultimedia import *
elif PYSIDE6:
    from PySide6.QtMultimedia import *
elif PYSIDE2:
    from PySide2.QtMultimedia import *
