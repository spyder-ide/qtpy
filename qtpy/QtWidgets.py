from . import API_NAME, _get_submodule

globals().update(_get_submodule(__name__).__dict__)


def exec_(self):
    self.exec()


globals()["QApplication"].exec_ = exec_

if "6" in API_NAME:
    globals()["QAction"] = getattr(_get_submodule("QtGui"), "QAction")
    globals()["QShortcut"] = getattr(_get_submodule("QtGui"), "QShortcut")
