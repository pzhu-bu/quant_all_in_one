from __future__ import annotations

from pathlib import Path

import typer
import yaml

REQUIRED_TABLE_KEYS = {
    "table",
    "description",
    "primary_key",
    "timezone",
    "currency",
    "calendar",
    "point_in_time",
    "columns",
}


def main(schema_dir: Path = Path("data/schema")) -> None:
    schemas = sorted(schema_dir.glob("*.yaml"))
    if not schemas:
        raise typer.BadParameter(f"no schema files found under {schema_dir}")

    failed = False
    for schema_path in schemas:
        payload = yaml.safe_load(schema_path.read_text(encoding="utf-8"))
        missing = REQUIRED_TABLE_KEYS.difference(payload)
        if missing:
            failed = True
            typer.echo(f"{schema_path}: missing {sorted(missing)}")

    if failed:
        raise typer.Exit(code=1)

    typer.echo(f"validated {len(schemas)} schema files")


if __name__ == "__main__":
    typer.run(main)
