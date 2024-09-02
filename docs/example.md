# Examples

## Formatter Objects

The main purpose is **Formatter Objects** for `parse` and `format` with string
value, such as `Datetime`, `Version`, and `Serial` formatter objects. These objects
were used for parse any filename with put the format string value.

The formatter able to enhancement any format value from sting value, like in
`Datetime`, for `%B` value that was designed for month shortname (`Jan`,
`Feb`, etc.) that does not support in build-in `datetime` package.

!!! important

    The main usage of this formatter object is `parse` and `format` method.

### Datetime

```python
from fmtutil import Datetime

datetime = Datetime.parse(value='Datetime_20220101_000101', fmt='Datetime_%Y%m%d_%H%M%S')
datetime.format('New_datetime_%Y%b-%-d_%H:%M:%S')
```

```text
>>> 'New_datetime_2022Jan-1_00:01:01'
```

### Version

```python
from fmtutil import Version

version = Version.parse(value='Version_2_0_1', fmt='Version_%m_%n_%c')
version.format('New_version_%m%n%c')
```

```text
>>> 'New_version_201'
```

### Serial

```python
from fmtutil import Serial

serial = Serial.parse(value='Serial_62130', fmt='Serial_%n')
serial.format('Convert to binary: %b')
```

```text
>>> 'Convert to binary: 1111001010110010'
```

### Naming

```python
from fmtutil import Naming

naming = Naming.parse(value='de is data engineer', fmt='%a is %n')
naming.format('Camel case is %c')
```

```text
>>> 'Camel case is dataEngineer'
```

### Storage

```python
from fmtutil import Storage

storage = Storage.parse(value='This file have 250MB size', fmt='This file have %M size')
storage.format('The byte size is: %b')
```

```text
>>> 'The byte size is: 2097152000'
```

### Constant

```python
from fmtutil import Constant, make_const
from fmtutil.exceptions import FormatterError

const = make_const({'%n': 'normal', '%s': 'special'})
try:
    parse_const: Constant = const.parse(value='Constant_normal', fmt='Constant_%n')
    parse_const.format('The value of %%s is %s')
except FormatterError:
    pass
```

```text
>>> 'The value of %s is special'
```

All formatter object can convert itself to constant formatter object for frozen
parsing value to constant by `.to_const()`.

!!! note

    This package already implement the environment constant object,
    `fmtutil.EnvConst`. \
    [Read more about the Formatter objects API](./api.md#formatter-objects)

## FormatterGroup Object

The **FormatterGroup** object, `FormatterGroup`, which is the grouping of needed
mapping formatter objects and its alias formatter object ref name together. You
can define a name of formatter that you want, such as `name` for `Naming`, or
`timestamp` for `Datetime`.

**Parse**:

```python
from fmtutil import make_group, Naming, Datetime, FormatterGroupType

group_obj: FormatterGroupType = make_group({'name': Naming, 'datetime': Datetime})
group_obj.parse('data_engineer_in_20220101_de', fmt='{name:%s}_in_{timestamp:%Y%m%d}_{name:%a}')
```

```text
>>> {
>>>     'name': Naming.parse('data engineer', '%n'),
>>>     'timestamp': Datetime.parse('2022-01-01 00:00:00.000000', '%Y-%m-%d %H:%M:%S.%f')
>>> }
```

**Format**:

```python
from fmtutil import FormatterGroup
from datetime import datetime

group_01: FormatterGroup = group_obj({'name': 'data engineer', 'datetime': datetime(2022, 1, 1)})
group_01.format('{name:%c}_{timestamp:%Y_%m_%d}')
```

```text
>>> dataEngineer_2022_01_01
```
