#!/bin/bash -ex

source $HOME/miniconda/etc/profile.d/conda.sh
conda activate test

if [ "$USE_CONDA" = "Yes" ]; then
    # There are no conda packages for PySide2
    exit 0
else
    pip uninstall -q -y pyqt5 sip
    # Simple solution to avoid failures with the
    # Qt3D modules
    pip install -q pyside2==5.12.3
fi

python qtpy/tests/runtests.py

pip uninstall -y -q pyside2
