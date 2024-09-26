# Datetime

!!! example

    ```python
    from fmtutil import Datetime

    datetime = Datetime.parse(value='Datetime_20220101_000101', fmt='Datetime_%Y%m%d_%H%M%S')
    datetime.format('New_datetime_%Y%b-%-d_%H:%M:%S')
    ```

    ```text
    >>> 'New_datetime_2022Jan-1_00:01:01'
    ```

## API

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
