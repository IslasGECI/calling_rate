from calling_rate import cli
import geci_test_tools as tt

from typer.testing import CliRunner


runner = CliRunner()


def tests_cli():
    result = runner.invoke(cli, "--help")
    assert result.exit_code == 0

    output_path = "tests/data/initial_population.json"
    tt.if_exist_remove(output_path)
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
            10,
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
