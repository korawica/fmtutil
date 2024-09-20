# Welcome to Fmtutil

Lightweight formatter objects, this fmtutil package was created for `parse`
and `format` any string values that match a format pattern which created base on
Python regular expression.

:dart: First objective of this project is include necessary formatter objects for
any data components package which mean we can `parse` any complicate names on
data source and ingest the right names to in-house or data target.

## :round_pushpin: Installation

```shell
pip install -U fmtutil
```

**Python version supported**:

| Python Version  | Installation                        | Support Fixed Bug  |
|-----------------|-------------------------------------|--------------------|
| `== 3.8`        | `pip install "fmtutil>=0.4,<0.5.0"` | :x:                |
| `>=3.9,<3.13`   | `pip install -U fmtutil`            | :heavy_check_mark: |

!!! note

    This package has one dependency package, `python-dateutil`, this package use
    for support add and sub datetime value on the Datetime formatter only.

## :beers: Getting Started

For example, we want to get filename with the format like, `filename_20220101.csv`,
on the file system storage, and we want to incremental ingest the latest file with
date **2022-03-25** date. So we will implement `Datetime` object and parse
that filename to it,

```python
assert (
    Datetime.parse('filename_20220101.csv', 'filename_%Y%m%d.csv').value
    == datetime.datetime(2022, 1, 1, 0)
)
```

The above example is :yawning_face: **NOT SURPRISE!!!** for us because Python
already provide the build-in `datetime` to parse by `datetime.strptime` and
format by `{dt}.strftime`. This package will be the special thing when we group
more than one format-able objects together as `Naming`, `Version`, and `Datetime`.

**For complex filename format like**:

```text
{filename:%s}_{datetime:%Y_%m_%d}.{version:%m.%n.%c}.csv
```

From above filename format string, the `datetime` package does not enough for
this scenario right? but you can handle by your hard-code object or create the
better package than this project.

!!! note

    Any formatter object was implemented the `self.valid` method for help us validate
    format string value like the above the example scenario,

    ```python
    this_date = Datetime.parse('20220101', '%Y%m%d')
    assert this_date.valid('any_files_20220101.csv', 'any_files_%Y%m%d.csv')
    ```
