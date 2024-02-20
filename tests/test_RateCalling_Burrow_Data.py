from calling_rate import (
    RateCalling_Burrow_Data,
)

import numpy as np
from collections import Counter
import pytest

recorder_data_path = "tests/data/puntos_grabaciones_estimacion_poblacion_nuevos.csv"
burrow_geci_data_path = "tests/data/coordenadas_madrigueras_geci.csv"
burrow_jm_data_path = "tests/data/coordenadas_madrigueras_jm.csv"
paths = {
    "recorders_data": recorder_data_path,
    "geci_data": burrow_geci_data_path,
    "jm_data": burrow_jm_data_path,
}
B = 100


def test_ratecalling_get_density_in_recorder_area():
    ratecalling_burrow_data = RateCalling_Burrow_Data(paths, B=B)
    obtained = ratecalling_burrow_data.get_density_in_recorder_area()
    print(obtained, "interval density computed by class")
    assert isinstance(obtained, np.ndarray)
    assert_have_the_3_interval_elements(obtained)


def test_get_bootstrapping_distribution_of_density_in_recorded_area():
    ratecalling_burrow_data = RateCalling_Burrow_Data(paths, B=B)
    obtained = ratecalling_burrow_data.get_distribution_density_in_recorder_area()
    assert_that_the_distribition_has_B_elements(obtained, B)


def assert_that_the_distribition_has_B_elements(obtained, B):
    expected_len = B
    assert len(obtained) == expected_len


def assert_have_the_3_interval_elements(obtained):
    expected_len = 3
    assert len(obtained) == expected_len


def test_ratecalling_bootstrapping():
    ratecalling_burrow_data = RateCalling_Burrow_Data(paths)
    obtained = ratecalling_burrow_data.bootstrapping()
    assert_the_nrow_is_the_same_to_the_original(obtained)
    assert_the_first_id_is_different_to_original_first_id(obtained)
    assert_the_first_id_is_stable(obtained)
    obtained = ratecalling_burrow_data.bootstrapping()
    assert_the_first_id_is_different_to_first_sample(obtained)

    paths_synthetic_data = paths
    paths_synthetic_data["recorders_data"] = "tests/data/synthetic_recorders_data.csv"
    ratecalling_burrow_data = RateCalling_Burrow_Data(paths_synthetic_data)
    obtained_ids = []
    for i in range(10000):
        resample = ratecalling_burrow_data.bootstrapping()
        obtained_ids.extend(resample.ID_punto.values)
    ocurrences = Counter(obtained_ids)
    print(ocurrences)
    prob_ocurrences = np.array(list(ocurrences.values())) / len(obtained_ids)
    print(prob_ocurrences)
    print(len(obtained_ids))
    print(np.mean(obtained_ids))
    print(np.std(obtained_ids) ** 2)
    assert_uniform_distribution_probability(prob_ocurrences)


def assert_uniform_distribution_probability(prob_ocurrences):
    for i in prob_ocurrences:
        assert i == pytest.approx(1 / 9, 0.01)


def assert_the_nrow_is_the_same_to_the_original(obtained):
    expected_number_samples = 85
    assert len(obtained) == expected_number_samples


def assert_the_first_id_is_different_to_original_first_id(obtained):
    original_first_id = 64
    obtained_first_id = obtained.ID_punto.values[0]
    assert obtained_first_id != original_first_id, "It did not shuffle"


def assert_the_first_id_is_stable(obtained):
    expected_first_id = 144
    obtained_first_id = obtained.ID_punto.values[0]
    assert obtained_first_id == expected_first_id


def assert_the_first_id_is_different_to_first_sample(obtained):
    expected_first_id = 144
    obtained_first_id = obtained.ID_punto.values[0]
    assert obtained_first_id != expected_first_id, "The seed is the same in each call of sample"
