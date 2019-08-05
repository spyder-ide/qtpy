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

You can set the use of one specific binding by setting up the ``QT_API``
environment variable. The default value for ``QT_API = 'pyqt5'``
(not case sensitive). For each selected binding, there will be more three
attempts if it is not found, following the most recent (Qt5) and most
stable (PyQt) API. See below:

* pyqt5: PyQt5, PySide2, PyQt4, PySide;
* pyside2: PySide2, PyQt5, PyQt4, PySide;
* pyqt4: PyQt4, PySide, PyQt5, PySide2;
* pyside: PySide, PyQt4, PyQt5, PySide2.

If one of the APIs has already been imported, then that one will be used.
(if the environment variable FORCE_QT_API is not set or set to false).
If you want to ensure that the set binding will be used, indepedent if
any other binding was imported before, you can set ``FORCE_QT_API = True``

The priority when setting the Qt binding API is detailed below:

1 QT_API is set but incorrectly, stop, error;

2 No bindings are found installed, stop, error;

3 Have NOT been already imported any Qt binding, independs on FORCE_QT_API:
    3.1 QT_API is set correctly;
        3.1.1 If binding is found, pass, no output;
        3.1.2 If binding is NOT found, try another one (three more);
            3.1.2.a If any is found (different from set), pass but warns;
    3.3 QT_API is not set, use default, continue to 3.1.1, without warning;

4 Have been already imported ONE Qt binding (not recommended):
    4.1 QT_API is set correctly;
        4.1.1 If the binding is is identical to QT_API, pass, no output,
              independs on FORCE_QT_API;
        4.1.2 If the binding is different from QT_API;
            4.1.2.a FORCE_QT_API is set false or not set, use that
                      imported binding, pass, but warns;
            4.1.2.b FORCE_QT_API is set true, stop, error;
    4.2 QT_API is not set, use default, continue to 4.1.1, without warning;

5 Have been already imported MORE than one Qt binding (highly unrecommended):
    5.1 QT_API is set correctly;
        5.1.1 If the binding is found in the imported bindings, pass,
              no output, independs on FORCE_QT_API;
        5.1.2 If the binding is NOT found in the imported bindings;
            5.1.2.a FORCE_QT_API is set false or not set, try another one
                    (three more);
                    5.1.2.a.i If any is found (different from set), pass
                            but warns;
            5.1.2.b FORCE_QT_API is set true, stop, error;
    5.2 QT_API is not set, use default, continue to 5.1.1, without warning.

Note:
    Always preffer set the things (QT_API and FORCE_QT_API) explicit at
    the beggining of your code. Also, do all your imports using QtPy,
    avoiding using imports from PySide or PyQt directly.

Important:
    We always preffer to not break the code when something is not
    found, so we use ``warnings`` module to alert changes and show
    information that may be useful when developing with QtPy. Remember
    to set warnings to show messages.

Caution:
    Importing more than one binding in the code could cause issues and
    errors that are unpredictable, for example, when comparing instance
    types, inserting widgets from one biding to another. So, it is not
    recommended you do that.

Warning:
    If any Qt binding is imported (a different one) after QtPy import,
    issues and errors may occur and QtPy won't be able to help you
    with any warning, see Caution note.


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

import os
import pkgutil
import platform
import sys
import warnings
from distutils.version import LooseVersion

# Version of QtPy
from ._version import __version__


class PythonQtError(RuntimeError):
    """Error raise if no bindings could be selected."""
    pass


class PythonQtWarning(Warning):
    """Warning if some features are not implemented in a binding."""
    pass


def get_installed_bindings(import_list):
    """Return a list of Qt bindings that are installed.

    Args:
        import_list (list): List of importing names to check, case sensitive.

    Returns:
        list: List of installed binding names.
    """

    installed_bindings = []

    for imp_name in import_list:
        # Using 'try...import' or __import__ to TEST causes the
        # imp_name to be imported and accumulating on sys.modules
        # Using pkgutil.get_loader(), that works on both py2 and py3
        # it works as expected without the need of restore sys.path
        can_import = pkgutil.get_loader(imp_name)

        if can_import:
            installed_bindings.append(imp_name)

    print(installed_bindings)

    return installed_bindings


def get_imported_bindings(import_list):
    """Return a list of Qt bindings that are imported (sys.modules).

    Args:
        import_list (list): List of importing names to check, case sensitive.

    Returns:
        list: List of imported binding names.
    """

    imported_bindings = []

    for imp_name in import_list:
        if imp_name in sys.modules:
            imported_bindings.append(imp_name)

    print(imported_bindings)

    return imported_bindings


def get_binding_info(binding_name, restore_sys_path=True):
    """Get binding, generator and Qt version information by the import system.

    All the tool names are given by their import names, so we get:

        - Bindings are PyQt4, PyQt5, PySide2, PySide;
        - Generators of code are the tools sip (for PyQt) and shiboken
          (for PySide).

    Note:
        - This function should be called after using the
          get_installed_bindings to avoid raise the PythonQtError
          by the not installed binding. So, this error will only be
          raised if the specific import used here fails.
        - It must be rewrite to use pkgutil/importlib to check version
          numbers when after only py36 be used.

    Args:
        binding_name (str): Importing binding name, case sensitive. Must be
            installed,, otherwise will raise an error.
        restore_sys_path (bool): If true, restore the sys.path, otherwise
            keep the import into it. Defauls to True.

    Raises:
        PythonQtError: If is not possible to import the selected binding,
            or if it is not recognized by the QtPy as a binding.

    Returns:
        tuple: Binding, generator and Qt version as strings.
    """

    # Copy sys path to restore later
    sys_path = sys.path
    binding_version = qt_version = ''

    if binding_name == 'PyQt4':
        try:
            from PyQt4.Qt import PYQT_VERSION_STR as binding_version  # analysis:ignore
            from PyQt4.Qt import QT_VERSION_STR as qt_version  # analysis:ignore
        except ImportError:
            raise PythonQtError('PyQt4 cannot be imported by QtPy..')

    elif binding_name == 'PyQt5':
        try:
            from PyQt5.QtCore import PYQT_VERSION_STR as binding_version  # analysis:ignore
            from PyQt5.QtCore import QT_VERSION_STR as qt_version  # analysis:ignore
        except ImportError:
            raise PythonQtError('PyQt5 cannot be imported by QtPy..')

    elif binding_name == 'PySide':
        try:
            from PySide import __version__ as binding_version  # analysis:ignore
            from PySide.QtCore import __version__ as qt_version  # analysis:ignore
        except ImportError:
            raise PythonQtError('PySide cannot be imported by QtPy..')

    elif binding_name == 'PySide2':
        try:
            from PySide2 import __version__ as binding_version  # analysis:ignore
            from PySide2.QtCore import __version__ as qt_version  # analysis:ignore
        except ImportError:
            raise PythonQtError('PySide2 cannot be imported by QtPy.')

    else:
        msg = '{} is not recognized as a binding by QtPy.'.format(binding_name)
        raise PythonQtError(msg)

    # Restore sys path
    if restore_sys_path:
        sys.path = sys_path

    print(binding_version, qt_version)

    return (binding_version, qt_version)


def set_binding(binding_name):
    """Set a binding to be used by QtPy and get information from it.

    Warning:
        - This function is not prepared to be called more than once in
          a unique import of QtPy, yet. Multiple calls will accumulate
          imports on 'sys.modules' if 'binding_name' is installed.
    Note:
        - It should not raise anything here because we have tested all
          things before call this. However, if any import problems
          appears after those tests, we could get some PythonQtError.

    Args:
        binding_name (str): Importing binding name, case sensitive.

    Raises:
        PythonQtError: If is not possible to import.
    """

    try:
        # Using get_binding_info without restore sys path keep the import
        binding_version, qt_version = get_binding_info(binding_name,
                                                       restore_sys_path=False)

    except PythonQtError as er:
        raise PythonQtError(str(er))

    else:

        # Set values for general configuration
        API_NAME = binding_name
        API_VERSION = binding_version
        QT_VERSION = qt_version

        if binding_name == 'PyQt4':
            # Set values for specific binding
            PYQT4 = True
            PYQT_VERSION = binding_version

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

            except ImportError:
                msg = 'SIP library (for PyQt4) cannot be imported in QtPy.'
                raise PythonQtError(msg)

        elif binding_name == 'PyQt5':
            # Set values for the specific binding
            PYQT5 = True
            PYQT_VERSION = binding_version

            if sys.platform == 'darwin':

                macos_version = LooseVersion(platform.mac_ver()[0])

                if macos_version < LooseVersion('10.10'):
                    if LooseVersion(QT_VERSION) >= LooseVersion('5.9'):
                        msg = "Qt 5.9 or higher only works in macOS 10.10 "
                        "or higher. Your program will fail in this system."
                        raise PythonQtError(msg)

                elif macos_version < LooseVersion('10.11'):
                    if LooseVersion(QT_VERSION) >= LooseVersion('5.11'):
                        msg = "Qt 5.11 or higher only works in macOS 10.11 "
                        "or higher. Your program will fail in this system."
                        raise PythonQtError(msg)

                del macos_version

        elif binding_name == 'PySide':
            # Set values for the specific binding
            PYSIDE = True
            PYSIDE_VERSION = binding_version

        elif binding_name == 'PySide2':
            # Set values for the specific binding
            PYSIDE2 = True
            PYSIDE_VERSION = binding_version

            if sys.platform == 'darwin':

                macos_version = LooseVersion(platform.mac_ver()[0])

                if macos_version < LooseVersion('10.11'):

                    if LooseVersion(QT_VERSION) >= LooseVersion('5.11'):
                        msg = "Qt 5.11 or higher only works in macOS 10.11 "
                        "or higher. Your program will fail in this system."
                        raise PythonQtError(msg)
                del macos_version


# Qt API environment variable name
QT_API = 'QT_API'

# When `FORCE_QT_API` is set, we disregard
# any previously imported python bindings
FORCE_QT_API = 'FORCE_QT_API'

# Default/Preferrable API/force, must be one of api_names keys
DEFAULT_API = 'pyqt5'
DEFAULT_FORCE = False

# All false/none/empty because they were not imported yet
PYQT5 = PYQT4 = PYSIDE = PYSIDE2 = False
PYQT_VERSION = PYSIDE_VERSION = ''
is_old_pyqt = is_pyqt46 = False

# API is not a good name for describing binding and its generator
# keep for compatibility with older versions
API = API_NAME = API_VERSION = ''

# Respective to Qt C++ compiled version
QT_VERSION = ''

# Binding name and version such as PySide, PyQt
BINDING_NAME = BINDING_VERSION = ''

# Generator name and version such as Sip and Shiboken
GENERATOR_NAME = GENERATOR_VERSION = ''

# Keys: names of the expected Qt API (internal names)
# Values: ordered list of importing names based on its key
# The sequence preserves the most recent (Qt5) and stable (PyQt)
# TODO: If 'pyside', keep chosen order as PySide2, PyQt5 or use PyQt5, PySide2?
api_names = {'pyqt4': ['PyQt4', 'PySide', 'PyQt5', 'PySide2'],
             'pyqt5': ['PyQt5', 'PySide2', 'PyQt4', 'PySide'],
             'pyside': ['PySide', 'PyQt4', 'PySide2', 'PyQt5'],
             'pyside2': ['PySide2', 'PyQt5', 'PySide', 'PyQt4']}

# Other keys for the same Qt API that can be used for compatibility
# pyqt4 -> pyqode.qt original name, pyqt -> name used in IPython.qt
api_names['pyqt'] = api_names['pyqt4']

# Detecting if a api/force was specified by the user, before setting default
api_specified = QT_API in os.environ
force_specified = FORCE_QT_API in os.environ

# Setting a default value for QT_API/FORCE_QT_API
os.environ.setdefault(QT_API, DEFAULT_API)
os.environ.setdefault(FORCE_QT_API, DEFAULT_FORCE)

# Get the value from environment (or default if not set)
env_api = os.environ[QT_API].lower()
env_force = bool(os.environ[FORCE_QT_API])

# Check if env_api was correctly set with environment variable
if env_api not in api_names.keys():
    msg = 'Qt binding "{}" is unknown. Use one from these: {}.'
    msg = msg.format(env_api, api_names[DEFAULT_API])
    raise PythonQtError(msg)


# NOW GET A LIST OF TRIALS (SET + 3 MORE) BASED ON SET VALUE AND API_NAMES


# The preference sequence is given by env_api
env_api_list = api_names[env_api]

# Initial value is get from environment first trial, index 0 (set value)
initial_api = env_api_list[0]

# Check if Qt bindings have been already imported in 'sys.modules'
imp_api_list = get_imported_bindings(api_names[env_api])

# Importing order for bindings if they are not found
api_trial_list = imp_api_list if imp_api_list else env_api_list

# Refined import order with installed ones
api_trial_avaliable_list = get_installed_bindings(api_trial_list)

# Check if something is installed
if not api_trial_avaliable_list:
    msg = 'No Qt binding can be imported. Install at least one of these: {}.'
    msg = msg.format(api_names[default_api])
    raise PythonQtError(msg)

# If more than one Qt binding is imported, just warns for now
if len(imp_api_list) >= 2:
    msg = 'There is more than one imported Qt binding: {}. '
    msg += 'This may cause some issues. Check your code for consistence.'
    msg = msg.format(imp_api_list)
    warnings.warn(msg, RuntimeWarning)

# In most cases, it will execute only the first item as expected
# because we already refined the list of installed bindings
# Only if any importing problem occurs it will try other ones
for api_name in api_trial_avaliable_list:
    try:
        API_VERSION, QT_VERSION = get_binding_info(api_name)
    except PythonQtError as er:
        msg = 'The binding "{}" is installed but cannot be used. '
        msg += 'Check the original error message: {}.'
        msg = msg.format(api_name, str(er))
        warnings.warn(msg, RuntimeWarning)
    else:
        if API_VERSION and QT_VERSION:
            API = api_name.lower()
            API_NAME = api_name

            if api_name == 'PyQt4':
                PYQT4 = True
                PYQT_VERSION = API_VERSION
                versions = ('4.4', '4.5', '4.6', '4.7')
                is_old_pyqt = PYQT_VERSION.startswith(versions)
                is_pyqt46 = PYQT_VERSION.startswith('4.6')

                import sip

                try:
                    API_NAME += (" (API v{0})".format(sip.getapi('QString')))
                except AttributeError:
                    pass
            elif api_name == 'PyQt5':
                PYQT5 = True
                PYQT_VERSION = API_VERSION
            elif api_name == 'PySide':
                PYSIDE = True
                PYSIDE_VERSION = API_VERSION
            elif api_name == 'PySide2':
                PYSIDE2 = True
                PYSIDE_VERSION = API_VERSION
            break

# Set the environment variable to the current used API after all tests
os.environ['QT_API'] = API

if API_NAME != initial_api and binding_specified:
    # If the code is using QtPy is not supposed do directly import Qt api's,
    # so a warning is sent to check consistence
    if imp_api_list:
        msg = 'Selected binding "{}" could not be set because "{}" has '
        msg += 'already been imported. Check your code for consistence.'
        msg = msg.format(initial_api, API_NAME)
        warnings.warn(msg, RuntimeWarning)
    # If a correct API name is passed to QT_API and it cannot be found,
    # switches to another and informs through the warning
    else:
        msg = 'Selected binding "{}" could not be found, using "{}".'
        msg = msg.format(initial_api, API_NAME)
        warnings.warn(msg, RuntimeWarning)


print("1", PYQT5, PYQT4, PYSIDE, PYSIDE2)
print("2", API, API_NAME, API_VERSION, QT_VERSION)
print("3", PYQT_VERSION, PYSIDE_VERSION)
print("4", is_old_pyqt, is_pyqt46)
