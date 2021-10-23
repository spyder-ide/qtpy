#!/bin/bash -ex

# Activate conda properly
eval "$(conda shell.bash hook)"

# Set conda channel
if [ "$USE_CONDA" = "No" ]; then
    CONDA_CHANNEL_ARG="-c anaconda"
fi

# Create and activate conda environment for this test
conda create -q -n test-${1} ${CONDA_CHANNEL_ARG} python=${PYTHON_VERSION} pytest pytest-cov
conda activate test-${1}

if [ "$USE_CONDA" = "Yes" ]; then

    if [ "${1}" = "pyqt5" ]; then
        conda install -q pyqt=${PYQT5_VERSION:-"5.12"}
    else
        exit 1
    fi

else

    if [ "${1}" = "pyqt5" ]; then
        pip install pyqt5==${PYQT5_VERSION:-"5.15"}.* PyQtWebEngine==${PYQT5_VERSION:-"5.15"}.*
    elif [ "${1}" = "pyside2" ]; then
        pip install pyside2==${PYSIDE2_VERSION:-"5.12"}.*
    elif [ "${1}" = "pyside6" ]; then
        pip install pyside6==${PYSIDE6_VERSION:-"6.2"}.*
    else
        exit 1
    fi

fi

# Install package
python -bb -X dev -W error -m pip install -e .

# Print environment information
conda list

# Run tests
python -I -bb -X dev -W error -m pytest qtpy

# Deactivate conda env after
conda deactivate
