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

Basically, you can write your code as if you were using `PySide2/PySide6`
but import Qt modules from `qtpy` instead of `PySide2/PySide6` (or `PyQt5/PyQt6`)

Following this idea, when porting code from using different Qt bindings (`PyQt` vs `PySide`) or Qt versions (5 vs 6) QtPy can help to do this in an easier way since it allows you to incrementally do it. You can go in your project checking file by file/module by module allowing you to better handle possible incompatibilities between bindings or Qt versions while keeping your project running! Examples of this approach can be checked in projects like [`git-cola`](https://github.com/git-cola/git-cola/issues/232).

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


## Contributing

Everyone is welcome to contribute!


## Sponsors

QtPy is funded thanks to the generous support of


[![Quansight](https://user-images.githubusercontent.com/16781833/142477716-53152d43-99a0-470c-a70b-c04bbfa97dd4.png)](https://www.quansight.com/)[![Numfocus](https://i2.wp.com/numfocus.org/wp-content/uploads/2017/07/NumFocus_LRG.png?fit=320%2C148&ssl=1)](https://numfocus.org/)

and the donations we have received from our users around the world through [Open Collective](https://opencollective.com/spyder/):

[![Sponsors](https://opencollective.com/spyder/sponsors.svg)](https://opencollective.com/spyder#support)
