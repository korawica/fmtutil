# Version

!!! example

    ```python
    from fmtutil import Version

    version = Version.parse(value='Version_2_0_1', fmt='Version_%m_%n_%c')
    version.format('New_version_%m%n%c')
    ```

    ```text
    >>> 'New_version_201'
    ```

## API

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
