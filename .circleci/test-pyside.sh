#!/bin/bash

source $HOME/miniconda/etc/profile.d/conda.sh
conda activate test

if [ "$USE_CONDA" = "No" ]; then
    exit 0
else
    conda remove -q qt pyqt
    conda install -q -c conda-forge qt=4.* pyside
fi

python qtpy/tests/runtests.py

# Force quitting if exit status of runtests.py was not 0
if [ $? -ne 0 ]; then
    exit 1
fi
