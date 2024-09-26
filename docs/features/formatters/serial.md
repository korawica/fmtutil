# Serial

!!! example

    ```python
    from fmtutil import Serial

    serial = Serial.parse(value='Serial_62130', fmt='Serial_%n')
    serial.format('Convert to binary: %b')
    ```

    ```text
    >>> 'Convert to binary: 1111001010110010'
    ```

## API

**Formatter Mapping**:

```text
%n  : Normal format
%p  : Padding number
%b  : Binary number
%c  : Normal with comma separate number
%u  : Normal with underscore separate number
```
