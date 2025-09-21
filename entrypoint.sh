#!/usr/bin/env bash

case $1 in
    start_app)
        python cafe_booking/web/main.py
    ;;
    shell)
        bash
    ;;
    sqlfluff)
        sqlfluff fix -d postgres -t placeholder --processes 0
    ;;
    mypy)
        mypy ./cafe_booking/
    ;;
    pytest)
        pytest -v -W ignore:ResourceWarning,error ./cafe_booking/
    ;;
    flake8)
        flake8 --count ./cafe_booking/
    ;;
    black)
        black --check ./cafe_booking/
    ;;
    isort)
        isort ./cafe_booking/
    ;;
    help) echo -e "
        Usage: $0 ARG
        Please use one from next arguments:
            'start_app' - start cafe_booking application
            'shell' - run shell into docker container of an application
            'format' - start formating Ruff linter
            'sqlfluff' - start linter SqlFluff
            'mypy' - start checking type annotation
            'pytest' - running all tests over pytest
            'flake8' - Run flake8 for linting
            'black' - Check code formatting using Black
            'isort' - Run isort for import sorting"
    ;;
    *) python cafe_booking/web/main.py
esac
