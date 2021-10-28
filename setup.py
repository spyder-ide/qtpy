#!/usr/bin/env python

"""
Setup script for qtpy
"""

import os

from setuptools import setup, find_packages

HERE = os.path.abspath(os.path.dirname(__file__))

version_ns = {}
with open(os.path.join(HERE, 'qtpy', '_version.py')) as f:
    exec(f.read(), {}, version_ns)

with open(os.path.join(HERE, 'README.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

setup(
    name='QtPy',
    version=version_ns['__version__'],
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    python_requires='>=3.6',
    install_requires=['packaging'],
    keywords=["qt PyQt5 PyQt6 PySide2 PySide6"],
    url='https://github.com/spyder-ide/qtpy',
    license='MIT',
    author='Colin Duquesnoy and the Spyder Development Team',
    author_email='spyder.python@gmail.com',
    maintainer='Spyder Development Team and QtPy Contributors',
    maintainer_email='spyder.python@gmail.com',
    description='Provides an abstraction layer on top of the various Qt '
                'bindings (PyQt5/6 and PySide2/6) and additional custom '
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
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        ]
)
