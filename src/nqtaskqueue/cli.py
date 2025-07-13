import typer
from typer import Typer
from . import tasks
from loguru import logger

app = Typer(add_completion=False, no_args_is_help=True)


@app.command()
def run_task() -> None:
    result = tasks.run_model.delay(
        params={"param1": "value1", "param2": "value2"}
    )

    logger.info(f"Task submitted with ID: {result.id}")
    logger.debug(f"{result=}")


@app.command()
def version() -> None:
    """Display the version of the application."""
    from . import __version__

    typer.echo(f"NQTaskQueue version: {__version__}")


def main() -> None:
    app()
