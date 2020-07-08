import click


@click.group()
def cli():
    pass


@cli.group()
def mypy():
    pass


@mypy.command()
def args():
    options = {False: '--always-false', True: '--always-true'}

    import qtpy

    apis_active = {name: qtpy.API.lower() == name.lower() for name in qtpy.APIS}
    print(' '.join(
        f'{options[is_active]}={name.upper()}'
        for name, is_active
        in apis_active.items()
    ))
