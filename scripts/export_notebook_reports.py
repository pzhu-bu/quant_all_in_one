from __future__ import annotations

from pathlib import Path
from subprocess import run

import typer


def main(notebooks_dir: Path = Path("notebooks"), output_dir: Path = Path("reports")) -> None:
    notebooks = sorted(notebooks_dir.glob("*.ipynb"))
    if not notebooks:
        typer.echo("no notebooks to export")
        return

    output_dir.mkdir(parents=True, exist_ok=True)
    for notebook in notebooks:
        run(
            [
                "jupyter",
                "nbconvert",
                "--to",
                "html",
                "--output-dir",
                str(output_dir),
                str(notebook),
            ],
            check=True,
        )


if __name__ == "__main__":
    typer.run(main)
