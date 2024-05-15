# API Documents

**Table of Contents**:

- [SlotLevel Object](#slotlevel-object)
- [Formatter Objects](#formatter-objects)
  - [Datetime](#datetime)
  - [Version](#version)
  - [Serial](#serial)
  - [Naming](#naming)
  - [Storage](#storage)
  - [EnvConst](#environment-constant)

## SlotLevel Object

```text
Slot level object for order priority values. This was mean if
you implement this slot level object to attribute on your class
and update level to an instance when it has some action, it will
be make the level more than another instance.

:param level: a level number of this slot instance.
:type level: int

Attributes:
    * level: int
        A number of level that represent n-layer of this instance.
    * slot: List[bool]
        A list of boolean that have index equal the level attribute.
    * count: int
        A counting number of True value in the slot.
    * value: int
        A sum of weighted value from a True value in any slot position.

Methods:
    * update: [Optional[Union[int, TupleInt]]] -> SlotLevel
        Self that was updated level
    * checker: [Union[int, TupleInt]] -> bool
        A True if all values in ``self.slot`` that match with index numbers
        are True.

Static-methods:
    * make_tuple: [Union[int, TupleInt]] -> TupleInt
        A tuple of integer value that was created from input.
```

## Formatter Objects

- [Datetime](#datetime)
- [Version](#version)
- [Serial](#serial)
- [Naming](#naming)
- [Storage](#storage)
- [EnvConst](#environment-constant)

```text
Formatter object for inherit to any formatter subclass that define
format and parse method. The base class will implement necessary
properties and method for subclass that should implement or enhance such
as `the cls.formatter()` method or the `cls.priorities` property.

:param formats: A mapping value of priority attribute data.
:type formats: Optional[dict](=None)
:param set_strict_mode: A flag to allow checking duplicate attribute value.
:type set_strict_mode: bool(=False)
:param set_std_value: A flag to allow for set standard value form string,
    `self.class-name.lower()` if it True.
:type set_std_value: bool(=True)

.. class attributes::
    * base_fmt: str
        The base default format string value for this object.
    * base_level: int
        The maximum level of slot level of this instance.
    * Config: object
        A Configuration object that use for group and keep any config for
        this sub-formatter object.

.. class-methods::
    * from_value: Formatter
        An instance of formatter that was use ``cls.parse`` method from any
        correct string value with the ``cls.base_fmt`` value.
    * parse: Formatter
        An instance of formatter that parse from a bytes or string value by
        a format string or base format string if it None.
    * gen_format: str
        A format string value that was changed to the regular expression
        string value for comply with the `re` module to any string value.
    * regex: DictStr
        A dict of format string, and it's regular expression string
        value that was generated from values of ``cls.formatter``.

.. attributes::
    * value: Any
        A value that define by property of this formatter object.
    * string: str
        A standard string value that define by property of this formatter
        object.
    * level: SlotLevel
        A SlotLevel instance that have level with ``cls.base_level``.
    * priorities: ReturnPrioritiesType
        A priorities value that define by property of this formatter object.

.. methods::
    * _setter_std_value: [bool] -> NoReturn
        Setting standard value that have an argument name be the class name
        with lower case if input flag is True.
    * values: [Optional[Any]] -> DictStr
        A dict of format string, and it's string value that was passed an
        input value to `cls.formatter` method.
    * format: [str] -> str
        A string value that was formatted from format string pattern.
    * validate: [] -> bool
        A Validate method that will call after setup all attributes in
        initialize layer.
    * valid: [] -> Any
        A True value if the value from ``cls.parse`` of a string value,
        and a format string pattern is valid with ``self.value``.
    * to_const: [] -> ConstantType
        A ConstantType class that have class name with
        ``f'{self.__class__.__name__}Const'`` with ``self.values()``.

.. static-methods::
    * __validate_format: [Optional[Dict[str, Any]]] -> Dict[str, Any]
        A formats value that validate with duplicate format string values.
    * formatter: [Optional[Any]] -> ReturnFormattersType
        A formatter value that define by property of this formatter object.
    * prepare_value: [Any] -> Any
        A prepared value with defined logic.

.. seealso::

    This class is abstract class for any formatter class. It will raise
`NotImplementedError` when the necessary attributes and methods does not
implement from subclass.
```

### Datetime

**Formatter Mapping**:

```text
%n  : Normal format with `%Y%m%d_%H%M%S`
%Y  : Year with century as a decimal number.
%y  : Year without century as a zero-padded decimal number.
%-y : Year without century as a decimal number.
%m  : Month as a zero-padded decimal number.
%-m : Month as a decimal number.
%b  : Abbreviated month name.
%B  : Full month name.
%a  : the abbreviated weekday name
%A  : the full weekday name
%w  : weekday as a decimal number, 0 as Sunday and 6 as Saturday.
%u  : weekday as a decimal number, 1 as Monday and 7 as Sunday.
%d  : Day of the month as a zero-padded decimal.
%-d : Day of the month as a decimal number.
%H  : Hour (24-hour clock) as a zero-padded decimal number.
%-H : Hour (24-hour clock) as a decimal number.
%I  : Hour (12-hour clock) as a zero-padded decimal number.
%-I : Hour (12-hour clock) as a decimal number.
%M  : minute as a zero-padded decimal number
%-M : minute as a decimal number
%S  : second as a zero-padded decimal number
%-S : second as a decimal number
%j  : day of the year as a zero-padded decimal number
%-j : day of the year as a decimal number
%U  : Week number of the year (Sunday as the first day of the
    week). All days in a new year preceding the first Sunday are
    considered to be in week 0.
%W  : Week number of the year (Monday as the first day of the week
    ). All days in a new year preceding the first Monday are
    considered
    to be in week 0.
%p  : Locale’s AM or PM.
%f  : Microsecond as a decimal number, zero-padded on the left.
```

### Version

**Formatter Mapping**:

```text
%f  : full version format with `%m_%n_%c`
%-f : full version format with `%m-%n-%c`
%m  : major number
%n  : minor number
%c  : micro number
%e  : epoch release
%q  : pre-release
%p  : post release
%-p : post release number
%d  : dev release
%l  : local release
%-l : local release number
```

### Serial

**Formatter Mapping**:

```text
%n  : Normal format
%p  : Padding number
%b  : Binary number
%c  : Normal with comma separate number
%u  : Normal with underscore separate number
```

### Naming

**Formatter Mapping**:

```text
%n  : Normal name format
%N  : Normal name upper case format
%-N : Normal name title case format
%u  : Upper case format
%l  : Lower case format
%t  : Title case format
%a  : Shortname format
%A  : Shortname upper case format
%f  : Flat case format
%F  : Flat upper case format
%c  : Camel case format
%-c : Upper first Camel case format
%p  : Pascal case format
%s  : Snake case format
%S  : Snake upper case format
%-S : Snake title case format
%k  : Kebab case format
%K  : Kebab upper case format
%-K : Kebab title case format (Train Case)
%T  : Train case format
%v  : normal name removed vowel
%V  : normal name removed vowel with upper case
```

### Storage

**Formatter Mapping**:

```text
%b  : Bit format
%B  : Byte format
%K  : Kilo-Byte format
%M  : Mega-Byte format
%G  : Giga-Byte format
%T  : Tera-Byte format
%P  : Peta-Byte format
%E  : Exa-Byte format
%Z  : Zetta-Byte format
%Y  : Yotta-Byte format
```

### Environment Constant

```text
%d  : development
%-d : dev
%D  : DEVELOPMENT
%-D : DEV
%s  : sit
%-s : sit
%S  : SIT
%u  : uat
%-u : uat
%U  : UAT
%p  : production
%-p : prd
%P  : PRODUCTION
%-P : PROD
%t  : test
%-t : test
%T  : TEST
%b  : sandbox
%-b : box
%B  : SANDBOX
%-B : BOX
%c  : poc
%C  : POC
```
