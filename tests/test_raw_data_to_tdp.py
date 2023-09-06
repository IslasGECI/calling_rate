from calling_rate import (
    shp_files_to_geojson,
    geojson_to_id_table,
    get_recording_coordinates,
    geojson_to_records_by_season_table,
)

import os

raw_path = "tests/data/nuevos_puntos_estimacion_poblacion2023.shp"


def test_shp_files_to_geojson():
    geojson_path = "tests/data/geojson_from_shp.geojson"
    if os.path.exists(geojson_path):
        os.remove(geojson_path)
    shp_files_to_geojson(raw_path, geojson_path)
    assert os.path.exists(geojson_path)
    os.remove(geojson_path)


geojson_path = "tests/data/geojson_for_tests.geojson"


def tests_geojson_to_id_table():
    obtained = geojson_to_id_table(geojson_path)
    obtained_columns = obtained.columns
    expected_columns = ["id", "X", "Y"]
    assert (obtained_columns == expected_columns).all()
    assert obtained.loc[1, "X"] == 502056.092813999974169
    assert obtained.loc[1, "Y"] == 2080525.00618


def test_geojson_to_records_by_season_table():
    geojson_to_records_by_season_table(geojson_path)


def test_get_recording_coordinates():
    geojson_path = "tmp.geojson"
    if os.path.exists(geojson_path):
        os.remove(geojson_path)
    get_recording_coordinates(raw_path)
    assert os.path.exists(geojson_path)
    os.remove(geojson_path)
