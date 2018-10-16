#!/bin/bash

export COVERALLS_REPO_TOKEN="xh75EzxFFMoTEyNPo3wXxXv8OVkul3eE5"
export PATH="$HOME/miniconda/bin:$PATH"
source activate test

coveralls

# Don't fail at this step
exit 0
