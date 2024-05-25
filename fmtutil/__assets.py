# ------------------------------------------------------------------------------
# Copyright (c) 2022 Korawich Anuttra. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for
# license information.
# ------------------------------------------------------------------------------
"""
Note:
        This file is assert of formatter value that will passing for generate
    any formatter object. I will use it instead create sub-class form Formatter
    class for simple and scalable usage.

        It will use the Pydantic BaseModel class instead the origin object for
    fast validate the asset value and able to create a new formatter object with
    changing the asset field.

        I will start define the concept but it does not fit will my creation
    flow. It will be finish on the major version 2.0

Migration Note:

*   I will improve the scalable of the Formatter object that able to transform
    coding from Python to Rust.
*   Change the initialize process of Formatter object that using dynamic self
    attributes to fixing attribute with dynamic asset instead.
"""
from __future__ import annotations

import re
from abc import ABC, abstractmethod
from collections import defaultdict
from dataclasses import dataclass, field
from datetime import datetime
from functools import partial
from typing import Any, Callable, ClassVar, Optional, Union

from typing_extensions import Self, TypeAlias

from fmtutil.exceptions import (
    FormatterArgumentError,
    FormatterKeyError,
    FormatterValueError,
)
from fmtutil.formatter import SlotLevel
from fmtutil.utils import bytes2str, can_int, itself, remove_pad, scache

DictStr: TypeAlias = dict[str, str]
String: TypeAlias = Union[str, bytes]
TupleInt: TypeAlias = tuple[int, ...]
TupleStr: TypeAlias = tuple[str, ...]


@dataclass
class BaseFormat:
    alias: str
    fmt: Callable[[str], partial[[], str]]


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


SERIAL_CONF = ConfigFormat(default_fmt="%n")


class Formatter(ABC):
    """The New Formatter object that will be the abstract parent class for any
    formatter sub-class object.
    """

    asset: ClassVar[dict[str, Format]]
    config: ClassVar[ConfigFormat]
    level: ClassVar[int]

    def __init_subclass__(
        cls,
        /,
        level: int = 1,
        asset: dict[str, Format] | None = None,
        config: ConfigFormat | None = None,
        **kwargs,
    ) -> None:
        cls.level: int = level
        cls.asset: dict[str, Format] = asset or cls.asset
        cls.config: ConfigFormat = config or cls.config

        if cls.asset is None:
            raise NotImplementedError(
                "Should define the `asset` class variable for create a new "
                "formatter object"
            )
        if cls.config is None:
            raise NotImplementedError(
                "Should define the `config` class variable for default values "
                "of a new formatter object"
            )

    @abstractmethod
    def __init__(self, *args, **kwargs):
        raise NotImplementedError(
            "Formatter should implement ``self.__init__`` for validate "
            "incoming parsing values"
        )

    @classmethod
    def parse(
        cls,
        value: String,
        fmt: Optional[str] = None,
    ) -> Self:
        _fmt: str = fmt or cls.config.default_fmt
        _value: str = bytes2str(value)

        if not _fmt:
            raise NotImplementedError(
                "This Formatter class does not set default format string "
                "value."
            )

        _fmt = cls.gen_format(_fmt)
        if _search := re.search(rf"^{_fmt}$", _value):
            return cls(
                **cls.__before_parsing(
                    cls.__validate_format(_search.groupdict())
                )
            )

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
    def __validate_format(formats: DictStr | None = None) -> DictStr:
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

    @classmethod
    def __before_parsing(
        cls,
        parsing: dict[str, str],
        set_strict_mode: bool = False,
    ) -> dict[str, Any]:
        # NOTE: This function was migrated from __init__ method.
        restruct_asset_values: dict[str, Format] = {
            v.alias: v
            for v in cls.asset.values()
            if not isinstance(v, CombineFormat)
        }

        rs: dict[str, Any] = {}
        level = SlotLevel(level=cls.level)
        for name, value in restruct_asset_values.items():
            attr = name.split("_", maxsplit=1)[0]

            if getter := rs.get(attr):
                if not set_strict_mode:
                    continue
                elif name in parsing and getter != (
                    p := value.parse(parsing[name])
                ):
                    raise FormatterValueError(
                        f"Parsing duplicate values do not equal, {getter} and "
                        f"{p}, in ``self.{attr}`` with strict mode."
                    )
            elif name in parsing:
                rs[attr] = value.parse(parsing[name])
                level.update(value.level)
        return rs

    @property
    @abstractmethod
    def value(self) -> Any:  # pragma: no cover
        raise NotImplementedError(
            "Please implement ``value`` property for sub-formatter object"
        )

    def format(self, fmt: str) -> str:
        """Return a string value that was formatted and filled by an input
        format string pattern.

        :param fmt: A format string value for mapping with formatter.
        :type fmt: str

        :raises KeyError: if it has any format pattern does not found in
            `cls.formatter`.

        :rtype: str
        :returns: A string value that was formatted from format string pattern.
        """
        fmt = fmt.replace("%%", "[ESCAPE]")
        for _fmt_match in re.finditer(r"(%[-+!*]?[A-Za-z])", fmt):
            _fmt_str: str = _fmt_match.group(0)
            try:
                _value = self.asset[_fmt_str].fmt(self.value)
                fmt = fmt.replace(_fmt_str, _value())
            except KeyError as err:
                raise FormatterKeyError(
                    f"the format: {_fmt_str!r} does not support for "
                    f"{self.__class__.__name__!r}"
                ) from err
        return fmt.replace("[ESCAPE]", "%")


class Serial(Formatter, asset=SERIAL_ASSET, config=SERIAL_CONF):

    def __init__(
        self,
        number: int | str | float | None,
    ) -> None:
        if number is None:
            self.number: int = 0
        if not can_int(number) or ((prepare := int(float(number))) < 0):
            raise FormatterValueError(
                f"Serial formatter does not support for, {number!r}."
            )
        self.number: int = prepare

    @property
    def value(self) -> int:
        return self.number


DATETIME_ASSET: dict[str, Format] = {
    "%n": parsing_format(
        {
            "alias": "normal",
            "cregex": "%Y%m%d_%H%M%S",
            "fmt": lambda x: partial(x.strftime, "%Y%m%d_%H%M%S"),
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
}


DATETIME_CONF = ConfigFormat(default_fmt="%Y-%m-%d %H:%M:%S")


class Datetime(Formatter, asset=DATETIME_ASSET, config=DATETIME_CONF, level=10):

    def __init__(
        self,
        year: int | None = None,
        month: int | None = None,
        day: int | None = None,
        hour: int = 0,
        minute: int = 0,
        second: int = 0,
        microsecond: int = 0,
        level: SlotLevel | None = None,
    ):
        self.year = int(year or 1990)
        self.month = int(month or 1)
        self.day = int(day or 1)
        self.hour: int = int(hour)
        self.minute: int = int(minute)
        self.second: int = int(second)
        self.microsecond: int = int(microsecond)
        self.slot: SlotLevel = level
        self.dt: datetime = datetime(
            year=self.year,
            month=self.month,
            day=self.day,
            hour=self.hour,
            minute=self.minute,
            second=self.second,
            microsecond=self.microsecond,
        )

    @property
    def value(self) -> datetime:
        return self.dt


def demo_number_formating():
    print(Serial.gen_format("This is a number `%n` but extra `%b`"))
    serial_instance = Serial.parse("Number: 20240101", fmt="Number: %n")
    assert 20240101 == serial_instance.value
    assert isinstance(serial_instance.value, int)

    print(serial_instance.format("%b"))
    assert "1001101001101011011100101" == serial_instance.format("%b")


def demo_datetime_formating():
    print(Datetime.gen_format("This is a datetime %Y%m and special %n"))
    dt_instance = Datetime.parse("date: 20240101", fmt="date: %Y%m%d")
    assert datetime(2024, 1, 1) == dt_instance.value
    assert isinstance(dt_instance.value, datetime)

    print(dt_instance.format("%n"))
    assert "2024" == dt_instance.format("%Y")


if __name__ == "__main__":
    demo_number_formating()
    print("-" * 140)
    demo_datetime_formating()
