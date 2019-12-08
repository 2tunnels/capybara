#! /usr/bin/env sh
set -e

exec gunicorn capybara.wsgi:application -b 0.0.0.0:8000 --access-logfile - --error-logfile -
