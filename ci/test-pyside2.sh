#!/bin/bash

export PATH="$HOME/miniconda/bin:$PATH"
source activate test

# We use container 3 to test with pip
if [ "$CIRCLE_NODE_INDEX" = "0" ]; then
    conda remove -q qt pyqt
    conda install -q -c conda-forge pyside2
elif [ "$CIRCLE_NODE_INDEX" = "3" ]; then
    pip uninstall -q -y pyqt5 sip
    conda install -q -c conda-forge pyside2
else
    exit 0
fi

python qtpy/tests/runtests.py

# Force quitting if exit status of runtests.py was not 0
if [ $? -ne 0 ]; then
    exit 1
fi

pip uninstall -y -q pyside2
