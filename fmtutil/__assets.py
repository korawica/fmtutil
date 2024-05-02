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
from typing import Any, Callable, Optional, Protocol, Union

from typing_extensions import TypeAlias

from fmtutil.exceptions import FormatterArgumentError, FormatterValueError
from fmtutil.utils import bytes2str, can_int, itself, remove_pad, scache

DictStr: TypeAlias = dict[str, str]
String: TypeAlias = Union[str, bytes]
TupleInt: TypeAlias = tuple[int, ...]


@dataclass
class BaseFormat:
    alias: str
    fmt: Callable[[str], str]


@dataclass
class CommonFormat(BaseFormat):
    regex: str
    parse: Callable[[str], str]
    level: Union[int, TupleInt] = field(default=(0,))


@dataclass
class CombineFormat(BaseFormat):
    cregex: str
    level: Union[int, TupleInt] = field(default=(0,))


Format = Union[CommonFormat, CombineFormat]


@dataclass
class ConfigFormat:
    default_fmt: str
    proxy: type[BaseProxy]
    validator: Callable[[Any], Any] = field(default_factory=itself)


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
    return value.rjust(SERIAL_MAX_PADDING, "0") if value else ""


def to_binary(value: str) -> str:
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
}


class BaseProxyProtocol(Protocol): ...


class BaseProxy:

    def receive(self, parsing: DictStr): ...


class SerialProxy(BaseProxy):

    def __init__(
        self,
        number: int | str | float | None,
    ):
        if number is None:
            self.number: int = 0
        if not can_int(number) or ((prepare := int(float(number))) < 0):
            raise FormatterValueError(
                f"Serial formatter does not support for value, {number!r}."
            )
        self.number: int = prepare

    @classmethod
    def receive(cls, parsing: DictStr):
        return cls(**parsing)


SERIAL_CONF = ConfigFormat(
    default_fmt="%n",
    proxy=SerialProxy,
)


DATETIME_ASSET: dict[str, Format] = {
    "%n": parsing_format(
        {
            "alias": "normal",
            "cregex": "%Y%m%d_%H%M%S",
            "fmt": lambda x: partial(x.strftime("%Y%m%d_%H%M%S")),
        }
    ),
    "%Y": parsing_format(
        {
            "alias": "year",
            "regex": r"\d{4}",
            "fmt": lambda x: partial(x.strftime, "%Y"),
            "parse": lambda x: x,
            "level": 10,
        }
    ),
    "%m": parsing_format(
        {
            "alias": "month_pad",
            "regex": "01|02|03|04|05|06|07|08|09|10|11|12",
            "fmt": lambda x: partial(x.strftime, "%m"),
            "parse": lambda x: x,
            "level": 9,
        }
    ),
    "%d": parsing_format(
        {
            "alias": "day_pad",
            "regex": "[0-3][0-9]",
            "fmt": lambda x: partial(x.strftime, "%d"),
            "parse": lambda x: x,
            "level": 8,
        }
    ),
    "%H": parsing_format(
        {
            "alias": "hour_pad",
            "regex": "[0-2][0-9]",
            "fmt": lambda x: partial(x.strftime, "%H"),
            "parse": lambda x: x,
            "level": 0,
        }
    ),
    "%M": parsing_format(
        {
            "alias": "minute_pad",
            "regex": "[0-6][0-9]",
            "fmt": lambda x: partial(x.strftime, "%M"),
            "parse": lambda x: x,
            "level": 0,
        }
    ),
    "%S": parsing_format(
        {
            "alias": "second_pad",
            "regex": "[0-6][0-9]",
            "fmt": lambda x: partial(x.strftime, "%S"),
            "parse": lambda x: x,
            "level": 0,
        }
    ),
    "_": parsing_format(
        {
            "alias": "",
            "regex": "",
            "fmt": lambda x: x,
            "parse": lambda x: x,
            "level": 0,
        }
    ),
}


DATETIME_CONF = ConfigFormat(
    default_fmt="%Y-%m-%d %H:%M:%S",
    proxy=BaseProxy,
)


class Formatter:
    asset: dict[str, Format]
    config: ConfigFormat

    def __init_subclass__(
        cls,
        /,
        asset: dict[str, Format] | None = None,
        config: ConfigFormat | None = None,
        **kwargs,
    ) -> None:
        cls.asset = asset or cls.asset
        cls.config = config or cls.config

        if cls.asset is None:
            raise NotImplementedError
        if cls.config is None:
            raise NotImplementedError

    @classmethod
    def parse(
        cls,
        value: String,
        fmt: Optional[str] = None,
    ) -> DictStr:
        _fmt: str = fmt or cls.config.default_fmt
        _value: str = bytes2str(value)

        if not _fmt:
            raise NotImplementedError(
                "This Formatter class does not set default format string "
                "value."
            )

        _fmt = cls.gen_format(_fmt)
        if _search := re.search(rf"^{_fmt}$", _value):
            return cls.__validate_format(_search.groupdict())

        raise FormatterValueError(
            f"value {_value!r} does not match with format {_fmt!r}"
        )

    @classmethod
    def gen_format(
        cls,
        fmt: str,
        *,
        prefix: Optional[str] = None,
        suffix: Optional[str] = None,
        alias: bool = True,
    ) -> str:
        _cache: dict[str, int] = defaultdict(int)
        _prefix: str = prefix or ""
        _suffix: str = suffix or ""
        regexes = cls._regex()
        for fmt_match in re.finditer(r"(%?%[-+!*]?[A-Za-z])", fmt):
            fmt_str: str = fmt_match.group()
            if fmt_str.startswith("%%"):
                fmt = fmt.replace(fmt_str, fmt_str[1:], 1)
                continue
            if fmt_str not in regexes:
                raise FormatterArgumentError(
                    "fmt",
                    (
                        f"The format string, {fmt_str!r}, does not exists in "
                        f"``cls.regex``."
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
                        (
                            f"(?P<{_prefix}{_sr_re}{scache(_cache[_sr_re])}"
                            f"{_suffix}>"
                        )
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

    @classmethod
    def _regex(cls) -> DictStr:
        results: DictStr = {}
        pre_results: DictStr = {}
        for f, props in cls.asset.items():
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

    @staticmethod
    def __validate_format(
        formats: DictStr | None = None,
    ) -> DictStr:
        results: DictStr = {}
        _formats: DictStr = formats or {}
        for fmt in _formats:
            _fmt: str = fmt.split("__", maxsplit=1)[0]
            if _fmt not in results:
                results[_fmt] = _formats[fmt]
                continue
            if results[_fmt] != _formats[fmt]:
                raise FormatterValueError(
                    "Parsing with some duplicate format name that have "
                    "value do not all equal."
                )
        return results


class Serial(Formatter, asset=SERIAL_ASSET, config=SERIAL_CONF):

    def __init__(
        self,
        number: int | str | float | None,
    ) -> None:
        if number is None:
            self.number: int = 0
        if not can_int(number) or ((prepare := int(float(number))) < 0):
            raise FormatterValueError(
                f"Serial formatter does not support for value, {number!r}."
            )
        self.number: int = prepare


class Datetime(Formatter, asset=DATETIME_ASSET, config=DATETIME_CONF): ...


def demo_number_formating():
    # Step 01: Initialize serial formatter with asset + config params.

    # Step 02: Generate format from string and Parsing with specific format.
    print(Serial.gen_format("This is a number `%n` but extra `%b`"))
    serial_proxy = Serial.parse("Number: 20240101", fmt="Number: %n")
    print(serial_proxy)

    # # Step Final: Parse and format.
    # serial_proxy = serial.parse("Number: 20240101", fmt="Number: %n")
    # print(serial_proxy.format("This is format number: %n"))


def demo_datetime_formating():
    # print(dt_format.regex)
    print(Datetime.gen_format("This is a datetime %Y%m and special %n"))


if __name__ == "__main__":
    demo_number_formating()
    demo_datetime_formating()
