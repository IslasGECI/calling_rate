import calling_rate

import typer

cli = typer.Typer(help="Tools to calculate initial population")


@cli.command()
def version():
    version = calling_rate.__version__
    print(version)
