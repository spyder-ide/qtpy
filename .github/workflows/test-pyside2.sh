#!/bin/bash -ex

# Create conda environment for this test
conda create -n test-pyside2
conda activate test-pyside2

if [ "$USE_CONDA" = "Yes" ]; then
    # There are no conda packages for PySide2
    exit 0
else
    # Simple solution to avoid failures with the
    # Qt3D modules
    conda install coveralls mock pytest pytest-cov python="$PYTHON_VERSION" -c conda-forge -q
    pip install -q pyside2==5.12.3
fi

# Install package
python setup.py develop

# Run tests
python qtpy/tests/runtests.py
