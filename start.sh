#!/bin/sh

# This script activates the virtual environment and starts the Django development server.
# Use it to start the server in an isolated environment.

source venv/bin/activate

port=8000

# Kill process; if port is already taken
sudo kill -9 $(lsof -t -i:$port) || true

python manage.py runserver 0.0.0.0:$port &
django_server_pid=$!

function cleanup() {
    sudo kill -9 $django_server_pid
    wait $django_server_pid 2>/dev/null
}

trap cleanup EXIT

wait
