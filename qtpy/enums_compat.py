# Copyright © 2009- The Spyder Development Team
# Copyright © 2012- University of North Carolina at Chapel Hill
#                   Luke Campagnola    ('luke.campagnola@%s.com' % 'gmail')
#                   Ogi Moore          ('ognyan.moore@%s.com' % 'gmail')
#                   KIU Shueng Chuan   ('nixchuan@%s.com' % 'gmail')
# Licensed under the terms of the MIT License

"""
Compatibility functions for scoped and unscoped enum access.
"""

from . import PYQT5, PYQT6

if PYQT6:
    import enum

    from . import sip

    def promote_enums(module):
        """
        Search enums in the given module and allow unscoped access.

        Taken from:
        https://github.com/pyqtgraph/pyqtgraph/blob/pyqtgraph-0.12.1/pyqtgraph/Qt.py#L331-L377
        and adapted to also copy enum values aliased under different names.

        """
        class_names = [name for name in dir(module) if name.startswith('Q')]
        for class_name in class_names:
            klass = getattr(module, class_name)
            if not isinstance(klass, sip.wrappertype):
                continue
            attrib_names = [name for name in dir(klass) if name[0].isupper()]
            for attrib_name in attrib_names:
                attrib = getattr(klass, attrib_name)
                if not isinstance(attrib, enum.EnumMeta):
                    continue
                for name, value in attrib.__members__.items():
                    setattr(klass, name, value)

if PYQT5:
    def demote_enums(module):
        """
        Search unscoped enums in the given module and allow scoped access.

        Special for PyQt5==5.9.*
        """
        class LookUp:
            def __init__(self, lookup_location):
                self._lookup_location = lookup_location

            def __getattr__(self, what):
                return getattr(self._lookup_location, what)

        for class_name in dir(module):
            if class_name == 'Qt' or (class_name[0] == 'Q' and class_name[1].isupper()):
                klass = getattr(module, class_name)
                for attrib_name in dir(klass):
                    if attrib_name[0].isupper() and type(getattr(klass, attrib_name)).__name__ == 'enum''type':
                        setattr(klass, attrib_name, LookUp(klass))
