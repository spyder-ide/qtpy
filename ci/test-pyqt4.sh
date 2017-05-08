#!/bin/bash

export PATH="$HOME/miniconda/bin:$PATH"
source activate test

# We use container 3 to test with pip and pyqt5
if [ "$CIRCLE_NODE_INDEX" = "3" ]; then
    exit 0
else
    conda remove -q qt pyqt
    conda install -q -c conda-forge qt=4.* pyqt=4.*
fi

python qtpy/tests/runtests.py

# Force quitting if exit status of runtests.py was not 0
if [ $? -ne 0 ]; then
    exit 1
fi
