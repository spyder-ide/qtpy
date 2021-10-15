#!/bin/bash -ex

# Create conda environment for this test
conda create -n test-pyside6
conda activate test-pyside6

if [ "$USE_CONDA" = "Yes" ]; then
    # There are no conda packages for PySide6
    exit 0
else
    # Simple solution to avoid failures with the Qt3D modules
    conda install -q coveralls pytest pytest-cov python="$PYTHON_VERSION" -c conda-forge
    pip install -q pyside6==6.2.0
fi

# Install package
python -m pip install -e .

# Run tests
python qtpy/tests/runtests.py
