# Error Handler

## Simple `try-catch`

```python
from fmtutil import Datetime
from fmtutil.exceptions import FormatterError

try:
    parse_dt: Datetime = Datetime.parse(value='Constant_normal', fmt='Constant_%n')
    parse_dt.format('The value of %%s is %s')
except FormatterError as err:
    print(f"Raise error: {err}")
```

```text
Raise error: ...
```
