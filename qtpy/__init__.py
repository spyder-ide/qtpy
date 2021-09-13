from __future__ import annotations

import os
import sys
import warnings
from importlib import abc, import_module, util
from typing import TYPE_CHECKING, Sequence

if TYPE_CHECKING:
    from importlib.machinery import ModuleSpec
    from types import ModuleType


class QtMissingError(ImportError):
    """Error raise if no bindings could be selected."""


VALID_APIS = {
    "pyqt5": "PyQt5",
    "pyqt6": "PyQt6",
    "pyside2": "PySide2",
    "pyside6": "PySide6",
}

# Detecting if a binding was specified by the user
_requested_api = os.getenv("QT_API", "").lower()
_forced_api = os.getenv("FORCE_QT_API")

# warn if an invalid API has been requested
if _requested_api and _requested_api not in VALID_APIS:
    warnings.warn(
        f"invalid QT_API specified: {_requested_api}. "
        f"Valid values include {set(VALID_APIS)}"
    )
    _forced_api = None
    _requested_api = ""

# TODO: FORCE_QT_API requires also using QT_API ... does that make sense?

# now we'll try to import QtCore
_QtCore: ModuleType | None = None

# If `FORCE_QT_API` is not set, we first look for previously imported bindings
if not _forced_api:
    for api_name, module_name in VALID_APIS.items():
        if module_name in sys.modules:
            _QtCore = import_module(f"{module_name}.QtCore")
            break

if _QtCore is None:
    # try the requested API first, and if _forced_api is True,
    # raise an ImportError if it doesn't work.
    # Otherwise go through the list of Valid APIs until something imports
    requested = VALID_APIS.get(_requested_api)
    for module_name in sorted(VALID_APIS.values(), key=lambda x: x != requested):
        try:
            _QtCore = import_module(f"{module_name}.QtCore")
            break
        except ImportError:
            if _forced_api:
                ImportError(
                    "FORCE_QT_API set and unable to import requested QT_API: {e}"
                )

# didn't find one...  not going to work
if _QtCore is None:
    raise QtMissingError(f"No QtCore could be found. Tried: {VALID_APIS.values()}")

# load variables based on what we found.
if not _QtCore.__package__:
    raise RuntimeError("QtCore does not declare __package__?")

API_NAME = _QtCore.__package__
PYSIDE2 = API_NAME == "PySide2"
PYSIDE6 = API_NAME == "PySide6"
PYQT5 = API_NAME == "PyQt5"
PYQT6 = API_NAME == "PyQt6"
PYSIDE = API_NAME.startswith("PySide")
PYQT = API_NAME.startswith("PyQt")
QT_VERSION = getattr(_QtCore, "QT_VERSION_STR", "") or getattr(_QtCore, "__version__")

# lastly, emit a warning if we ended up with an API other than the one requested
if _requested_api and API_NAME != VALID_APIS[_requested_api]:
    warnings.warn(
        f"Selected binding {_requested_api!r} could not be found, using {API_NAME!r}"
    )


# Setup the meta path finder that lets us import anything using `qtpy.module`
class QtPyImporter(abc.MetaPathFinder):
    def find_spec(
        self,
        fullname: str,
        path: Sequence[bytes | str] | None,
        target: ModuleType | None = None,
    ) -> ModuleSpec | None:
        """Find a spec for the specified module.

        See https://docs.python.org/3/reference/import.html#the-meta-path
        """
        if fullname.startswith(__name__):
            return util.find_spec(fullname.replace(__name__, API_NAME))
        return None


sys.meta_path.append(QtPyImporter())


def _get_submodule(mod_name: str, globals=None, name_changes=None):
    """Convenience to get a submodule from the current QT_API"""
    _mod_name = mod_name.rsplit(".", maxsplit=1)[-1]
    mod = import_module(f"{API_NAME}.{_mod_name}")
    if globals is not None:
        globals.update(mod.__dict__)
    if name_changes is not None:
        _update_ns(name_changes, globals)
    return mod


def _update_ns(name_changes: dict[str, dict[str, str]], globals) -> None:

    for ns, changes in name_changes.items():
        if ns in API_NAME:
            for new, old in changes.items():
                globals[new] = getattr(_QtCore, old)
