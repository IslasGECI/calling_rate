from calling_rate import cli
import test_tools as tt

from typer.testing import CliRunner


runner = CliRunner()


def tests_cli():
    result = runner.invoke(cli, "--help")
    assert result.exit_code == 0

    output_path = "tests/data/initial_population.json"
    tt.if_exist_remove(output_path)
    result = runner.invoke(
        cli,
        ["write-initial-population", "--output-path", output_path, "--bootstrapping-number", 10],
    )
    assert result.exit_code == 0
    tt.assert_exist(output_path)
