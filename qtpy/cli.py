# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Copyright © 2009- The QtPy Contributors
#
# Released under the terms of the MIT License
# (see LICENSE.txt for details)
# -----------------------------------------------------------------------------

"""Provide a CLI to allow configuring developer settings, including mypy."""

# Standard library imports
import argparse
import sys
import textwrap


class RawDescriptionArgumentDefaultsHelpFormatter(
    argparse.RawDescriptionHelpFormatter,
    argparse.ArgumentDefaultsHelpFormatter,
):
    pass


def cli(args=sys.argv[1:]):
    parser = argparse.ArgumentParser(
        description="Features in support of development with QtPy.",
        formatter_class=RawDescriptionArgumentDefaultsHelpFormatter,
    )

    parser.set_defaults(func=parser.print_help)

    cli_subparsers = parser.add_subparsers()

    mypy_args_parser = cli_subparsers.add_parser(
        name='mypy-args',
        description=textwrap.dedent(
            """\
            Generate command line arguments for using mypy with QtPy.

            This will generate strings similar to the following which help guide mypy
            through which library QtPy would have used so that mypy can get the proper
            underlying type hints.

                --always-false=PYQT5 --always-false=PYQT6 --always-true=PYSIDE2 --always-false=PYSIDE6

            Use such as:

                env/bin/mypy --package mypackage $(env/bin/qtpy mypy-args)
            """
        ),
        formatter_class=RawDescriptionArgumentDefaultsHelpFormatter,
    )
    mypy_args_parser.set_defaults(func=mypy_args)

    arguments = parser.parse_args(args=args)

    reserved_parameters = {'func'}
    cleaned = {
        k: v
        for k, v in vars(arguments).items()
        if k not in reserved_parameters
    }

    arguments.func(**cleaned)


def mypy_args():
    options = {False: '--always-false', True: '--always-true'}

    import qtpy

    apis_active = {name: qtpy.API == name for name in qtpy.API_NAMES}
    print(' '.join(
        f'{options[is_active]}={name.upper()}'
        for name, is_active
        in apis_active.items()
    ))
