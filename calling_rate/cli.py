import calling_rate

import typer

cli = typer.Typer(help="Tools to calculate initial population")


@cli.command()
def write_initial_population(bootstrapping_number: int = typer.Option()):
    pass


@cli.command()
def version():
    version = calling_rate.__version__
    print(version)
