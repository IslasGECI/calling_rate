from calling_rate import cli

from typer.testing import CliRunner


runner = CliRunner()


def tests_cli():
    result = runner.invoke(cli, "--help")
    assert result.exit_code == 0

    result = runner.invoke(cli, ["write-initial-population", "--bootstrapping_number", 10])
    assert result.exit_code == 0
