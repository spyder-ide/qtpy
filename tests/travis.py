import os

os.environ['QT_API'] = os.environ['USE_QT_API']

from qtpy import QtCore, QtGui

print('Qt version:%s' % QtCore.__version__)
print(QtCore.QEvent)
print(QtGui.QPainter)
print(QtGui.QWidget)
