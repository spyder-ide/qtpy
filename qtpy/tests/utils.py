"""Utility functions for tests."""

import os

import pytest

from qtpy import _parse_version


def using_conda():
    return os.environ.get("USE_CONDA", "Yes") == "Yes"


def not_using_conda():
    return os.environ.get("USE_CONDA", "No") == "No"


def pytest_importorskip(module, **kwargs):
    """
    Skip the test if the module cannot be imported.

    This is a wrapper around `pytest.importorskip` to support using it with
    Python 3.7+. The `exc_type` argument was added in `pytest` 8.2.0.
    See spyder-ide/qtpy#485
    """
    if _parse_version(pytest.__version__) < _parse_version("8.2.0"):
        return pytest.importorskip(module, **kwargs)
    return pytest.importorskip(module, **kwargs, exc_type=ImportError)
