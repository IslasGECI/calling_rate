from calling_rate import curator
from typer.testing import CliRunner


runner = CliRunner()


def tests_curator():
    result = runner.invoke(curator, "--help")
    assert result.exit_code == 0
