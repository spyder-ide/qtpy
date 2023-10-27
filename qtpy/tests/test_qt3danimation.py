import importlib
from typing import TYPE_CHECKING

import pytest

from qtpy import API_NAME

if TYPE_CHECKING:
    from types import ModuleType


def test_qt3danimation():
    """Test the qtpy.Qt3DAnimation namespace"""
    Qt3DAnimation = pytest.importorskip("qtpy.Qt3DAnimation")

    assert Qt3DAnimation.QAnimationController is not None
    assert Qt3DAnimation.QAdditiveClipBlend is not None
    assert Qt3DAnimation.QAbstractClipBlendNode is not None
    assert Qt3DAnimation.QAbstractAnimation is not None
    assert Qt3DAnimation.QKeyframeAnimation is not None
    assert Qt3DAnimation.QAbstractAnimationClip is not None
    assert Qt3DAnimation.QAbstractClipAnimator is not None
    assert Qt3DAnimation.QClipAnimator is not None
    assert Qt3DAnimation.QAnimationGroup is not None
    assert Qt3DAnimation.QLerpClipBlend is not None
    assert Qt3DAnimation.QMorphingAnimation is not None
    assert Qt3DAnimation.QAnimationAspect is not None
    assert Qt3DAnimation.QVertexBlendAnimation is not None
    assert Qt3DAnimation.QBlendedClipAnimator is not None
    assert Qt3DAnimation.QMorphTarget is not None


def test_namespace_not_polluted():
    """Test that no extra members are exported into the module namespace."""
    qtpy_module: ModuleType = pytest.importorskip("qtpy.Qt3DAnimation")
    original_module: ModuleType = importlib.import_module(
        qtpy_module.__name__.replace("qtpy", API_NAME),
    )

    extra_members = (
        frozenset(object.__dir__(qtpy_module))
        - frozenset(dir(original_module))
        - frozenset(
            # These are unavoidable:
            [
                "__builtins__",
                "__cached__",
            ],
        )
        - frozenset(
            # These don't show up in `dir()` when on PySide2/6:
            [*dir(object), "QAbstractAnimation", "QAbstractAnimationClip", "QAbstractClipAnimator", "QAbstractClipBlendNode", "QAdditiveClipBlend", "QAnimationAspect", "QAnimationCallback", "QAnimationClip", "QAnimationClipLoader", "QAnimationController", "QAnimationGroup", "QBlendedClipAnimator", "QClipAnimator", "QClock", "QKeyFrame", "QKeyframeAnimation", "QLerpClipBlend", "QMorphTarget", "QMorphingAnimation", "QSkeletonMapping", "QVertexBlendAnimation", "__annotations__", "__dict__", "__module__"],
        )
        - frozenset(
            # These don't show up in `dir()` when on PySide6:
            [*dir(object), "QAbstractChannelMapping", "QAnimationClipData", "QChannel", "QChannelComponent", "QChannelMapper", "QChannelMapping", "QClipBlendValue"],
        )
    )
    assert not extra_members
