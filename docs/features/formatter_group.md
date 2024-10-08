# Formatter Group

The **FormatterGroup** object, `FormatterGroup`, which is the grouping of needed
mapping formatter objects and its alias formatter object ref name together. You
can define a name of formatter that you want, such as `name` for `Naming`, or
`timestamp` for `Datetime`.

!!! example

    Define a formatter group object;

    ```python
    from fmtutil import make_group, Naming, Datetime, FormatterGroupType

    group_obj: FormatterGroupType = make_group({'name': Naming, 'datetime': Datetime})

    ```

    **Parse**:

    ```python
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

## API

```text
Group of Formatters with dynamic group naming like 'timestamp' for
Datetime, 'name' for Naming. This class will use for ``make_group``
constructor function because of different and complicate group of formatter
instances.

:param formats: A mapping value of priority attribute data.
:type formats: FormatsGroupType
:param ignore_construct: A flag for ignore pass an input formats value to
    validate and construct function.
:type ignore_construct: bool(=False)

:raises FormatterGroupValueError: If any group naming from an input formats
    does not exist in ``cls.base_groups`` value.

.. class-attributes::
    * base_groups: BaseGroupsType
        The base group of naming and Formatter class.

.. class-method::
    * __parse: ReturnParseType
        A mapping of fmt, value, and props keys that passing from searching
        step with `re` module.
    * parse: Self
        An instance of formatter group that parse from a bytes or string
        value by a format string.
    * gen_format: Tuple[str, ReturnGroupGenFormatType]
        A tuple of group naming and format string value that change format
        string to regular expression string for complied to the `re` module.
    * from_formatter: Self
        An instance of formatter group that was pass formats value directly
        to its formatter object.
    * from_value: Self
        An instance of formatter group that was use ``cls.from_value``
        method from any formatter object and its value.

.. attributes::
    * groups: GroupsType
        A dict of group naming and Formatter instance.

.. methods::
    * __construct_groups: [str, Union[DictStr, Formatter, Any]] -> Formatter
        A Formatter instance.
    * format: [str] -> str
        A string value that was formatted and filled by an input format
        string pattern.
    * adjust: [Dict[str, Any]] -> Self
        Adjust any formatter instance in ``self.groups`` of this formatter
        group.
    * to_const: list[str] | None -> FormatterGroupType
        A FormatterGroup object that create from constant of ``self.groups``
        values.

.. seealso::

    This class is an abstract class for any formatter group that override
the ``cls.base_groups`` value with mapping for group naming and Formatter
object.
```
