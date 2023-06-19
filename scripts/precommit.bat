@ECHO OFF

CALL pre-commit install
CALL pre-commit install --install-hooks
CALL pre-commit run --all-files
