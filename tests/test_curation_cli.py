from calling_rate import curator

from typer.testing import CliRunner
import os
import pandas as pd


runner = CliRunner()


def tests_curator():
    result = runner.invoke(curator, "--help")
    assert result.exit_code == 0

    shp_path = "tests/data/nuevos_puntos_estimacion_poblacion2023.shp"
    output_path = "tests/data/recording_coordinates.csv"

    if os.path.exists(output_path):
        os.remove(output_path)
    result = runner.invoke(curator, ["write-recording-coordinates", shp_path, output_path])
    assert result.exit_code == 0
    assert os.path.exists(output_path)
    output_df = pd.read_csv(output_path)
    assert output_df.shape[1] == 3
    os.remove(output_path)
