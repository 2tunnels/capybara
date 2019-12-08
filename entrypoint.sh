#! /usr/bin/env sh
set -e

./wait-for-it.sh "$CAPYBARA_POSTGRES_HOST:$CAPYBARA_POSTGRES_PORT" -- echo "postgres is up"

./manage.py migrate
./manage.py check

exec "$@"
