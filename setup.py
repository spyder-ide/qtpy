#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Setup script for qtpy
"""

import os
import io

from setuptools import setup, find_packages

HERE = os.path.abspath(os.path.dirname(__file__))

version_ns = {}
with open(os.path.join(HERE, 'qtpy', '_version.py')) as f:
    exec(f.read(), {}, version_ns)

with io.open(os.path.join(HERE, 'README.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

setup(
    name='QtPy',
    version=version_ns['__version__'],
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    keywords=["qt PyQt4 PyQt5 PySide"],
    url='https://github.com/spyder-ide/qtpy',
    license='MIT',
    author='Colin Duquesnoy, The Spyder Development Team',
    author_email='goanpeca@gmail.com',
    maintainer='Gonzalo Peña-Castellanos',
    maintainer_email='goanpeca@gmail.com',
    description='Provides an abstraction layer on top of the various Qt '
                'bindings (PyQt5, PyQt4 and PySide) and additional custom '
                'QWidgets.',
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: X11 Applications :: Qt',
        'Environment :: Win32 (MS Windows)',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5'],
    entry_points={'console_scripts': 'qtpy = qtpy.__main__:main [cli]'},
    include_package_data=True
)
