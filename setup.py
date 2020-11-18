#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Setup script for qtpy
"""

import os

from setuptools import setup

HERE = os.path.abspath(os.path.dirname(__file__))

version_ns = {}
with open(os.path.join(HERE, 'qtpy', '_version.py')) as f:
    exec(f.read(), {}, version_ns)

setup(version=version_ns['__version__'])
