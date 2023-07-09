from __future__ import annotations  # no cov

import sys

import click


@click.group()
def cli():
    """A simple command line tool."""
    pass  # pragma: no cover.


@cli.command()
def log():
    sys.exit(0)


def main() -> None:
    cli.main()


if __name__ == "__main__":
    main()
