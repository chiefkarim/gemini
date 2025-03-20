#!/bin/sh -e
set -x

ruff check routes services models scripts --fix
ruff format routes services models scripts
