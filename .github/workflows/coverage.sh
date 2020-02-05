#!/bin/bash

eval "$(conda shell.bash hook)"
conda deactivate
conda activate test-pyqt5

export COVERALLS_REPO_TOKEN="xh75EzxFFMoTEyNPo3wXxXv8OVkul3eE5"
coveralls

# Don't fail at this step
exit 0
