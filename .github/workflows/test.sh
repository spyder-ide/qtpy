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
        conda install -q qt=${PYQT5_QT_VERSION:-"5.12"} pyqt=${PYQT5_VERSION:-"5"}
    elif [ "${1}" = "pyside2" ]; then
        conda install -q qt=${PYSIDE2_QT_VERSION:-"5.12"} pyside2=${PYSIDE2_VERSION:-"5"}
    else
        exit 1
    fi

else

    if [ "${1}" = "pyqt5" ]; then
        pip install pyqt5==${PYQT5_VERSION:-"5.15"}.* PyQtWebEngine==${PYQT5_VERSION:-"5.15"}.*
    elif [ "${1}" = "pyqt6" ]; then
        pip install pyqt6==${PYQT6_VERSION:-"6.2"}.* PyQt6-WebEngine==${PYQT6_VERSION:-"6.2"}.*
    elif [ "${1}" = "pyside2" ]; then
        pip install pyside2==${PYSIDE2_VERSION:-"5.12"}.*
    elif [ "${1}" = "pyside6" ]; then
        pip install pyside6==${PYSIDE6_VERSION:-"6.2"}.*
    else
        exit 1
    fi

fi

# Build wheel of package
git clean -xdf
python -bb -X dev setup.py sdist bdist_wheel  # Needs migration to modern PEP 517-based build backend

# Install package from build wheel
echo dist/*.whl | xargs -I % python -bb -X dev -W error -m pip install --upgrade %

# Print environment information
conda list

# Run tests
cd qtpy  # Hack to work around non-src layout pulling in local instead of installed package for cov
python -I -bb -X dev -W error -m pytest --cov-config ../.coveragerc
