# -*- coding: utf-8 -*-
#
# Copyright © 2009- The Spyder Development Team
# Copyright © 2014-2015 Colin Duquesnoy
#
# Licensed under the terms of the MIT License
# (see LICENSE.txt for details)

"""
**QtPy** is a shim over the various Python Qt bindings. It is used to
write Qt binding independent libraries or applications.

If one of the APIs has already been imported, then it will be used.

Otherwise, the shim will automatically select the first available API
following the list below; in that case, you can force the use of one
specific binding (e.g. if your application is using one specific binding
and you need to use a library that uses QtPy) by setting up the
``QT_API`` environment variable.

For each selected binding, there will be more three attempts if it is
not found, following the most recent (Qt5) and most stable (PyQt) API.
See below:

* pyqt5: PyQt5, PySide2, PyQt4, PySide
* pyside2: PySide2, PyQt5, PyQt4, PySide
* pyqt4: PyQt4, PySide, PyQt5, PySide2
* pyside: PySide, PyQt4, PyQt5, PySide2

The clearest way to set which API is to be used by QtPy is setting
``QT_API`` environment variable. The default value for ``QT_API = 'pyqt5'``
(not case sensitive).

The priority when setting the Qt binding API is detailed below:

1 Have been already imported any Qt binding (not recommended, implicit):
    1.1 QT_API is not set, pass, no output;
    1.2 QT_API is set to the same binding, pass, no output;
    1.3 QT_API is set to a different binding, ignore QT_API, pass but warns;

2 Have NOT been already imported any Qt binding (explicitly setting):
    2.1 QT_API is set correctly, pass;
        2.1.1 If binding is found, pass, no output;
        2.1.2 If binding is not found, try another one (more three);
            2.1.2.a If any is found (different from set), pass but warns;
            2.1.2.b If no one is found, stop, error;
    2.2 QT_API is not set correctly, stop, error;

Note 1: if any Qt binding is imported (a different one) after QtPy
import, issues and errors may occur and QtPy won't be able to help you
with any warning.

Note 2: we always preffer to not break the code when something is not
found, so we use ``warnings`` module to alert changes and show information
that may be useful when developing using QtPy. Remember to set warnings
to show messages.

PyQt5
=====

For PyQt5, you don't have to set anything as it will be used automatically::

    >>> from qtpy import QtGui, QtWidgets, QtCore
    >>> print(QtWidgets.QWidget)

PySide2
=======

Set the QT_API environment variable to 'PySide2' before importing other
packages::

    >>> import os
    >>> os.environ['QT_API'] = 'pyside2'
    >>> from qtpy import QtGui, QtWidgets, QtCore
    >>> print(QtWidgets.QWidget)

PyQt4
=====

Set the ``QT_API`` environment variable to 'PyQt4' before importing any python
package::

    >>> import os
    >>> os.environ['QT_API'] = 'pyqt4'
    >>> from qtpy import QtGui, QtWidgets, QtCore
    >>> print(QtWidgets.QWidget)

PySide
======

Set the QT_API environment variable to 'PySide' before importing other
packages::

    >>> import os
    >>> os.environ['QT_API'] = 'pyside'
    >>> from qtpy import QtGui, QtWidgets, QtCore
    >>> print(QtWidgets.QWidget)

"""

import importlib.util
import os
import sys
import warnings

# Version of QtPy
from ._version import __version__


class PythonQtError(Exception):
    """Error raise if no bindings could be selected."""
    pass


class PythonQtWarning(Warning):
    """Warning if some features are not implemented in a binding."""
    pass


def get_imported_api(apis_to_search):
    """Return an ordered list of Qt bindings that have been already imported."""
    imported_api = []

    for api_name in apis_to_search:
        if api_name in sys.modules:
            imported_api.append(api_name)

    return imported_api


def get_available_api(apis_to_search):
    """Return an ordered list of Qt bindings that are available (installed)."""
    available_api = []

    for api_name in apis_to_search:
        module_spec = importlib.util.find_spec(api_name)
        if module_spec:
            available_api.append(api_name)

    return available_api


def get_api_information(api_name):
    """Get API information of version and Qt version, also"""

    if api_name == 'PyQt4':
        try:
            import sip
            try:
                sip.setapi('QString', 2)
                sip.setapi('QVariant', 2)
                sip.setapi('QDate', 2)
                sip.setapi('QDateTime', 2)
                sip.setapi('QTextStream', 2)
                sip.setapi('QTime', 2)
                sip.setapi('QUrl', 2)
            except (AttributeError, ValueError):
                # PyQt < v4.6
                pass
            from PyQt4.Qt import PYQT_VERSION_STR as api_version  # analysis:ignore
            from PyQt4.Qt import QT_VERSION_STR as qt_version  # analysis:ignore
        except ImportError:
            raise PythonQtError('PyQt4 cannot be imported in QtPy.')

    elif api_name == 'PyQt5':
        try:
            from PyQt5.QtCore import PYQT_VERSION_STR as api_version  # analysis:ignore
            from PyQt5.QtCore import QT_VERSION_STR as qt_version  # analysis:ignore
        except ImportError:
            raise PythonQtError('PyQt5 cannot be imported in QtPy.')

    elif api_name == 'PySide':
        try:
            from PySide import __version__ as api_version  # analysis:ignore
            from PySide.QtCore import __version__ as qt_version  # analysis:ignore
        except ImportError:
            raise PythonQtError('PySide cannot be imported in QtPy.')

    elif api_name == 'PySide2':
        try:
            from PySide2 import __version__ as api_version  # analysis:ignore
            from PySide2.QtCore import __version__ as qt_version  # analysis:ignore
        except ImportError:
            raise PythonQtError('PySide2 cannot be imported in QtPy.')
    else:
        return (None, None)

    return (api_version, qt_version)


# Qt API environment variable name
QT_API = 'QT_API'

# Keys: names of the expected Qt API (internal names)
# Values: ordered list of importing names based on its key
# The sequence preserves the most recent (Qt5) and stable (PyQt) api
api_names = {'pyqt4': ['PyQt4', 'PySide', 'PyQt5', 'PySide2'],
             'pyqt5': ['PyQt5', 'PySide2', 'PyQt4', 'PySide'],
             'pyside': ['PySide', 'PyQt4', 'PyQt5', 'PySide2'],
             'pyside2': ['PySide2', 'PyQt5', 'PyQt4', 'PySide']}

# Other keys for the same Qt API that can be used, for compatibility
# pyqt4 -> pyqode.qt original name
# pyqt -> name used in IPython.qt
api_names['pyqt'] = api_names['pyqt4']

# Default/Preferrable API, must be one of api_names keys
default_api = 'pyqt5'

# Check if API's are available, maybe overtested
if not get_available_api(api_names[default_api]):
    raise PythonQtError('No Qt API can be imported. Please, install at least '
                        'one of these: {}.'.format(api_names[default_api]))

# All False/None because they were not imported yet
PYQT5 = PYQT4 = PYSIDE = PYSIDE2 = False
API_VERSION = QT_VERSION = ''

is_old_pyqt = is_pyqt46 = False
api_trial = []

# Setting a default value for QT_API and get the value from environment
os.environ.setdefault(QT_API, default_api)
env_api = os.environ[QT_API].lower()

# Check if it was correctly set with environment variable
if env_api not in api_names.keys():
    raise PythonQtError('Qt binding "{}" is unknown, please use a name '
                        '(not case sensitive) from {}'.format(env_api,
                                                              list(api_names.keys())))
environment_api_list = api_names[env_api]

# Check if Qt binding was already imported in 'sys.modules'
# The preference sequence is given by env_api if set or by default_api
imported_api_list = get_imported_api(api_names[env_api])

# If more than one Qt binding is imported, just warns for now
if len(imported_api_list) >= 2:
    warnings.warn('There is more than one imported Qt binding {}.'
                  'This may cause some issues, check your code '
                  'consistence'.format(imported_api_list), RuntimeWarning)

# Priority for imported binding(s), even QT_API is set
if imported_api_list:
    api_trial = imported_api_list
else:
    api_trial = environment_api_list

# Initial value for API is get always from environment
initial_api = environment_api_list[0]

for api_name in api_trial:
    try:
        api_version, qt_version = get_api_information(api_name)
    except PythonQtError:
        pass
    else:
        if api_version and qt_version:
            API = api_name
            API_VERSION = api_version
            QT_VERSION = qt_version
            if API == 'PyQt4':
                PYQT4 = True
            elif API == 'PyQt5':
                PYQT5 = True
            elif API == 'PySide':
                PYSIDE = True
            elif API == 'PySide2':
                PYSIDE2 = True
            break

# If a correct API name is passed to QT_API and it cannot be found,
# switches to another and informs through the warning
if API != initial_api:
    if imported_api_list:
        # If the code is using QtPy is not supposed do directly import Qt api's,
        # so a warning is sent to check consistence
        warnings.warn('Selected binding "{}" could not be set because there is '
                      'already imported "{}", please check your code for '
                      'consistence'.format(initial_api, API), RuntimeWarning)
    else:
        warnings.warn('Selected binding "{}" could not be found, '
                      'using "{}"'.format(initial_api, API), RuntimeWarning)

API_NAME = API

if PYQT4:
    is_old_pyqt = API_VERSION.startswith(('4.4', '4.5', '4.6', '4.7'))
    is_pyqt46 = API_VERSION.startswith('4.6')
    import sip
    try:
        API_NAME += (" (API v{0})".format(sip.getapi('QString')))
    except AttributeError:
        pass
