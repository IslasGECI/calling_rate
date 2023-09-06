from calling_rate import shp_files_to_geojson


def test_shp_files_to_geojson():
    raw_path = "tests/data/nuevos_puntos_estimacion_poblacion2023.shp"
    shp_files_to_geojson(raw_path)
