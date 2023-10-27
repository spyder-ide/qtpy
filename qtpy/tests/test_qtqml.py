# coding=utf-8
import importlib
from types import ModuleType

from qtpy import API_NAME, PYSIDE2, PYSIDE6, QtQml


def test_qtqml():
    """Test the qtpy.QtQml namespace"""
    assert QtQml.QJSEngine is not None
    assert QtQml.QJSValue is not None
    assert QtQml.QJSValueIterator is not None
    assert QtQml.QQmlAbstractUrlInterceptor is not None
    assert QtQml.QQmlApplicationEngine is not None
    assert QtQml.QQmlComponent is not None
    assert QtQml.QQmlContext is not None
    assert QtQml.QQmlEngine is not None
    assert QtQml.QQmlImageProviderBase is not None
    assert QtQml.QQmlError is not None
    assert QtQml.QQmlExpression is not None
    assert QtQml.QQmlExtensionPlugin is not None
    assert QtQml.QQmlFileSelector is not None
    assert QtQml.QQmlIncubationController is not None
    assert QtQml.QQmlIncubator is not None
    if not (PYSIDE2 or PYSIDE6):
        # https://wiki.qt.io/Qt_for_Python_Missing_Bindings#QtQml
        assert QtQml.QQmlListProperty is not None
    assert QtQml.QQmlListReference is not None
    assert QtQml.QQmlNetworkAccessManagerFactory is not None
    assert QtQml.QQmlParserStatus is not None
    assert QtQml.QQmlProperty is not None
    assert QtQml.QQmlPropertyValueSource is not None
    assert QtQml.QQmlScriptString is not None
    assert QtQml.QQmlPropertyMap is not None


def test_namespace_not_polluted():
    """Test that no extra members are exported into the module namespace."""
    qtpy_module: ModuleType = QtQml
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
