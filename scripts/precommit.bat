@ECHO OFF

CALL pre-commit install
CALL pre-commit run --all-files
