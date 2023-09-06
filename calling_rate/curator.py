import calling_rate

import typer

curator = typer.Typer(help="Tools to clean calling rates data")


@curator.command()
def version():
    version = calling_rate.__version__
    print(version)
