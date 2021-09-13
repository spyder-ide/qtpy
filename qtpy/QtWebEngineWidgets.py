from . import API_NAME, _get_submodule

globals().update(_get_submodule(__name__).__dict__)


# TODO:
WEBENGINE = True
