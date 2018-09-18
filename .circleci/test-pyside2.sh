#!/bin/bash

source $HOME/miniconda/etc/profile.d/conda.sh
conda activate test

# Download PySide2 wheels
export URL="http://download.qt.io/snapshots/ci/pyside/5.11/latest/"

if [ "$USE_CONDA" = "Yes" ]; then
    if [ "$PYTHON_VERSION" = "2.7" ]; then
        conda remove -q qt pyqt
        pip install -q --index-url=${URL} pyside2 --trusted-host download.qt.io
    else
        exit 0
    fi
else
    pip uninstall -q -y pyqt5 sip
    pip install -q --index-url=${URL} pyside2 --trusted-host download.qt.io
fi

python qtpy/tests/runtests.py

# Force quitting if exit status of runtests.py was not 0
if [ $? -ne 0 ]; then
    exit 1
fi

pip uninstall -y -q pyside2
