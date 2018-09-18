#!/bin/bash

export TRAVIS_OS_NAME="linux"
export CONDA_DEPENDENCIES_FLAGS="--quiet"
export CONDA_DEPENDENCIES="pytest pytest-cov mock"
export PIP_DEPENDENCIES="coveralls"

# Download and install miniconda and conda/pip dependencies
# with astropy helpers
echo -e "PYTHON = $PYTHON_VERSION \n============"
git clone git://github.com/astropy/ci-helpers.git > /dev/null
source ci-helpers/travis/setup_conda_$TRAVIS_OS_NAME.sh

# Activate conda
source $HOME/miniconda/etc/profile.d/conda.sh
conda activate test

# Install the package in develop mode
pip install -e .
