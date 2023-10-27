# coding=utf-8
import importlib
from types import ModuleType

import pytest

from qtpy import API_NAME


def test_sip():
    """Test the qtpy.sip namespace"""
    sip = pytest.importorskip("qtpy.sip")

    assert sip.assign is not None
    assert sip.cast is not None
    assert sip.delete is not None
    assert sip.dump is not None
    assert sip.enableautoconversion is not None
    assert sip.isdeleted is not None
    assert sip.ispycreated is not None
    assert sip.ispyowned is not None
    assert sip.setdeleted is not None
    assert sip.settracemask is not None
    assert sip.simplewrapper is not None
    assert sip.transferback is not None
    assert sip.transferto is not None
    assert sip.unwrapinstance is not None
    assert sip.voidptr is not None
    assert sip.wrapinstance is not None
    assert sip.wrapper is not None
    assert sip.wrappertype is not None


def test_namespace_not_polluted():
    """Test that no extra members are exported into the module namespace."""
    qtpy_module: ModuleType = pytest.importorskip("qtpy.sip")
    original_module: ModuleType = importlib.import_module(
        qtpy_module.__name__.replace('qtpy', API_NAME)
    )

    extra_members = (
        frozenset(dir(qtpy_module))
        - frozenset(dir(original_module))
        - frozenset(
            # These are unavoidable:
            [
                "__builtins__",
                "__cached__",
            ]
        )
    )
    assert not extra_members
