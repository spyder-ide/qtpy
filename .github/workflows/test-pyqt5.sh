#!/bin/bash -ex

# Create conda environment for this test
conda create -n test-pyqt5
conda activate test-pyqt5

# Select build with QtMultimedia
if [ "$(uname)" == "Darwin" ]; then

    if [ "$PYTHON_VERSION" = "2.7" ]; then
        export QT_VER=5.9
    elif [ "$PYTHON_VERSION" = "3.6" ]; then
        export QT_VER=5.12
    else
        export QT_VER=5.*
    fi

elif [ "$(expr substr $(uname -s) 1 5)" == "Linux" ]; then

    if [ "$PYTHON_VERSION" = "2.7" ]; then
        export QT_VER=5.9
    elif [ "$PYTHON_VERSION" = "3.6" ]; then
        export QT_VER=5.12
    else
        export QT_VER=5.*
    fi

else

    if [ "$PYTHON_VERSION" = "2.7" ]; then
        exit 0
    elif [ "$PYTHON_VERSION" = "3.6" ]; then
        export QT_VER=5.9
    else
        export QT_VER=5.*
    fi

fi

if [ "$USE_CONDA" = "Yes" ]; then
    conda install coveralls mock pytest pytest-cov python="$PYTHON_VERSION" -c conda-forge -q
    conda install -q qt=$QT_VER pyqt=$QT_VER -c conda-forge -q
else
    if [ "$PYTHON_VERSION" = "2.7" ]; then
        # There are no pyqt5 wheels for Python 2
        exit 0
    else
        # We are getting segfaults in 5.10
        conda install coveralls mock pytest pytest-cov python="$PYTHON_VERSION" -c anaconda -q
        pip install -q pyqt5 PyQtWebEngine
    fi
fi

# Install package
python -m pip install -e .

# Run tests
python qtpy/tests/runtests.py
