# Constant

All formatter object can convert itself to constant formatter object for frozen
parsing value to constant by `.to_const()`.

!!! note

    This package already implement the environment constant object,
    [`fmtutil.EnvConst`](#environment-constant).

!!! examples

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

## Environment Constant

```text
%d  : development
%-d : dev
%D  : DEVELOPMENT
%-D : DEV
%s  : sit
%-s : sit
%S  : SIT
%u  : uat
%-u : uat
%U  : UAT
%p  : production
%-p : prd
%P  : PRODUCTION
%-P : PROD
%t  : test
%-t : test
%T  : TEST
%b  : sandbox
%-b : box
%B  : SANDBOX
%-B : BOX
%c  : poc
%C  : POC
```
