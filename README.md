# QtPy: Abstraction layer for PyQt5/PySide2/PyQt6/PySide6

[![license](https://img.shields.io/pypi/l/qtpy.svg)](./LICENSE)
[![pypi version](https://img.shields.io/pypi/v/qtpy.svg)](https://pypi.org/project/QtPy/)
[![conda version](https://img.shields.io/conda/vn/conda-forge/qtpy.svg)](https://www.anaconda.com/download/)
[![download count](https://img.shields.io/conda/dn/conda-forge/qtpy.svg)](https://www.anaconda.com/download/)
[![OpenCollective Backers](https://opencollective.com/spyder/backers/badge.svg?color=blue)](https://opencollective.com/spyder/)
[![Join the chat at https://gitter.im/spyder-ide/public](https://badges.gitter.im/spyder-ide/spyder.svg)](https://gitter.im/spyder-ide/public)<br>
[![PyPI status](https://img.shields.io/pypi/status/qtpy.svg)](https://github.com/spyder-ide/qtpy)
[![Github build status](https://github.com/spyder-ide/qtpy/workflows/Tests/badge.svg)](https://github.com/spyder-ide/qtpy/actions)
[![Coverage Status](https://coveralls.io/repos/github/spyder-ide/qtpy/badge.svg?branch=master)](https://coveralls.io/github/spyder-ide/qtpy?branch=master)

*Copyright © 2009– The Spyder Development Team*

## Description

**QtPy** provides a uniform interface to support PyQt5, PySide2, PyQt6, and PySide6 through a single codebase.
It abstracts the differences between bindings and versions, allowing software to remain portable and easier to maintain.

Import from `qtpy` instead of PySide/PyQt:

```python
from qtpy import QtWidgets, QtCore

app = QtWidgets.QApplication()
widget = QtWidgets.QWidget()
widget.show()
app.exec()
```

## Installation

```bash
pip install qtpy
```

or

```bash
conda install qtpy
```

### Requirements

The installation requires one of the supported packages (PySide2, PySide6, PyQt5, PyQt6) as QtPy does not install any
binding by itself.
If several of these packages are found, PyQt5 is used by default.

To set a specific binding, set the `QT_API` environment variable to on of the following values:

* `pyside2` (to use PySide2).
* `pyside6` (to use PySide6).
* `pyqt5` (to use PyQt5).
* `pyqt6` (to use PyQt6).

## Features

* Supports multiple Qt bindings (PyQt5/6, PySide2/6) without requiring conditional imports or logic branching.

* Detects and loads the available Qt binding automatically based on what is installed or already imported.

* Normalizes the module structure to follow the modern Qt5 layout (`QtGui` / `QtWidgets`).

* Simplifies the process of porting applications between Qt5 and Qt6 by handling API incompatibilities internally.

* Enables incremental updates to project modules rather than requiring a full-scale rewrite when changing Qt providers.

### Module Aliases

QtPy provides aliases following the Qt5 module layout:

| PyQt5/6                 | Alias             |
|-------------------------|-------------------|
| `QtCore.pyqtSignal`     | `QtCore.Signal`   |
| `QtCore.pyqtSlot`       | `QtCore.Slot`     |
| ``QtCore.pyqtProperty`` | `QtCore.Property` |'

* For PyQt6 enums, unscoped enum access was added by promoting the enums of the
  `QtCore`, `QtGui`, `QtTest` and `QtWidgets` modules.

* Compatibility is added between the `QtGui` and `QtOpenGL` modules for
  the `QOpenGL*` classes.

### Module Constants

| Constant              | Value                                                       |
|-----------------------|-------------------------------------------------------------|
| `QtCore.__version__`  | The current Qt version.                                     |
| `qtpy.QT_VERSION`     | The current Qt version.                                     |
| `qtpy.PYSIDE_VERSION` | The current binding version for PySide. `None` if not used. |
| `qtpy.PYQT_VERSION`   | The current binding version for PyQt. `None` if not used.   |
| `qtpy.API_NAME`       | The current selected binding.                               |
| `qtpy.PYSIDE2`        | `True`/`False` if PySide2 is currently used.                |
| `qtpy.PYSIDE6`        | `True`/`False` if PySide6 is currently used.                |
| `qtpy.PYQT5`          | `True`/`False` if PyQt5 is currently used.                  |
| `qtpy.PYQT6`          | `True`/`False` if PyQt6 is currently used.                  |
| `qtpy.QT5`            | `True`/`False` if Qt5 is currently used.                    |
| `qtpy.QT6`            | `True`/`False` if Qt6 is currently used.                    |

### Compat Module

The `qtpy.compat` module provides wrappers for `QFileDialog` static methods and SIP/Shiboken functions.

| Source                               | Wrappers                           |
|--------------------------------------|------------------------------------|
| `QFileDialog.getExistingDirectory`   | `qtpy.compat.getexistingdirectory` |
| `QFileDialog.getOpenFileName`        | `qtpy.compat.getopenfilename`      |
| `QFileDialog.getOpenFileNames`       | `qtpy.compat.getopenfilenames`     |
| `QFileDialog.getSaveFileName`        | `qtpy.compat.getsavefilename`      |
| `sip.isdeleted` / `shiboken.isValid` | `qtpy.compat.isalive`              |

### Type Checker Integration

Type checkers have no knowledge of installed packages, so these tools require
additional configuration.

A Command Line Interface (CLI) is offered to help with usage of QtPy (to get MyPy
and Pyright/Pylance args/configurations).

#### Mypy

The `mypy-args` command helps you to generate command line arguments for Mypy
that will enable it to process the QtPy source files with the same API
as QtPy itself would have selected.

To output a string of Mypy CLI args that will reflect the currently selected
Qt API run:

```bash
qtpy mypy-args
```

For example, in an environment where PyQt5 is installed and selected
(or the default fallback, if no binding can be found in the environment),
this would output the following:

```text
--always-true=PYQT5 --always-false=PYSIDE2 --always-false=PYQT6 --always-false=PYSIDE6
```

Using Bash or a similar shell, this can be injected into the Mypy command line invocation:

```bash
mypy --package mypackage $(qtpy mypy-args)
```

#### Pyright/Pylance

In the case of Pyright, instead of runtime arguments, it is required to create a
config file for the project, called `pyrightconfig.json` or a `pyright` section
in `pyproject.toml`. Refer to the
[Pyright Configuration](https://github.com/microsoft/pyright/blob/main/docs/configuration.md)
for reference. In order to set this configuration, QtPy offers the `pyright-config`
command for guidance.

To add necessary configs in your project files run:

```bash
qtpy pyright-config
```

If you don't have them, it is recommended to create the latter. For example,
in an environment where PyQt5 is installed and selected (or the default fallback,
if no binding can be found in the environment), this would output the following files:

`pyrightconfig.json`

```json
{
  "defineConstant": {
    "PYQT5": true,
    "PYSIDE2": false,
    "PYQT6": false,
    "PYSIDE6": false
  }
}
```

`pyproject.toml`

```toml
[tool.pyright.defineConstant]
PYQT5 = true
PYSIDE2 = false
PYQT6 = false
PYSIDE6 = false
```

**Note**: These configurations are necessary for the correct usage of the default VSCode's type
checking feature while using QtPy in your source code.

## Testing Matrix

Currently, QtPy runs tests for different bindings on Linux, Windows and macOS, using
Python 3.9, 3.11 and 3.13, and installing those bindings with `conda` and `pip`. For the
PyQt bindings, the installation of extra packages is also checked via `pip`.

Following this, the current test matrix looks something like this:

|         | Python            | 3.9                |      | 3.11               |                            | 3.13               |                            |
|---------|-------------------|--------------------|------|--------------------|----------------------------|--------------------|----------------------------|
| OS      | Binding / manager | conda              | pip  | conda              | pip                        | conda              | pip                        |
| Linux   | PyQt5             | 5.12               | 5.15 | 5.15               | 5.15 (with extras)         | 5.15               | 5.15                       |
|         | PyQt6             | skip (unavailable) | 6.5  | skip (unavailable) | 6.8 (with extras)          | skip (unavailable) | 6.8                        |
|         | PySide2           | 5.13               | 5.12 | 5.15               | skip (no wheels available) | skip (unavailable) | skip (no wheels available) |
|         | PySide6           | 6.5                | 6.5  | 6.8                | 6.8                        | 6.8                | 6.8                        |
| Windows | PyQt5             | 5.12               | 5.15 | 5.15               | 5.15 (with extras)         | 5.15               | 5.15                       |
|         | PyQt6             | skip (unavailable) | 6.2  | skip (unavailable) | 6.8 (with extras)          | skip (unavailable) | 6.8                        |
|         | PySide2           | 5.13               | 5.15 | 5.15               | skip (no wheels available) | skip (unavailable) | skip (no wheels available) |
|         | PySide6           | 6.5                | 6.2  | 6.8                | 6.8                        | 6.8                | 6.8                        |
| MacOS   | PyQt5             | 5.12               | 5.15 | skip               | 5.15 (with extras)         | 5.15               | 5.15                       |
|         | PyQt6             | skip (unavailable) | 6.2  | skip               | 6.8 (with extras)          | skip (unavailable) | 6.8                        |
|         | PySide2           | 5.13               | 5.12 | skip               | skip (no wheels available) | skip (unavailable) | skip (no wheels available) |
|         | PySide6           | 6.8                | 6.2  | skip               | 6.8                        | 6.8                | 6.8                        |

**Note**: The mentioned extra packages for the PyQt bindings are the following:

* `PyQt3D` and `PyQt6-3D`
* `PyQtChart` and `PyQt6-Charts`
* `PyQtDataVisualization` and `PyQt6-DataVisualization`
* `PyQtNetworkAuth` and `PyQt6-NetworkAuth`
* `PyQtPurchasing`
* `PyQtWebEngine` and `PyQt6-WebEngine`
* `QScintilla` and `PyQt6-QScintilla`

## Attribution and Acknowledgments

This project is based on the [pyqode.qt](https://github.com/pyQode/pyqode.qt)
project and the [spyderlib.qt](https://github.com/spyder-ide/spyder/tree/2.3/spyderlib/qt)
module from the [Spyder](https://github.com/spyder-ide/spyder) project, and
also includes contributions adapted from
[qt-helpers](https://github.com/glue-viz/qt-helpers), developed as part of the
[glue](http://glueviz.org) project.

Unlike `pyqode.qt` this is not a namespace package, so it is not tied
to a particular project or namespace.

## License

This project is released under the [MIT license](LICENSE).

## Contributing

Everyone is welcome to contribute! See our [Contributing guide](CONTRIBUTING.md) for more details.

## Sponsors

QtPy is funded thanks to the generous support of

[![Chan Zuckerberg Initiative](https://raw.githubusercontent.com/spyder-ide/spyder/master/img_src/czi.png)](https://chanzuckerberg.com/)[![Numfocus](https://i2.wp.com/numfocus.org/wp-content/uploads/2017/07/NumFocus_LRG.png?fit=320%2C148&ssl=1)](https://numfocus.org/)

and the donations we have received from our users around the world
through [Open Collective](https://opencollective.com/spyder/):

[![Sponsors](https://opencollective.com/spyder/sponsors.svg)](https://opencollective.com/spyder#support)
