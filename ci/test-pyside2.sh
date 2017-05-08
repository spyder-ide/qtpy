#!/bin/bash

export PATH="$HOME/miniconda/bin:$PATH"
source activate test

# Download PySide2 wheel
wget -q https://bintray.com/fredrikaverpil/pyside2-wheels/download_file?file_path=ubuntu14.04%2FPySide2-2.0.0.dev0-cp27-none-linux_x86_64.whl -O PySide2-2.0.0.dev0-cp27-none-linux_x86_64.whl

# We only use container 0 for PySide2
if [ "$CIRCLE_NODE_INDEX" = "0" ]; then
    conda remove -q qt pyqt
    pip install PySide2-2.0.0.dev0-cp27-none-linux_x86_64.whl
else
    exit 0
fi

# Make symlinks for Qt libraries (else imports fail)
pushd "$HOME/miniconda/envs/test/lib/python2.7/site-packages/PySide2/"

for file in `ls Qt*x86_64-linux-gnu.so`
do
    symlink=${file%.x86_64-linux-gnu.so}.so
    ln -s $file $symlink
done

popd

python qtpy/tests/runtests.py

# Force quitting if exit status of runtests.py was not 0
if [ $? -ne 0 ]; then
    exit 1
fi
