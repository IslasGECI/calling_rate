from calling_rate import shp_files_to_geojson, geojson_to_id_table

import os


def test_shp_files_to_geojson():
    raw_path = "tests/data/nuevos_puntos_estimacion_poblacion2023.shp"
    geojson_path = "tests/data/geojson_from_shp.geojson"
    if os.path.exists(geojson_path):
        os.remove(geojson_path)
    shp_files_to_geojson(raw_path, geojson_path)
    assert os.path.exists(geojson_path)
    os.remove(geojson_path)


def tests_geojson_to_id_table():
    obtained = geojson_to_id_table("tests/data/geojson_for_tests.geojson")
    obtained_columns = obtained.columns
    expected_columns = ["id", "X", "Y"]
    assert (obtained_columns == expected_columns).all()
    assert obtained.loc[1, "X"] == 502056.092813999974169
