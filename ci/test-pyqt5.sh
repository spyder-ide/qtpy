#!/bin/bash

export PATH="$HOME/miniconda/bin:$PATH"
source activate test

# We use container 3 to test with pip
if [ "$CIRCLE_NODE_INDEX" != "3" ]; then
    conda install -q qt=5.* pyqt=5.*
else
    pip install -q pyqt5
fi

python qtpy/tests/runtests.py

# Force quitting if exit status of runtests.py was not 0
if [ $? -ne 0 ]; then
    exit 1
fi
