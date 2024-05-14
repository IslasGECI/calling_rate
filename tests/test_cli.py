from calling_rate import cli

from typer.testing import CliRunner


runner = CliRunner()


def tests_cli():
    result = runner.invoke(cli, "--help")
    assert result.exit_code == 0
