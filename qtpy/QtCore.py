from . import _get_submodule, PYQT5

_name_changes = {
    "PyQt": {
        "Property": "pyqtProperty",
        "Signal": "pyqtSignal",
        "SignalInstance": "pyqtBoundSignal",
        "Slot": "pyqtSlot",
        "__version__": "QT_VERSION_STR",
    }
}
_get_submodule(__name__, globals(), _name_changes)

if PYQT5:
    QDateTime = globals()["QDateTime"]
    QDateTime.toPython = QDateTime.toPyDateTime
