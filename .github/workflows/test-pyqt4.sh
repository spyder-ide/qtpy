#!/bin/bash -ex

eval "$(conda shell.bash hook)"

# Create conda environment for this test
conda create -n test-pyqt4
conda activate test-pyqt4

if [ "$USE_CONDA" = "No" ]; then
    exit 0
elif [ "$PYTHON_VERSION" = "3.6" ]; then
    exit 0
else
    conda install coveralls mock pytest pytest-cov python="$PYTHON_VERSION" -c anaconda -q
    conda install qt=4.* pyqt=4.* -c anaconda -q
fi

# Install package
python setup.py develop

# Run tests
python qtpy/tests/runtests.py
