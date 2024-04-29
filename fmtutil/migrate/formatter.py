# ------------------------------------------------------------------------------
# Copyright (c) 2022 Korawich Anuttra. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for
# license information.
# ------------------------------------------------------------------------------
"""
Migration Note:

*   I will improve the scalable of the Formatter object that able to transform
    coding from Python to Rust.
*   Change the initialize process of Formatter object that using dynamic self
    attributes to fixing attribute with dynamic asset instead.
"""
from __future__ import annotations

import re
from collections import defaultdict
from dataclasses import dataclass, field
from functools import partial
from typing import Any, Callable, Optional, Union

from fmtutil.exceptions import FormatterArgumentError, FormatterValueError
from fmtutil.utils import itself, remove_pad

DictStr = dict[str, str]


@dataclass
class BaseFormat:
    alias: str
    fmt: Callable[[str], str]
    parse: Callable[[str], str]


@dataclass
class CommonFormat(BaseFormat):
    regex: str
    level: Union[int, tuple[int, ...]] = field(default=(0,))


@dataclass
class CombineFormat(BaseFormat):
    cregex: str
    level: Union[int, tuple[int, ...]] = field(default=(0,))


Format = Union[CommonFormat, CombineFormat]


def parsing_format(
    value: dict[str, CommonFormat | CombineFormat | Any],
) -> Format:
    """Parsing any mapping value to Format dataclass."""
    if "regex" in value.keys() and "cregex" in value.keys():
        raise ValueError("Format does not support for getting all regex keys.")
    elif "regex" in value.keys():
        return CommonFormat(**value)
    elif "cregex" in value.keys():
        return CombineFormat(**value)
    raise ValueError("Format does not have any regex key, `regex` or `cregex`.")


SERIAL_MAX_PADDING: int = 3
SERIAL_MAX_BINARY: int = 8


def to_padding(value: str) -> str:
    """Return a padding string value with zero by setting config
    ``Serial.Config.serial_max_padding`` value.

    :param value: A string value that want to pad with zero.
    :type value: str

    :rtype: str
    :return: A padding string value with zero by setting config
        ``Serial.Config.serial_max_padding`` value.
    """
    return value.rjust(SERIAL_MAX_PADDING, "0") if value else ""


def to_binary(value: str) -> str:
    """Return a binary number string value with limit of max zero padding
    by setting config ``Serial.Config.serial_max_binary`` value.

    :param value: A string value that want to convert to binary.
    :type value: str

    :rtype: str
    :return: A binary number string value with limit of max zero padding
        by setting config ``Serial.Config.serial_max_binary`` value.
    """
    return f"{int(value):0{str(SERIAL_MAX_BINARY)}b}" if value else ""


SERIAL_ASSET: dict[str, Format] = {
    "%n": parsing_format(
        {
            "alias": "number",
            "regex": r"[0-9]*",
            "fmt": lambda x: partial(itself, str(x)),
            "parse": lambda x: x,
            "level": 1,
        }
    ),
    "%p": parsing_format(
        {
            "alias": "number_pad",
            "regex": rf"[0-9]{{{SERIAL_MAX_PADDING}}}",
            "fmt": lambda x: partial(to_padding, str(x)),
            "parse": lambda x: remove_pad(x),
            "level": 1,
        }
    ),
    "%b": parsing_format(
        {
            "alias": "number_binary",
            "regex": rf"[0-1]{{{SERIAL_MAX_BINARY}}}",
            "fmt": lambda x: partial(to_binary, str(x)),
            "parse": lambda x: str(int(x, 2)),
            "level": 1,
        }
    ),
    "%c": parsing_format(
        {
            "alias": "number_comma",
            "regex": r"\d{1,3}(?:,\d{3})*",
            "fmt": lambda x: partial(itself, f"{x:,}"),
            "parse": lambda x: x.replace(",", ""),
            "level": 1,
        }
    ),
    "%u": parsing_format(
        {
            "alias": "number_underscore",
            "regex": r"\d{1,3}(?:_\d{3})*",
            "fmt": lambda x: partial(itself, f"{x:_}"),
            "parse": lambda x: x.replace("_", ""),
            "level": 1,
        }
    ),
    # TODO: remove %e from testing asset.
    "%e": parsing_format(
        {
            "alias": "number_extra",
            "cregex": "%n_%p_%c_%n",
            "fmt": lambda x: partial(itself, str(x)),
            "parse": lambda x: x,
            "level": 1,
        }
    ),
    # "_": parsing_format(
    #     {
    #         "alias": "number_default",
    #     }
    # )
}

DATETIME_ASSET: dict[str, Format] = {
    "%n": parsing_format(
        {
            "alias": "datetime_normal",
            "regex": "%Y%m%d_%H%M%S",
            "fmt": lambda x: partial(x.strftime("%Y%m%d_%H%M%S")),
            "parse": ...,
        }
    ),
    "%Y": parsing_format(
        {
            "alias": "datetime_year",
            "regex": "",
            "fmt": "",
            "parse": ...,
        }
    ),
}


class Formatter:

    def __init__(
        self,
        asset: dict[str, Format],
        *,
        validator=None,
    ):
        self.asset: dict[str, Format] = asset
        self.regex: DictStr = self._regex()

    def gen_format(
        self,
        fmt: str,
        *,
        prefix: Optional[str] = None,
        suffix: Optional[str] = None,
        alias: bool = True,
    ) -> str:
        _cache: dict[str, int] = defaultdict(int)
        _prefix: str = prefix or ""
        _suffix: str = suffix or ""
        regexes = self.regex
        for fmt_match in re.finditer(r"(%[-+!*]?[A-Za-z])", fmt):
            fmt_str: str = fmt_match.group()
            if fmt_str not in regexes:
                raise FormatterArgumentError(
                    "fmt",
                    (
                        f"The format string, {fmt_str!r}, does not exists in "
                        f"``self.regex``."
                    ),
                )
            regex: str = regexes[fmt_str]
            insided: bool = False
            for fmt_inside in re.finditer(
                r"\(\?P<(?P<alias>\w+)>(?P<fmt>(?:(?!\(\?P<\w+>).)*)\)",
                regex,
            ):
                _sr_re: str = fmt_inside.group("alias")
                regex = re.sub(
                    rf"\(\?P<{_sr_re}>",
                    (
                        f"(?P<{_prefix}{_sr_re}__{_cache[_sr_re]}{_suffix}>"
                        if alias
                        else "("
                    ),
                    regex,
                    count=1,
                )
                _cache[_sr_re] += 1
                insided = True
            if not insided:
                raise FormatterValueError(
                    "Regex format string does not set group name for "
                    "parsing value to its class."
                )
            fmt = fmt.replace(fmt_str, regex, 1)
        return fmt

    def _regex(self) -> DictStr:
        results: DictStr = {}
        pre_results: DictStr = {}
        for f, props in self.asset.items():
            if isinstance(props, CommonFormat):
                results[f] = f"(?P<{props.alias}>{props.regex})"
            elif isinstance(props, CombineFormat):
                pre_results[f] = props.cregex
            else:
                raise FormatterValueError(
                    "formatter does not contain `regex` or `cregex` "
                    "in dict value"
                )
        for f, cr in pre_results.items():
            cr = cr.replace("%%", "[ESCAPE]")
            for cm in re.finditer(r"(%[-+!*]?[A-Za-z])", cr):
                cs: str = cm.group()
                if cs in results:
                    cr = cr.replace(cs, results[cs], 1)
                else:
                    raise FormatterArgumentError(
                        "format",
                        (
                            f"format cregex string that contain {cs} regex "
                            f"does not found."
                        ),
                    )
            results[f] = cr.replace("[ESCAPE]", "%%")
        return results


def demo_number_formating():
    # print(NUMBER_ASSET)
    serial: Formatter = Formatter(asset=SERIAL_ASSET)
    # print(serial.regex)
    print(serial.gen_format("This is a number %n but extra %e"))


def demo_datetime_formating():
    dt_format: Formatter = Formatter(asset=DATETIME_ASSET)
    print(dt_format.regex)
    print(dt_format.gen_format("This is a datetime %n"))


if __name__ == "__main__":
    demo_number_formating()
    # demo_datetime_formating()
