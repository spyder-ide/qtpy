import warnings

from . import PYQT5
from . import PYQT4
from . import PYSIDE
from . import PYSIDE2
from . import PythonQtWarning

if PYQT5:
    from PyQt5.QtMultimedia import *
elif PYSIDE2:
    # Current wheels don't have this module
    # from PySide2.QtMultimedia import *
    warnings.warn("QtMultimedia binding is missing in PySide2", PythonQtWarning)
elif PYQT4:
    from PyQt4.QtMultimedia import *
    from PyQt4.QtGui import QSound
elif PYSIDE:
    from PySide.QtMultimedia import *
    from PySide.QtGui import QSound
