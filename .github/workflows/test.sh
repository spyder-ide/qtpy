#!/bin/bash -ex

# Activate conda properly
eval "$(conda shell.bash hook)"

# Remove any existing env
conda remove -q -n test-env --all || true

# Create and activate conda environment for this test
BINDING=$(echo "$1" | tr '[:lower:]' '[:upper:]')
QT_VERSION_VAR=${BINDING}_QT_VERSION

# pytest-qt >=4 doesn't support Qt <=5.9
if [ "${!QT_VERSION_VAR:0:3}" = "5.9" ]; then
    PYTESTQT_VERSION="=3.3.0"
    PYTEST_VERSION=">=6,!=7.0.0,!=7.0.1,<7.2.0"
fi

conda create -q -n test-env python=${PYTHON_VERSION} pytest${PYTEST_VERSION:-">=6,!=7.0.0,!=7.0.1"} "pytest-cov>=3.0.0" pytest-qt${PYTESTQT_VERSION:-}
conda activate test-env

if [ "$USE_CONDA" = "Yes" ]; then

    if [ "${1}" = "pyqt5" ]; then
        conda install -q qt=${PYQT5_QT_VERSION} pyqt=${PYQT5_VERSION}
    elif [ "${1}" = "pyside2" ]; then
        conda install -q qt=${PYSIDE2_QT_VERSION} pyside2=${PYSIDE2_VERSION}
    elif [ "${1}" = "pyside6" ]; then
        conda install -q qt6-main=${PYSIDE6_QT_VERSION} pyside6=${PYSIDE6_VERSION}
    else
        exit 1
    fi

else

    if [ "${1}" = "pyqt5" ]; then
        pip install pyqt5==${PYQT5_VERSION}.* PyQtWebEngine==${PYQT5_VERSION}.* QScintilla==${QSCINTILLA_VERSION}.*
    elif [ "${1}" = "pyqt6" ]; then
        pip install pyqt6==${PYQT6_VERSION}.* PyQt6-WebEngine==${PYQT6_VERSION}.* PyQt6-Qt6==${PYQT6_QT_VERSION}.* PyQt6-QScintilla==${QSCINTILLA_VERSION}.*
    elif [ "${1}" = "pyside2" ]; then
        pip install pyside2==${PYSIDE2_VERSION}.*
    elif [ "${1}" = "pyside6" ]; then
        if [ "${PYSIDE6_VERSION:0:3}" = "6.2" ]; then
            pip install pyside6==${PYSIDE6_VERSION}.*
        else
            pip install pyside6==${PYSIDE6_VERSION}.* pyside6-addons==${PYSIDE6_VERSION}.* pyside6-essentials==${PYSIDE6_VERSION}.*
        fi
    else
        exit 1
    fi

fi

# Build wheel of package
git clean -xdf -e *.coverage
python -m pip install --upgrade build
python -bb -X dev -W error -m build

# Install package from built wheel
echo dist/*.whl | xargs -I % python -bb -X dev -W error -W "ignore::DeprecationWarning:pip._internal.locations._distutils" -W "ignore::DeprecationWarning:distutils.command.install" -m pip install --upgrade %

# Print environment information
conda list

# Run tests
mkdir -p temp_test_dir
pushd temp_test_dir # Hack to work around non-src layout pulling in local instead of installed package for cov
python -I -bb -X dev -W error -m pytest ../qtpy --cov-config ../.coveragerc --cov-append

# Save QtPy base dir for coverage
python -c "from pathlib import Path; import qtpy; print(Path(qtpy.__file__).parent.parent.resolve().as_posix())" > qtpy_basedir.txt
cat qtpy_basedir.txt
popd

# Check package and environment
pipx run twine check --strict dist/*
pip check -v || ${SKIP_PIP_CHECK:-false}
