# -------------------------------------------------------------------------
# Copyright (c) 2022 Korawich Anuttra. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for
# license information.
# --------------------------------------------------------------------------
# mypy: disable-error-code="attr-defined"
"""
The standard object that use for keep main value for compare data in formatter.
"""
from __future__ import annotations

from functools import total_ordering
from typing import (
    Any,
    Optional,
    Union,
)


class Version:  # type: ignore  # no cov
    ...


@total_ordering
class relativeserial:
    """Relative delta for the Serial object.

    .. examples::

        >>> 5 + relativeserial(**{"number": 5})
        10

        >>> relativeserial(**{"number": 5}) + 5
        10

        >>> relativeserial(**{"number": 5}) - 5
        0

        >>> relativeserial(**{"number": 5}) - 12
        -7

        >>> 10 - relativeserial(**{"number": 5})
        5

        >>> 2 - relativeserial(**{"number": 5})
        -3

        >>> -relativeserial(**{"number": 5})
        <relativeserial(number=-5)>

    """

    def __init__(self, number: int = 0) -> None:
        self.number: int = number

    def __hash__(self) -> int:
        return hash(self.number)

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__}(number={self.number})>"

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, int):
            return self.number == other
        elif isinstance(other, relativeserial):
            return self.number == other.number
        return NotImplemented

    def __lt__(self, other: Any) -> bool:
        if isinstance(other, int):
            return self.number < other
        elif isinstance(other, relativeserial):
            return self.number < other.number
        return NotImplemented

    def __le__(self, other: Any) -> bool:
        if isinstance(other, int):
            return self.number <= other
        elif isinstance(other, relativeserial):
            return self.number <= other.number
        return NotImplemented

    def __neg__(self) -> relativeserial:
        return self.__class__(number=-self.number)

    def __add__(
        self,
        other: Union[int, relativeserial],
    ) -> Union[int, relativeserial]:
        if isinstance(other, int):
            return self.__radd__(other)
        return self.__class__(number=(self.number + other.number))

    def __sub__(
        self,
        other: Union[int, relativeserial],
    ) -> Union[int, relativeserial]:
        if isinstance(other, int):
            return self.number - other
        return self.__class__(number=(self.number - other.number))

    def __radd__(self, other: int) -> int:
        return other + self.number

    def __rsub__(self, other: int) -> int:
        return other - self.number


# TODO: create relativeversion
# @total_ordering
class relativeversion:  # no cov
    def __init__(
        self,
        epoch: int = 0,
        major: int = 0,
        minor: int = 0,
        micro: int = 0,
        alpha: Optional[int] = None,
        beta: Optional[int] = None,
        pre: Optional[int] = None,
        post: Optional[int] = None,
        dev: Optional[int] = None,
        local: Optional[str] = None,
    ) -> None:
        self.epoch: int = epoch
        self.major: int = major
        self.minor: int = minor
        self.micro: int = micro
        self.alpha: Optional[int] = alpha
        self.beta: Optional[int] = beta
        self.pre: Optional[int] = pre
        self.post: Optional[int] = post
        self.dev: Optional[int] = dev
        self.local: Optional[str] = local

    def __hash__(self) -> int:
        release = f"{self.major}.{self.minor}.{self.micro}"
        if self.alpha:
            release = f"{release}.a{self.alpha}"
        if self.beta:
            release = f"{release}.b{self.beta}"
        if self.pre:
            release = f"{release}.pre{self.pre}"
        if self.post:
            release = f"{release}.post{self.post}"
        if self.dev:
            release = f"{release}.dev{self.post}"
        if self.local:
            release = f"{release}+local{self.post}"
        return hash(release)  # type: ignore

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__}()>"

    def __eq__(self, other) -> bool:  # type: ignore
        if isinstance(other, relativeversion):
            return (
                self.epoch == other.epoch
                and self.major == other.major
                and self.minor == other.minor
                and self.micro == other.micro
                and self.alpha == other.alpha
            )
        return ...  # type: ignore

    def __lt__(self, other: Any) -> bool:  # type: ignore
        return ...  # type: ignore

    def __le__(self, other: Any) -> bool:  # type: ignore
        return ...  # type: ignore

    def __neg__(self) -> relativeversion:
        return self.__class__(
            epoch=-self.epoch,
            major=-self.major,
            minor=-self.minor,
            micro=-self.micro,
            alpha=(-self.alpha if self.alpha else None),
            beta=(-self.beta if self.beta else None),
            pre=(-self.pre if self.pre else None),
            post=(-self.post if self.post else None),
            dev=(-self.dev if self.dev else None),
            local=self.local,
        )  # type: ignore

    def __add__(
        self,
        other: Union[relativeversion],
    ):  # type: ignore
        return ...

    def __sub__(
        self,
        other: Union[relativeversion],
    ):  # type: ignore
        return ...

    def __radd__(self, other):  # type: ignore
        return ...

    def __rsub__(self, other):  # type: ignore
        return ...
