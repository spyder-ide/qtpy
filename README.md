# QtPy: Abstraction layer for PyQt5/PyQt4/PySide2/PySide

Copyright © 2009- The Spyder Development Team.

## Project details
[![license](https://img.shields.io/pypi/l/qtpy.svg)](./LICENSE)
[![pypi version](https://img.shields.io/pypi/v/qtpy.svg)](https://pypi.python.org/pypi/qtpy)
[![Join the chat at https://gitter.im/spyder-ide/public](https://badges.gitter.im/spyder-ide/spyder.svg)](https://gitter.im/spyder-ide/public)
[![OpenCollective Backers](https://opencollective.com/spyder/backers/badge.svg?color=blue)](#backers)
[![OpenCollective Sponsors](https://opencollective.com/spyder/sponsors/badge.svg?color=blue)](#sponsors)

## Build status
[![Build status](https://ci.appveyor.com/api/projects/status/62y6i02vhn4hefg0/branch/master?svg=true)](https://ci.appveyor.com/project/spyder-ide/qtpy/branch/master)
[![CircleCI](https://circleci.com/gh/spyder-ide/qtpy.svg?style=shield)](https://circleci.com/gh/spyder-ide/qtpy)
[![Coverage Status](https://coveralls.io/repos/github/spyder-ide/qtpy/badge.svg?branch=master)](https://coveralls.io/github/spyder-ide/qtpy?branch=master)
[![Scrutinizer Code Quality](https://scrutinizer-ci.com/g/spyder-ide/qtpy/badges/quality-score.png?b=master)](https://scrutinizer-ci.com/g/spyder-ide/qtpy/?branch=master)

----

## Important Announcement: Spyder is unfunded!

Since mid November/2017, [Anaconda, Inc](https://www.anaconda.com/) has
stopped funding Spyder development, after doing it for the past 18
months. Because of that, development will focus from now on maintaining
Spyder 3 at a much slower pace than before.

If you want to contribute to maintain Spyder, please consider donating at

https://opencollective.com/spyder

We appreciate all the help you can provide us and can't thank you enough for
supporting the work of Spyder devs and Spyder development.

If you want to know more about this, please read this
[page](https://github.com/spyder-ide/spyder/wiki/Anaconda-stopped-funding-Spyder).

----

## Description

**QtPy** is a small abstraction layer that lets you
write applications using a single API call to either PyQt or PySide.

It provides support for PyQt5, PyQt4, PySide2 and PySide using the Qt5 layout
(where the QtGui module has been split into QtGui and QtWidgets).

Basically, you write your code as if you were using PySide2 but import Qt modules
from `qtpy` instead of `PySide2` (or `PyQt5`)


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

You need PyQt5, PyQt4, PySide2 or PySide installed in your system to make use
of QtPy. If several of these packages are found, PyQt5 is used by
default unless you set the `QT_API` environment variable.

`QT_API` can take the following values:

* `pyqt5` (to use PyQt5).
* `pyqt` or `pyqt4` (to use PyQt4).
* `pyside2` (to use PySide2)
* `pyside` (to use PySide).


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

## Backers

Support us with a monthly donation and help us continue our activities.

[![Backers](https://opencollective.com/spyder/backers.svg)](https://opencollective.com/spyder#support)


## Sponsors

Become a sponsor to get your logo on our README on Github.

[![Sponsors](https://opencollective.com/spyder/sponsors.svg)](https://opencollective.com/spyder#support)
