# -----------------------------------------------------------------------------
# Copyright © 2023- The Spyder Development Team
#
# Released under the terms of the MIT License
# (see LICENSE.txt for details)
# -----------------------------------------------------------------------------

"""Provides utility functions for use by QtPy itself."""

import qtpy


def _wrap_missing_optional_dep_error(
        attr_error,
        *,
        import_error,
        wrapper=qtpy.QtModuleNotInstalledError,
        **wrapper_kwargs,
    ):
    """Create a __cause__-chained wrapper error for a missing optional dep."""
    qtpy_error = wrapper(**wrapper_kwargs)
    import_error.__cause__ = attr_error
    qtpy_error.__cause__ = import_error
    return qtpy_error


def _getattr_missing_optional_dep(name, module_name, optional_names):
    """Wrap AttributeError in a special error if it matches."""
    attr_error = AttributeError(f'module {module_name!r} has no attribute {name!r}')
    if name in optional_names:
        return _wrap_missing_optional_dep_error(attr_error, **optional_names[name])
    return attr_error
