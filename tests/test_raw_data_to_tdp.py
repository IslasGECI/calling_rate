import utm
from calling_rate import (
    geojson_to_id_table,
    geojson_to_records_by_season_table,
    get_recording_coordinates,
    get_recording_data,
    replace_utm_to_lat_lon,
    shp_files_to_geojson,
)

import geopandas
import os
import pytest

raw_path = "tests/data/nuevos_puntos_estimacion_poblacion2023.shp"


def test_shp_files_to_geojson():
    geojson_path = "tests/data/geojson_from_shp.geojson"
    if os.path.exists(geojson_path):
        os.remove(geojson_path)
    shp_files_to_geojson(raw_path, geojson_path)
    assert os.path.exists(geojson_path)
    # os.remove(geojson_path)


geojson_path = "tests/data/geojson_for_tests.geojson"


def test_replace_utm_to_lat_lon():
    geodataframe = geopandas.read_file(geojson_path)
    print(geodataframe)

    obtained = replace_utm_to_lat_lon(geodataframe)
    print(geodataframe)
    print(obtained)
    obtained_longitude = obtained.get_coordinates().x[0]
    obtained_latitude = obtained.get_coordinates().y[0]
    expected_latitude = 18.789393
    expected_longitude = -110.960561
    assert pytest.approx(obtained_longitude, 0.1) == expected_longitude
    assert pytest.approx(obtained_latitude, 0.1) == expected_latitude


def tests_geojson_to_id_table():
    obtained = geojson_to_id_table(geojson_path)
    obtained_columns = obtained.columns
    expected_columns = ["id", "lat", "lon"]
    assert (obtained_columns == expected_columns).all()
    assert obtained.loc[1, "lon"] == -110.98048594639367
    assert obtained.loc[1, "lat"] == 18.81651004


def test_geojson_to_records_by_season_table():
    obtained = geojson_to_records_by_season_table(geojson_path)
    obtained_columns = obtained.columns
    expected_columns = ["Temporada", "id", "Estatus", "Pres-Ause", "Cant Voc", "Tasa Voc"]
    assert (obtained_columns == expected_columns).all()


def test_get_recording_coordinates():
    geojson_path = "tmp.geojson"
    if os.path.exists(geojson_path):
        os.remove(geojson_path)
    get_recording_coordinates(raw_path)
    assert os.path.exists(geojson_path)
    os.remove(geojson_path)


def test_get_records_data():
    geojson_path = "tmp.geojson"
    if os.path.exists(geojson_path):
        os.remove(geojson_path)
    get_recording_data(raw_path)
    assert os.path.exists(geojson_path)
    os.remove(geojson_path)
