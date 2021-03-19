import argparse
import inspect


class RawDescriptionArgumentDefaultsHelpFormatter(
    argparse.RawDescriptionHelpFormatter,
    argparse.ArgumentDefaultsHelpFormatter,
):
    pass


def cli():
    """Features in support of development with QtPy."""

    parser = argparse.ArgumentParser(
        description=inspect.getdoc(cli),
        formatter_class=RawDescriptionArgumentDefaultsHelpFormatter,
    )

    parser.set_defaults(func=parser.print_help)

    cli_subparsers = parser.add_subparsers()

    mypy_parser = cli_subparsers.add_parser(
        name=mypy.__name__,
        description=inspect.getdoc(mypy),
        formatter_class=RawDescriptionArgumentDefaultsHelpFormatter,
    )
    mypy_parser.set_defaults(func=mypy)

    mypy_subparsers = mypy_parser.add_subparsers()

    mypy_args_parser = mypy_subparsers.add_parser(
        name=args.__name__,
        description=inspect.getdoc(args),
        formatter_class=RawDescriptionArgumentDefaultsHelpFormatter,
    )
    mypy_args_parser.set_defaults(func=args)

    arguments = parser.parse_args()

    reserved_parameters = {'func'}
    cleaned = {
        k: v
        for k, v in vars(args).items()
        if k not in reserved_parameters
    }

    arguments.func(**cleaned)


def mypy():
    """Features in support of running mypy"""

    pass


def args():
    """Generate command line arguments for using mypy with QtPy.

    This will generate strings similar to the following which help guide mypy
    through which library QtPy would have used so that mypy can get the proper
    underlying type hints.

        --always-false=PYQT4 --always-false=PYQT5 --always-false=PYSIDE --always-true=PYSIDE2

    Use such as:

        env/bin/mypy --package mypackage $(env/bin/qtpy mypy args)
    """

    options = {False: '--always-false', True: '--always-true'}

    import qtpy

    apis_active = {name: qtpy.API.lower() == name.lower() for name in qtpy.APIS}
    print(' '.join(
        f'{options[is_active]}={name.upper()}'
        for name, is_active
        in apis_active.items()
    ))
