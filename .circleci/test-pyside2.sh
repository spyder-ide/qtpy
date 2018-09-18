#!/bin/bash

source $HOME/miniconda/etc/profile.d/conda.sh
conda activate test

if [ "$USE_CONDA" = "Yes" ]; then
    # There are no conda packages for PySide2
    exit 0
else
    pip uninstall -q -y pyqt5 sip
    pip install -q pyside2
fi

python qtpy/tests/runtests.py

# Force quitting if exit status of runtests.py was not 0
if [ $? -ne 0 ]; then
    exit 1
fi

pip uninstall -y -q pyside2
