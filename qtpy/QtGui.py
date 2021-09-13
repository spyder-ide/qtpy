from . import API_NAME, _get_submodule

globals().update(_get_submodule(__name__).__dict__)


if "6" in API_NAME:

    def pos(self, *a):
        _pos = self.position(*a)
        return _pos.toPoint()

    globals()["QMouseEvent"].pos = pos
