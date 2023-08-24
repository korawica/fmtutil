from __future__ import annotations  # pragma: no cover.

import sys
import datetime

import click

from .formatter import Datetime, Serial, Version, Naming


MAP_FMTS: dict = {
    'datetime': Datetime,
    'serial': Serial,
    'version': Version,
    'naming': Naming,
}


@click.group()
def cli():
    """A simple command line tool."""
    pass  # pragma: no cover.


@click.group(name="datetime")
def cli_datetime():
    """Datetime Formatter Object Interface CLI"""
    pass

@click.group(name="serial")
def cli_serial():
    """Serial Formatter Object Interface CLI"""
    pass

@click.group(name="version")
def cli_version():
    """Version Formatter Object Interface CLI"""
    pass

@click.group(name="naming")
def cli_naming():
    """Naming Formatter Object Interface CLI"""
    pass

def dynamic_parse(name: str):

    @click.option(
        "-v", "--value",
        type=click.STRING,
    )
    @click.option(
        "-f", "--format-in",
        type=click.STRING,
        default="%Y-%m-%d %H:%M:%S",
    )
    @click.option(
        "-o","--format-out",
        type=click.STRING,
        default="%Y-%m-%d %H:%M:%S",
    )
    def parse(value, format_in, format_out):
        dt = Datetime.parse(
            value=value,
            fmt=format_in
        )
        sys.exit(dt.format(fmt=format_out))

    parse.__doc__ = f"""Parse {name.capitalize()} Formatter Object"""

    return parse


@cli_datetime.command()
@click.option(
    "-f", "--format-out",
    type=click.STRING,
    default="%Y-%m-%d %H:%M:%S",
)
def now(format_out):
    """Get Now Datetime with any string format value.
    """
    sys.exit(
        Datetime.parse(
            value=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            fmt="%Y-%m-%d %H:%M:%S"
        ).format(format_out)
    )

cli_datetime.command(dynamic_parse('datetime'))
cli_serial.command(dynamic_parse('serial'))
cli_version.command(dynamic_parse('version'))
cli_naming.command(dynamic_parse('naming'))


def main() -> None:
    cli.add_command(cli_datetime)
    cli.add_command(cli_serial)
    cli.add_command(cli_version)
    cli.add_command(cli_naming)
    cli.main()


if __name__ == "__main__":
    main()
