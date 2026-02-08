import pytest

from qtpy import PYQT5, PYQT_VERSION
from tests.utils import pytest_importorskip


def test_qtdbus():
    """Test the qtpy.QtDBus namespace"""
    QtDBus = pytest_importorskip("qtpy.QtDBus")

    assert QtDBus.QDBusAbstractAdaptor is not None
    assert QtDBus.QDBusAbstractInterface is not None
    assert QtDBus.QDBusArgument is not None
    assert QtDBus.QDBusConnection is not None


@pytest.mark.skipif(
    PYQT5 and PYQT_VERSION.startswith("5.9"),
    reason=(
        "A specific setup with at least sip 4.9.9 is needed for PyQt5 5.9.* "
        "to work with scoped enum access"
    ),
)
def test_enum_access():
    """Test scoped and unscoped enum access."""
    QtDBus = pytest_importorskip("qtpy.QtDBus")

    assert (
        QtDBus.QDBusError.InvalidSignature
        == QtDBus.QDBusError.ErrorType.InvalidSignature
    )
