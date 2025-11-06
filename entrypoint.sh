#!/usr/bin/env bash

case $1 in
    start_app)
        python tmpauth/web/main.py
    ;;
    shell)
        bash
    ;;
    sqlfluff)
        sqlfluff fix -d postgres -t placeholder --processes 0
    ;;
    mypy)
        mypy ./tmpauth/
    ;;
    pytest)
        pytest -v -W ignore:ResourceWarning,error ./tmpauth/
    ;;
    flake8)
        flake8 --count ./tmpauth/
    ;;
    black)
        black --check ./tmpauth/
    ;;
    isort)
        isort ./tmpauth/
    ;;
    help) echo -e "
        Usage: $0 ARG
        Please use one from next arguments:
            'start_app' - start tmpauth application
            'shell' - run shell into docker container of an application
            'sqlfluff' - start linter SqlFluff
            'mypy' - start checking type annotation
            'pytest' - running all tests over pytest
            'flake8' - Run flake8 for linting
            'black' - Check code formatting using Black
            'isort' - Run isort for import sorting"
    ;;
    *) python tmpauth/web/main.py
esac
