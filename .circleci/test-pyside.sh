#!/bin/bash -ex

source $HOME/miniconda/etc/profile.d/conda.sh
conda activate test

if [ "$USE_CONDA" = "No" ]; then
    exit 0
else
    conda remove -q qt pyqt
    conda install -q -c conda-forge qt=4.* pyside
fi

python qtpy/tests/runtests.py
