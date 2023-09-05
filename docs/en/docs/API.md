# API Document

**Table of Contents**:

- [Formatter Objects](#formatter-objects)
  - [Datetime](#datetime)
  - [Version](#version)
  - [Serial](#serial)
  - [Naming](#naming)
  - [Storage](#storage)

## Formatter Objects

- [Datetime](#datetime)
- [Version](#version)
- [Serial](#serial)
- [Naming](#naming)
- [Storage](#storage)

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
%-K : Kebab title case format
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
