#!/bin/bash -ex

# Create conda environment for this test
conda create -n test-pyqt5
conda activate test-pyqt5

# Select build with QtMultimedia
if [ "$(uname)" == "Darwin" ]; then

    if [ "$PYTHON_VERSION" = "2.7" ]; then
        export PYQT_VER=5.9.2=py27h655552a_0
    elif [ "$PYTHON_VERSION" = "3.6" ]; then
        export PYQT_VER=5.9.2=py36h11d3b92_0
    else
        export PYQT_VER=5.*
    fi

elif [ "$(expr substr $(uname -s) 1 5)" == "Linux" ]; then

    if [ "$PYTHON_VERSION" = "2.7" ]; then
        export PYQT_VER=5.9.2=py27h22d08a2_0
    elif [ "$PYTHON_VERSION" = "3.6" ]; then
        export PYQT_VER=5.9.2=py36h751905a_0
    else
        export PYQT_VER=5.*
    fi

else

    if [ "$PYTHON_VERSION" = "2.7" ]; then
        exit 0
    elif [ "$PYTHON_VERSION" = "3.6" ]; then
        export PYQT_VER=5.9.2=py36h1aa27d4_0
    else
        export PYQT_VER=5.*
    fi

fi

if [ "$USE_CONDA" = "Yes" ]; then
    conda install coveralls mock pytest pytest-cov python="$PYTHON_VERSION" -c anaconda -q
    conda install -q qt=5.* pyqt=$PYQT_VER -c anaconda -q
    # conda install -q sip=4.19.8 -c anaconda -q
else
    if [ "$PYTHON_VERSION" = "2.7" ]; then
        # There are no pyqt5 wheels for Python 2
        exit 0
    else
        # We are getting segfaults in 5.10
        conda install coveralls mock pytest pytest-cov python="$PYTHON_VERSION" -c anaconda -q
        pip install -q pyqt5
    fi
fi

# Install package
python setup.py develop

# Run tests
python qtpy/tests/runtests.py
