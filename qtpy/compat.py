#
# Copyright © 2009- The Spyder Development Team
# Licensed under the terms of the MIT License

"""
Compatibility functions
"""
import enum
import sys

from . import (
    PYQT5,
    PYQT6,
    PYSIDE2,
    PYSIDE6,
)
from .QtWidgets import QFileDialog

TEXT_TYPES = (str,)


def is_text_string(obj):
    """Return True if `obj` is a text string, False if it is anything else,
    like binary data."""
    return isinstance(obj, str)


def to_text_string(obj, encoding=None):
    """Convert `obj` to (unicode) text string"""
    if encoding is None:
        return str(obj)
    if isinstance(obj, str):
        # In case this function is not used properly, this could happen
        return obj

    return str(obj, encoding)


# =============================================================================
# QVariant conversion utilities
# =============================================================================
PYQT_API_1 = False


def to_qvariant(obj=None):  # analysis:ignore
    """Convert Python object to QVariant
    This is a transitional function from PyQt API#1 (QVariant exist)
    to PyQt API#2 and Pyside (QVariant does not exist)"""
    return obj


def from_qvariant(qobj=None, pytype=None):  # analysis:ignore
    """Convert QVariant object to Python object
    This is a transitional function from PyQt API #1 (QVariant exist)
    to PyQt API #2 and Pyside (QVariant does not exist)"""
    return qobj


# =============================================================================
# Wrappers around QFileDialog static methods
# =============================================================================
def getexistingdirectory(
    parent=None,
    caption="",
    basedir="",
    options=QFileDialog.ShowDirsOnly,
):
    """Wrapper around QtGui.QFileDialog.getExistingDirectory static method
    Compatible with PyQt >=v4.4 (API #1 and #2) and PySide >=v1.0"""
    # Calling QFileDialog static method
    if sys.platform == "win32":
        # On Windows platforms: redirect standard outputs
        _temp1, _temp2 = sys.stdout, sys.stderr
        sys.stdout, sys.stderr = None, None
    try:
        result = QFileDialog.getExistingDirectory(
            parent,
            caption,
            basedir,
            options,
        )
    finally:
        if sys.platform == "win32":
            # On Windows platforms: restore standard outputs
            sys.stdout, sys.stderr = _temp1, _temp2
    if not is_text_string(result):
        # PyQt API #1
        result = to_text_string(result)
    return result


def _qfiledialog_wrapper(
    attr,
    parent=None,
    caption="",
    basedir="",
    filters="",
    selectedfilter="",
    options=None,
):
    if options is None:
        options = QFileDialog.Option(0)

    func = getattr(QFileDialog, attr)

    # Calling QFileDialog static method
    if sys.platform == "win32":
        # On Windows platforms: redirect standard outputs
        _temp1, _temp2 = sys.stdout, sys.stderr
        sys.stdout, sys.stderr = None, None
    result = func(parent, caption, basedir, filters, selectedfilter, options)
    if sys.platform == "win32":
        # On Windows platforms: restore standard outputs
        sys.stdout, sys.stderr = _temp1, _temp2

    output, selectedfilter = result

    # Always returns the tuple (output, selectedfilter)
    return output, selectedfilter


def getopenfilename(
    parent=None,
    caption="",
    basedir="",
    filters="",
    selectedfilter="",
    options=None,
):
    """Wrapper around QtGui.QFileDialog.getOpenFileName static method
    Returns a tuple (filename, selectedfilter) -- when dialog box is canceled,
    returns a tuple of empty strings
    Compatible with PyQt >=v4.4 (API #1 and #2) and PySide >=v1.0"""
    return _qfiledialog_wrapper(
        "getOpenFileName",
        parent=parent,
        caption=caption,
        basedir=basedir,
        filters=filters,
        selectedfilter=selectedfilter,
        options=options,
    )


def getopenfilenames(
    parent=None,
    caption="",
    basedir="",
    filters="",
    selectedfilter="",
    options=None,
):
    """Wrapper around QtGui.QFileDialog.getOpenFileNames static method
    Returns a tuple (filenames, selectedfilter) -- when dialog box is canceled,
    returns a tuple (empty list, empty string)
    Compatible with PyQt >=v4.4 (API #1 and #2) and PySide >=v1.0"""
    return _qfiledialog_wrapper(
        "getOpenFileNames",
        parent=parent,
        caption=caption,
        basedir=basedir,
        filters=filters,
        selectedfilter=selectedfilter,
        options=options,
    )


def getsavefilename(
    parent=None,
    caption="",
    basedir="",
    filters="",
    selectedfilter="",
    options=None,
):
    """Wrapper around QtGui.QFileDialog.getSaveFileName static method
    Returns a tuple (filename, selectedfilter) -- when dialog box is canceled,
    returns a tuple of empty strings
    Compatible with PyQt >=v4.4 (API #1 and #2) and PySide >=v1.0"""
    return _qfiledialog_wrapper(
        "getSaveFileName",
        parent=parent,
        caption=caption,
        basedir=basedir,
        filters=filters,
        selectedfilter=selectedfilter,
        options=options,
    )


# =============================================================================
def isalive(obj):
    """Wrapper around sip.isdeleted and shiboken.isValid which tests whether
    an object is currently alive."""
    if PYQT5 or PYQT6:
        from . import sip

        return not sip.isdeleted(obj)
    if PYSIDE2 or PYSIDE6:
        from . import shiboken

        return shiboken.isValid(obj)
    return None


# =============================================================================
def getenumasint(enum_value):
    """Get the integer value of a Qt enum
    For example:
        Qt.AlignmentFlag.AlignBaseline -> 256
        Qt.WidgetAttribute.WA_AcceptDrops -> 78
    If an integer is passed in, simply return it.
    PySide2's enums are themselves classes, not enum values per se, so if
    we get an integer or a class, return the class.
    """
    if isinstance(enum_value, enum.Enum):
        if PYSIDE2 or PYQT5:
            return int(enum_value)
        return enum_value.value
    return enum_value


# =============================================================================
def getenumfromint(enum_class, i):
    """Get the Qt enum value from an integer"""
    return enum_class(i)
