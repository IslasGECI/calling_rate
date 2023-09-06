import geopandas


def shp_files_to_geojson(raw_data: str, output_path: str):
    geopandas_df = geopandas.read_file(raw_data)
    geopandas_df.to_file(output_path)
