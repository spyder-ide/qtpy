import pytest

from qtpy import QtBindingInNewerVersionError


def test_qtstatemachine():
    """Test the qtpy.QtStateMachine namespace"""
    try:
        from qtpy import QtStateMachine
    except QtBindingInNewerVersionError:
        pytest.skip("QtStateMachine not available in this binding version")

    assert QtStateMachine.QAbstractState is not None
    assert QtStateMachine.QAbstractTransition is not None
    assert QtStateMachine.QEventTransition is not None
    assert QtStateMachine.QFinalState is not None
    assert QtStateMachine.QHistoryState is not None
    assert QtStateMachine.QKeyEventTransition is not None
    assert QtStateMachine.QMouseEventTransition is not None
    assert QtStateMachine.QSignalTransition is not None
    assert QtStateMachine.QState is not None
