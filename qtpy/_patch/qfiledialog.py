# -*- coding: utf-8 -*-
"""QFileDialog patch."""

import sys

from .py3compat import to_text_string, is_text_string


def patch_filedialog(QFileDialog):
    """Patch QFile Dialog."""

    def _qfiledialog_wrapper(attr, parent=None, caption='', basedir='',
                             filters='', selectedfilter='', options=None):
        if options is None:
            options = QFileDialog.Options(0)
        try:
            # PyQt <v4.6 (API #1)
            from .QtCore import QString
        except ImportError:
            # PySide or PyQt >=v4.6
            QString = None  # analysis:ignore
        tuple_returned = True
        try:
            # PyQt >=v4.6
            func = getattr(QFileDialog, attr+'AndFilter')
        except AttributeError:
            # PySide or PyQt <v4.6
            func = getattr(QFileDialog, attr)
            if QString is not None:
                selectedfilter = QString()
                tuple_returned = False

        # Calling QFileDialog static method
        if sys.platform == "win32":
            # On Windows platforms: redirect standard outputs
            _temp1, _temp2 = sys.stdout, sys.stderr
            sys.stdout, sys.stderr = None, None
        try:
            result = func(parent, caption, basedir,
                          filters, selectedfilter, options)
        except TypeError:
            # The selectedfilter option (`initialFilter` in Qt) has only been
            # introduced in Jan. 2010 for PyQt v4.7, that's why we handle here
            # the TypeError exception which will be raised with PyQt v4.6
            # (see Issue 960 for more details)
            result = func(parent, caption, basedir, filters, options)
        finally:
            if sys.platform == "win32":
                # On Windows platforms: restore standard outputs
                sys.stdout, sys.stderr = _temp1, _temp2
    
        # Processing output
        if tuple_returned:
            # PySide or PyQt >=v4.6
            output, selectedfilter = result
        else:
            # PyQt <v4.6 (API #1)
            output = result
        if QString is not None:
            # PyQt API #1: conversions needed from QString/QStringList
            selectedfilter = to_text_string(selectedfilter)
            if isinstance(output, QString):
                # Single filename
                output = to_text_string(output)
            else:
                # List of filenames
                output = [to_text_string(fname) for fname in output]
    
        # Always returns the tuple (output, selectedfilter)
        return output, selectedfilter


    def _getOpenFileName(parent=None, caption='', basedir='', filters='',
                        selectedfilter='', options=None):
        """
        Wrapper around QtGui.QFileDialog.getOpenFileName static method.

        Returns a tuple (filename, selectedfilter) -- when dialog box is
        canceled, returns a tuple of empty strings.

        Compatible with PyQt >=v4.4 (API #1 and #2) and PySide >=v1.0.
        """
        return _qfiledialog_wrapper('getOpenFileName',
                                    parent=parent,
                                    caption=caption,
                                    basedir=basedir,
                                    filters=filters,
                                    selectedfilter=selectedfilter,
                                    options=options)


    def _getOpenFileNames(parent=None, caption='', basedir='', filters='',
                         selectedfilter='', options=None):
        """
        Wrapper around QtGui.QFileDialog.getOpenFileNames static method.

        Returns a tuple (filenames, selectedfilter) -- when dialog box is
        canceled, returns a tuple (empty list, empty string).

        Compatible with PyQt >=v4.4 (API #1 and #2) and PySide >=v1.0.
        """
        return _qfiledialog_wrapper('getOpenFileNames',
                                    parent=parent,
                                    caption=caption,
                                    basedir=basedir,
                                    filters=filters,
                                    selectedfilter=selectedfilter,
                                    options=options)


    def _getSaveFileName(parent=None, caption='', basedir='', filters='',
                        selectedfilter='', options=None):
        """
        Wrapper around QtGui.QFileDialog.getSaveFileName static method.

        Returns a tuple (filename, selectedfilter) -- when dialog box is
        canceled, returns a tuple of empty strings.

        Compatible with PyQt >=v4.4 (API #1 and #2) and PySide >=v1.0.
        """
        return _qfiledialog_wrapper('getSaveFileName',
                                    parent=parent,
                                    caption=caption,
                                    basedir=basedir,
                                    filters=filters,
                                    selectedfilter=selectedfilter,
                                    options=options)


    def _getExistingDirectory(parent=None, caption='', basedir='',
                             options=QFileDialog.ShowDirsOnly):
        """
        Wrapper around QtGui.QFileDialog.getExistingDirectory static method.

        Compatible with PyQt >=v4.4 (API #1 and #2) and PySide >=v1.0.
        """
        # Calling QFileDialog static method
        if sys.platform == "win32":
            # On Windows platforms: redirect standard outputs
            _temp1, _temp2 = sys.stdout, sys.stderr
            sys.stdout, sys.stderr = None, None
        try:
            result = QFileDialog.getExistingDirectory(parent,
                                                      caption,
                                                      basedir,
                                                      options)
        finally:
            if sys.platform == "win32":
                # On Windows platforms: restore standard outputs
                sys.stdout, sys.stderr = _temp1, _temp2
        if not is_text_string(result):
            # PyQt API #1
            result = to_text_string(result)
        return result

    QFileDialog.getOpenFileName2 = _getOpenFileName
    QFileDialog.getOpenFileNames2 = _getOpenFileNames
    QFileDialog.getSaveFileName2 = _getSaveFileName
    QFileDialog.getExistingDirectory2 = _getExistingDirectory
