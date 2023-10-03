import re
from functools import wraps
from typing import (
    Callable,
    ClassVar,
    Collection,
    Dict,
    Iterable,
    Optional,
    Pattern,
    SupportsInt,
    Tuple,
    Type,
    Union,
    cast,
    get_args,
)

from .__type import String

Comparable = Union["BaseVersion", Dict[str, int], Collection[int], str]
Comparator = Callable[["BaseVersion", Comparable], bool]


class RegVersion:
    version: str = r"""
        ^
        (?P<major>0|[1-9]\d*)
        (?:
            \.
            (?P<minor>0|[1-9]\d*)
            (?:
                \.
                (?P<patch>0|[1-9]\d*)
            ){opt_patch}
        ){opt_minor}
    """

    version_semantic: str = r"""
        ^
        (?P<major>0|[1-9]\d*)
        (?:
            \.
            (?P<minor>0|[1-9]\d*)
            (?:
                \.
                (?P<patch>0|[1-9]\d*)
            ){opt_patch}
        ){opt_minor}
        (?:-(?P<prerelease>
            (?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*)
            (?:\.(?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*))*
        ))?
        (?:\+(?P<build>
            [0-9a-zA-Z-]+
            (?:\.[0-9a-zA-Z-]+)*
        ))?
        $
    """


def _comparator(operator: Comparator) -> Comparator:
    """Wrap a Version binary op method in a type-check."""

    @wraps(operator)
    def wrapper(self: "BaseVersion", other: Comparable) -> bool:
        comparable_types = (
            BaseVersion,
            dict,
            tuple,
            list,
            *get_args(String),
        )
        if not isinstance(other, comparable_types):
            return NotImplemented
        return operator(self, other)

    return wrapper


def _cmp(a, b) -> int:
    """Return negative if a < b, zero if a == b, positive if a > b."""
    return (a > b) - (a < b)


def increment(s: str) -> str:
    """Look for the last sequence of number(s) in a string and increment.

    :param s: the string to search for.

    :return: the incremented string
    """
    if m := re.compile(r"(?:\D*(\d+)\D*)+").search(s):
        next_value = str(int(m.group(1)) + 1)
        start, end = m.span(1)
        s = s[: max(end - len(next_value), start)] + next_value + s[end:]
    return s


class BaseVersion:
    """A Base Version class.

    :param major: version when you make incompatible API changes.
    :param minor: version when you add functionality in a backwards-compatible
        manner.
    :param patch: version when you make backwards-compatible bug fixes.
    """

    __slots__ = (
        "major",
        "minor",
        "patch",
    )

    #: The names of the different parts of a version
    NAMES: ClassVar[Tuple[str, ...]] = tuple([item[1:] for item in __slots__])

    regex: ClassVar[Pattern[str]] = re.compile(
        RegVersion.version.format(opt_patch="", opt_minor=""),
        re.VERBOSE,
    )

    def __init__(
        self,
        major: SupportsInt,
        minor: SupportsInt = 0,
        patch: SupportsInt = 0,
    ):
        version_parts = {
            "major": int(major),
            "minor": int(minor),
            "patch": int(patch),
        }

        for name, value in version_parts.items():
            if value < 0:
                raise ValueError(
                    f"{name!r} is negative. A version can only be positive."
                )

        self.major = version_parts["major"]
        self.minor = version_parts["minor"]
        self.patch = version_parts["patch"]

    def __setattr__(self, attr, value):
        if hasattr(self, attr) and attr in self.__class__.__slots__:
            raise AttributeError(f"attribute {attr!r} is readonly")
        super().__setattr__(attr, value)

    def to_tuple(self) -> Tuple[int, int, int]:
        """Convert the BaseVersion object to a tuple.

        :rtype: Tuple[int, int, int]
        :return: A tuple with all the parts
        """
        return self.major, self.minor, self.patch

    def to_dict(self) -> Dict[str, int]:
        """Convert the Version object to a dict.

        :return: A dict with the keys in the order ``major``, ``minor``, and
            ``patch``.
        """
        return {
            "major": self.major,
            "minor": self.minor,
            "patch": self.patch,
        }

    def __iter__(self) -> Iterable[int]:
        """Return iter(self)."""
        yield from self.to_tuple()

    def bump_major(self) -> "BaseVersion":
        """Raise the major part of the version, return a new object
        but leave self untouched.

        :return: new object with the raised major part
        """
        return self.__class__(self.major + 1)

    def bump_minor(self) -> "BaseVersion":
        """Raise the minor part of the version, return a new object
        but leave self untouched.

        :return: new object with the raised minor part
        """
        return self.__class__(self.major, self.minor + 1)

    def bump_patch(self) -> "BaseVersion":
        """Raise the patch part of the version, return a new object
        but leave self untouched.

        :return: new object with the raised patch part
        """
        return self.__class__(self.major, self.minor, self.patch + 1)

    def compare(self, other: Comparable) -> int:
        """Compare self with this other.

        :param other: the second version
        :return: The return value is negative if ver1 < ver2,
            zero if ver1 == ver2 and strictly positive if ver1 > ver2
        """
        cls = type(self)
        if isinstance(other, get_args(String)):
            other = cls.parse(other)
        elif isinstance(other, dict):
            other = cls(**other)
        elif isinstance(other, (tuple, list)):
            other = cls(*other)
        elif not isinstance(other, cls):
            raise TypeError(
                f"Expected str, bytes, dict, tuple, list, or {cls.__name__} "
                f"instance, but got {type(other)}"
            )
        return _cmp(
            self.to_tuple(),
            other.to_tuple(),
        )

    def next_version(
        self,
        part: str,
    ) -> "BaseVersion":
        """Determines next version, preserving natural order.

        :param part: One of "major", "minor", "patch"

        :return: new object with the appropriate part raised
        """
        valid_parts: Tuple[str, ...] = self.__class__.__slots__
        if part not in self.__class__.__slots__:
            raise ValueError(
                f"Invalid part. Expected one of {valid_parts}, but got {part!r}"
            )

        version = self
        return getattr(version, "bump_" + part)()

    @_comparator
    def __eq__(self, other: Comparable) -> bool:  # type: ignore
        return self.compare(other) == 0

    @_comparator
    def __ne__(self, other: Comparable) -> bool:  # type: ignore
        return self.compare(other) != 0

    @_comparator
    def __lt__(self, other: Comparable) -> bool:
        return self.compare(other) < 0

    @_comparator
    def __le__(self, other: Comparable) -> bool:
        return self.compare(other) <= 0

    @_comparator
    def __gt__(self, other: Comparable) -> bool:
        return self.compare(other) > 0

    @_comparator
    def __ge__(self, other: Comparable) -> bool:
        return self.compare(other) >= 0

    def __getitem__(
        self,
        index: Union[int, slice],
    ) -> Union[int, Optional[str], Tuple[Union[int, str], ...]]:
        """If the part requested is undefined, or a part of the range requested
        is undefined, it will throw an index error.

        Negative indices are not supported.

        :raises IndexError: if index is beyond the range or a part is None

        :param index: a positive integer indicating the offset or a ``slice``
            object.
        :return: the requested part of the version at position index
        """
        if isinstance(index, int):
            index = slice(index, index + 1)
        index = cast(slice, index)

        if (
            isinstance(index, slice)
            and (index.start is not None and index.start < 0)
            or (index.stop is not None and index.stop < 0)
        ):
            raise IndexError("BaseVersion index cannot be negative")

        part = tuple(
            filter(
                lambda p: p is not None,
                cast(Iterable, self.to_tuple()[index]),
            )
        )

        if len(part) == 1:
            return part[0]
        elif not part:
            raise IndexError("BaseVersion part undefined")
        return part

    def __repr__(self) -> str:
        s: Iterable[str] = (f"{k}={v!r}" for k, v in self.to_dict().items())
        return f"{type(self).__name__}({', '.join(s)})"

    def __str__(self) -> str:
        return ".".join(str(x) for x in self.to_tuple())

    def __hash__(self) -> int:
        return hash(self.to_tuple())

    def match(self, match_expr: str) -> bool:
        """Compare self to match a match expression.

        :param match_expr: optional operator and version; valid operators are
            ``<``   smaller than
            ``>``   greater than
            ``>=``  greator or equal than
            ``<=``  smaller or equal than
            ``==``  equal
            ``!=``  not equal

        :return: True if the expression matches the version, otherwise False
        """
        prefix = match_expr[:2]
        if prefix in (">=", "<=", "==", "!="):
            match_version = match_expr[2:]
        elif prefix and prefix[0] in (">", "<"):
            prefix = prefix[0]
            match_version = match_expr[1:]
        elif match_expr and match_expr[0] in "0123456789":
            prefix = "=="
            match_version = match_expr
        else:
            raise ValueError(
                f"match_expr parameter should be in format <op><ver>, "
                f"where <op> is one of "
                f"['<', '>', '==', '<=', '>=', '!=']. "
                f"You provided: {match_expr!r}"
            )

        possibilities_dict = {
            ">": (1,),
            "<": (-1,),
            "==": (0,),
            "!=": (-1, 1),
            ">=": (0, 1),
            "<=": (-1, 0),
        }

        possibilities = possibilities_dict[prefix]
        cmp_res = self.compare(match_version)

        return cmp_res in possibilities

    @classmethod
    def parse(
        cls: Type["BaseVersion"],
        version: String,
    ) -> "BaseVersion":
        """Parse version string to a Version instance.

        :param version: version string

        :raises ValueError: if version is invalid
        :raises TypeError: if version contains the wrong type

        :return: a new :class:`Version` instance
        """
        if isinstance(version, bytes):
            version = version.decode("UTF-8")
        elif not isinstance(version, str):
            raise TypeError(f"not expecting type '{type(version)}'")

        if (match := cls.regex.match(version)) is None:
            raise ValueError(f"{version} is not valid SemVer string")

        return cls(**match.groupdict())

    def replace(self, **parts: Union[int, Optional[str]]) -> "BaseVersion":
        """Replace one or more parts of a version and return a new
        ``BaseVersion`` instance, but leave self untouched.

        :param parts: the parts to be updated. Valid keys are:
            ``major``, ``minor``, ``patch``, ``prerelease``, or ``build``

        :raises TypeError: if ``parts`` contain invalid keys

        :return: the new :class:`~semver.version.Version` object with
            the changed parts
        """
        version = self.to_dict()
        version.update(parts)
        try:
            return type(self)(**version)  # type: ignore
        except TypeError as err:
            unknown = set(parts) - set(self.to_dict())
            error = "replace() got %d unexpected keyword argument(s): %s" % (
                len(unknown),
                ", ".join(unknown),
            )
            raise TypeError(error) from err

    @classmethod
    def is_valid(cls, version: str) -> bool:
        """Check if the string is a valid base version.

        :param version: the version string to check
        :return: True if the version string is a valid base version, False
                otherwise.
        """
        try:
            cls.parse(version)
            return True
        except ValueError:
            return False

    def is_compatible(self, other: "BaseVersion") -> bool:
        """
        Check if current version is compatible with other version.

        The result is True, if either of the following is true:

        * both versions are equal, or
        * both majors are equal and higher than 0. Same for both minors.
            Both pre-releases are equal, or
        * both majors are equal and higher than 0. The minor of b's
            minor version is higher than a's. Both pre-releases are equal.

        The algorithm does *not* check patches.

        :param other: the version to check for compatibility
        :return: True, if ``other`` is compatible with the old version,
            otherwise False
        """
        if not isinstance(other, BaseVersion):
            raise TypeError(f"Expected a Version type but got {type(other)}")

        # All major-0 versions should be incompatible with anything but itself
        if (0 == self.major == other.major) and (self[:3] != other[:3]):
            return False

        return (self.major == other.major) and (other.minor >= self.minor)


class VersionPackage(BaseVersion):
    ...


class VersionSemver(BaseVersion):
    ...
