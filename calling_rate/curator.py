import calling_rate

import typer

curator = typer.Typer(help="Tools to clean calling rates data")


@curator.command()
def write_recording_coordinates(shp_path: str, output_path: str):
    geojson_path = "tmp.geojson"
    calling_rate.shp_files_to_geojson(shp_path, geojson_path)


@curator.command()
def version():
    version = calling_rate.__version__
    print(version)
