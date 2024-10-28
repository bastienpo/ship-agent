"""FastAgent CLI."""

from rich import print
from typer import Typer

app = Typer()


@app.command()
def init() -> None:
    """Initialize a new FastAgent project."""
    print("Initializing FastAgent project...")


@app.command()
def run() -> None:
    """Run the FastAgent server."""
    print("Starting FastAgent server...")


if __name__ == "__main__":
    app()
