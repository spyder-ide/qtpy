#!/bin/bash -ex

# Create conda environment for this test
conda create -n test-pyside
conda activate test-pyside

if [ "$USE_CONDA" = "No" ]; then
    exit 0
else
    if [ "$PYTHON_VERSION" = "3.6" ]; then
        exit 0
    elif [ "$PYTHON_VERSION" = "3.5" ]; then
        exit 0
    else
        conda install coveralls mock pytest pytest-cov python="$PYTHON_VERSION" -c anaconda -q
        conda install qt=4.* pyside -c anaconda -q
    fi
fi

# Install package
python setup.py develop

# Run tests
python qtpy/tests/runtests.py
