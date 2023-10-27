# coding=utf-8
import importlib
from types import ModuleType

import pytest

from qtpy import API_NAME, PYSIDE2


@pytest.mark.skipif(PYSIDE2, reason="QtDesigner is not available in PySide2")
def test_qtdesigner():
    """Test the qtpy.QtDesigner namespace."""
    QtDesigner = pytest.importorskip("qtpy.QtDesigner")

    assert QtDesigner.QAbstractExtensionFactory is not None
    assert QtDesigner.QAbstractExtensionManager is not None
    assert QtDesigner.QDesignerActionEditorInterface is not None
    assert QtDesigner.QDesignerContainerExtension is not None
    assert QtDesigner.QDesignerCustomWidgetCollectionInterface is not None
    assert QtDesigner.QDesignerCustomWidgetInterface is not None
    assert QtDesigner.QDesignerFormEditorInterface is not None
    assert QtDesigner.QDesignerFormWindowCursorInterface is not None
    assert QtDesigner.QDesignerFormWindowInterface is not None
    assert QtDesigner.QDesignerFormWindowManagerInterface is not None
    assert QtDesigner.QDesignerMemberSheetExtension is not None
    assert QtDesigner.QDesignerObjectInspectorInterface is not None
    assert QtDesigner.QDesignerPropertyEditorInterface is not None
    assert QtDesigner.QDesignerPropertySheetExtension is not None
    assert QtDesigner.QDesignerTaskMenuExtension is not None
    assert QtDesigner.QDesignerWidgetBoxInterface is not None
    assert QtDesigner.QExtensionFactory is not None
    assert QtDesigner.QExtensionManager is not None
    assert QtDesigner.QFormBuilder is not None


@pytest.mark.skipif(PYSIDE2, reason="QtDesigner is not available in PySide2")
def test_namespace_not_polluted():
    """Test that no extra members are exported into the module namespace."""
    qtpy_module: ModuleType = pytest.importorskip("qtpy.QtDesigner")
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
