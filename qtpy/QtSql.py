# -----------------------------------------------------------------------------
# Copyright © 2009- The Spyder Development Team
#
# Licensed under the terms of the MIT License
# (see LICENSE.txt for details)
# -----------------------------------------------------------------------------

"""Provides QtSql classes and functions."""
from functools import partialmethod

from packaging.version import parse

from . import PYQT5, PYQT6, PYSIDE2, PYSIDE6, QT_VERSION

if PYQT5:
    from PyQt5.QtSql import *
elif PYQT6:
    from PyQt6.QtSql import *

    if parse(QT_VERSION) >= parse("6.6"):
        # `QSqlDatabase.exec` is deprecated since 6.6

        def database_exec(db, query):
            q = QSqlQuery(db)
            q.exec(query)
            return q

        QSqlDatabase.exec = partialmethod(database_exec)
        del database_exec

    QSqlDatabase.exec_ = partialmethod(QSqlDatabase.exec)
    QSqlQuery.exec_ = partialmethod(QSqlQuery.exec)
    QSqlResult.exec_ = partialmethod(QSqlResult.exec)
elif PYSIDE6:
    from PySide6.QtSql import *

    if parse(QT_VERSION) >= parse("6.6"):
        # `QSqlDatabase.exec` is deprecated since 6.6

        def database_exec(db, query):
            q = QSqlQuery(db)
            q.exec(query)
            return q

        QSqlDatabase.exec = partialmethod(database_exec)
        del database_exec

    # Map DeprecationWarning methods
    QSqlDatabase.exec_ = partialmethod(QSqlDatabase.exec)
    QSqlQuery.exec_ = partialmethod(QSqlQuery.exec)
    QSqlResult.exec_ = partialmethod(QSqlResult.exec)
elif PYSIDE2:
    from PySide2.QtSql import *

del PYQT5, PYQT6, PYSIDE2, PYSIDE6, QT_VERSION
del parse
del partialmethod
