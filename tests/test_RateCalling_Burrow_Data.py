from calling_rate import RateCalling_Burrow_Data

recorder_data_path = "tests/data/puntos_grabaciones_estimacion_poblacion_nuevos.csv"
burrow_geci_data_path = "tests/data/coordenadas_madrigueras_geci.csv"
burrow_jm_data_path = "tests/data/coordenadas_madrigueras_jm.csv"
paths = {
    "recorders_data": recorder_data_path,
    "geci_data": burrow_geci_data_path,
    "jm_data": burrow_jm_data_path,
}


def test_ratecalling_get_density_in_recorder_area():
    ratecalling_burrow_data = RateCalling_Burrow_Data(paths)
    obtained = ratecalling_burrow_data.get_density_in_recorder_area()
    assert isinstance(obtained, list)
    assert_have_3_elements(obtained)


def assert_have_3_elements(obtained):
    expected_len = 3
    assert len(obtained) == expected_len


def test_ratecalling_bootstrapping():
    ratecalling_burrow_data = RateCalling_Burrow_Data(paths)
    obtained = ratecalling_burrow_data.bootstrapping()
    assert_the_nrow_is_the_same_to_the_original(obtained)
    assert_the_first_id_is_different_to_64(obtained)
    assert_the_first_id_is_stable(obtained)


def assert_the_nrow_is_the_same_to_the_original(obtained):
    expected_number_samples = 85
    assert len(obtained) == expected_number_samples


def assert_the_first_id_is_different_to_64(obtained):
    original_first_id = 64
    obtained_first_id = obtained.ID_punto.values[0]
    assert obtained_first_id != original_first_id


def assert_the_first_id_is_stable(obtained):
    expected_first_id = 225
    obtained_first_id = obtained.ID_punto.values[0]
    assert obtained_first_id == expected_first_id
