from calling_rate import curator
from typer.testing import CliRunner


runner = CliRunner()


def tests_curator():
    result = runner.invoke(curator, "--help")
    assert result.exit_code == 0

    shp_path = "tests/data/nuevos_puntos_estimacion_poblacion2023.shp"
    output_path = "tests/data/recording_coordinates.csv"
    result = runner.invoke(curator, ["write-recording-coordinates", shp_path, output_path])
    assert result.exit_code == 0
