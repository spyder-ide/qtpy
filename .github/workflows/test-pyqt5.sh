#!/bin/bash -ex

# Create conda environment for this test
conda create -n test-pyqt5
conda activate test-pyqt5

# Select build with QtMultimedia
if [ "$(uname)" == "Darwin" ]; then

    if [ "$PYTHON_VERSION" = "3.6" ]; then
        export QT_VER=5.12
    else
        export QT_VER=5.*
    fi

elif [ "$(expr substr $(uname -s) 1 5)" == "Linux" ]; then

    if [ "$PYTHON_VERSION" = "3.6" ]; then
        export QT_VER=5.12
    else
        export QT_VER=5.*
    fi

else

    if [ "$PYTHON_VERSION" = "3.6" ]; then
        export QT_VER=5.9
    else
        export QT_VER=5.*
    fi

fi

if [ "$USE_CONDA" = "Yes" ]; then
    conda install -q coveralls pytest pytest-cov python="$PYTHON_VERSION" -c conda-forge
    conda install -q qt=$QT_VER pyqt=$QT_VER -c conda-forge
else
    # We are getting segfaults in 5.10
    conda install -q coveralls pytest pytest-cov python="$PYTHON_VERSION" -c anaconda
    pip install -q pyqt5 PyQtWebEngine
fi

# Install package
python -m pip install -e .

# Run tests
python qtpy/tests/runtests.py
