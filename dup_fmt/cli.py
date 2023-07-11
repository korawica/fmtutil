from __future__ import annotations  # pragma: no cover.

import sys

import click


@click.group()
def cli():
    """A simple command line tool."""
    pass  # pragma: no cover.


@cli.command()
def say():
    """Say Hello World"""
    sys.exit("Hello World")


def main() -> None:
    cli.main()


if __name__ == "__main__":
    main()
