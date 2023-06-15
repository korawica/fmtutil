@ECHO OFF

CALL coverage run -m pytest --disable-pytest-warnings
CALL coverage combine --append
CALL coverage report --show-missing
CALL coverage html
