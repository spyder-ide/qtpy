import sys
import pytest

from qtpy import PYQT6, PYSIDE2, PYSIDE6
from qtpy.tests.utils import using_conda

# @pytest.mark.skipif(
#     PYQT6 or PYSIDE6, reason="Not availible on Qt6-based bindings")
# @pytest.mark.skipif(
#     sys.platform != "win32" or using_conda(),
#     reason="Only available in Qt5 bindings > 5.9 with pip on Windows in CIs")
def test_qtwinextras():
    QtX11Extras = pytest.importorskip("qtpy.QtX11Extras")

    # TODO: this is just a placeholder file

    # assert QtX11Extras.QSomething is not None
