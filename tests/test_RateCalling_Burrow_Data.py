from calling_rate import RateCalling_Burrow_Data


def test_ratecalling_bootstrapping():

    recorder_data_path = "tests/data/puntos_grabaciones_estimacion_poblacion_nuevos.csv"
    burrow_geci_data_path = "tests/data/coordenadas_madrigueras_geci.csv"
    burrow_jm_data_path = "tests/data/coordenadas_madrigueras_jm.csv"
    paths = {
        "recorders_data": recorder_data_path,
        "geci_data": burrow_geci_data_path,
        "jm_data": burrow_jm_data_path,
    }
    ratecalling_burrow_data = RateCalling_Burrow_Data(paths)
    obtained = ratecalling_burrow_data.bootstrapping()
    print(obtained)
    assert_the_nrow_is_the_same_to_the_original(obtained)
    assert_the_first_id_is_different_to_64(obtained)


def assert_the_nrow_is_the_same_to_the_original(obtained):
    expected_number_samples = 85
    assert len(obtained) == expected_number_samples
