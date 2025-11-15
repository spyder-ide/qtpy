import pytest

from qtpy import PYQT5, PYQT_VERSION, PYSIDE2
from qtpy.tests.utils import pytest_importorskip


@pytest.mark.skipif(PYSIDE2, reason="QtDesigner is not available in PySide2")
def test_qtdesigner():
    """Test the qtpy.QtDesigner namespace."""
    QtDesigner = pytest_importorskip("qtpy.QtDesigner")

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


@pytest.mark.skipif(
    PYQT5 and PYQT_VERSION.startswith("5.9"),
    reason=(
        "A specific setup with at least sip 4.9.9 is needed for PyQt5 5.9.* "
        "to work with scoped enum access"
    ),
)
def test_enum_access():
    """Test scoped and unscoped enum access."""
    QtDesigner = pytest_importorskip("qtpy.QtDesigner")

    assert (
        QtDesigner.QDesignerFormWindowInterface.EditFeature
        == QtDesigner.QDesignerFormWindowInterface.FeatureFlag.EditFeature
    )
