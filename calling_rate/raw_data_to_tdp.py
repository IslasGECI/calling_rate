import geopandas


def shp_files_to_geojson(raw_data: str, output_path: str):
    geopandas_df = geopandas.read_file(raw_data)
    geopandas_df.to_file(output_path, driver="GeoJSON")


def geojson_to_id_table(geojson_path: str):
    geopandas_df = geopandas.read_file(geojson_path)
    geopandas_coordinates = geopandas_df.get_coordinates()
    geopandas_df[["X", "Y"]] = geopandas_coordinates
    return geopandas_df.loc[:, ["id", "X", "Y"]]
