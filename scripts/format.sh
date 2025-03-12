#!/bin/sh -e
set -x

ruff check routes utils models scripts --fix
ruff format routes utils models scripts
