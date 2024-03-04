import re
from collections import defaultdict
from dataclasses import dataclass, field
from functools import partial
from typing import Any, Callable, Optional, Union

from fmtutil.exceptions import FormatterArgumentError, FormatterValueError
from fmtutil.utils import itself

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


Format = Union[CombineFormat, CombineFormat]


def parsing_format(value: dict[str, Any]) -> Format:
    if "regex" in value.keys():
        return CommonFormat(**value)
    elif "cregex" in value.keys():
        return CombineFormat(**value)
    raise ValueError("Format does not have any regex key")


number_asset: dict[str, Format] = {
    "%n": parsing_format(
        {
            "alias": "number",
            "regex": r"[0-9]*",
            "fmt": lambda x: partial(itself, str(x)),
            "parse": lambda x: x,
            "level": 1,
        }
    ),
    "%e": parsing_format(
        {
            "alias": "number_extra",
            "cregex": "%n_%n",
            "fmt": lambda x: partial(itself, str(x)),
            "parse": lambda x: x,
            "level": 1,
        }
    ),
}

datetime_asset: dict[str, Format] = {
    "%n": parsing_format(
        {
            "alias": "datetime_normal",
            "cregex": "%Y%m%d_%H%M%S",
            "fmt": lambda x: x.strftime("%Y%m%d_%H%M%S"),
            "parse": ...,
        }
    ),
}


class Formatter:

    def __init__(self, register):
        self.regis: dict[str, Format] = register
        self.regex = self._regex()

    def gen_format(
        self,
        fmt: str,
        *,
        prefix: Optional[str] = None,
        suffix: Optional[str] = None,
        alias: bool = True,
    ):
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
                        f"``cls.regex``."
                    ),
                )
            regex: str = regexes[fmt_str]
            print(regex)
            if _alias_match := re.search(
                r"^\(\?P<(?P<alias_name>\w+)>(?P<fmt_regex>.+)?\)$",
                regex,
            ):
                _sr_re: str = _alias_match.group("alias_name")
                if alias:
                    regex = re.sub(
                        rf"\(\?P<{_sr_re}>",
                        f"(?P<{_prefix}{_sr_re}__{_cache[fmt_str]}{_suffix}>",
                        regex,
                    )
                else:
                    regex = re.sub(rf"\(\?P<{_sr_re}>", "(", regex)
            else:
                raise FormatterValueError(
                    "Regex format string does not set group name for parsing "
                    "value to its class."
                )
            _cache[fmt_str] += 1
            fmt = fmt.replace(fmt_str, regex, 1)
        return fmt

    def _regex(self) -> DictStr:
        results: DictStr = {}
        pre_results: DictStr = {}
        for f, props in self.regis.items():
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


if __name__ == "__main__":
    print(number_asset)
    naming_fmt = Formatter(register=number_asset)
    print(naming_fmt.regex)
    print(naming_fmt.gen_format("This is a number %n but extra %e"))
