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
    """Generate command line arguments for using mypy with QtPy."""

    options = {False: '--always-false', True: '--always-true'}

    import qtpy

    apis_active = {name: qtpy.API.lower() == name.lower() for name in qtpy.APIS}
    print(' '.join(
        f'{options[is_active]}={name.upper()}'
        for name, is_active
        in apis_active.items()
    ))
