# -----------------------------------------------------------------------------
# Copyright © 2009- The Spyder Development Team
#
# Licensed under the terms of the MIT License
# (see LICENSE.txt for details)
# -----------------------------------------------------------------------------

"""Provides QtSql classes and functions."""
from functools import partialmethod

from packaging.version import Version

from . import PYQT5, PYQT6, PYSIDE2, PYSIDE6, QT_VERSION

if PYQT5:
    from PyQt5.QtSql import *
elif PYQT6:
    from PyQt6.QtSql import *

    if QT_VERSION and Version(QT_VERSION) >= Version("6.6"):
        # `QSqlDatabase.exec` is deprecated since 6.6

        def database_exec(db, query):
            q = QSqlQuery(db)
            q.exec(query)
            return q

        QSqlDatabase.exec = partialmethod(database_exec)
        del database_exec

    QSqlDatabase.exec_ = lambda self, *args, **kwargs: self.exec(
        *args,
        **kwargs,
    )
    QSqlQuery.exec_ = lambda self, *args, **kwargs: self.exec(*args, **kwargs)
    QSqlResult.exec_ = lambda self, *args, **kwargs: self.exec(*args, **kwargs)
elif PYSIDE6:
    from PySide6.QtSql import *

    if QT_VERSION and Version(QT_VERSION) >= Version("6.6"):
        # `QSqlDatabase.exec` is deprecated since 6.6

        def database_exec(db, query):
            q = QSqlQuery(db)
            q.exec(query)
            return q

        QSqlDatabase.exec = partialmethod(database_exec)
        del database_exec

    # Map DeprecationWarning methods
    QSqlDatabase.exec_ = lambda self, *args, **kwargs: self.exec(
        *args,
        **kwargs,
    )
    QSqlQuery.exec_ = lambda self, *args, **kwargs: self.exec(*args, **kwargs)
    QSqlResult.exec_ = lambda self, *args, **kwargs: self.exec(*args, **kwargs)
elif PYSIDE2:
    from PySide2.QtSql import *

del PYQT5, PYQT6, PYSIDE2, PYSIDE6, QT_VERSION
del Version
del partialmethod
