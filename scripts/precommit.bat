@ECHO OFF

;; CALL pre-commit install
CALL pre-commit install --hook-type commit-msg --hook-type pre-push
CALL pre-commit install-hooks
CALL pre-commit run --all-files
