import calling_rate

import typer
import json

cli = typer.Typer(help="Tools to calculate initial population")


@cli.command()
def write_initial_population(
    bootstrapping_number: int = typer.Option(),
    output_path: str = typer.Option(),
    burrow_jm_data_path: str = typer.Option(),
    burrow_geci_data_path: str = typer.Option(),
    calling_numbers_data_path: str = typer.Option(),
):
    dict_to_write = {"b_number": bootstrapping_number}
    with open(output_path, "w") as jsonfile:
        json.dump(dict_to_write, jsonfile)


@cli.command()
def version():
    version = calling_rate.__version__
    print(version)
