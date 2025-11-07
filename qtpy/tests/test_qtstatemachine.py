import pytest

from qtpy import PYQT6, PYQT_VERSION, PYSIDE6
from qtpy.tests.utils import using_conda


@pytest.mark.skipif(
    PYQT6 and int(PYQT_VERSION.split(".")[1]) < 9,
    reason="QtStateMachine has been added to PyQt6 in version 6.9",
)
@pytest.mark.skipif(
    PYSIDE6 and using_conda(),
    reason="Not available on PySide6 with conda",
)
def test_qtstatemachine():
    """Test the qtpy.QtStateMachine namespace"""
    from qtpy import QtStateMachine

    assert QtStateMachine.QAbstractState is not None
    assert QtStateMachine.QAbstractTransition is not None
    assert QtStateMachine.QEventTransition is not None
    assert QtStateMachine.QFinalState is not None
    assert QtStateMachine.QHistoryState is not None
    assert QtStateMachine.QKeyEventTransition is not None
    assert QtStateMachine.QMouseEventTransition is not None
    assert QtStateMachine.QSignalTransition is not None
    assert QtStateMachine.QState is not None
