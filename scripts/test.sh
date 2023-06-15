#!/usr/bin/env bash

set -e
set -x

coverage run --module pytest --verbose tests ${@}
