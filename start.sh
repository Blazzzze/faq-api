#!/bin/sh
source venv/bin/activate

port=8000

python manage.py runserver 0.0.0.0:$port &
django_server_pid=$!

function cleanup() {
    sudo kill -9 $django_server_pid
    wait $django_server_pid 2>/dev/null
}

trap cleanup EXIT

wait