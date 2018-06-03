#!/bin/bash

export PATH="$HOME/miniconda/bin:$PATH"
source activate test

# Download PySide2 wheels
export URL="download.qt.io/snapshots/ci/pyside/5.11/latest/pyside2/"
wget -r --no-parent -A 'PySide2-*-linux_x86_64.whl' http://${URL}

# We use container 3 to test with pip
if [ "$CIRCLE_NODE_INDEX" = "0" ]; then
    conda remove -q qt pyqt
    pip install ./${URL}/PySide2-*-cp27-cp27mu-linux_x86_64.whl
elif [ "$CIRCLE_NODE_INDEX" = "3" ]; then
    pip uninstall -q -y pyqt5 sip
    pip install ./${URL}/PySide2-*-cp36-cp36m-linux_x86_64.whl
else
    exit 0
fi

python qtpy/tests/runtests.py

# Force quitting if exit status of runtests.py was not 0
if [ $? -ne 0 ]; then
    exit 1
fi

pip uninstall -y -q pyside2
