# QtPy: Abstraction layer for PyQt5/PyQt6/PySide2/PySide6

[![license](https://img.shields.io/pypi/l/qtpy.svg)](./LICENSE)
[![pypi version](https://img.shields.io/pypi/v/qtpy.svg)](https://pypi.org/project/QtPy/)
[![conda version](https://img.shields.io/conda/vn/conda-forge/qtpy.svg)](https://www.anaconda.com/download/)
[![download count](https://img.shields.io/conda/dn/conda-forge/qtpy.svg)](https://www.anaconda.com/download/)
[![OpenCollective Backers](https://opencollective.com/spyder/backers/badge.svg?color=blue)](#backers)
[![Join the chat at https://gitter.im/spyder-ide/public](https://badges.gitter.im/spyder-ide/spyder.svg)](https://gitter.im/spyder-ide/public)<br>
[![PyPI status](https://img.shields.io/pypi/status/qtpy.svg)](https://github.com/spyder-ide/qtpy)
[![Github build status](https://github.com/spyder-ide/qtpy/workflows/Tests/badge.svg)](https://github.com/spyder-ide/qtpy/actions)
[![Coverage Status](https://coveralls.io/repos/github/spyder-ide/qtpy/badge.svg?branch=master)](https://coveralls.io/github/spyder-ide/qtpy?branch=master)

*Copyright © 2009–2021 The Spyder Development Team*


## Description

**QtPy** is a small abstraction layer that lets you
write applications using a single API call to either PyQt or PySide.

It provides support for PyQt5, PyQt6, PySide6, PySide2 using the Qt5 layout
(where the QtGui module has been split into QtGui and QtWidgets).

Basically, you can write your code as if you were using PyQt or PySide directly,
but import Qt modules from `qtpy` instead of `PyQt5`, `PyQt6`, `PySide2`, or `PySide6`.

Accordingly, when porting code between different Qt bindings (PyQt vs PySide) or Qt versions (Qt5 vs Qt6), QtPy makes this much more painless, and allows you to easily and incrementally transition between them. QtPy handles incompatibilities and differences between bindings or Qt versions for you while keeping your project running, so you can focus more on your own code and less on keeping track of supporting every Qt version and binding. Furthermore, when you do want to upgrade or support new bindings, it allows you to update your project module by module rather than all at once.  You can check out examples of this approach in projects using QtPy, like [git-cola](https://github.com/git-cola/git-cola/issues/232).

### Attribution and acknowledgments

This project is based on the [pyqode.qt](https://github.com/pyQode/pyqode.qt)
project and the [spyderlib.qt](https://github.com/spyder-ide/spyder/tree/2.3/spyderlib/qt)
module from the [Spyder](https://github.com/spyder-ide/spyder) project, and
also includes contributions adapted from
[qt-helpers](https://github.com/glue-viz/qt-helpers), developed as part of the
[glue](http://glueviz.org) project.

Unlike `pyqode.qt` this is not a namespace package, so it is not tied
to a particular project or namespace.


### License

This project is released under the MIT license.


### Requirements

You need PyQt5, PyQt6, PySide2 or PySide6 installed in your system to make use
of QtPy. If several of these packages are found, PyQt5 is used by
default unless you set the `QT_API` environment variable.

`QT_API` can take the following values:

* `pyqt5` (to use PyQt5).
* `pyqt6` (to use PyQt6).
* `pyside6` (to use PySide6)
* `pyside2` (to use PySide2)


### Installation

```bash
pip install qtpy
```

or

```bash
conda install qtpy
```


### Mypy integration

A CLI is offered to help with usage of QtPy.
Presently, the only feature is to generate command line arguments for Mypy
that will enable it to process the QtPy source files with the same API
as QtPy itself would have selected.

If you run

```bash
qtpy mypy-args
```

QtPy will output a string of Mypy CLI args that will reflect the currently
selected Qt API.
For example, in an environment where `PYQT5` would be selected
(or the default fallback, if no binding can be found in the environment),
this would output the following:

```text
--always-true=PYQT5 --always-false=PYQT6 --always-false=PYSIDE2 --always-false=PYSIDE6
```

If using Bash or a similar shell, this can be injected into
the Mypy command line invocation as follows:

```bash
mypy --package mypackage $(qtpy mypy-args)
```


## Contributing

Everyone is welcome to contribute!


## Sponsors

QtPy is funded thanks to the generous support of


[![Quansight](https://user-images.githubusercontent.com/16781833/142477716-53152d43-99a0-470c-a70b-c04bbfa97dd4.png)](https://www.quansight.com/)[![Numfocus](https://i2.wp.com/numfocus.org/wp-content/uploads/2017/07/NumFocus_LRG.png?fit=320%2C148&ssl=1)](https://numfocus.org/)

and the donations we have received from our users around the world through [Open Collective](https://opencollective.com/spyder/):

[![Sponsors](https://opencollective.com/spyder/sponsors.svg)](https://opencollective.com/spyder#support)
