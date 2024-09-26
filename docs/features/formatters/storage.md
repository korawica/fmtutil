# Storage

!!! example

    ```python
    from fmtutil import Storage

    storage = Storage.parse(value='This file have 250MB size', fmt='This file have %M size')
    storage.format('The byte size is: %b')
    ```

    ```text
    >>> 'The byte size is: 2097152000'
    ```

## API

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
