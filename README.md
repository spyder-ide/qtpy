# QtPy: Abtraction layer for PyQt5/PyQt4/PySide

Copyright © 2009- The Spyder Development Team.

## Project details
[![license](https://img.shields.io/pypi/l/qtpy.svg)](./LICENSE)
[![pypi version](https://img.shields.io/pypi/v/qtpy.svg)](https://pypi.python.org/pypi/qtpy)
[![Join the chat at https://gitter.im/spyder-ide/public](https://badges.gitter.im/spyder-ide/spyder.svg)](https://gitter.im/spyder-ide/public)

## Build status
[![Travis status](https://travis-ci.org/spyder-ide/qtpy.svg?branch=master)](https://travis-ci.org/spyder-ide/qtpy)
[![Build status](https://ci.appveyor.com/api/projects/status/ab01a09cbx3m0ao9?svg=true)](https://ci.appveyor.com/project/goanpeca/qtpy)
[![CircleCI](https://circleci.com/gh/spyder-ide/qtpy.svg?style=shield)](https://circleci.com/gh/spyder-ide/qtpy)
[![Coverage Status](https://coveralls.io/repos/github/spyder-ide/qtpy/badge.svg?branch=master)](https://coveralls.io/github/spyder-ide/qtpy?branch=master)
[![Code Issues](https://www.quantifiedcode.com/api/v1/project/c769241c7d7f4463b1e6f67863dabace/badge.svg)](https://www.quantifiedcode.com/app/project/c769241c7d7f4463b1e6f67863dabace)
[![Scrutinizer Code Quality](https://scrutinizer-ci.com/g/spyder-ide/qtpy/badges/quality-score.png?b=master)](https://scrutinizer-ci.com/g/spyder-ide/qtpy/?branch=master)

## Description

**QtPy** (pronounced *'cutie pie'*) is a small abstraction layer that lets you
write applications using a single API call to either PyQt or PySide.

It provides support for PyQt5, PyQt4 and PySide using the PyQt5 layout (where
the QtGui module has been split into QtGui and QtWidgets).

Basically, you write your code as if you were using PyQt5 but import Qt modules
from `qtpy` instead of `PyQt5`.


### Attribution and acknowledgements

This project is based on the [pyqode.qt](https://github.com/pyQode/pyqode.qt)
project and the [spyderlib.qt](https://github.com/spyder-ide/spyder/tree/2.3/spyderlib/qt)
module from the [Spyder](https://github.com/spyder-ide/spyder) project, and
also includes contributions adapted from
[qt-helpers](https://github.com/glue-viz/qt-helpers), developed as part of the
[glue](http://glueviz.org) project.

Unlike `pyqode.qt` this is not a namespace package, so it is not tied
to a particular project or namespace.


### License

This project is licensed under the MIT license.


### Requirements

You need PyQt5, PyQt4 or PySide installed in your system to make use
of QtPy. If several of these packages are found, PyQt5 is used by
default unless you set the `QT_API` environment variable.

`QT_API` can take the following values:

* `pyqt5` (to use PyQt5).
* `pyqt` or `pyqt4` (to use PyQt4).
* `pyside` (to use PySide).


### Installation

```bash
pip install qtpy
```

or

```bash
conda install qtpy
```
