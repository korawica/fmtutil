# Search Files

If you have multi-format filenames on the data source directory, and you want to
dynamic getting max datetime on these filenames to your function, you can use a
formatter group.

## Scenario 01: search with naming and datetime

On the source directory that you want to get the latest file from a business date
in the filename (It so easy if you want to get the latest modified date) include
other files that not has format name relate with your requirement.

```text
|
|--- googleMap_20230101.json
|--- googleMap_20230103.json
|--- googleMap_20230103_bk.json
|--- googleMap_with_usage_20230105.json
|--- googleDrive_with_usage_20230105.json
```

### Code

```python
from fmtutil import (
  make_group, Naming, Datetime, FormatterGroup, FormatterGroupType, FormatterArgumentError
)

name: Naming = Naming.parse('Google Map', fmt='%t')

fmt_group: FormatterGroupType = make_group({
    "naming": name.to_const(),
    "timestamp": Datetime,
})

rs: list[FormatterGroup] = []
for file in (
    'googleMap_20230101.json',
    'googleMap_20230103.json',
    'googleMap_20230103_bk.json',
    'googleMap_with_usage_20230105.json',
    'googleDrive_with_usage_20230105.json',
):
    try:
        rs.append(
            fmt_group.parse(file, fmt=r'{naming:c}_{timestamp:%Y%m%d}\.json')
        )
    except FormatterArgumentError:
        continue

repr(max(rs).groups['timestamp'])
```

```text
>>> <Datetime.parse('2023-01-03 00:00:00.000000', '%Y-%m-%d %H:%M:%S.%f')>
```

!!! note

    The above **Example** will convert the `name`, **Naming** instance, to **Constant**
    instance before passing to the **Formatter Group** because it does not want
    to dynamic parsing this format when find any matching filenames at destination
    path.
