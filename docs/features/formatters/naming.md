# Naming

!!! example

    ```python
    from fmtutil import Naming

    naming = Naming.parse(value='de is data engineer', fmt='%a is %n')
    naming.format('Camel case is %c')
    ```

    ```text
    >>> 'Camel case is dataEngineer'
    ```

## API

**Formatter Mapping**:

```text
%n  : Normal name format
%N  : Normal name upper case format
%-N : Normal name title case format
%u  : Upper case format
%l  : Lower case format
%t  : Title case format
%a  : Shortname format
%A  : Shortname upper case format
%f  : Flat case format
%F  : Flat upper case format
%c  : Camel case format
%-c : Upper first Camel case format
%p  : Pascal case format
%s  : Snake case format
%S  : Snake upper case format
%-S : Snake title case format
%k  : Kebab case format
%K  : Kebab upper case format
%-K : Kebab title case format (Train Case)
%T  : Train case format
%v  : normal name removed vowel
%V  : normal name removed vowel with upper case
```
