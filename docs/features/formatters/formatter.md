# Formatter

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
