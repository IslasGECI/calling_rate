from calling_rate import curator
from typer.testing import CliRunner


runner = CliRunner()


def tests_curator():
    result = runner.invoke(curator, "--help")
    assert result.exit_code == 0

    shp_path = "tests/data/nuevos_puntos_estimacion_poblacion2023.shp"
    output_path = "tests/data/recorder_coordinates.csv"
    result = runner.invoke(curator, "run", "--shp-path", shp_path, "--output-path", output_path)
    assert result.exit_code == 0
