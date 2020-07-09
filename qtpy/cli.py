import click


@click.group()
def cli():
    """Features in support of development with QtPy."""

    pass


@cli.group()
def mypy():
    """Features in support of running mypy"""

    pass


@mypy.command()
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
