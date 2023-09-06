from calling_rate import shp_files_to_geojson

import os


def test_shp_files_to_geojson():
    raw_path = "tests/data/nuevos_puntos_estimacion_poblacion2023.shp"
    geojson_path = "tests/data/geojson_from_shp.json"
    if os.path.exists(geojson_path):
        os.remove(geojson_path)
    shp_files_to_geojson(raw_path, geojson_path)
    assert os.path.exists(geojson_path)
    os.remove(geojson_path)
