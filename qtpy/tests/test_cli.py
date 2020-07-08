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

    if qtpy.PYQT5:
        expected = b'--always-true=PYQT5 --always-false=PYQT6 --always-false=PYSIDE2 --always-false=PYSIDE6\n'
    elif qtpy.PYQT6:
        expected = b'--always-false=PYQT5 --always-true=PYQT6 --always-false=PYSIDE2 --always-false=PYSIDE6\n'
    elif qtpy.PYSIDE2:
        expected = b'--always-false=PYQT5 --always-false=PYQT6 --always-true=PYSIDE2 --always-false=PYSIDE6\n'
    elif qtpy.PYSIDE6:
        expected = b'--always-false=PYQT5 --always-false=PYQT6 --always-false=PYSIDE2 --always-true=PYSIDE6\n'
    else:
        assert False, 'No valid API to test'

    assert output == expected
