from __future__ import annotations

import re
from collections.abc import Iterable
from decimal import Decimal
from typing import (
    Any,
    Callable,
    Union,
    get_args,
)

from .__type import String

FMT_STR_MAP: dict[str, str] = {
    "-": "minus",
    "+": "plus",
    "!": "exclamation",
    "*": "asterisk",
}

FMT_STR_OTAN_MAP: dict[str, str] = {
    "A": "alpha",
    "B": "bravo",
    "C": "charlie",
    "D": "delta",
    "E": "echo",
    "F": "foxtrot",
    "G": "golf",
    "H": "hotel",
    "I": "india",
    "J": "juliet",
    "K": "kilo",
    "L": "lima",
    "M": "mike",
    "N": "november",
    "O": "oscar",
    "P": "papa",
    "Q": "quebec",
    "R": "romeo",
    "S": "sierra",
    "T": "tango",
    "U": "uniform",
    "V": "victor",
    "W": "whiskey",
    "X": "xray",
    "Y": "yankee",
    "Z": "zulu",
}

concat: Callable[[Union[list[str], Iterable[str]]], str] = "".join


def itself(x: Any = None) -> Any:
    """Return itself value"""
    return x


def default(value: Any) -> Callable[[], Any]:
    """Return wrapper function of value"""
    return lambda: value


def caller(func: Union[Callable[[], Any], Any]) -> Any:
    """Call function if it was callable

    Examples:

    >>> some_func = lambda: 100
    >>> caller(some_func)
    100
    """
    return func() if callable(func) else func


def convert_fmt_str(fmt: str) -> str:
    """Convert format string to format string name

    Examples:

    >>> convert_fmt_str('%a')
    'alpha'
    >>> convert_fmt_str('%!b')
    'bravo_exclamation'
    >>> convert_fmt_str('%S')
    'sierra_upper'
    >>> convert_fmt_str('%-N')
    'november_upper_minus'
    >>> convert_fmt_str('G')
    'G'
    >>> convert_fmt_str('%H')
    'hotel_upper'
    """
    _fmt_re: str = fmt
    if search := re.search(r"^%(?P<prefix>[-+!*]?)(?P<format>[a-zA-Z])$", fmt):
        search_dict = search.groupdict()
        _fmt: str
        if (_fmt := search_dict["format"]).isupper():
            _fmt_re = f"{FMT_STR_OTAN_MAP[_fmt]}upper"
        else:
            _fmt = _fmt.upper()
            _fmt_re = FMT_STR_OTAN_MAP[_fmt]

        if prefix := search_dict["prefix"]:
            _fmt_re = f"{_fmt_re}{FMT_STR_MAP[prefix]}"
    return _fmt_re


def can_int(value: Any) -> bool:
    """Check value that able cast to integer.

    Example:

    >>> can_int('0.0')
    True
    >>> can_int('-1.0')
    True
    """
    try:
        return float(str(value)).is_integer()
    except (TypeError, ValueError):
        return False


def can_float(value: Any) -> bool:
    """Check value that able cast to float.

    Example:

    >>> can_float('0.01')
    True
    >>> can_float('0.1a')
    False
    """
    if value is None:
        return False
    try:
        float(value)
        return True
    except ValueError:
        return False


def remove_pad(value: str) -> str:
    """Remove zero padding of string

    Examples:

    >>> remove_pad('000')
    '0'
    >>> remove_pad('0123')
    '123'
    """
    return _last_char if (_last_char := value[-1]) == "0" else value.lstrip("0")


def bytes2str(value: String) -> str:
    """Convert byte to string

    Example:

    >>> bytes2str(b'foo')
    'foo'
    >>> bytes2str('foo')
    'foo'
    """
    if isinstance(value, bytes):
        value = str(value, "utf-8", "strict")
    elif not isinstance(value, get_args(String)):
        raise TypeError(f"not expecting type '{type(value)}'")
    return value


def float2decimal(value: float, precision: int = 15) -> Decimal:
    """Convert float to decimal with default precision value."""
    return Decimal(value).quantize(Decimal(10) ** -precision)
