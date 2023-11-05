import importlib
from typing import TYPE_CHECKING

import pytest

from qtpy import API_NAME, PYQT6, PYSIDE6

if TYPE_CHECKING:
    from types import ModuleType


@pytest.mark.skipif(PYQT6, reason="Not complete in PyQt6")
@pytest.mark.skipif(PYSIDE6, reason="Not complete in PySide6")
def test_qt3dcore():
    """Test the qtpy.Qt3DCore namespace"""
    Qt3DCore = pytest.importorskip("qtpy.Qt3DCore")

    assert Qt3DCore.QPropertyValueAddedChange is not None
    assert Qt3DCore.QSkeletonLoader is not None
    assert Qt3DCore.QPropertyNodeRemovedChange is not None
    assert Qt3DCore.QPropertyUpdatedChange is not None
    assert Qt3DCore.QAspectEngine is not None
    assert Qt3DCore.QPropertyValueAddedChangeBase is not None
    assert Qt3DCore.QStaticPropertyValueRemovedChangeBase is not None
    assert Qt3DCore.QPropertyNodeAddedChange is not None
    assert Qt3DCore.QDynamicPropertyUpdatedChange is not None
    assert Qt3DCore.QStaticPropertyUpdatedChangeBase is not None
    assert Qt3DCore.ChangeFlags is not None
    assert Qt3DCore.QAbstractAspect is not None
    assert Qt3DCore.QBackendNode is not None
    assert Qt3DCore.QTransform is not None
    assert Qt3DCore.QPropertyUpdatedChangeBase is not None
    assert Qt3DCore.QNodeId is not None
    assert Qt3DCore.QJoint is not None
    assert Qt3DCore.QSceneChange is not None
    assert Qt3DCore.QNodeIdTypePair is not None
    assert Qt3DCore.QAbstractSkeleton is not None
    assert Qt3DCore.QComponentRemovedChange is not None
    assert Qt3DCore.QComponent is not None
    assert Qt3DCore.QEntity is not None
    assert Qt3DCore.QNodeCommand is not None
    assert Qt3DCore.QNode is not None
    assert Qt3DCore.QPropertyValueRemovedChange is not None
    assert Qt3DCore.QPropertyValueRemovedChangeBase is not None
    assert Qt3DCore.QComponentAddedChange is not None
    assert Qt3DCore.QNodeCreatedChangeBase is not None
    assert Qt3DCore.QNodeDestroyedChange is not None
    assert Qt3DCore.QArmature is not None
    assert Qt3DCore.QStaticPropertyValueAddedChangeBase is not None
    assert Qt3DCore.ChangeFlag is not None
    assert Qt3DCore.QSkeleton is not None


@pytest.mark.skipif(PYQT6, reason="Not complete in PyQt6")
@pytest.mark.skipif(PYSIDE6, reason="Not complete in PySide6")
def test_namespace_not_polluted():
    """Test that no extra members are exported into the module namespace."""
    qtpy_module: ModuleType = pytest.importorskip("qtpy.Qt3DCore")
    original_module: ModuleType = importlib.import_module(
        qtpy_module.__name__.replace("qtpy", API_NAME),
    )

    extra_members = (
        frozenset(object.__dir__(qtpy_module))
        - frozenset(object.__dir__(original_module))
        - frozenset(
            # These are unavoidable:
            [
                "__builtins__",
                "__cached__",
            ],
        )
        - frozenset(
            # These don't show up in `dir()` when on PySide:
            {
                "AllChanges",
                "CallbackTriggered",
                "ChangeFlag",
                "ChangeFlags",
                "CommandRequested",
                "ComponentAdded",
                "ComponentRemoved",
                "NodeCreated",
                "NodeDeleted",
                "PropertyUpdated",
                "PropertyValueAdded",
                "PropertyValueRemoved",
                "QAbstractAspect",
                "QAbstractSkeleton",
                "QArmature",
                "QAspectEngine",
                "QAspectJob",
                "QBackendNode",
                "QComponent",
                "QComponentAddedChange",
                "QComponentRemovedChange",
                "QDynamicPropertyUpdatedChange",
                "QEntity",
                "QJoint",
                "QNode",
                "QNodeCommand",
                "QNodeCreatedChangeBase",
                "QNodeDestroyedChange",
                "QNodeId",
                "QNodeIdTypePair",
                "QPropertyNodeAddedChange",
                "QPropertyNodeRemovedChange",
                "QPropertyUpdatedChange",
                "QPropertyUpdatedChangeBase",
                "QPropertyValueAddedChange",
                "QPropertyValueAddedChangeBase",
                "QPropertyValueRemovedChange",
                "QPropertyValueRemovedChangeBase",
                "QSceneChange",
                "QSkeleton",
                "QSkeletonLoader",
                "QStaticPropertyUpdatedChangeBase",
                "QStaticPropertyValueAddedChangeBase",
                "QStaticPropertyValueRemovedChangeBase",
                "QTransform",
                "__annotations__",
                "__dict__",
                "__module__",
                "qHash",
                "qIdForNode",
            },
        )
    )
    assert not extra_members
