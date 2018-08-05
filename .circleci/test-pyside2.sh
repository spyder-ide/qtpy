#!/bin/bash

export PATH="$HOME/miniconda/bin:$PATH"
source activate test

# Download PySide2 wheels
export URL="http://download.qt.io/snapshots/ci/pyside/5.11/latest/"

# We use container 3 to test with pip
if [ "$CIRCLE_NODE_INDEX" = "0" ]; then
    conda remove -q qt pyqt
    pip install --index-url=${URL} pyside2 --trusted-host download.qt.io
elif [ "$CIRCLE_NODE_INDEX" = "3" ]; then
    pip uninstall -q -y pyqt5 sip
    pip install --index-url=${URL} pyside2 --trusted-host download.qt.io
else
    exit 0
fi

python qtpy/tests/runtests.py

# Force quitting if exit status of runtests.py was not 0
if [ $? -ne 0 ]; then
    exit 1
fi

pip uninstall -y -q pyside2
