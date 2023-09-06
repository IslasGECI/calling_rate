import calling_rate

import typer

curator = typer.Typer(help="Tools to clean calling rates data")


@curator.command()
def write_recording_coordinates(shp_path: str, output_path: str):
    geojson_path = "tmp.geojson"
    calling_rate.shp_files_to_geojson(shp_path, geojson_path)
    recording_coordinates_df = calling_rate.geojson_to_id_table(geojson_path)
    recording_coordinates_df.to_csv(output_path, index=False)


@curator.command()
def version():
    version = calling_rate.__version__
    print(version)
