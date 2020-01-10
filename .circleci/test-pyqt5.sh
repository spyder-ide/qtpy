#!/bin/bash -ex

source $HOME/miniconda/etc/profile.d/conda.sh
conda activate test

# Select build with QtMultimedia
if [ "$PYTHON_VERSION" = "2.7" ]; then
    export BUILD=py27h22d08a2_0
elif [ "$PYTHON_VERSION" = "3.5" ]; then
    export BUILD=py35h751905a_0
elif [ "$PYTHON_VERSION" = "3.6" ]; then	
    export BUILD=py36h751905a_0
elif [ "$PYTHON_VERSION" = "3.7" ]; then    
    export BUILD=py37h22d08a2_1
elif [ "$PYTHON_VERSION" = "3.8" ]; then    
    export BUILD=py38h05f1152_4
fi

if [ "$USE_CONDA" = "Yes" ]; then
    conda install -q qt=5.* pyqt=5.9.2=$BUILD
    conda install -q sip=4.19.8
else
    if [ "$PYTHON_VERSION" = "2.7" ]; then
        # There are no pyqt5 wheels for Python 2
        exit 0
    else
        # We are getting segfaults in 5.10
        pip install -q pyqt5==5.9.2
    fi
fi

python qtpy/tests/runtests.py
