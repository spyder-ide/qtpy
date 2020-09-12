from __future__ import absolute_import

import subprocess
import sys

import pytest

import qtpy


subcommands = [
    ['mypy'],
    ['mypy', 'args'],
]


@pytest.mark.parametrize(
    argnames=['subcommand'],
    argvalues=[[subcommand] for subcommand in subcommands],
    ids=[' '.join(subcommand) for subcommand in subcommands],
)
def test_cli_help_does_not_fail(subcommand):
    # .check_call() over .run(..., check=True) because of py2
    subprocess.check_call(
        [sys.executable, '-m', 'qtpy', *subcommand, '--help'],
    )


def test_cli_mypy_args():
    output = subprocess.check_output(
        [sys.executable, '-m', 'qtpy', 'mypy', 'args'],
    )

    if qtpy.PYQT4:
        expected = b'--always-true=PYQT4 --always-false=PYQT5 --always-false=PYSIDE --always-false=PYSIDE2\n'
    elif qtpy.PYQT5:
        expected = b'--always-false=PYQT4 --always-true=PYQT5 --always-false=PYSIDE --always-false=PYSIDE2\n'
    elif qtpy.PYSIDE:
        expected = b'--always-false=PYQT4 --always-false=PYQT5 --always-true=PYSIDE --always-false=PYSIDE2\n'
    elif qtpy.PYSIDE2:
        expected = b'--always-false=PYQT4 --always-false=PYQT5 --always-false=PYSIDE --always-true=PYSIDE2\n'
    else:
        assert False, 'No valid API to test'

    assert output == expected
