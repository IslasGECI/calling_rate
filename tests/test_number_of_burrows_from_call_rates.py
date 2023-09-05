import pytest
from calling_rate import (
    get_area_for_each_recorder,
    get_call_rate_in_burrow_area,
    get_call_rate_in_recorder_area,
    get_density_in_burrow_area,
    get_density_in_recorder_area,
    get_number_of_burrows_in_recorder_area,
    get_number_of_recorders,
    get_recorder_area,
    get_recorder_coordinates,
    is_inside_burrow_area,
)


# Calcula la densidad (𝜎) de madrigueras en el polígono envolvente
def test_get_density_in_burrow_area():
    expected_density = 3.559479030607237e-5
    burrow_geci_data_path = "tests/data/coordenadas_madrigueras_geci.csv"
    burrow_jm_data_path = "tests/data/coordenadas_madrigueras_jm.csv"
    obtained_density = get_density_in_burrow_area(burrow_geci_data_path, burrow_jm_data_path)
    assert obtained_density == expected_density


recorder_data_path = "tests/data/puntos_grabaciones_estimacion_poblacion.csv"


# Lee los datos de tasas de vocalización
def test_get_recorder_coordinates():
    expected_n_recorders = 80
    obtained_n_recorders = get_recorder_coordinates(recorder_data_path).shape[0]
    assert obtained_n_recorders == expected_n_recorders


# Calcula el promedio de tasas de vocalización (v) dentro de la envolvente
def test_is_inside_burrow_area():
    expected_inside = 10
    obtained_inside = sum(is_inside_burrow_area(recorder_data_path))
    assert obtained_inside == expected_inside


def test_get_call_rate_in_burrow_area():
    expected_call_rate = 3.01
    obtained_call_rate = get_call_rate_in_burrow_area(recorder_data_path)
    assert pytest.approx(obtained_call_rate, 0.001) == expected_call_rate


# Calcula el promedio de tasas de vocalización (V) en toda el área (A) de las grabadoras
def test_get_call_rate_in_recorder_area():
    expected_call_rate = 2.06
    obtained_call_rate = get_call_rate_in_recorder_area(recorder_data_path)
    assert pytest.approx(obtained_call_rate, 0.01) == expected_call_rate


# Calcula densidad (𝚺) promedio para toda el área (A) de las grabadoras (𝚺 = 𝜎·V/v)
def test_get_density_in_recorder_area():
    expected_density = 2.4316208493973858e-05
    obtained_density = get_density_in_recorder_area(recorder_data_path)
    assert obtained_density == expected_density


# Calcula el area de las grabadoras (A=n·dA)
def test_get_area_for_each_recorder():
    expected_area = 300 * 300
    obtained_area = get_area_for_each_recorder(recorder_data_path)
    assert obtained_area == expected_area


def test_get_number_of_recorders():
    expected_n_recorders = 80
    obtained_n_recorders = get_number_of_recorders(recorder_data_path)
    assert obtained_n_recorders == expected_n_recorders


def test_get_recorder_area():
    expected_area = 7200000
    obtained_area = get_recorder_area(recorder_data_path)
    assert obtained_area == expected_area


# Calcula el número total de madrigueras N = 𝚺·A
def test_get_number_of_burrows_in_recorder_area():
    expected_number_of_burrows = 175
    obtained_number_of_burrows = get_number_of_burrows_in_recorder_area(recorder_data_path)
    assert pytest.approx(obtained_number_of_burrows, 0.1) == expected_number_of_burrows
    new_recorders_path = "tests/data/puntos_grabaciones_estimacion_poblacion_nuevos.csv"
    obtained_number_of_burrows = get_number_of_burrows_in_recorder_area(new_recorders_path)
    assert pytest.approx(obtained_number_of_burrows, 0.1) == 350
