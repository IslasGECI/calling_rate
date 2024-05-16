from calling_rate import cli
import geci_test_tools as tt

from typer.testing import CliRunner
import json
import pytest

runner = CliRunner()


def test_real_parameters():
    output_path = "tosh_initial_population_2021.json"
    b_number = 2000
    burrow_jm_data_path = "tests/data/coordenadas_madrigueras_jm.csv"
    burrow_geci_data_path = "tests/data/coordenadas_madrigueras_geci.csv"
    calling_numbers_data_path = "tests/data/puntos_grabaciones_estimacion_poblacion.csv"
    result = runner.invoke(
        cli,
        [
            "write-initial-population",
            "--output-path",
            output_path,
            "--bootstrapping-number",
            b_number,
            "--burrow-geci-data-path",
            burrow_geci_data_path,
            "--burrow-jm-data-path",
            burrow_jm_data_path,
            "--calling-numbers-data-path",
            calling_numbers_data_path,
        ],
    )
    assert result.exit_code == 0
    tt.assert_exist(output_path)
