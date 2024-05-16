from calling_rate import cli
import geci_test_tools as tt

from typer.testing import CliRunner
import json
import pytest

runner = CliRunner()


def tests_cli_version():
    result = runner.invoke(cli, "version")
    assert result.stdout == "0.4.0\n"

def tests_cli():
    result = runner.invoke(cli, "--help")
    assert result.exit_code == 0

    output_path = "tests/data/initial_population.json"
    tt.if_exist_remove(output_path)
    b_number = 10
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

    population_interval = read_json(output_path)
    assert population_interval["b_number"] == b_number
    assert population_interval["intervals"][1] == pytest.approx(149.5, 0.01)


def read_json(output_path):
    with open(output_path, "r") as read_file:
        json_content = json.load(read_file)
    return json_content
